from method_checks import *
from equation_methods import *
from system_methods import *
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()
origins = [
    "http://localhost:8000",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class NonlinearEquations(BaseModel):
    equation: int
    a: float
    b: float
    eps: float
    method: int
    inFile: bool


def write_system_to_file(a):
    with open("1.txt", "w", encoding="utf-8") as f:
        f.writelines(f"i: {a["i"]}\n")
        f.writelines(f"x: {a["x"]}\n")
        f.writelines(f"y: {a["y"]}\n\n")


def write_nonliner_to_file(a):
    with open("1.txt", "w", encoding="utf-8") as f:
        f.writelines(f"Количество итераций: {a["i"]}\n")
        f.writelines(f"Корень {a["x"]}\n")
        f.writelines(f"Значение функции в точке корня {a["res"]}\n\n")


@app.post("/nonLiner")
def solve_nonlinear_equations(nonlinear_equations: NonlinearEquations):
    print(nonlinear_equations)
    if check_single_root(nonlinear_equations.equation, nonlinear_equations.a, nonlinear_equations.b):
        solution = solve(nonlinear_equations.method, nonlinear_equations.equation, nonlinear_equations.a,
                         nonlinear_equations.b, nonlinear_equations.eps)
        if nonlinear_equations.inFile:
            write_nonliner_to_file(solution)
            return FileResponse("1.txt", media_type="text/plain;charset=UTF-8")
        print(solution)
        return solution
    else:
        print({"error": "system doesn't converge to this initial values."})


class SystemEquations(BaseModel):
    system: int
    x0: float
    y0: float
    eps: float
    inFile: bool


@app.post("/system")
def solve_system_equations(system_equations: SystemEquations):
    print(system_equations)
    if check_convergence(system_equations.system, system_equations.x0, system_equations.y0):
        solution = solve_system(system_equations.system, system_equations.x0, system_equations.y0, system_equations.eps)
        if system_equations.inFile:
            write_system_to_file(solution)
            return FileResponse("1.txt", media_type="text/plain;charset=UTF-8")
        print(solution)
        return solution

    else:
        return {"error": "system doesn't converge to this initial values."}


class FileData(BaseModel):
    equation: int
    a: float
    b: float
    eps: float
    method: int
    inFile: bool


@app.post("/file")
def solve_file(file: FileData):
    if file.method in [1, 2, 3]:
        if check_single_root(file.equation, file.a, file.b):
            solution = solve(file.method, file.equation, file.a, file.b, file.eps)
            if file.inFile:
                write_nonliner_to_file(solution)
                return FileResponse("1.txt", media_type="text/plain;charset=UTF-8")
            print(solution)
            return solution
        else:
            print({"error": "system doesn't converge to this initial values."})
    elif file.method == 4:
        if check_convergence(file.equation, file.a, file.b):
            solution = solve_system(file.equation, file.a, file.b,
                                    file.eps)
            if file.inFile:
                write_system_to_file(solution)
                return FileResponse("1.txt", media_type="text/plain;charset=UTF-8")
            print(solution)
            return solution
        else:
            return {"error": "system doesn't converge to this initial values."}
    else:
        return {"error": "method is not"}
