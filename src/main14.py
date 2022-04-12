import numpy as np

from main01 import draw


configs = {
    "A": {
        "A": 1 / 3,
        "B": 1 / 3,
        "C": 1 / 3,
    },
    "B": {
        "A": 0,
        "B": 0.5,
        "C": 0.5,
    },
    "C": {
        "A": 1,
        "B": 0,
        "C": 0,
    },
}


def fill(config, total=27) -> str:
    return "".join([int(total * v) * k for k, v in config.items()])


def simulate(jars):
    draws = 20

    choice = "A"
    ball = draw(jars["A"])
    output = f" Jar {choice}[{ball}],"

    for _ in range(draws):
        choice = ball
        ball = draw(jars[choice])
        output += f" Jar {choice}[{ball}],"
    return output


def main():
    jars = {k: fill(v) for k, v in configs.items()}

    output = simulate(jars)

    print(jars)
    print(output[::5].replace(" ", ""))
    print(output)


if __name__ == "__main__":
    main()
