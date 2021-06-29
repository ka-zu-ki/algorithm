"""
bubbleソート
一つ前の値と比べて入れ替えていく
リストの終わりまで調べていく
１周目のループが終わったらlimitを一つずらす
"""

list = [2, 5, 1, 8, 7, 3]

def in_order(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False
    return True


def bubblr_sort(list):
    limit = 0
    for i in range(1, len(list)-limit):
        if list[i] < list[i-1]:
            tmp = list[i]
            list[i] = list[i-1]
            list[i-1] = tmp

    if not in_order(list):
        limit += 1
        return bubblr_sort(list)
    else:
      return list


print(bubblr_sort(list))


"""
模範解答
"""
from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
  len_number = len(numbers)
  for i in range(len_number):
    for j in range(len_number - i):
      if numbers[j] > numbers[j+1]:
        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
  return numbers


import random
nums = [random.randint(0, 1000) for _ in range(10)]
print(bubblr_sort(nums))