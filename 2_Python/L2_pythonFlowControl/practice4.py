num = int(input("Enter a number: "))
check_later_num = num
s = 0
while num:
    digit = num % 10
    s += digit ** 3
    print("Digit " + str(digit) + " & Sum = " + str(s))
    num //= 10

if s == check_later_num:
    print("The number is an armstrong number!")
else:
    print("The number is not an armstrong number.")
