import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)


def add(a: int | float, b: int | float) -> int | float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    logging.info(f"Adding {a} and {b}")
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    logging.info(f"Subtracting {a} and {b}")
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    logging.info(f"Multiplying {a} and {b}")
    return a * b


def divide(a: int | float, b: int | float) -> int | float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    logging.info(f"Dividing {a} and {b}")
    return a / b


def square(a: int | float) -> int | float:
    if not isinstance(a, (int, float)):
        raise ValueError("Value must be a number")
    logging.info(f"Squaring {a}")
    return a ** 2


def square_root(a: int | float) -> int | float:
    if not isinstance(a, (int, float)):
        raise ValueError("Value must be a number")
    if a < 0:
        raise ValueError("Value must be more than 0")
    logging.info(f"Square root of {a}")
    return a ** 0.5


def log_action(action: str, user: str = "default"):
    timestamp = datetime.now().isoformat()
    record = {"time": timestamp, "user": user, "actions": action}

    with open("history.json", "a") as f:
        f.write(f"{record}\n")

    logging.info(f"Logged action: {action} by {user}")
