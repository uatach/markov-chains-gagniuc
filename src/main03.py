import numpy as np


def extract_counts(sequence):
    symbols = list(sorted(set(sequence)))
    size = len(symbols)

    counts = np.zeros((size, size))

    for x in range(1, len(sequence) - 1):
        i = symbols.index(sequence[x])
        j = symbols.index(sequence[x + 1])
        counts[i][j] += 1
    return counts


def extract_probs(sequence):
    counts = extract_counts(sequence)
    return counts / counts.sum(axis=1, keepdims=True)


def main():
    sequence = "SRRSRSRRSRSRRSS"
    probs = np.round(extract_probs(sequence), 1)
    print(extract_counts(sequence))
    print(probs)


if __name__ == "__main__":
    main()
