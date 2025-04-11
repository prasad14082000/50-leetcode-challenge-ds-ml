# Day 03: Longest Substring Without Repeating Characters

## 🧠 Problem

Given a string `s`, find the **length** of the longest substring without repeating characters.

> A substring is a part of the string that occurs in order and is continuous.

---

## 🧪 Examples

```python
Input: "abcabcbb"
Output: 3
Explanation: The longest substrings without repeating characters are "abc" and "bca", both of length 3.
```

```python
Input: "bbbbb"
Output: 1
Explanation: The longest substring without repeats is just "b".
```

```python
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke".
```

---

## 🧰 Concepts Used

### 1. Set
A data structure that only holds **unique** items — perfect for checking repeats quickly.

### 2. Sliding Window
We use two pointers (`left` and `right`) that move along the string to define a “window” of current characters we are checking.

---

## 🧠 Logic

1. Start with two pointers: `left = 0` and `right = 0`
2. Create an empty set called `seen`
3. Move `right` one step at a time:
   - If the character at `right` is **not in seen**:
     - Add it to the set
     - Update max length
   - If the character **is in seen**:
     - Remove the character at `left` and move `left` forward until no duplicates
4. Keep track of the largest window found.

---

## 💻 Code

```python
def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
            
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

---

## 🔁 Example Walkthrough

For `s = "abcabcbb"`:

- Window starts at "a" → seen = {a}
- Extend to "ab" → seen = {a, b}
- Extend to "abc" → seen = {a, b, c} → max = 3
- Next "a" is a repeat → remove "a", move left
- Now window is "bca", again length = 3

Final answer: **3**

---

## 🕒 Time and Space Complexity

| Type         | Value                     |
|--------------|---------------------------|
| **Time**     | O(n) — each character is visited at most twice |
| **Space**    | O(min(n, m)) — for the set (at most 26 if lowercase only) |

---

## 📝 Notes

- This problem teaches the **sliding window technique** and how to keep a window "clean" from repeats.
- Sets help us check for duplicates super fast!

This is one of the most popular interview questions and teaches you a LOT about string manipulation!