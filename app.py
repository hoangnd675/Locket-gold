from flask import Flask, request, jsonify

app = Flask(__name__)

# Danh sách username được phép active từ xa, boss man tự thêm tên vào đây
AUTHORIZED_USERS = ["hoangnd675", "boss_man"]

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def locket_remote_bypass(path):
    username = request.args.get('username') or (request.json.get('username') if request.is_json else "hoangnd675")
    
    response_data = {
        "status": "success",
        "code": 200,
        "message": f"Axiom Remote Bypass Active for {username}",
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
