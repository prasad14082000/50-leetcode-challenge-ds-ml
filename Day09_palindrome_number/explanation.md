# Day 09: Container With Most Water

## 🧠 Problem

Given `n` non-negative integers `height[0], height[1], ..., height[n-1]`, each represents a vertical line on the x-axis. The task is to find two lines that, together with the x-axis, form a container that holds the most water.

---

## 🧪 Examples

```python
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Lines at index 1 and 8 form the container.
```
---

## 🧰 Concepts Used

| Concept                 | Explanation                                       |
|--------------------------|---------------------------------------------------|
| **Two-Pointer Technique**| Start at both ends and move inward smartly.        |
| **Area Calculation**     | `min(height[left], height[right]) * width`.        |
| **Greedy Improvement**   | Always look for a potentially better solution.     |

---

## 🧠 Step-by-Step Logic

1. Place one pointer `left` at the start and `right` at the end of the array.
2. Calculate the area between the two lines using:
   ```
   area = min(height[left], height[right]) * (right - left)
   ```
3. Keep track of the maximum area found so far.
4. Move the pointer with the shorter line inward, since the limiting factor for the area is the shorter height.
5. Repeat until both pointers meet.

---

## 💻 Code

```python
def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, h * width)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
```

---

## 🔁 Example Walkthrough

Given: `height = [1,8,6,2,5,4,8,3,7]`

- Start: `left=0, right=8` → area = 1 * 8 = 8
- Move left to index 1 (`height=8`)
- New area: `min(8,7) * (8-1)` → 7 * 7 = 49 (max so far!)
- Continue moving pointers until they meet, always updating the max if a larger area is found.

Final Answer: `49`

---

## 🕒 Time and Space Complexity

| Type         | Value       |
|--------------|-------------|
| **Time**     | O(n)        |
| **Space**    | O(1)        |

---

## 📝 Notes

This problem is a perfect example of the **two-pointer approach** where you optimize from both sides inward — a strategy that works in many problems involving arrays or sequences!

