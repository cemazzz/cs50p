def main():
    ok(input("File Name: ").strip().lower())


def ok(text):
    if text.endswith((".jpg", ".jpeg")):
        print("image/jpeg")
    elif text.endswith(".gif"):
        print("image/gif")
    elif text.endswith(".pdf"):
        print("application/pdf")
    elif text.endswith(".txt"):
        print("text/plain")
    elif text.endswith(".zip"):
        print("application/zip")
    elif text.endswith(".png"):
        print("image/png")
    else:
        print("application/octet-stream")


main()
