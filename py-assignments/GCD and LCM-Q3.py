import math

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

gcd = math.gcd(num1, num2)

lcm = (num1 * num2) // gcd

print("GCD =", gcd)
print("LCM =", lcm)