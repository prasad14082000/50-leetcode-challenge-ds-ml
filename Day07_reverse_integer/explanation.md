# Day 07: Reverse Integer

## 🧠 Problem

Given an integer `x`, reverse its digits. If the reversed integer overflows the 32-bit signed integer range `[-2³¹, 2³¹ - 1]`, return `0`. Otherwise, return the reversed number.

---

## 🧪 Examples

```python
Input: 123
Output: 321
```

```python
Input: -456
Output: -654
```

```python
Input: 1534236469
Output: 0  # Out of 32-bit signed integer range after reversal
```

---

## 🧰 Concepts Used

| Concept            | Explanation                                                |
|---------------------|------------------------------------------------------------|
| **String Conversion** | Turn number into string for easy reversal                  |
| **Sign Handling**      | Store and apply the original sign back after reversing    |
| **Range Checking**     | Make sure result is inside valid integer limits           |

---

## 🧠 Step-by-Step Logic

1. Detect if the number is **negative** or **positive** and store the sign.
2. Convert the **absolute value** of the number into a string, reverse the string, and convert it back into an integer.
3. Reapply the **sign**.
4. Check if the reversed number is within `[-2³¹, 2³¹ - 1]`. If not, return `0`. Otherwise, return the reversed number.

---

## 💻 Code

```python
def reverse(x):
    # Step 1: Detect the sign
    sign = -1 if x < 0 else 1

    # Step 2: Reverse the absolute value
    reversed_num = int(str(abs(x))[::-1]) * sign

    # Step 3: Check for 32-bit signed integer overflow
    if -2**31 <= reversed_num <= 2**31 - 1:
        return reversed_num
    else:
        return 0
```

---

## 🔁 Example Walkthrough

For `x = -456`:

1. The number is negative (`sign = -1`).
2. `abs(-456)` → `456`. Reverse the string: `"654"`.
3. Apply sign: `-654`.
4. `-654` is within the valid range, so return `-654`.

---

## 🕒 Time and Space Complexity

| Type         | Value                             |
|--------------|-----------------------------------|
| **Time**     | O(log₁₀(n)) — one digit at a time |
| **Space**    | O(1) — constant auxiliary space   |

---

## 📝 Notes

This problem helps practice clean, defensive coding — especially when working with systems that have strict memory or storage limits. Handling edge cases (like overflows) is something interviewers really look for!

