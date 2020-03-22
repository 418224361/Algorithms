import math


#  栈
class Stack:
    def __init__(self, length):
        self.length = length
        self.array = [None for _ in range(length)]
        self.top = -1  # 堆栈顶端元素的索引值

    def full(self):
        if self.top == self.length - 1:
            return True
        return False

    def empty(self):
        return self.top == -1

    def push(self, x):
        if self.full():
            raise IndexError('Overflow')
        self.top += 1
        self.array[self.top] = x

    def pop(self):
        if self.empty():
            raise IndexError('Underflow')
        self.top -= 1
        return self.array[self.top + 1]

    def show(self):
        return [self.array[i] for i in range(self.top + 1)]


# 队列
class Queue:
    def __init__(self, length):
        self.array = [None for _ in range(length)]
        self.head = None
        self.tail = 0
        self.length = length

    def full(self):
        if self.head == self.tail:
            return True
        return False

    def empty(self):
        if self.head is None or self.head == (self.tail - 1) % self.length:
            return True
        return False

    def enqueue(self, x):
        if self.full():
            raise IndexError('Overflow')
        self.array[self.tail] = x
        self.tail = (self.tail + 1) % self.length
        if self.head is None:
            self.head = 0

    def dequeue(self):
        if self.empty():
            raise IndexError('Underflow')
        x = self.array[self.head]
        self.head = (self.head + 1) % self.length
        return x

    def show(self):
        if self.head < self.tail:
            return [self.array[i] for i in range(self.head, self.tail)]
        else:
            lst = [self.array[i] for i in range(self.head, self.length)]
            lst.extend([self.array[i] for i in range(self.tail - 1)])
            return lst


# 练习10.1-2，在一个长度为n的数组上实现两个堆栈，两个堆栈长度之和小于n
class DStack:
    def __init__(self, length):
        self.length = length
        self.array = [None for _ in range(self.length)]
        self.top1 = -1  # 左空栈
        self.top2 = self.length  # 右空栈

    def lpush(self, x):
        self.top1 += 1
        if self.top1 == self.top2:
            raise IndexError('Overflow')
        self.array[self.top1] = x

    def rpush(self, x):
        self.top2 -= 1
        if self.top1 == self.top2:
            raise IndexError('Overflow')
        self.array[self.top2] = x

    def lempty(self):
        return self.top1 == -1

    def rempty(self):
        return self.top2 == self.length

    def lpop(self):
        if self.lempty():
            raise IndexError('left array underflow')
        self.top1 -= 1
        return self.array[self.top1 + 1]

    def rpop(self):
        if self.rempty():
            raise IndexError('right array underflow')
        self.top1 += 1
        return self.array[self.top1 - 1]


# 双端队列
class Deque:
    def __init__(self, length):
        self.length = length
        self.array = [None for _ in range(length)]
        self.head = None
        self.tail = 0

    def full(self):
        if self.head == self.tail:
            return True
        return False

    def empty(self):
        if self.head is None or self.head == (self.tail - 1) % self.length:
            return True
        return False

    def henque(self, x):
        if self.full():
            raise IndexError('Overflow')
        if self.head is None:
            self.head = 0
            self.tail = 1
        else:
            self.head -= 1
        self.array[self.head] = x

    def tenque(self, x):
        if self.full():
            raise IndexError('Overflow')
        self.array[self.tail] = x
        self.tail = (self.tail + 1) % self.length
        if self.head is None:
            self.head = 0

    def hdeque(self):
        if self.empty():
            raise IndexError('Underflow')
        x = self.array[self.head]
        self.head = (self.head + 1) % self.length
        return x

    def tdeque(self):
        if self.empty():
            raise IndexError
        x = self.array[self.tail - 1]
        self.tail = (self.tail - 1) % self.length
        return x

    def show(self):
        if self.head < self.tail:
            return [self.array[i] for i in range(self.head, self.tail)]
        else:
            lst = [self.array[i] for i in range(self.head, self.length)]
            lst.extend([self.array[i] for i in range(self.tail - 1)])
            return lst


