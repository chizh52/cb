import sys

def main():
    for line in sys.stdin:
        from_site, to_site = line.strip().split()
        sys.stdout.write("{0}\t{1}\n".format(to_site, from_site))


if __name__ == "__main__":
    main()
