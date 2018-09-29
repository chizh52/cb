import sys


def main():
    last_key = None
    count = 0

    for line in sys.stdin:
        word, one = line.strip().split('\t')
        if last_key is None:
            last_key = word
            count = 1
        elif word != last_key:
            sys.stdout.write("{0}\t{1}\n".format(last_key, count))
            last_key = word
            count = 1
        else:
            count += 1

    sys.stdout.write("{0}\t{1}\n".format(last_key, count))


if __name__ == "__main__":
    main()

