#!/usr/bin/python
#-*- coding: utf8 -*-
#超时间限制

from itertools import product
class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        mostnum=0
        for i in range(1,len(str(N))+1) :
            numlist=list(product(D, repeat=i))
            for numi in numlist :
                stri="".join(numi)
                if int(stri) <= N :
                    mostnum+=1
        print(mostnum)

l = ["2","3","4","5","6","7","8"]
solution=Solution()
solution.atMostNGivenDigitSet(l,5487819)