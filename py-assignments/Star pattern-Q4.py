n = int(input("Enter the maximum number of stars for the last row: "))

for i in range(1, n + 1, 2):
    print("*" * i)