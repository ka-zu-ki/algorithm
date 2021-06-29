""""
selectソート
start位置の数字をtempに保持する　tempと他の数字を比べていく
一番小さい数字の位置と先頭を入れ替える
startの位置を後ろにずらす　同じことを続ける
"""

import random
from typing import List


def select_sort(numbers: List[int]) -> List[int]:
    len_number = len(numbers)
    # 周回のループ
    for i in range(len_number):
        min_idx = i

        # リストの中身のループ
        for j in range(i+1, len_number):
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    return numbers


nums = [random.randint(0, 1000) for _ in range(10)]
print(select_sort(nums))
