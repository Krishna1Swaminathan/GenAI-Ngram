from ngram_model import NGramModel


def load_file(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            tokens = line.strip().split()
            data.append(tokens)
    return data


if __name__ == "__main__":
    train_data = load_file("data/train.txt")
    val_data = load_file("data/val.txt")

    for n in [3, 5, 7]:
        print(f"\nTraining {n}-gram model")

        model = NGramModel(n, alpha=0.1)

        print("Building vocab...")
        model.build_vocab(train_data)

        print("Training...")
        model.train(train_data)

        ppl = model.perplexity(val_data)
        print(f"Validation Perplexity (n={n}): {ppl}")
