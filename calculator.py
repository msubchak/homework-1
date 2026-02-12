import logging

logging.basicConfig(level=logging.INFO)


def add(a: int | float, b: int | float) -> int | float:
    logging.info(f"Adding {a} and {b}")
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    logging.info(f"Subtracting {a} and {b}")
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    logging.info(f"Multiplying {a} and {b}")
    return a * b


def divide(a: int | float, b: int | float) -> int | float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    logging.info(f"Dividing {a} and {b}")
    return a / b


def square(a: int | float) -> int | float:
    logging.info(f"Squaring {a}")
    return a ** 2


def square_root(a: int | float) -> int | float:
    logging.info(f"Squaring root of {a}")
    return a ** 0.5
