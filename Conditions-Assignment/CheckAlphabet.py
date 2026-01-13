vovel = ['a', 'e', 'i', 'o', 'u']

ch = input()
if ch.lower() in vovel:
    print("Alphabet is vovel!")
elif ch.isalpha():
    print("Alphabet is consonant!")
else:
    print("invalid input!")

