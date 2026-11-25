def main():
    text = input("Expression: ")
    uk(text)


def uk(text):
    x, y, z = text.split(" ")
    n_x = float(x)
    n_z = float(z)
    if y == "+":
        print(f"{n_x + n_z}")
    if y == "-":
        print(f"{n_x - n_z}")
    if y == "*":
        print(f"{n_x * n_z}")
    if y == "/":
        print(f"{n_x / n_z}")


main()
