# 练习8.3-2
class GeneralComparision:
    """
    没有equal的场景
    """

    def __init__(self, value, significant_tuple):
        self.value = value
        # tuple元素优先级按从左到右降序排列
        if isinstance(significant_tuple, tuple):
            self.significant_tuple = significant_tuple
        else:
            self.significant_tuple = (significant_tuple,)

    def __gt__(self, other):
        if self.value > other.value:
            return True
        elif self.value < other.value:
            return False
        else:
            for i in range(len(self.significant_tuple)):
                if self.significant_tuple[i] > other.significant_tuple[i]:
                    return True
                elif self.significant_tuple[i] < other.significant_tuple[i]:
                    return False
            raise ValueError(
                '无法确定{},{}和{},{}谁更大'.format(self.value, *self.significant_tuple, other.value, *other.significant_tuple))

    def __lt__(self, other):
        if self.value < other.value:
            return True
        elif self.value > other.value:
            return False
        else:
            for i in range(len(self.significant_tuple)):
                if self.significant_tuple[i] < other.significant_tuple[i]:
                    return True
                elif self.significant_tuple[i] > other.significant_tuple[i]:
                    return False
            raise ValueError(
                '无法确定{},{}和{},{}谁更小'.format(self.value, *self.significant_tuple, other.value, *other.significant_tuple))


def general_greater(item1, item2):
    """
    对数字，字母，字符等序列进行比较(满足稳定排序的比较)
    :return: item1大于item2，返回True，小于返回False，等于则报错
    """
    if len(item1) <= 1 or len(item2) <= 1:
        raise ValueError('缺少优先级标志位')
    p1 = GeneralComparision(item1[0], item1[1::])
    p2 = GeneralComparision(item2[0], item2[1::])
    if p1 > p2:
        return True
    return False


# -------------------- 快速排序(稳定排序版本) -------------------
def _partition(array, p, r):
    """
    选取array[r-1]为主元(pivot element)，对列表array[p:r]进行原址重排。注意不含r
    :return: 重排后的列表以及主元
    """
    pivot = array[r - 1]
    i = p - 1
    for j in range(p, r - 1):
        if not general_greater(array[j], pivot):  # array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r - 1] = array[r - 1], array[i + 1]
    return array, i + 1


def quick_sort_basic(array, p=None, r=None):
    """
    快速排序的基本版本。从小到大排序。
    待排序的序列为 array[p:r]
    :return: 排序后的array[p:r]
    """
    if p is None and r is None:
        p = 0
        r = len(array)
    if p >= r - 1:
        return array
    else:
        array, q = _partition(array, p, r)
        quick_sort_basic(array, p, q)
        quick_sort_basic(array, q, r)
        return array


def stable_quick_sort(array, p=None, r=None, reverse=True):
    """
    快速排序的稳定排序版本
    为每个元素增加一个索引值，在元素值相等的情况下，比较索引值后排序
    :return: 稳定排序后的array[p:r]
    """
    if p is None and r is None:
        p = 0
        r = len(array)
    # 为每个元素添加索引值
    for i in range(p, r):  # 纯数字
        if str(array[i]).isdigit:
            array[i] = array[i], i
        else:  # 含有字母，数字和符号
            if reverse is True:  # 从最低位开始排序
                split_list = array[i].split()[::-1]
            else:  # 从最高位开始排序
                split_list = array[i].split()[::-1]
            array[i] = array[i], split_list, i
    # 调用稳定排序版本的quick_sort
    array = quick_sort_basic(array, p, r)
    # 去除索引值
    for i in range(len(array)):
        array[i] = array[i][0]
    return array


# TODO 待链表数据结构完成后补充
def radix_sorting(array):
    # 检查array的元素长度是否一样
    d = len(array[0])
    for item in array:
        if len(item) != d:
            raise ValueError('{}的长度不一样'.format(item))


if __name__ == '__main__':
    # C = [1, 2, 3, 4, 5, 6.1, 7, 4, 4, 3]
    # print(stable_quick_sort(C))

    alphabeta = ['cow', 'dog', 'sea', 'rug', 'row', 'mob', 'box', 'tab', 'bar', 'ear', 'tar', 'dig', 'big', 'tea',
                 'now', 'fox']

    print(stable_quick_sort(alphabeta))
