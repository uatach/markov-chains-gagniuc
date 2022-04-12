import numpy as np


probs = np.array(
    [
        [
            1 / 3,
            1 / 3,
            1 / 3,
        ],
        [
            0.5,
            0.5,
            0,
        ],
        [
            0,
            0,
            1,
        ],
    ]
)


def main():
    n_chains = 5
    preds = (1, 0, 0)

    for i in range(n_chains):
        preds = preds @ probs
        print(" | ".join(map(lambda x: f"{x:.8f}", preds)))


if __name__ == "__main__":
    main()