# 练习10.1-6，用两个栈实现一个队列
class SQueue:
    """
    队列长度为偶数，否则会损失一个存储位
    """
    def __init__(self, length):
        self.stack_len = math.floor(length / 2)
        self.length = length
        self.s1, self.s2 = self.__initstack()

    def __initstack(self):
        s1 = Stack(self.stack_len)
        s2 = Stack(self.stack_len)
        return s1, s2

    def full(self):
        return self.s1.full() and self.s2.full()

    def empty(self):
        return self.s1.empty() and self.s2.empty()

    def enque(self, x):
        if self.full():
            raise IndexError('Overflow')
        elif self.s1.full() and self.s2.empty():  # s1满，s2空
            for i in range(self.s1.top+1):
                self.s2.push(self.s1.pop())
        elif self.s1.full():  # s1满，s2不空
            self.s1.top = -1
            for i in range(self.s2.top + 1):
                self.s1.push(self.s2.pop())
        self.s1.push(x)

    def deque(self):
        if self.empty():
            raise IndexError('Underflow')
        elif self.s2.empty():  # s2空，s1不空
            for i in range(self.s1.top + 1):
                self.s2.push(self.s1.pop())
        return self.s2.pop()


# 练习10.1-7 用两个队列实现一个栈
class QStack:
    """
    队列长度为偶数，否则会损失一个存储位
    """

    def __init__(self, length):
        self.queue_len = math.floor(length / 2)
        self.length = length
        self.s1, self.s2 = self.__initstack()

    def __initstack(self):
        s1 = Queue(self.queue_len)
        s2 = Queue(self.queue_len)
        return s1, s2
    # TODO 继续写
    def full(self):
        return self.s1.full() and self.s2.full()

    def empty(self):
        return self.s1.empty() and self.s2.empty()

    def enque(self, x):
        if self.full():
            raise IndexError('Overflow')
        elif self.s1.full() and self.s2.empty():  # s1满，s2空
            for i in range(self.s1.top + 1):
                self.s2.push(self.s1.pop())
        elif self.s1.full():  # s1满，s2不空
            self.s1.top = -1
            for i in range(self.s2.top + 1):
                self.s1.push(self.s2.pop())
        self.s1.push(x)

    def deque(self):
        if self.empty():
            raise IndexError('Underflow')
        elif self.s2.empty():  # s2空，s1不空
            for i in range(self.s1.top + 1):
                self.s2.push(self.s1.pop())
        return self.s2.pop()


if __name__ == '__main__':
    # 练习10.1-1 堆栈操作
    # s = Stack(6)
    # s.push(4)
    # print(s.show())
    # s.push(1)
    # print(s.show())
    # s.push(3)
    # print(s.show())
    # s.pop()
    # print(s.show())
    # s.push(8)
    # print(s.show())
    # s.pop()
    # print(s.show())
    # print('-' * 10)
    #
    # # 练习10.1-3 队列操作
    # q = Queue(6)
    # q.enqueue(4)
    # print(q.show())
    # q.enqueue(1)
    # print(q.show())
    # q.enqueue(3)
    # print(q.show())
    # q.dequeue()
    # print(q.show())
    # q.enqueue(8)
    # print(q.show())
    #
    # print('-' * 10)
    # r = Queue(3)
    # r.enqueue(3)
    # print(r.show())
    # r.enqueue(2)
    # print(r.show())
    # r.enqueue(1)
    # print(r.show())
    # r.dequeue()
    # print(r.show())
    # print('-' * 10)
    #
    # # 练习10.1-5 双端队列deque
    # dq = Deque(3)
    # dq.tenque(2)
    # print(dq.show())
    # dq.tenque(3)
    # print(dq.show())
    # dq.henque(1)
    # print(dq.show())
    # x = dq.hdeque()
    # print(x)
    # print(dq.show())
    # x = dq.tdeque()
    # print(x)
    # print(dq.show())

    # 用两个栈实现一个队列
    sq = SQueue(6)
    for i in range(6):
        sq.enque(i)
    for i in range(6):
        print(sq.deque(), end=',')
