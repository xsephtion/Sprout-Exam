from pydantic import BaseModel
from enum import Enum
from typing import Optional


class EmployeeType(str, Enum):
    REGULAR = "regular"
    CONTRACTUAL = "contractual"


class Employee(BaseModel):
    first_name: str
    last_name: str
    email: str
    employee_type: EmployeeType
    number_of_leaves: Optional[int] = None
    benefits: Optional[str] = None
    contract_end_date: Optional[str] = None
    project: Optional[str] = None


class Login(BaseModel):
    username: str
    password: str
