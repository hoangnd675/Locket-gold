"""Locket Companion: safe status dashboard and diagnostic API.

This service does not modify Locket traffic or grant paid entitlements.
"""
from __future__ import annotations

import os
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.after_request
def add_security_headers(response):
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "DENY")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
    if response.mimetype == "text/html":
        response.headers.setdefault("Content-Security-Policy", "default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'")
    return response


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/health")
def health():
    return jsonify({
        "ok": True,
        "service": "Locket Companion",
        "version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }), 200


@app.get("/api/account/status")
def account_status():
    """Report integration state honestly; no unofficial account probing."""
    return jsonify({
        "connected": False,
        "status": "not_connected",
        "message": "Chưa kết nối nguồn dữ liệu tài khoản được Locket hỗ trợ.",
        "premium_status": "unknown",
        "note": "Ứng dụng không giả lập hoặc thay đổi quyền Gold.",
    }), 200


@app.get("/api/diagnostics")
def diagnostics():
    return jsonify({
        "ok": True,
        "checks": [
            {"name": "Flask application", "status": "pass"},
            {"name": "Health endpoint", "status": "pass"},
            {"name": "Account integration", "status": "not_configured"},
        ],
        "environment": "vercel" if os.getenv("VERCEL") else "self-hosted",
    }), 200


@app.errorhandler(404)
def not_found(_error):
    return jsonify({"ok": False, "error": "not_found", "message": "Không tìm thấy đường dẫn."}), 404


@app.errorhandler(500)
def internal_error(_error):
    return jsonify({"ok": False, "error": "internal_error", "message": "Đã xảy ra lỗi máy chủ."}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
