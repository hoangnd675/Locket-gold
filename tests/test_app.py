from app import app

def test_homepage_renders_dashboard():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Locket Companion" in response.data

def test_health_endpoint():
    response = app.test_client().get("/api/health")
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["ok"] is True
    assert payload["service"] == "Locket Companion"

def test_account_status_does_not_claim_gold():
    response = app.test_client().get("/api/account/status")
    payload = response.get_json()
    assert response.status_code == 200
    assert payload["connected"] is False
    assert payload["premium_status"] == "unknown"

def test_diagnostics():
    response = app.test_client().get("/api/diagnostics")
    payload = response.get_json()
    assert response.status_code == 200
    assert payload["ok"] is True
    assert any(item["name"] == "Flask application" for item in payload["checks"])

def test_unknown_route_returns_json_404():
    response = app.test_client().get("/does-not-exist")
    assert response.status_code == 404
    assert response.get_json()["error"] == "not_found"
