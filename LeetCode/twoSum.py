
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Example : nums = [2,7,11,15], target = 9 ; output [0,1]
# (Because nums[0] + nums[1] == 9, we return [0, 1])


def sum(nums=[], target=0):
    output = []
    for i_index, i in enumerate(nums):
        for j_index, j in enumerate(nums):
            if i + j == target and i_index != j_index:
                output.append(i_index)
    return output

print(sum([3,2,4],6))
