import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def _query(client: TestClient, query: str) -> dict:
    response = client.post("/graphql", json={"query": query})
    assert response.status_code == 200
    body = response.json()
    assert "errors" not in body
    return body["data"]


def test_salesorder_list(client: TestClient) -> None:
    data = _query(
        client,
        "{ salesorder_list { id accountName amount status } }",
    )
    orders = data["salesorder_list"]
    assert isinstance(orders, list)
    assert len(orders) >= 2
    for order in orders:
        assert order["id"]
        assert order["accountName"]
        assert order["amount"] is not None
        assert order["status"]
    ids = {order["id"] for order in orders}
    assert "SO-001" in ids
    assert "SO-002" in ids


def test_employee_list(client: TestClient) -> None:
    data = _query(
        client,
        "{ employee_list { id firstName lastName department email } }",
    )
    employees = data["employee_list"]
    assert isinstance(employees, list)
    assert len(employees) >= 2
    for employee in employees:
        assert employee["id"]
        assert employee["firstName"]
        assert employee["lastName"]
        assert employee["department"]
        assert employee["email"]
    ids = {employee["id"] for employee in employees}
    assert "EMP-001" in ids
    assert "EMP-002" in ids


def test_get_salesorder_by_id_valid(client: TestClient) -> None:
    data = _query(
        client,
        '{ get_salesorder_by_id(id: "SO-001") { id accountName amount status } }',
    )
    order = data["get_salesorder_by_id"]
    assert order is not None
    assert order["id"] == "SO-001"
    assert order["accountName"]
    assert order["amount"] is not None
    assert order["status"]


def test_get_salesorder_by_id_invalid(client: TestClient) -> None:
    data = _query(
        client,
        '{ get_salesorder_by_id(id: "SO-999") { id } }',
    )
    assert data["get_salesorder_by_id"] is None


def test_get_employee_by_id_valid(client: TestClient) -> None:
    data = _query(
        client,
        '{ get_employee_by_id(id: "EMP-001") { id firstName lastName department email } }',
    )
    employee = data["get_employee_by_id"]
    assert employee is not None
    assert employee["id"] == "EMP-001"
    assert employee["firstName"]
    assert employee["lastName"]
    assert employee["department"]
    assert employee["email"]


def test_get_employee_by_id_invalid(client: TestClient) -> None:
    data = _query(
        client,
        '{ get_employee_by_id(id: "EMP-999") { id } }',
    )
    assert data["get_employee_by_id"] is None


def test_passport_list(client: TestClient) -> None:
    data = _query(
        client,
        "{ passport_list { id employeeId issueDate expiryDate } }",
    )
    passports = data["passport_list"]
    assert isinstance(passports, list)
    assert len(passports) >= 1
    for passport in passports:
        assert passport["id"]
        assert passport["employeeId"]
        assert passport["issueDate"]
        assert passport["expiryDate"]


def test_legalcase_list(client: TestClient) -> None:
    data = _query(
        client,
        "{ legalcase_list { id caseNumber summary status } }",
    )
    cases = data["legalcase_list"]
    assert isinstance(cases, list)
    assert len(cases) >= 1
    for case in cases:
        assert case["id"]
        assert case["caseNumber"]
        assert case["summary"]
        assert case["status"]
