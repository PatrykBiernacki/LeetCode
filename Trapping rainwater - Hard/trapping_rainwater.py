class Solution:
    def trap(self, height: list[int]) -> int:
        local_max = 0
        step = 0
        for index, value in enumerate(height):



            height_set = set(height)
            current_height = max(height_set)
        while current_height > 0:
            if current_height not in height_set:
                current_height -=1
                continue
            