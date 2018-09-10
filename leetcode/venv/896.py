class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 2 : return True
        lastnum=A[0]
        numsu=1
        numtrend=0
        for numa in A[1::] :
            if numtrend == 1 :
                if numa < lastnum :
                    break
                numsu+=1
                lastnum=numa
            elif numtrend == 2 :
                if numa > lastnum :
                    break
                numsu+=1
                lastnum=numa
            elif not numtrend and numa > lastnum :
                numtrend=1 #up
                numsu+=1
                lastnum=numa
            elif not numtrend and numa < lastnum :
                numtrend=2 #down
                numsu+=1
                lastnum=numa
            elif not numtrend and numa == lastnum :
                numsu+=1
        if numsu == len(A) :
            return True
        return False
solution=Solution()
output=solution.isMonotonic([1,1,1,1])
print(output)