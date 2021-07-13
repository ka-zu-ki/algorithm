'''
linearサーチ
前から探していく
'''


def linear_search(numbers, value):
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1


nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
print(linear_search(nums, 15))
