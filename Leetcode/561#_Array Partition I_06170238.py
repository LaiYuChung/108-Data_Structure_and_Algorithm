
# coding: utf-8

# 2020 / 1 / 10 edit
# <br>From : leetcode
# <br>Level : easy
# <br>Qusetion : No.561 -- Array Partition I

# Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
# <br>say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
# 
# <br>Input: [1,4,3,2]
# <br>Output: 4
# <br>Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

# In[ ]:


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        i = 0
        while i < len(nums):
            sum +=nums[i]
            i+=2
        return sum


# Testcase:
# <br>[1,4,3,2]

# Output:
# <br>4
