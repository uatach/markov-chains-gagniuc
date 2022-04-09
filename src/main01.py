import random


random.seed(42)


def draw(jar):
    choice = random.randrange(len(jar))
    return jar[choice]


def simulate(jars):
    draws = 17
    choice = random.choice(list(jars.keys()))
    ball = draw(jars[choice])
    output = f" Jar {choice}[{ball}],"

    for _ in range(draws):
        choice = ball
        ball = draw(jars[choice])
        output += f" Jar {choice}[{ball}],"
    return output


def main():
    jars = {
        "W": "WWBBBBBBBB",
        "B": "WWWWWBBBBB",
    }

    print(simulate(jars))


if __name__ == "__main__":
    main()
