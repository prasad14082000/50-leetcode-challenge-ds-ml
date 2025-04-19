# Day 08: String to Integer (atoi)

## 🧠 Problem

Given a string `s`, convert it to a 32-bit signed integer. Follow these steps:

1. Ignore leading whitespace.
2. Check for an optional '+' or '-' sign.
3. Read in the digits until a non-digit character is found.
4. Clamp the integer to fit in the 32-bit signed integer range: `[-2³¹, 2³¹-1]`.

---

## 🧪 Examples

```python
Input: "42"
Output: 42
```

```python
Input: "   -42"
Output: -42
```

```python
Input: "4193 with words"
Output: 4193
```

```python
Input: "words and 987"
Output: 0  # No valid number at the start
```

```python
Input: "-91283472332"
Output: -2147483648  # Clamped to lower limit
```

---

## 🧰 Concepts Used

| Concept            | Explanation                                      |
|---------------------|--------------------------------------------------|
| **Trimming**         | Remove extra whitespace                          |
| **Sign Handling**    | Detect '+' or '-'                                 |
| **Digit Extraction** | Read digits until a non-digit is found            |
| **Boundary Clamping**| Make sure result fits in the valid integer range  |

---

## 🧠 Step-by-Step Logic

1. **Trim Leading Whitespace** using `lstrip()`.
2. Detect the **Sign** (`+` or `-`). Default is `+`.
3. Traverse character by character and accumulate digits into `result`.
4. Multiply by `sign` to apply the correct sign.
5. Clamp the final result between `-2³¹` and `2³¹ - 1`.

---

## 💻 Code

```python
def myAtoi(s):
    s = s.lstrip()  # Step 1: Trim leading spaces.
    if not s:
        return 0

    sign = 1
    index = 0
    result = 0

    if s[0] == '-' or s[0] == '+':
        sign = -1 if s[0] == '-' else 1
        index += 1

    while index < len(s) and s[index].isdigit():
        result = result * 10 + int(s[index])
        index += 1

    result *= sign

    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result
```

---

## 🔁 Example Walkthrough

For `s = "   -42abc"`:

- Trim spaces → `"-42abc"`.
- Detect sign: `sign = -1`.
- Extract digits: `42`.
- Apply sign: `-42`.
- `-42` is in valid range, so return `-42`.

---

## 🕒 Time and Space Complexity

| Type         | Value         |
|--------------|---------------|
| **Time**     | O(n) — linear scan through string |
| **Space**    | O(1) — constant extra space        |

---

## 📝 Notes

This problem is all about defensive coding — handling spaces, signs, and numeric overflows carefully. Perfect practice for real-world programming!

