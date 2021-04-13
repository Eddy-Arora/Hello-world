
names = ["Aaditya", "Rahul", "Yash", "Rishanh"]
wishes= ["Good morning","Good morning","Good night","Good afternoon"]
for name in names:
    print(name)
for wish in wishes:
    print(wish)

print("----------")
for i in range(4):
    print(f"{i}. {wishes[i]} {names[i]}")

