import sys

def main():
    for line in sys.stdin:
        word, count = line.strip().split("\t")
        sys.stdout.write("{0}\t{1}\n".format(int(count) * -1, word))


if __name__ == "__main__":
    main()
