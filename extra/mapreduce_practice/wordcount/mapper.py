import sys

def main():
    for line in sys.stdin:
        for word in line.strip().split():
            sys.stdout.write("{0}\t1\n".format(word.lower()))


if __name__ == "__main__":
    main()
