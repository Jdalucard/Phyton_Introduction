box = [10, 20, 30, 40, 50]
count = 0

while box:
    if box[0] == 30:
        box.pop(0)
        continue
    print(f"Processing {box[0]}")
    box.pop(0)


while count < 50:
    print(f"Count is {count}")
    count += 1*10
    box.append(count)

print(f"Final box contents: {box}")
