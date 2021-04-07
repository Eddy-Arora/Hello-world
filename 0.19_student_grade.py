age = int(input("Enter age: "))


if age < 5:
    print("Infant")
elif age < 13:
    print("child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("adult")
else:
    print("Sr. citizen")
    