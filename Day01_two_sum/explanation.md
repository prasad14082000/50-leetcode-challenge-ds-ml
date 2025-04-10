# Day 01: Two Sum

## Problem
You are given:
- A list of numbers called `nums`
- A target number called `target`

You need to find **two different numbers** from the list that add up to the `target`.  
Then, return the positions (indexes) of those two numbers in the list.

## Approach
Create an empty dictionary seen = {}

Loop through each number with its index using enumerate(nums)

For each number:

Calculate how much more you need: target - num

Check if that "needed" number is already in seen

✅ If yes → return both indexes

❌ If no → add current number to the dictionary

## Complexity
Time and Space Complexity:

🕒 Time: O(n) — we only look at each number once

🧠 Space: O(n) — we store seen numbers in a dictionary

## Notes
This is a super common coding interview question.
Understanding it teaches you how to use dictionaries and why they’re so powerful.
Now you know how to solve it in a smart way!