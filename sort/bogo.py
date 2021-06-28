"""
配列を順番どおりになるまでランダムに並べ替える
"""

import random
from typing import List

def in_order(numbers: List[int]) -> bool:
  # numbers[i+1]と比較しているので-1とする
  return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))

    # for i in range(len(numbers)-1):
        # if numbers[i] > numbers[i+1]:
            # return False
    # return True


def bogo_sort(numbers: List[int]) -> List[int]:
    while not in_order(numbers):
        # random.shuffle -> 配列をランダムに並び替える
        random.shuffle(numbers)
    return numbers


if __name__ == '__main__':
    # for _ in -> indexを使わないときは'_'を使う
    # random.randint(0, 1000) -> 0から10000のランダムな整数を作る
    # リスト内包表記
    num = [random.randint(0, 1000) for _ in range(10)]
    print(bogo_sort(num))
