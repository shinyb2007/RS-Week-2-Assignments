str1 = input("Enter First String: ").lower()
str2 = input("Enter Second String: ").lower()

list1 = list(str1)
list2 = list(str2)

list1.sort()
list2.sort()

if list1 == list2:
    print("Strings are Anagrams")

else:
    print("Strings are Not Anagrams")