class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) - 1
        count = 0

        for i in range(n):
            if nums[i] > nums[i+1]:
                count += 1

                if count > 1:
                    return False
                elif nums[0] < nums[n]:
                    return False
        return True
