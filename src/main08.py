from main03 import extract_probs
from main04 import update


def main():
    sequence = "SRCCRRSSCSRCSR"
    probs = extract_probs(sequence)

    n_chains = 5
    preds = (0, 1, 0)
    for i in range(n_chains):
        preds = preds @ probs
        print(" | ".join(map(lambda x: f"{x:.8f}", preds)))


if __name__ == "__main__":
    main()
