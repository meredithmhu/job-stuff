class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_arr = []
        p1 = 0
        p2 = 0
        if m == 0:
            nums1 = nums2
        if n == 0:
            return
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                new_arr.append(nums1[p1])
                p1 += 1
            elif nums1[p1] == nums2[p2]:
                new_arr.append(nums1[p1])
                new_arr.append(nums2[p2])
                p1 += 1
                p2 += 1
            else:
                new_arr.append(nums2[p2])
                p2 += 1
        if p1 >= m:
            for i in range(n-p2):
                new_arr.append(nums2[p2])
                p2 += 1
        if p2 >= n:
            for i in range(m-p2):
                new_arr.append(nums1[p1])
                p1 += 1
        nums1 = new_arr
        return nums1

l1 = [1,2,3,0,0,0]
l2 = [2,5,6]
solution = Solution()
print(solution.merge(l1, 3, l2, 3))