import sys


def count_words(path: str) -> int:
    word_count = 0
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            word_count += len(line.split())

    return word_count


def count_lines(path: str) -> int:
    line_count = 0
    with open(path, "r", encoding="utf-8") as file:
        for _ in file:
            line_count += 1
    return line_count


def search_word(path: str, word: str) -> list[str]:
    line_list = [] 
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if word in line:
                line_list.append(line)

    return line_list

def main() -> None:
    args = len(sys.argv) - 1  # ignore the filename
    if args < 2:
        print("error: expected at least 2 arguments", file=sys.stderr)
        sys.exit(2)

    file_path = sys.argv[1]
    action = sys.argv[2]

    if action == "count_words":
        word_count = count_words(file_path)
        print("Words: ", word_count)
    elif action == "count_lines":
        line_count = count_lines(file_path)
        print("Lines: ", line_count)
    elif action == "search_word":
        if args < 3:
            print("error: expected at least 3 arguments", file=sys.stderr)
            sys.exit(2)

        word = sys.argv[3]
        lines_found = search_word(file_path, word)
        for line in lines_found:
            print(line, end="")  # remove newline characters at the end
        print()  # additional newline to make the output readable
    else:
        print(
            "error: action must be one of: ",
            "\n - count_words",
            "\n - count_lines",
            "\n - search_word",
            file=sys.stderr,
        )
        sys.exit(2)


if __name__ == "__main__":
    main()
