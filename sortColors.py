# Time: O(n), single pass
# space: O(1)
#issues faced: did not run the simulation in order. so thought about cases that would not appear
# Approach:
# using one pointer to point 1st non 0 index and another one to point last non 2 index
# using another pointer to traverse the array until 2dn pointer is not crossed, which means the array is sorted

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, ptr, j = 0, 0, len(nums)-1
        while ptr <= j:
            if nums[ptr] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr+=1; i+=1
            elif nums[ptr] == 1:
                ptr+=1
            else:
                nums[j], nums[ptr] = nums[ptr], nums[j]
                j-=1