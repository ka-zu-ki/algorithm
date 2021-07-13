'''
mergeソート
'''


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    #//は小数点を切り捨てる
    center = len(numbers) // 2
    #centerのindexより前
    left = numbers[:center]
    #centerのindexより後
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
          numbers[k] = left[i]
          i += 1
        else:
          numbers[k] = right[j]
          j += 1
        k += 1
    
    while i < len(left):
      numbers[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      numbers[k] = right[j]
      j += 1
      k += 1
    
    return numbers

import random

nums = [random.randint(0, 1000) for _ in range(10)]
print(merge_sort(nums))
