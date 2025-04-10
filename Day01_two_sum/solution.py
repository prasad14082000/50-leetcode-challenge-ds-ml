# Write your solution here
def twoSum(nums, target):
    seen={}   #this is our magic notebook
    for i, num in enumerate(nums):   #check each number with its index
        need = target - num     # how much more we need to reach this target

        if need in seen:   #have we seen that number before?
            return [seen[need], i]    #if yes, return its index and current index
        
        seen[num] = i  # otherwise, write this number into the notebook.