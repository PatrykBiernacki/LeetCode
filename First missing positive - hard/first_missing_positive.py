class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        print (range(1,len(nums_set)+2))
        for i in range(1, len(nums_set)+2):
            if i not in nums_set:
                return i

if __name__ == '__main__':
    solution1 = Solution()
    print(solution1.firstMissingPositive([1]))
    print(solution1.firstMissingPositive([3,4,-1,1]))
    print(solution1.firstMissingPositive([7,8,9,11,12]))
    print(solution1.firstMissingPositive([0]))
    print(solution1.firstMissingPositive([-1]))