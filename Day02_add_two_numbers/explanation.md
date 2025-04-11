# Day 02: Add Two Numbers

## 🧠 Problem

You are given two numbers, but they are stored as **linked lists**.  
Each node in the list contains **one digit**, and the digits are stored in **reverse order**.

🎯 Your task: Add the two numbers and return the sum as a new linked list (also in reverse order).

---

## 🧪 Example

```
Input:
l1 = 2 → 4 → 3  (represents 342)
l2 = 5 → 6 → 4  (represents 465)

Output:
7 → 0 → 8  (represents 807, because 342 + 465 = 807)
```

---

## 🧰 Tools & Concepts Used

### 1. Linked List
A sequence of nodes, like train cars:
```python
2 → 4 → 3
```

Each node has:
- A `val` (digit)
- A `next` pointer to the next node

### 2. Carry
Just like adding by hand. If a sum is over 9:
- Put one digit in the result
- Carry the rest to the next digit

### 3. Dummy Node
We start the result list with a fake first node (dummy) to make building it easier.

---

## 🧠 Step-by-Step

1. Create a dummy node.
2. Use a `current` pointer to add new nodes to the result list.
3. Use a variable `carry = 0`.
4. Loop through both lists:
   - Add both digits (if they exist) + carry
   - Store the **ones place** in the new node
   - Carry the **tens place**
5. Move to next nodes in l1 and l2.
6. Return `dummy.next` (real result list starts here).

---

## 💻 Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry

        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next
```

---

## 🔁 Example Walkthrough

Let's say:
```
l1 = 2 → 4 → 3
l2 = 5 → 6 → 4
```

Step-by-step:
- 2 + 5 = 7 → result = 7
- 4 + 6 = 10 → result = 0, carry = 1
- 3 + 4 + 1 = 8 → result = 8

Final: `7 → 0 → 8` ✅

---

## 🕒 Time & Space Complexity

- **Time:** O(max(m, n)) — we go through all nodes
- **Space:** O(max(m, n)) — for the result list

---

## 📝 Summary

- Simulate addition just like paper math
- Handle carry carefully
- Linked lists can be tricky, but dummy nodes help a lot

Now you're adding big numbers like a pro — with linked lists!