import string
import random

def gen_domain():
    return "".join([
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_lowercase)
    ]) + ".ru"

def main():
    with open("sample.txt", "w") as sample:
        for i in range(10000000):
            sample.write(
                gen_domain() + "\t" + gen_domain() + "\n"
            )


if __name__ == "__main__":
    main()
