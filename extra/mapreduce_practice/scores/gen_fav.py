import random

def main():
    with open("sample_fav.txt", "w") as sample:
        with open("surnames.txt", "r") as surnames:
            sns = [l.strip() for l in surnames.readlines()]

        with open("subjects_clean.txt", "r") as subjs:
            sbjs = [l.strip() for l in subjs.readlines()]
        for sn in sns:
            sample.write("{0}\t{1}\n".format(sn, random.choice(sbjs)))
 








if __name__ == "__main__":
    main()

