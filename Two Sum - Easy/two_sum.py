class Solution:
    def __init__(self) -> None:
        pass

    def two_sum(self, nums:list[int], target:int)->list[int]:

        # for num_id, num in enumerate(nums):
        #     for num_id2, num2 in enumerate(nums):
        #         if num_id == num_id2:
        #             continue
        #         if num+num2 != target:
        #             continue
        #         return [num_id, num_id2]

        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                j = nums[i+1:].index(target - nums[i])+i+1
                return [i,j]
            else:
                continue

if __name__ == '__main__':

    solution1 = Solution()
    print (solution1.two_sum([2,7,11,15], 9))
    print (solution1.two_sum([3,3], 6))
    print (solution1.two_sum([3,2,4], 6))
    print (solution1.two_sum([1,8,4,4,16,8], 16))
    