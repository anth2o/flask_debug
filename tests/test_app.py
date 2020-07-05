from flask_debug.app import app

def test_app():
    with app.test_client() as c:
        response = c.get("/")
    assert response.status_code == 200
