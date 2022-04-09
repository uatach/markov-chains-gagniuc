import numpy as np


def update(preds, probs):
    x = preds[0] * probs[0][0] + preds[1] * probs[1][0]
    y = preds[0] * probs[0][1] + preds[1] * probs[1][1]
    return (x, y)


def main():
    probs = np.array(
        [
            [
                0.375,
                0.625,
            ],
            [
                0.8,
                0.2,
            ],
        ]
    )

    n_chains = 5
    preds = (0, 1)
    for i in range(n_chains):
        preds = update(preds, probs)
        print(" | ".join(map(lambda x: f"{x:.8f}", preds)))


if __name__ == "__main__":
    main()
