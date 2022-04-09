from main01 import simulate


def fill(ratio):
    white = int(100 * ratio)
    black = 100 - white
    assert white + black == 100
    return white * "W" + black * "B"


def main():
    jars = {
        "W": fill(0.2),
        "B": fill(0.6),
    }

    print(simulate(jars))


if __name__ == "__main__":
    main()
