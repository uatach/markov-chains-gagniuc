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


def fill02(ratio):
    white = int(100 * ratio)
    black = 100 - white
    assert white + black == 100
    return white * "W" + black * "B"


def algo02():
    jars = {
        "W": fill02(0.2),
        "B": fill02(0.6),
    }

    print(simulate01(jars))


def algo03():
    sequence = "SRRSRSRRSRSRRSS"

    symbols = list(sorted(set(sequence)))
    n_symbols = len(symbols)

    counts = np.zeros((n_symbols, n_symbols))

    for x in range(1, len(sequence) - 1):
        i = symbols.index(sequence[x])
        j = symbols.index(sequence[x + 1])
        counts[i][j] += 1

    print(counts)
    print(np.round(counts / counts.sum(axis=1, keepdims=True), 1))


def algo04():
    probs = np.array(
        [
            [
                0.2,
                0.625,
            ],
            [
                0.8,
                0.375,
            ],
        ]
    )

    n_chains = 5
    preds = (1, 0)
    for i in range(n_chains):
        x = preds[0] * probs[0][0] + preds[1] * probs[0][1]
        y = preds[0] * probs[1][0] + preds[1] * probs[1][1]
        preds = (x, y)
        print(" | ".join(map(lambda x: f"{x:.8f}", preds)))


if __name__ == "__main__":
    algo04()
