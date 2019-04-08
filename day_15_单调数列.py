class Solution:
    """
    如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false
    """
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n == 1:
            return True
        if A[0] < A[n-1]:
            for i in range(1,n):
                if A[i] < A[i-1]:
                    return False
            return True
        elif A[0] > A[n-1]:
            for i in range(1,n):
                if A[i] > A[i-1]:
                    return False
            return True
        elif A[0] == A[n-1]:
            for i in range(1,n):
                if A[i] != A[i-1]:
                    return False
            return True
        else:
            return True
