"""
    1. Two Sum - https://leetcode.com/problems/two-sum/
    made at 16/11/2022

    Given an array of integers nums and an integer target, return indicies of the two numbers such that they add up to
    target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order


    # Example 1:

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    # Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]

"""

nums = [3, 2, 4]
target = 6
result = []
for index, element in enumerate(nums):
    for sub_index, sub_element in enumerate(nums):
        if index != sub_index and element + sub_element == target:
            result.append(index)
            result.append(sub_index)
            break

result = list(set(result))
print(result)