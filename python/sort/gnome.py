"""
gnomeソート　bubbleソートと類似
先頭から1つ前の値と比較していく　数字を入れ替えたら一つ前に戻り比較する
1つ前の値がマイナスにならないようにする
"""

import random
from typing import List


def gnome_sort(numbers: List[int]) -> List[int]:
    len_number = len(numbers)
    index = 0
    while index < len_number:
        # 先頭に戻ってきた時に１つ前と比べるためにindexを１にずらす
        if index == 0:
            index += 1
        # 順番通りに並んでいる
        if numbers[index] >= numbers[index-1]:
            index += 1
        # 順番通りに並んでいない
        else:
            numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
            index -= 1
    return numbers


nums = [random.randint(0, 1000) for i in range(10)]
print(gnome_sort(nums))
