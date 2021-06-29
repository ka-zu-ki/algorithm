"""
combソート（櫛をとかしていくという意味）　不安定
リストの中の数を1.3で割ったものをgapとする
gap -> 離れている数を並べ替える
2周目はgapを1.3で割ったものを新しいgapとして処理を進めていく
gapが1になるまで続ける　1になったらswapをつかってfalseになるまで確かめていく
"""

import random
from typing import List


def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

    while gap != 1 or swapped:
        # int() -> 整数に変換
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                swapped = True

    return numbers


nums = [random.randint(0, 1000) for _ in range(10)]
print(comb_sort(nums))
