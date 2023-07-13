#Time: O(n), single pass
# Sapce: O(1)
# did the code run? yes
#issues faced: none
# Approach:
# using 2 pointers, at both ends of the array
# move the pointer whose element is min of both the pointers one step towards the center
# if both the elements are equal then, move both of them one step towards center
# the min value pointer is shifted because, it is the value used in computing height among both the heights
# trying to move the min height because, the max height can be utilised to gain more volume.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, volume = 0, len(height)-1, 0
        while i < j:
            volume = max(volume, (j-i)*min(height[i], height[j]))
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
        return volume