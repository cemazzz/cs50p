ok = (
    input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    .strip()
    .lower()
)
if ok == "42" or ok == "forty two" or ok == "forty-two":
    print("Yes")
else:
    print("No")
