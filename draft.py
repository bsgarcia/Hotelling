import numpy as np

def main():

    a = np.random.randint(10, size=10)
    print(a)
    print(normalize(a, min_=0, max_=10))


def normalize(x, min_, max_):
    x_scaled = (x - min_) / (max_ - min_)
    return x_scaled

if __name__ == "__main__":

    main()