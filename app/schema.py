import strawberry
from typing import Optional

from app.mocks import HR_EMPLOYEES, HR_PASSPORTS, LEGAL_CASES, SALESFORCE_ORDERS


@strawberry.type
class SalesOrder:
    id: str
    account_name: str
    amount: float
    status: str


@strawberry.type
class Employee:
    id: str
    first_name: str
    last_name: str
    department: str
    email: str


@strawberry.type
class Passport:
    id: str
    employee_id: str
    issue_date: str
    expiry_date: str


@strawberry.type
class LegalCase:
    id: str
    case_number: str
    summary: str
    status: str


@strawberry.type
class Query:
    @strawberry.field(name="salesorder_list")
    def salesorder_list(self) -> list[SalesOrder]:
        return [SalesOrder(**order) for order in SALESFORCE_ORDERS]

    @strawberry.field(name="employee_list")
    def employee_list(self) -> list[Employee]:
        return [Employee(**employee) for employee in HR_EMPLOYEES]

    @strawberry.field(name="get_salesorder_by_id")
    def get_salesorder_by_id(self, id: str) -> Optional[SalesOrder]:
        for order in SALESFORCE_ORDERS:
            if order["id"] == id:
                return SalesOrder(**order)
        return None

    @strawberry.field(name="get_employee_by_id")
    def get_employee_by_id(self, id: str) -> Optional[Employee]:
        for employee in HR_EMPLOYEES:
            if employee["id"] == id:
                return Employee(**employee)
        return None

    @strawberry.field(name="passport_list")
    def passport_list(self) -> list[Passport]:
        return [Passport(**passport) for passport in HR_PASSPORTS]

    @strawberry.field(name="legalcase_list")
    def legalcase_list(self) -> list[LegalCase]:
        return [LegalCase(**case) for case in LEGAL_CASES]


schema = strawberry.Schema(query=Query)
