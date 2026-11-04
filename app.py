from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def locket_bypass_handler(path):
    response_data = {
        "status": "success",
        "code": 200,
        "message": "Axiom Vercel Serverless Bypass Active",
        "data": {
            "is_pro": True,
            "tier": "gold",
            "entitlements": {
                "pro": {
                    "expires_date": "2099-12-31T23:59:59Z",
                    "purchase_date": "2026-01-01T00:00:00Z",
                    "product_identifier": "com.locket.gold.yearly"
                }
            },
            "subscription": {
                "status": "active",
                "plan": "gold_lifetime"
            }
        }
    }
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=False)
