import os

PITCH = "Tell an agent in plain words about the app idea you keep talking about, and it will build a first version you can actually try \u2014 with no coding from you, and the idea stays yours."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PITCH + "\n")


if __name__ == "__main__":
    main()
