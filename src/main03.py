import numpy as np


def main():
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


if __name__ == "__main__":
    main()
