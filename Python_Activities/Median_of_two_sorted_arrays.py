class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        x, y = len(A), len(B)
        low, high = 0, x

        while low <= high:
            i = (low + high) // 2
            j = (x + y + 1) // 2 - i

            A_left = A[i - 1] if i > 0 else float('-inf')
            A_right = A[i] if i < x else float('inf')
            B_left = B[j - 1] if j > 0 else float('-inf')
            B_right = B[j] if j < y else float('inf')

            if A_left <= B_right and B_left <= A_right:
                if (x + y) % 2 == 1:
                    return max(A_left, B_left)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                high = i - 1
            else:
                low = i + 1





