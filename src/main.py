import random

import numpy as np


random.seed(42)


def draw01(jar):
    choice = random.randrange(len(jar))
    return jar[choice]


def simulate01(jars):
    draws = 17
    choice = random.choice(list(jars.keys()))
    ball = draw01(jars[choice])
    output = f" Jar {choice}[{ball}],"

    for _ in range(draws):
        choice = ball
        ball = draw01(jars[choice])
        output += f" Jar {choice}[{ball}],"
    return output


def algo01():
    jars = {
        "W": "WWBBBBBBBB",
        "B": "WWWWWBBBBB",
    }

    print(simulate01(jars))


def fill(ratio):
    white = int(100 * ratio)
    black = 100 - white
    assert white + black == 100
    return white * "W" + black * "B"


def algo02():
    jars = {
        "W": fill(0.2),
        "B": fill(0.6),
    }

    print(simulate01(jars))


def algo03():
    sequence = "SRRSRSRRSRSRRSS"

    symbols = list(sorted(set(sequence)))
    n_symbols = len(symbols)

    counts = np.zeros((n_symbols, n_symbols))

    for x in range(1, len(sequence) - 1):
        i = symbols.index(sequence[x])
        j = symbols.index(sequence[x+1])
        counts[i][j] += 1

    print(counts)
    print(np.round(counts / counts.sum(axis=1, keepdims=True), 1))


if __name__ == "__main__":
    algo03()
