class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # make a dict of each and compare
        nums1_dict = {}
        for item in nums1:
            if item in nums1_dict:
                nums1_dict[item] +=1
            else:
                nums1_dict[item] = 1
        nums2_dict = {}
        for item in nums2:
            if item in nums2_dict:
                nums2_dict[item] +=1
            else:
                nums2_dict[item] = 1
        # compare dicts
        match = []
        for item in nums1_dict:
            if item in nums2_dict:
                if nums2_dict[item] == nums1_dict[item]:
                    match += ([item] * nums2_dict[item])
                elif nums2_dict[item] < nums1_dict[item]:
                    match += ([item] * nums2_dict[item])
                else:
                    match += ([item] * nums1_dict[item])

        return match