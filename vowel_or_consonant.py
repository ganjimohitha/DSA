# Question: Check whether a character is a vowel or consonant.

ch = input()
ch = ch.lower()

#if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonent")
