class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            print(enumerate(nums))
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i


cls = Solution()

cls.twoSum([3, 2, 4], 6)