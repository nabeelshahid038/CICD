from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Math and Student API")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "FastAPI CI/CD is working!"}


class Student(BaseModel):
    name: str
    marks: float


@app.post("/result")
def calculate_result(student: Student) -> dict[str, str | float]:
    status = "Pass" if student.marks >= 50 else "Fail"
    return {"name": student.name, "marks": student.marks, "status": status}


@app.get("/add")
def add(a: float, b: float) -> dict[str, float]:
    return {"result": a + b}


@app.get("/subtract")
def subtract(a: float, b: float) -> dict[str, float]:
    return {"result": a - b}


@app.get("/multiply")
def multiply(a: float, b: float) -> dict[str, float]:
    return {"result": a * b}


@app.get("/divide")
def divide(a: float, b: float) -> dict[str, float]:
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}


@app.get("/square")
def square(n: float) -> dict[str, float]:
    return {"result": n * n}
