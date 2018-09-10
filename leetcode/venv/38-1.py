#!/usr/bin/python
#-*- coding: utf8 -*-
#报数改进版
#from leetcode-StefanPochmann
import re
class Solution:
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s
solution=Solution()
output=solution.countAndSay(5)
print(output)