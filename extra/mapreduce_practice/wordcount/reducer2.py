import sys


def main():
    counter = 0
    for line in sys.stdin:
        count, word = line.strip().split('\t')
        sys.stdout.write("{0}\t{1}\n".format(word, int(count) * -1))
        counter += 1
        if counter == 10:
            break


if __name__ == "__main__":
    main()

