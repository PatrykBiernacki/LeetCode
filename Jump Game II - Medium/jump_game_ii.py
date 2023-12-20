class Solution:
    def jump(self, nums: list[int]) -> int:
        position = 0
        steps = 0
        if nums[0] == 0 or len(nums)<2:
            return 0

        while position < len(nums)-1:
            steps += 1
            maxstep = nums[position]
            if position + maxstep >= len(nums)-1:
                return steps
            
            farthest_move = 1

            for move, cell_value in enumerate(nums[position+1:position+maxstep+1]):
                if move + 1 + cell_value > farthest_move and cell_value != 0 :
                    farthest_move = move + 1 + cell_value
                    best_move = move + 1
            position += best_move

if __name__ == '__main__':
    solution1 = Solution()
    print(solution1.jump([2,3,1,1,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]))
    print(solution1.jump([0]))
    print(solution1.jump([1]))