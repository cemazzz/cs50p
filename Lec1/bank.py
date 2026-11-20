oki = input("Greeting: ").strip().lower()
if oki.startswith("hello"):
    print("$0")
elif oki.startswith("h"):
    print("$20")
else:
    print("$100")
