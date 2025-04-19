# Write your solution here
def reverse(x):
    #step 1: Detect the sign
    sign = -1 if x < 0 else 1

    #step 2: Reverse the absolute value
    reversed_num = int(str(abs(x))[::-1]) * sign

    #step 3: Check if it fits in 32-bit signed integer range
    if -2**31 <= reversed_num <= 2**31 -1:
        return reversed_num
    else:
        return 0