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

    n_chains = 50
    preds = (1, 0)
    for i in range(n_chains):
        x = preds[0] * probs[0][0] + preds[1] * probs[0][1]
        y = preds[0] * probs[1][0] + preds[1] * probs[1][1]

        if np.allclose(preds, (x, y)):
            print(f"steady steate at {i}")
            return
        else:
            print(f"{i:02d}: [{x:.8f} | {y:.8f}]")
        preds = (x, y)


if __name__ == "__main__":
    main()
