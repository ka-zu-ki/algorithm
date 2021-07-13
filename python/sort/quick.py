'''
quickソート
'''

from typing import List, NoReturn


def partition(numbers: List[int], low: int, height: int) -> int:
    # iは−１から　入れ替える数字のindex
    i = low - 1
    # pivotは配列の最後の数字
    pivot = numbers[height]
    for j in range(low, height):
        # jは配列の比較する数字のindex
        if numbers[j] <= pivot:
            i += 1
            #入れ替え
            numbers[i], numbers[j] = numbers[j], numbers[i]
    # 最後までいったらi番目まではソート済みなのでi+1と入れ替える
    numbers[i+1], numbers[height] = numbers[height], numbers[i+1]
    return i+1


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, height: int) -> None:
        if low < height:
            partition_index = partition(numbers, low, height)
            _quick_sort(numbers, low, partition_index-1)
            _quick_sort(numbers, partition_index+1, height)

    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(quick_sort(nums))
