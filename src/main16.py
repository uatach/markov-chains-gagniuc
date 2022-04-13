from main03 import extract_probs


def main():
    sequence = (
        "BABABDCB"
        "ABDCBCBD"
        "CBDCBABD"
        "CBCBCBCB"
        "DCBCBDCB"
        "DCBDCBAB"
        "ABABDCBD"
        "CBABABDC"
        "BABCBABC"
        "BABDCBDC"
        "BABABABA"
        "BCBABCBD"
        "CBDC"
    )
    print(extract_probs(sequence))


if __name__ == "__main__":
    main()
