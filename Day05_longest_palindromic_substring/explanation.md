# Day 05: Longest Palindromic Substring

## 🧠 Problem

Given a string `s`, find the **longest substring** that reads the same forwards and backwards.

---

## 🧪 Examples

```python
Input: "babad"
Output: "bab" or "aba"
```

```python
Input: "cbbd"
Output: "bb"
```

---

## 🧰 Concepts Used

| Concept                   | Explanation                                      |
|----------------------------|--------------------------------------------------|
| **Palindrome**            | A string that reads the same forward and backward. |
| **Expand Around Center**  | For each character (or pair), expand outward to check palindromes. |

---

## 🧠 Step-by-Step Logic

1. Loop through each character in the string.
2. Treat the character as the **center** of a possible palindrome.
3. Expand outwards from the center as long as the characters on both sides are equal.
4. Track the **longest palindrome** found during this process.
5. Return the longest substring.

This method checks both:
- **Odd-length palindromes** (centered at one character).
- **Even-length palindromes** (centered between two characters).

---

## 💻 Code

```python
def longestPalindrome(s):
    if not s:
        return ""

    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""

    for i in range(len(s)):
        temp1 = expandAroundCenter(i, i)         # Odd-length
        temp2 = expandAroundCenter(i, i + 1)     # Even-length

        if len(temp1) > len(longest):
            longest = temp1
        if len(temp2) > len(longest):
            longest = temp2

    return longest
```

---

## 🔁 Example Walkthrough

For `s = "babad"`:

- Center at index `1` → expands to `"bab"`.
- Center at index `2` → expands to `"aba"`.
- The longest of them is either `"bab"` or `"aba"` — both valid answers.

---

## 🕒 Time and Space Complexity

| Type         | Value                |
|--------------|-----------------------|
| **Time**     | O(n²) — for each center we may expand almost the whole string |
| **Space**    | O(1) — constant extra space (ignoring return value) |

---

## 📝 Notes

This problem is a great example of **expansion strategy** where you use two pointers and expand outward to explore the solution space. Once you master this, many string problems will become easier!
