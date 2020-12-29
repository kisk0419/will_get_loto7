import sys
import time
from typing import List
from random import randint

SET_NUM = 10295472


def get_numbers(min: int = 1, max: int = 37) -> List[int]:
    """
    ランダムに番号を7つ取得する
    """
    return [randint(min, max) for _ in range(7)]


def is_correct_numbers(numbers: List[int]) -> bool:
    """
    番号に重複がない正しい数列かチェックする
    """
    s = set(numbers)
    return len(s) == 7


def get_latest_winning_number() -> str:
    """
    直近の当選番号を取得する
    """
    print('直近の当選番号を半角空白で区切って入力してください。')
    print('例）>> 1 2 3 4 5 6 7')
    print('>> ')
    f = sys.stdin
    s = f.readline()
    l = list(map(int, s.split(' ')))
    if not is_correct_numbers(l):
        return get_latest_winning_number()
    return to_strnum(l)


def ready(set_num: int = SET_NUM):
    print('準備中...')
    correct_num_cnt = 0
    while set_num >= correct_num_cnt:
        nums = get_numbers()
        if is_correct_numbers(nums):
            correct_num_cnt += 1
    

def to_strnum(numbers: List[int]) -> str:
    """
    数値の配列を文字列に変換する
    """
    num = map(str, sorted(numbers))
    num = ' '.join(num)
    return num


def get_new_winning_number(latest_number: str) -> str:
    print('当選番号算出中...')
    found = False
    winning_number = None
    #for _ in range(SET_NUM * 2):
    count = 0
    while True:
        count += 1
        numbers = get_numbers()
        if is_correct_numbers(numbers) :
            num = to_strnum(numbers)
            #print(num)
            if found:
                winning_number = num
                break
            elif num == latest_number:
                found = True
        #time.sleep(0.01)
    
    print(f'試行回数：{count}')
    return winning_number


def main():
    latest_winning_number = get_latest_winning_number()
    #ready()
    new_winning_number = get_new_winning_number(latest_winning_number)

    print('当選番号です！')
    print(new_winning_number)


if __name__ == '__main__':
    main()
    #num = get_latest_winning_number()
    #print(num)
    #to_num = to_strnum([1, 2, 3, 4, 5, 6, 7])
    #rint(num == to_num)

