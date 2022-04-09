import numpy as np

from main04 import probs, update


def main():
    n_chains = 50
    preds = (0, 1)
    for i in range(n_chains):
        x, y = update(preds, probs)

        if np.allclose(preds, (x, y)):
            print(f"steady steate at {i}")
            return
        else:
            print(f"{i:02d}: [{x:.8f} | {y:.8f}]")
        preds = (x, y)


if __name__ == "__main__":
    main()
