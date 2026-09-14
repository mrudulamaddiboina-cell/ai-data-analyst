from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to AI Data Analyst!"


def test_analyze_csv():
    csv_content = """Name,Department,Age,Marks,Attendance
Ananya,CSE,20,88,92
Rahul,CSE,21,76,85
Sneha,ECE,20,91,96
"""

    response = client.post(
        "/analyze",
        files={
            "file": (
                "test.csv",
                csv_content,
                "text/csv"
            )
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["filename"] == "test.csv"
    assert data["analysis"]["rows"] == 3
    assert data["analysis"]["columns"] == 5
