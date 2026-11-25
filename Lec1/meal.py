def main():
    time = input("What time is it? ").strip()
    timev2 = convert(time)
    if 7 <= timev2 <= 8:
        print("breakfast time")
    if 12 <= timev2 <= 13:
        print("lunch time")
    if 18 <= timev2 <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()
