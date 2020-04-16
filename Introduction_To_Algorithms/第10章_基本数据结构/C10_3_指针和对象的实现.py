# 多数组表示的双向链表
def allocate_object(free_list):
    """
    该分配方式是紧凑的，即总是尽量使用连续的一段存储空间
    :param free_list: 自由表
    :return: 自由表的最后一个元素，在数值上等于数组的下标
    """
    #
    if free_list is None:
        return ValueError('out of space')
    else:
        x = free_list.pop()
        return x


def free_object(x, free_list):
    """
    该分配方式是紧凑的，即总是尽量使用连续的一段存储空间
    :param x: 释放的元素在链表中的下标
    :param free_list: 自由表
    :return: 释放一个元素后的自由表
    """
    free_list.append(x)


def init(free_list_size=0, lst=None):
    """
    初始化一个多数组表示的双向链表
    :param free_list_size: 自由表的长度，也就是链表的长度
    :param lst: 链表元素的初始值，以列表形式表示
    :return: [link_head, prev, key, next]和一个自由表
    """
    if lst:
        size = len(lst)
    else:
        return [], [], []
    if free_list_size < size:
        raise ValueError('free list size can not be less than that of list')
    next = [None] * size
    key = [None] * size
    prev = [None] * size
    free_list = list(range(free_list_size - 1, -1, -1))
    link_head = None
    while lst and len(free_list) > free_list_size - size:
        prev_index = None
        free_index = free_list.pop()
        link_head = free_index
        for i in range(len(lst)):
            key[free_index] = lst[i]
            prev[free_index] = prev_index
            prev_index = free_index
            if len(free_list) > free_list_size - size:
                next_index = allocate_object(free_list)
            else:
                next_index = None
            next[free_index] = next_index
            free_index = next_index
    link = [link_head, prev, key, next]
    return link, free_list


def delete(link, free_list, index):
    """
    删除双向链表中的下标为x的元素
    :param link: [prev, key, next]
    :param free_list: 自由表
    :param index: 待删除的下标值
    :return: [prev, key, next]和自由表
    """
    link_head, prev, key, next = link
    if link_head is None:
        raise ValueError('Empty link')
    elif index in free_list:
        raise ValueError('index {} already is free'.format(index))
    if index == link_head:
        link_head = next[index]
    left_index = prev[index]  # x pre的下标
    right_index = next[index]  # x next的下标
    if left_index is not None:
        next[left_index] = right_index
    if right_index is not None:
        prev[right_index] = left_index
    free_object(index, free_list)
    return [link_head, prev, key, next], free_list


def add(link, free_list, value):
    """
    向链表中增加一个元素，值为value，使用自由表free_list的空间
    :return: [prev, key, next]和自由表
    """
    link_head, prev, key, next = link
    if not free_list:
        raise ValueError('No space')
    free_index = free_list.pop()
    key[free_index] = value
    next[free_index] = link_head
    prev[free_index] = None
    link_head = free_index
    if next[free_index] is not None:
        prev[next[free_index]] = free_index
    return [link_head, prev, key, next], free_list


def search(link, value):
    """
    在链表中搜索value值对应的下标
    :param link: 链表
    :param value: 待搜索的值
    :return: 值在链表中的下标，从0开始计数
    """
    link_head, prev, key, next = link
    current_index = link_head
    while key[current_index] != value:
        if next[current_index] is None:
            raise ValueError('{} not exits'.format(value))
        current_index = next[current_index]
    return current_index


if __name__ == '__main__':
    link, free_list1 = init(10, [13, 4, 8, 19, 5, 11])
    print('初始化后的链表:', '\n', link, free_list1)
    link, free_list1 = delete(link, free_list1, 1)
    link, free_list = delete(link, free_list1, 2)
    link, free_list1 = delete(link, free_list1, 3)
    link, free_list1 = delete(link, free_list1, 0)
    link, free_list1 = delete(link, free_list1, 4)
    link, free_list1 = delete(link, free_list1, 5)
    print('删空后的链表:', '\n', link, free_list1)
    link, free_list1 = add(link, free_list1, 11)
    link, free_list1 = add(link, free_list1, 5)
    link, free_list1 = add(link, free_list1, 19)
    link, free_list1 = add(link, free_list1, 8)
    link, free_list1 = add(link, free_list1, 4)
    link, free_list1 = add(link, free_list1, 13)
    print('重新添加元素后的链表:', '\n', link, free_list1)
    print(search(link, 4))
