import os

JOKE = (
    "The demo crashed live, and my AI coding agent reacted like a true senior "
    "engineer: it blamed the Wi-Fi, renamed the error a \u201cfeature preview,\u201d "
    "and pushed the postmortem before I\u2019d even finished panicking."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
