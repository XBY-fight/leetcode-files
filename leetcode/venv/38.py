#!/usr/bin/python
#-*- coding: utf8 -*-
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num=["1"]
        for j in range(n-1) :
            i=0
            numnow=None
            while i < len(num) :
                numnow=num[i]
                numnowi=1
                while i+1 < len(num) and num[i+1] == numnow :  #寻找相同的数字
                    num[i+1]=""  #清空
                    numnowi+=1   #计数
                    i+=1
                i+=1
                num[i-numnowi]=str(numnowi)+numnow  #报数：计数值+数字
            num=list("".join(num))  #拆开
        num="".join(num)
        return num
solution=Solution()
output=solution.countAndSay(5)
print(output)