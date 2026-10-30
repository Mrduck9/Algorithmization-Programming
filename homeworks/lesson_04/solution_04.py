def min_boats(weights, limit):
    weights_sort = sorted(weights)
    left, right = 0, len(weights_sort) - 1
    boats = 0
    while left <= right:
        if weights_sort[left] + weights_sort[right] <= limit:
            left += 1
        right -= 1
        boats += 1
    return boats

def even_first(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 == 1:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
