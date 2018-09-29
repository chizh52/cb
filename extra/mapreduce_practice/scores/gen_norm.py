import random

from scipy.stats import truncnorm

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

# X = get_truncated_normal(mean=3.5, sd=2, low=2, upp=5)

def main():
    with open("sample.txt", "w") as sample:
        with open("surnames.txt", "r") as surnames:
            sns = [l.strip() for l in surnames.readlines()]
 
        X = get_truncated_normal(mean=3.5, sd=2, low=2, upp=5)
        for i in range(10000):
            sample.write("{0}\t{1}\n".format(
                random.choice(sns),
                int(round(X.rvs()))
            ))


if __name__ == "__main__":
    main()

