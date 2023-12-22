from itertools import permutations

class Solution:
    def permute_oneliner(self, nums: list[int]) -> list[list[int]]:
        return set(permutations(nums))

    def permute_2nd(self, nums: list[int]) -> list[list[int]]:
        
        answer_set = set()

        def helper(nums, path):
            if not nums:
                answer_set.add(tuple(path))
                return
            for i in range(len(nums)):
                helper(nums[:i] + nums[i+1:], path + [nums[i]]) 
        
        helper(nums, []) 

        return answer_set
    

    def permute(self, nums: list[int]) -> list[list[int]]:

        def permuter(nums:list)->list:
            if len(nums) <= 1:
                    yield nums
                    return
            for perm in permuter(nums[1:]):
                for i in range(len(nums)):
                    # nb elements[0:1] works in both string and list contexts
                    yield perm[:i] + nums[0:1] + perm[i:]
        
        return list(permuter(nums))
     
if __name__ == '__main__':
    solution1 = Solution()
    print(solution1.permute([1,2,3]))
    print('')
    print(solution1.permute([0,1]))
    print('')
    print(solution1.permute([1]))
    print('')
    print(solution1.permute([1,2,3,4,5]))