import re

def tokenize(method):
    # Separate punctuation from words
    method = re.sub(r'([(){};.,=+\-*/<>!&|])', r' \1 ', method)
    method = re.sub(r'\s+', ' ', method)
    return method.strip()

def is_ascii(s):
    try:
        s.encode("ascii")
        return True
    except:
        return False

def main():
    with open("data/all_methods_raw.txt", "r", encoding="utf-8") as f:
        methods = f.readlines()

    cleaned = set()

    for m in methods:
        m = m.strip()

        # Remove non-ASCII
        if not is_ascii(m):
            continue

        # Tokenize
        m = tokenize(m)

        tokens = m.split()

        # Filter short methods (<10 tokens)
        if len(tokens) < 10:
            continue

        cleaned.add(m)

    print(f"Final cleaned methods: {len(cleaned)}")

    with open("data/all_methods_clean.txt", "w", encoding="utf-8") as out:
        for m in cleaned:
            out.write(m + "\n")


if __name__ == "__main__":
    main()
