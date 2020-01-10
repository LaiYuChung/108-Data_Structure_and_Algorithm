
# coding: utf-8

# 2020 / 1 / 8 edit
# <br>From : leetcode
# <br>Level : easy
# <br>Qusetion : No.771 -- `Jewels and Stones`

# You're given strings J representing the types of stones that are jewels, 
# <br>and S representing the stones you have.  Each character in S is a type of stone you have.  
# <br>You want to know how many of the stones you have are also jewels.
# 
# <br>The letters in J are guaranteed distinct, and all characters in J and S are letters. 
# <br>Letters are case sensitive, so "a" is considered a different type of stone from "A".
# 
# <br>Input: J = "aA", S = "aAAbbbb"
# <br>Output: 3

# In[ ]:


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in J:
            for j in S:
                if i == j:
                    count+=1
                else:
                    pass
        return count


# Testcase:
# <br>"aA"
# <br>"aAAbbbb"

# Output:
# <br>3
