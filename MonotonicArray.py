class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        isUp = True
        isDown = True
        for i in range( 1, len(A) ):
            if isUp == True or isDown == True:
                if A[i] > A[i-1]:
                    isDown = False
                elif A[i] < A[i-1]:
                    isUp = False
            else:
                break
                
        if isUp == False and isDown == False:
            return False
        
        return True
