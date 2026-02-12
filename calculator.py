def add(a: int | float, b: int | float) -> int | float:
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    return a * b


def divide(a: int | float, b: int | float) -> int | float:
    if b == 0:
        raise "Cannot divide by zero"
    return a / b


def square(a: int | float) -> int | float:
    return a ** 2


def square_root(a: int | float) -> int | float:
    return a ** 0.5
