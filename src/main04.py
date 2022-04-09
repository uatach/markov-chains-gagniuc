import numpy as np


def main():
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
    main()
