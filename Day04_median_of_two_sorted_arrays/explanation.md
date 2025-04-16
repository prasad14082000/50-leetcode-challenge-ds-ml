# Day 04: Median of Two Sorted Arrays

## 🧠 Problem

Given two sorted arrays `nums1` and `nums2`, find the **median** of the combined sorted array, but you are **not allowed to fully merge them**.

The goal is to solve it in **O(log(min(m, n)))** time, where `m` and `n` are the sizes of the two arrays.

---

## 🧪 Examples

```python
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0
Explanation: Combined = [1, 2, 3]. Median = 2.
```

```python
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
Explanation: Combined = [1, 2, 3, 4]. Median = (2 + 3) / 2 = 2.5.
```

---

## 🧰 Concepts Used

| Concept            | Explanation                                   |
|---------------------|-----------------------------------------------|
| **Median**          | Middle number in a sorted list                |
| **Binary Search**   | Splitting the search space in half each step  |
| **Partitioning**    | Splitting two arrays at smart positions       |

---

## 🧠 Step-by-Step Logic

1. Ensure `nums1` is the **smaller array** (helps optimize binary search).
2. Use **binary search** on `nums1` to try slicing it at position `i`.
3. Automatically slice `nums2` at `j = half_len - i`.
4. Check the condition:
   ```
   nums1[i-1] <= nums2[j]  AND  nums2[j-1] <= nums1[i]
   ```
5. If the condition is true → calculate the median! 🎯
6. If not:
   - Adjust `i` using binary search until the perfect partition is found.

---

## 💻 Code

```python
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    half_len = (m + n + 1) // 2

    left, right = 0, m

    while left <= right:
        i = (left + right) // 2
        j = half_len - i

        if i < m and nums2[j - 1] > nums1[i]:
            left = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            right = i - 1
        else:
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0
```

---

## 🔁 Example Walkthrough

For `nums1 = [1, 2]` and `nums2 = [3, 4]`:

1. Binary search slices both lists until the left side holds 2 numbers.
2. Checks the partition condition.
3. Calculates `max_of_left = 2` and `min_of_right = 3`.
4. Final median = `(2 + 3) / 2 = 2.5`.

---

#🧠 Time Complexity
⚡ What’s Happening?
The code uses:

Binary Search on the smaller array.

Let’s say:

ini
Copy code
m = length of nums1
n = length of nums2
In each binary search step:

You cut the search range in half.

So the number of steps is:


log₂(m)  (if nums1 is the array being searched)
👉 Because we always search the smaller of the two arrays (nums1 or nums2), the complexity is based on the smaller size.

✅ Final Time Complexity:

O(log(min(m, n)))
💡 Meaning:
Even if nums2 has a million elements, as long as nums1 is small, the search will be super fast.

🧠 Space Complexity
⚡ What’s Happening?
The algorithm doesn’t create new arrays.

It uses a few variables:

left, right, i, j, max_of_left, min_of_right

All of those are just numbers (fixed-size) no matter how long your input is.

✅ Final Space Complexity:

O(1)  (constant space)
💡 Meaning:
No extra memory is used that grows with input size.

🏆 Final Complexity Table
Complexity Type	Value
Time	O(log(min(m, n)))
Space	O(1) (constant space)
💡 Why Is This Important?
✅ This is way more efficient than:

Brute-force merging (O(m + n))

Sorting merged arrays (O((m+n)log(m+n)))

In coding interviews, being able to write logarithmic time algorithms like this is often the difference between a pass and a fail. 💪


⚠️ What About Complexity?
Sorting itself has a cost.

Step	Complexity
Sorting nums1	O(m log m)
Sorting nums2	O(n log n)
Median Search	O(log(min(m, n)))
So the total time becomes:


O(m log m + n log n)  (if sorting is needed first)
💡 Bottom Line:
Scenario	Algorithm Used	Time Complexity
Arrays are sorted	Binary Search Partition	O(log(min(m, n)))
Arrays are unsorted	Sort both + Median Algorithm	O(m log m + n log n)

---

## 📝 Notes

This problem is a brilliant example of how binary search can be used to solve complex problems without brute force! Learning this improves your algorithm skills massively.
