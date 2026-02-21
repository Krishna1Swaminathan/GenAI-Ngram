import random

def main():
    with open("data/all_methods_clean.txt", "r") as f:
        methods = f.readlines()

    random.shuffle(methods)

    val = methods[:1000]
    self_test = methods[1000:2000]
    training_pool = methods[2000:]

    print(f"Validation: {len(val)}")
    print(f"Self Test: {len(self_test)}")
    print(f"Training pool: {len(training_pool)}")

    # Save files
    with open("data/val.txt", "w") as f:
        f.writelines(val)

    with open("data/self_test.txt", "w") as f:
        f.writelines(self_test)

    with open("data/train_full.txt", "w") as f:
        f.writelines(training_pool)

if __name__ == "__main__":
    main()
