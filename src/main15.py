import numpy as np

from main01 import draw
from main14 import fill


configs = {
    "A": {
        "A": 0,
        "B": 1,
        "C": 0,
        "D": 0,
    },
    "B": {
        "A": 1 / 3,
        "B": 0,
        "C": 1 / 3,
        "D": 1 / 3,
    },
    "C": {
        "A": 0,
        "B": 1,
        "C": 0,
        "D": 0,
    },
    "D": {
        "A": 0,
        "B": 0,
        "C": 1,
        "D": 0,
    },
}


def simulate(jars):
    draws = 100

    choice = "A"
    ball = draw(jars["A"])
    output = f"{ball}"

    for _ in range(draws):
        choice = ball
        ball = draw(jars[choice])
        output += f"{ball}"
    return output


def main():
    jars = {k: fill(v, 100) for k, v in configs.items()}
    print(simulate(jars))


if __name__ == "__main__":
    main()
