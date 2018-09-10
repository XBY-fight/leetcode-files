#!/usr/bin/python
#-*- coding: utf8 -*-
##from leeetcode-zhoubaowei
class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res, cur = set(), set()
        for i in A:
            r=set()
            r.add(i)   #进行组合
            for j in res :
                r.add(i|j)  #实现连续子数组组合
            res=r
            for j in res :
                cur.add(j)
        return len(cur)
solution=Solution()
output=solution.subarrayBitwiseORs([1,1,2])
print(output)