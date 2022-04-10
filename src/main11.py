def main():
    values = (
        "159,82,187,194,179,115,197,102,105,104,95,126,74,143,143,"
        "127,98,70,92,170,168,182,149,85,137,100,170,180,61,177,"
        "86,195,198,182,150,197,103,103,186,100,96,196"
    ).split(",")

    top = 200
    bottom = 60

    bands = list("ABCD")
    size = len(bands)
    width = (top - bottom) / size

    get_band = lambda x: int((int(x) - int(bottom)) / width)

    sequence = list(map(get_band, values))

    print(",".join(map(str, sequence)))
    print("".join(map(lambda x: bands[x], sequence)))


if __name__ == "__main__":
    main()
