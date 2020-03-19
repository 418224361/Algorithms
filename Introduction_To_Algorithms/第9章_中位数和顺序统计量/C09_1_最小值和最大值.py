#  在O(n+lg(n)-2)的时间内找到最大和次最大值
import sys


def update_winner_loser(dic, key, new_value):
    if key in dic.keys() and dic[key] < new_value:
        dic[key] = new_value
    elif key not in dic.keys():
        dic.update({key: new_value})
    return dic


def _first_second_place(array, winner_loser=None):
    """
    在O(n+lg(n)-2)的时间内找到array中的最大和次最大值
    :param array:待比赛的选手，只有上一轮获胜的选手，才是本轮待比赛选手
    :param winner_loser:比赛结果，以字典形式储存每轮比赛的胜负方，若胜方胜出多次，则记录负方值最大的那一轮
    :return: 本轮所有获胜选手, 本轮比赛后的winner_loser
    """
    if winner_loser is None:
        winner_loser = dict()
    if len(array) == 1:
        return array, winner_loser
    winner_array = []
    for i in range(0, len(array), 2):
        if i + 1 <= len(array) - 1:  # 能够凑成整对儿
            if array[i] >= array[i + 1]:
                winner_loser = update_winner_loser(winner_loser, array[i], array[i + 1])
                winner_array.append(array[i])
            else:
                winner_loser = update_winner_loser(winner_loser, array[i + 1], array[i])
                winner_array.append(array[i + 1])
        elif i == len(array) - 1:  # 剩余一个选手没有比赛过，默认获胜，自动进入下一轮比赛
            winner_loser = update_winner_loser(winner_loser, array[i], sys.float_info.min)
            winner_array.append(array[i])
    list(set(winner_array))  # 去重
    return _first_second_place(winner_array, winner_loser)


def first_second_place(array, winner_loser=None):
    winner, winner_loser = _first_second_place(array, winner_loser)
    return winner[0], winner_loser[winner[0]]


if __name__ == '__main__':
    c = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21, 34, 52, 56, 24, 78, 32]
    print(first_second_place(c))
