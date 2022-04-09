from main03 import extract_probs


def main():
    sequence = "TACTTCGATTTAAGCGCGGCGGCCTATATTA"
    probs = extract_probs(sequence)

    n_chains = 5
    preds = (1, 0, 0, 0)

    for i in range(n_chains):
        preds = preds @ probs
        print(" | ".join(map(lambda x: f"{x:.8f}", preds)))


if __name__ == "__main__":
    main()
