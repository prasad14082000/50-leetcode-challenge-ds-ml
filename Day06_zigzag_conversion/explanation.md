# Day 06: Zigzag Conversion

## 🧠 Problem

Given a string `s` and an integer `numRows`, write the string in a **Zigzag pattern** on `numRows` and read it line by line.

---

## 🧪 Example

```
Input:
s = "PAYPALISHIRING"
numRows = 3

Zigzag Pattern:
P   A   H   N
A P L S I I G
Y   I   R

Output: "PAHNAPLSIIGYIR"
```

---

## 🧰 Concepts Used

| Concept                | Explanation                                        |
|-------------------------|----------------------------------------------------|
| **Zigzag Pattern**      | Write down the string in a wave-like shape          |
| **List of Strings**     | Use an array to collect characters for each row     |
| **Direction Control**   | Flip direction at the top and bottom of rows        |

---

## 🧠 Step-by-Step Logic

1. If `numRows` is 1, return the original string (no zigzag possible).
2. Create a list of strings for each row.
3. Start at row `0` and direction `down`.
4. For each character in the string:
    - Add it to the current row.
    - If you're at the **top** (`row == 0`) or **bottom** (`row == numRows-1`), reverse direction.
    - Move `current_row` based on direction.
5. Join all rows together and return the final string!

---

## 💻 Code

```python
def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [""] * numRows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return "".join(rows)
```

---

## 🔁 Example Walkthrough

For `s = "PAYPALISHIRING"` and `numRows = 3`:

```
Row 0: P   A   H   N
Row 1: A P L S I I G
Row 2: Y   I   R
```

Final concatenated output: `"PAHNAPLSIIGYIR"`

---

## 🕒 Time and Space Complexity

| Type         | Value                   |
|--------------|--------------------------|
| **Time**     | O(n) — single pass over input string |
| **Space**    | O(n) — for the result string         |

---

## 📝 Notes

This problem is a great exercise in understanding:
- Movement patterns in arrays (zigzag, spiral, waves)
- Direction flipping logic (`going_down`)
- Organizing multi-level data with lists.

It's simple, elegant, and shows up often in interview rounds to test your systematic thinking!
