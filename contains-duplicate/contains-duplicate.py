class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        val_dict = {}
        for i in range(len(nums)):
            if nums[i] in val_dict:
                return True
            else:
                val_dict[nums[i]] = i
        return False