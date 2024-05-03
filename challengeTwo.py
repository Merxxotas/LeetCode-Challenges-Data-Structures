class Solution(object):
    def containsDuplicate(self, nums):
        hashmap = {}
        for number in nums:
            if hashmap.get(number):
                return True
            hashmap[number]=1
        return False
        """
        :type nums: List[int]
        :rtype: bool
