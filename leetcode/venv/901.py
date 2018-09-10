#!/usr/bin/python
#-*- coding: utf8 -*-
class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res=1
        while self.stack and self.stack[-1][0] <= price :
            res+=self.stack.pop()[-1]
        self.stack.append([price, res])
        return res

S=StockSpanner()
output=S.next(100)
print(output)
output=S.next(80)
print(output)
output=S.next(60)
print(output)