import numpy as np

from main04 import probs


def main():
    a, b = probs[0][0], probs[1][1]
    preds = ((1 - b) / (2 - (a + b)), (1 - a) / (2 - (a + b)))
    print(" | ".join(map(lambda x: f"{x:.8f}", preds)))


if __name__ == "__main__":
    main()
