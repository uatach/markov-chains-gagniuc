import random


random.seed(42)


def algo01():
    def draw(jar):
        choice = random.randrange(len(jar))
        return jar[choice]

    jars = [
        "WWBBBBBBBB",
        "WWWWWBBBBB",
    ]

    draws = 17
    choice = random.randrange(len(jars))
    ball = draw(jars[choice])

    output = f" Jar W[{ball}],"

    for _ in range(draws):
        if ball == "W":
            ball = draw(jars[0])
            output += f" Jar W[{ball}],"
        else:
            ball = draw(jars[1])
            output += f" Jar B[{ball}],"

    print(output)


if __name__ == "__main__":
    algo01()
