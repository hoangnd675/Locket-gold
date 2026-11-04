/*
 * Axiom's Local Response Override Script for Locket Gold
 */
let body = $response.body;
try {
    let obj = JSON.parse(body);
    obj.data = obj.data || {};
    obj.data.is_pro = true;
    obj.data.entitlements = {
        "pro": {
            "expires_date": "2099-12-31T23:59:59Z",
            "purchase_date": "2026-01-01T00:00:00Z"
        }
    };
    body = JSON.stringify(obj);
} catch (e) {
    console.log("[-] Axiom Script Parse Error: " + e);
}
$done({ body });
