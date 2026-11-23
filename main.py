import os

JOKE = (
    "The demo ran perfectly: my AI coding agent wrote the code, fixed the bugs, "
    "and rehearsed every click \u2014 my only live contribution was moving the mouse "
    "slowly, so the audience would believe a human was driving."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
