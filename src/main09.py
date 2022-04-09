from main03 import extract_probs
from main04 import update


def main():
    sequence = "TACTTCGATTTAAGCGCGGCGGCCTATATTA"
    probs = extract_probs(sequence)

    bases = list(sorted(set(sequence)))
    prediction = ""

    n_chains = 3
    preds = (1, 0, 0, 0)

    for i in range(n_chains):
        preds = preds @ probs
        print(" | ".join(map(lambda x: f"{x:.8f}", preds)))
        prediction += bases[preds.argmax()]
    print(f"prediction: {prediction}")


if __name__ == "__main__":
    main()
