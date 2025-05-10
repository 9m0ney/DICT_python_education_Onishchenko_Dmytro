def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")


def format_plain():
    return input("Text: ")


def format_bold():
    return f"**{input('Text: ')}**"


def format_italic():
    return f"*{input('Text: ')}*"


def format_inline_code():
    return f"`{input('Text: ')}`"


def format_link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def format_header():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                break
            else:
                print("The level should be within the range of 1 to 6")
        except ValueError:
            print("Please enter a number from 1 to 6")
    text = input("Text: ")
    return f"{'#' * level} {text}\n"


def format_new_line():
    return "\n"


def format_list(ordered=False):
    while True:
        try:
            rows = int(input("Number of rows: "))
            if rows > 0:
                break
            else:
                print("The number of rows should be greater than zero")
        except ValueError:
            print("Please enter a valid number")

    result = []
    for i in range(1, rows + 1):
        row = input(f"Row #{i}: ")
        if ordered:
            result.append(f"{i}. {row}")
        else:
            result.append(f"* {row}")
    return "\n".join(result)


def main():
    result = ""
    formatters = {
        "plain": format_plain,
        "bold": format_bold,
        "italic": format_italic,
        "inline-code": format_inline_code,
        "link": format_link,
        "header": format_header,
        "new-line": format_new_line,
        "ordered-list": lambda: format_list(ordered=True),
        "unordered-list": lambda: format_list(ordered=False)
    }

    while True:
        command = input("Choose a formatter: ")
        if command == "!help":
            print_help()
        elif command == "!done":
            with open("output.md", "w", encoding="utf-8") as file:
                file.write(result)
            break
        elif command in formatters:
            result += formatters[command]() + "\n"
            print(result.strip())
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()
