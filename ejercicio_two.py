#ask the user to say any real text
text = input("Please enter any text: ")

word=0.5

words= text.split()
count= len(words)

phrase=word*count
phrase_speed = phrase / 1.30 
print(f"takes time to say the sentence, {phrase} seconds" )
print("The number of words is:", count)


print(f"takes time to say the sentence fast, {phrase_speed} fast seconds" )

if phrase > 120:
    print("Flaco Tampoco pedi un testamento.")

