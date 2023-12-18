class Solution:
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
    nums = [3,2,4]
    target = 6

    print (Solution.two_sum('_', nums=nums, target=target))