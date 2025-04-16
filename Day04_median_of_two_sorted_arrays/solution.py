# Write your solution here
'''

for using the binary search for finding the median array the array of numbers used
should be sorted in ascending order.

nums1 = []
nums2 = []

nums1.sort()
nums2.sort()

'''

def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1     #Always binary search on the smaller array

    m, n = len(nums1), len(nums2)
    half_len = (m + n + 1) // 2

    left, right = 0, m
    while left <= right:
        i = (left + right) // 2
        j = half_len - i

        if i < m and nums2[j - 1] > nums1[i]:
            left = i + 1 # i is to small, must move right
        elif i > 0 and nums1[i - 1] > nums2[j]:
            right = i - 1 #i is too big, must move left
        else:
            #found correct partition
            if i == 0: 
                max_of_left = nums2[j - 1]
            elif j == 0: 
                max_of_left = nums1[i - 1]
            else: 
                max_of_left = max(nums1[i - 1], nums2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left  #odd length
            
            if i == m: min_of_right = nums2[j]
            elif j == n: min_of_right = nums1[i]
            else: min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0
    

#💡 Bottom Line:
#Scenario	           Algorithm Used	                    Time Complexity
#Arrays are sorted	  Binary Search Partition	          O(log(min(m, n)))
#Arrays are unsorted	Sort both + Median Algorithm	  O(m log m + n log n)