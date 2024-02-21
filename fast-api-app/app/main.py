from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/calc/plus/{num1}/{num2}")
def read_plus(num1: float, num2: float):
    return {"result": num1 + num2}

@app.get("/calc/minus/{num1}/{num2}")
def read_minus(num1: float, num2: float):
    return {"result": num1 - num2}

@app.get("/calc/times/{num1}/{num2}")
def read_times(num1: float, num2: float):
    return {"result": num1 * num2}

@app.get("/calc/divided/{num1}/{num2}")
def read_divided(num1: float, num2: float):
    return {"result": num1 / num2}