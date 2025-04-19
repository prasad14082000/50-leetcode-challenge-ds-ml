# Write your solution here
def myAtoi(s):
    s = s.lstrip() # Step 1: Remove leading space
    if not s:
        return 0
    
    sign = 1
    index = 0
    result = 0

    if s[0] == '-' or s[0] =='+':
        sign = -1 if s[0] == '-' else 1
        index += 1

    while index < len(s) and s[index].isdigit():
        result = result * 10 + int(s[index])
        index += 1

    result *= sign

    #Step 4: Clamp tp 32-bit integer range
    INT_MIN, INT_MAX = -2**31, 2**31-1
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX
    
    return result
