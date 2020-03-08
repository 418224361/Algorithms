def radix_sorting(array):
    # 检查array的元素长度是否一样
    d = len(array[0])
    for item in array:
        if len(item) != d:
            raise ValueError('{}的长度不一样'.format(item))



alphabeta = ['cow', 'dog', 'sea', 'rug', 'row', 'mob', 'box', 'tab', 'bar', 'ear', 'tar', 'dig', 'big', 'tea',
             'now', 'fox']
print(list(zip(item for item in alphabeta)))
