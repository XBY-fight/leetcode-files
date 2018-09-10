#!/usr/bin/python
#-*- coding: utf8 -*-
#from leetcode-lee215
class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        N = str(N)
        n = len(str(N))
        res = sum(len(D) ** i for i in range(1, n))
        i = 0
        while i < len(N):
            res += sum(c < N[i] for c in D) * (len(D) ** (n - i - 1))
            if N[i] not in D: break
            i += 1
        return res + (i == n)

l = ["1","3","5","7"]
solution=Solution()
solution.atMostNGivenDigitSet(l,100)