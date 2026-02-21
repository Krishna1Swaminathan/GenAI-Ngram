import random


def load_all_methods(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            tokens = line.strip().split()
            if len(tokens) >= 10:   # enforce 10-token rule early
                data.append(tokens)
    return data


def create_splits(data):
    random.shuffle(data)

    val = data[:1000]
    test = data[1000:2000]

    remaining = data[2000:]

    T1 = remaining[:15000]
    T2 = remaining[:25000]
    T3 = remaining[:35000]

    return T1, T2, T3, val, test

