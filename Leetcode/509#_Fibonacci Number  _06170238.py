
# coding: utf-8

# 2020 / 1 / 10 edit
# <br>From : leetcode
# <br>Level : easy
# <br>Qusetion : No.509 -- `Fibonacci Number`

# F(0) = 0,   F(1) = 1
# <br>F(N) = F(N - 1) + F(N - 2), for N > 1.
# <br>Given N, calculate F(N).

# In[ ]:


class Solution:
    def fib(self, N: int) -> int:
        if N ==0:
            return 0
        elif N==1:
            return 1
        else:
            return self.fib(N-1) + self.fib(N-2)


# Testcase:
# <br>2

# Out put:
# <br>1
