"""
insertionソート
先頭から一つ前の値と比べていく
tempに避難して適切な位置まで一つ前の値と比較していく
"""

from typing import List

def insertion_sort(numbers: List[int]) -> List[int]:
    len_number = len(numbers)
    for i in range(1, len_number):
      # 先頭から２番目をtempに避難する
      temp = numbers[i]
      # 一つ前の数字
      j = i - 1
      # 一つ前のindexが0より大きいとき and 一つ前のindexが避難させた値より大きいとき
      while j >= 0 and numbers[j] > temp:
        # 空になっているnumbers[j+1]に入れる
        numbers[j+1] = numbers[j]
        # 後ろの値を一つずつ前にずらす
        j -= 1

      numbers[j+1] = temp
    
    return numbers



import random
nums = [random.randint(0, 1000) for _ in range(10)]
print(insertion_sort(nums))