"""
cocktailソート（シェイカーソート)　bubbleの改良版
基本的にはbubbleと同じ　前の数字と入れ替わったらswapをtrueに変える
1周終わるとswapをfalseに戻しlimitを一つ前に移動
2週目は後ろから同じことをやる　3周目はlimitが前から一つ後ろに移動
swapがtrueである限り続く
"""

import random
from typing import Coroutine, List


def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        # swappedがfalseのままだったらループ抜ける
        if not swapped:
            break

        swapped = False
        # limitを前にずらす
        end = end - 1

        # end - 1 -> 3 から -1の一つ前まで-1ずつループする
        for i in range(end - 1, start - 1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        # limitを後ろにずらす
        start = start + 1

    return numbers


nums = [random.randint(0, 1000) for _ in range(10)]
print(cocktail_sort(nums))
