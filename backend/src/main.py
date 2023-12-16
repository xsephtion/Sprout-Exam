
from fastapi import FastAPI, HTTPException, Form
from typing import Annotated
from classes.request import Employee, EmployeeType, Login
from classes.db import DatabaseSingleton
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
db = DatabaseSingleton()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):

    if username == "admin" and password == "password":
        return {"message": "Login successful"}
    else:
        raise HTTPException(
            status_code=401, detail="Invalid username or password"
        )


@app.post("/employees")
def create_employee(employee: Employee):
    if employee.employee_type == EmployeeType.REGULAR:
        db.insert_regular_employee(employee)
    elif employee.employee_type == EmployeeType.CONTRACTUAL:
        db.insert_contractual_employee(employee)
    else:
        raise HTTPException(
            status_code=400, detail="Invalid employee type")
    return {"message": "Regular employee created successfully"}


@app.get("/employees")
def get_employees(employee_id: int = None):
    res = db.find_employee_by_id(employee_id)
    if res is None:
        raise HTTPException(
            status_code=404, detail="Employee not found")
    return res


@app.put("/employees/{employee_id}")
def update_regular_employee(employee_id: int, employee: Employee):
    if employee_id < 0:
        raise HTTPException(
            status_code=404, detail="Regular employee not found")
    if db.update_employee_by_id(employee_id, employee) is None:
        raise HTTPException(
            status_code=404, detail="Regular employee not found")
    if employee.employee_type == EmployeeType.REGULAR:
        return {"message": "Regular employee updated successfully"}
    if employee.employee_type == EmployeeType.CONTRACTUAL:
        return {"message": "Contractual employee updated successfully"}


@app.delete("/employees/{employee_id}")
def delete_regular_employee(employee_id: int):
    if employee_id < 0:
        raise HTTPException(
            status_code=404, detail="Regular employee not found")
    db.delete_employee_by_id(employee_id)
    return {"message": "Employee deleted successfully"}
