/***********************************************
 * Locket Clean Unlock Script
 * Giúp mở khóa quyền lợi Gold/Premium một cách sạch sẽ
 ***********************************************/

let body = $response.body;

try {
    let obj = JSON.parse(body);

    // Thiết lập quyền sở hữu gói Gold chính hãng vĩnh viễn
    if (obj.subscriber) {
        if (!obj.subscriber.entitlements) {
            obj.subscriber.entitlements = {};
        }
        
        obj.subscriber.entitlements.gold = {
            "is_sandbox": false,
            "ownership_type": "PURCHASED",
            "billing_issues_detected_at": null,
            "period_type": "normal",
            "expires_date": "2099-12-31T23:59:59Z",
            "grace_period_expires_date": null,
            "unsubscribe_detected_at": null,
            "original_purchase_date": "2024-01-01T00:00:00Z",
            "purchase_date": "2024-01-01T00:00:00Z",
            "store": "app_store"
        };

        if (!obj.subscriber.subscriptions) {
            obj.subscriber.subscriptions = {};
        }

        obj.subscriber.subscriptions["com.locket.premium.yearly"] = {
            "is_sandbox": false,
            "billing_issues_detected_at": null,
            "unsubscribe_detected_at": null,
            "expires_date": "2099-12-31T23:59:59Z",
            "original_purchase_date": "2024-01-01T00:00:00Z",
            "purchase_date": "2024-01-01T00:00:00Z",
            "ownership_type": "PURCHASED",
            "store": "app_store"
        };
    }

    body = JSON.stringify(obj);
} catch (e) {
    // Bỏ qua lỗi nếu cấu trúc không khớp
}

$done({ body });
