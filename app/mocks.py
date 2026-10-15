SALESFORCE_ORDERS: list[dict] = [
    {
        "id": "SO-001",
        "account_name": "Acme Corp",
        "amount": 15000.0,
        "status": "Open",
    },
    {
        "id": "SO-002",
        "account_name": "Globex Industries",
        "amount": 28500.0,
        "status": "Closed",
    },
]

HR_EMPLOYEES: list[dict] = [
    {
        "id": "EMP-001",
        "first_name": "Alice",
        "last_name": "Smith",
        "department": "Engineering",
        "email": "alice.smith@example.com",
    },
    {
        "id": "EMP-002",
        "first_name": "Bob",
        "last_name": "Jones",
        "department": "Sales",
        "email": "bob.jones@example.com",
    },
]

HR_PASSPORTS: list[dict] = [
    {
        "id": "PP-001",
        "employee_id": "EMP-001",
        "issue_date": "2023-01-15",
        "expiry_date": "2028-01-15",
    },
]

LEGAL_CASES: list[dict] = [
    {
        "id": "LC-001",
        "case_number": "2024-CV-00123",
        "summary": "Contract dispute with vendor",
        "status": "Active",
    },
]
