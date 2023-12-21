from itertools import permutations

class Solution:
    # def permute_oneliner(self, nums: list[int]) -> list[list[int]]:
    #     return set(permutations(nums))

    def permute(self, nums: list[int]) -> list[list[int]]:
        return set(permutations(nums))


if __name__ == '__main__':
    solution1 = Solution()
    print(solution1.permute([1,2,3]))
    print(solution1.permute([0,1]))
    print(solution1.permute([1]))
    print(solution1.permute([1,2,3,4,5,6]))