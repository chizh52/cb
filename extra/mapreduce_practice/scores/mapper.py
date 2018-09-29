import sys

for l in sys.stdin:
    name, value = l.strip().split("\t")
    if value.isdigit():
        sys.stdout.write("{0}\t{1}\t{2}\n".format(name, "score", value))
    else:
        sys.stdout.write("{0}\t{1}\t{2}\n".format(name, "subject", value))
