def convert(text):
    return text.replace(":)", "🙂").replace(":()", "😮").replace(":(", "🙁")


def main():
    print(convert(input()))


main()
