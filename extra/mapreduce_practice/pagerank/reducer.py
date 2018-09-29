import sys

def main():
    last_site = None
    links_from = []

    for line in sys.stdin:
        to_site, from_site = line.strip().split('\t')
        if last_site is None:
            last_site = to_site
            links_from.append(from_site)
        elif to_site == last_site:
            links_from.append(from_site)
        else:
            sys.stdout.write(to_site + "\t" + ", ".join(links_from) + "\n")
            last_site = to_site
            links_from = []

    sys.stdout.write(to_site + "\t" + ", ".join(links_from) + "\n")


if __name__ == "__main__":
    main()

