import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


@pytest.mark.parametrize(
    ("path", "params", "expected"),
    [
        ("/add", {"a": 7, "b": 3}, 10),
        ("/subtract", {"a": 7, "b": 3}, 4),
        ("/multiply", {"a": 7, "b": 3}, 21),
        ("/divide", {"a": 7, "b": 2}, 3.5),
        ("/square", {"n": 4}, 16),
    ],
)
def test_calculation_routes(path, params, expected):
    response = client.get(path, params=params)

    assert response.status_code == 200
    assert response.json() == {"result": expected}


def test_divide_by_zero_returns_bad_request():
    response = client.get("/divide", params={"a": 5, "b": 0})

    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}


def test_missing_operand_returns_validation_error():
    response = client.get("/add", params={"a": 5})

    assert response.status_code == 422


def test_root_route():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI CI/CD is working!"}


@pytest.mark.parametrize(
    ("marks", "expected_status"),
    [(75, "Pass"), (35, "Fail")],
)
def test_student_result(marks, expected_status):
    response = client.post(
        "/result",
        json={"name": "Student", "marks": marks},
    )

    assert response.status_code == 200
    assert response.json()["status"] == expected_status
