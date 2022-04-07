import random


random.seed(42)


def algo01():
    def draw(jar):
        choice = random.randrange(len(jar))
        return jar[choice]

    jars = {
        "W": "WWBBBBBBBB",
        "B": "WWWWWBBBBB",
    }

    draws = 17
    choice = random.choice(list(jars.keys()))
    ball = draw(jars[choice])

    output = f" Jar {choice}[{ball}],"

    for _ in range(draws):
        choice = ball
        ball = draw(jars[choice])
        output += f" Jar {choice}[{ball}],"

    print(output)


if __name__ == "__main__":
    algo01()
