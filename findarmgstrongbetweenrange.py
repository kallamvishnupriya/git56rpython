def check_armstrong_number(start, end):
    for i in range(start, end+1):
        temp = i
        # count digits using while loop
        digits = 0
        temp2 = temp
        while temp2 > 0:
            digits += 1
            temp2 //= 10

        # now calculate sum of powers
        total = 0
        temp2 = temp
        while temp2 > 0:
            digit = temp2 % 10
            total += digit ** digits
            temp2 //= 10

        if i == total:
            print(i)

check_armstrong_number(1, 1000)