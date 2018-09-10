class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        groupA=self.getAllGroup(A)
        groupout=[]
        for groupa in groupA :
            if groupa :
                numand=groupa[0]
                for num in groupa[1::] :
                    numand=numand|num
                groupout.append(numand)
        groupset=set(groupout)
        print(groupA)
        print(groupset)
        print(len(groupset))
        print(l2)

    def getAllGroup(self, L) :
        result=[]
        for i in range(len(L)) :
            j=i+1
            p=0
            while j <= len(L) :
                result.append(L[p:j])
                j+=1
                p+=1
        return result
solution=Solution()
solution.subarrayBitwiseORs([1,1,2])