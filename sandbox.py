'''script for testing functionality'''
# nums = [0,1,2,3,4,5,5,-5]
# nums.sort()
# print(nums)

positives = {10:1, 12:1}
negatives = {-10:1, -12:1}
triplets = set()

for positiv in positives:
    if 0 - positiv in negatives:
        add_list = [0 - positiv, 0, positiv]
        triplets.add(tuple(add_list))

print (triplets)