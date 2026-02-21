import re

def extract_methods_from_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()
    except:
        return []

    # Simple method pattern (not perfect but acceptable for assignment)
    pattern = r'(?:public|protected|private)[^{;]+?\([^)]*\)\s*\{[^}]*\}'

    matches = re.findall(pattern, code, re.DOTALL)
    return matches


def main():
    with open("data/java_files.txt", "r") as f:
        files = f.readlines()

    all_methods = []

    for file in files:
        file = file.strip()
        methods = extract_methods_from_file(f"data/{file}")
        all_methods.extend(methods)

    print(f"Extracted {len(all_methods)} methods")

    with open("data/all_methods_raw.txt", "w", encoding="utf-8") as out:
        for m in all_methods:
            out.write(m.replace("\n", " ") + "\n")


if __name__ == "__main__":
    main()
