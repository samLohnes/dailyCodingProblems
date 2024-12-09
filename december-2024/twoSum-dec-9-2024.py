
def twoSum(nums, target):


    comps = {}
    for i in range(len(nums)):
        if nums[i] in comps:
            return [i, comps[nums[i]]]
        comps[target - nums[i]] = i


#output: [0, 1] in any order
print(twoSum(nums=[2,7,11,15], target=9)) 

#output: [1, 2] in any order
print(twoSum(nums=[3,2,4], target=6))

#output: [0, 1] in any order
print(twoSum(nums=[3,3], target=6))

