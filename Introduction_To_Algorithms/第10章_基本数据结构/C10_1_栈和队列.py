#  栈
class Stack:
    def __init__(self, length):
        self.length = length
        self.array = [None for _ in range(length)]
        self.top = -1  # 堆栈顶端元素的索引值

    def push(self, x):
        self.top += 1
        if self.top == self.length:
            raise IndexError('Overflow')
        self.array[self.top] = x

    def empty(self):
        return self.top == -1

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

    def enqueue(self, x):
        # if self.head == (self.tail + 1) % self.length:
        if self.head == self.tail:
            raise IndexError('Overflow')
        self.array[self.tail] = x
        self.tail = (self.tail + 1) % self.length
        if self.head is None:
            self.head = 0

    def dequeue(self):
        if self.head is None or self.head == (self.tail - 1) % self.length:
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


if __name__ == '__main__':
    # 练习10.1-1
    s = Stack(6)
    s.push(4)
    print(s.show())
    s.push(1)
    print(s.show())
    s.push(3)
    print(s.show())
    s.pop()
    print(s.show())
    s.push(8)
    print(s.show())
    s.pop()
    print(s.show())
    print('-'*10)
    # 练习10.1-3
    q = Queue(6)
    q.enqueue(4)
    print(q.show())
    q.enqueue(1)
    print(q.show())
    q.enqueue(3)
    print(q.show())
    q.dequeue()
    print(q.show())
    q.enqueue(8)
    print(q.show())

    print('-'*10)
    r = Queue(3)
    r.enqueue(3)
    print(r.show())
    r.enqueue(2)
    print(r.show())
    r.enqueue(1)
    print(r.show())
    r.dequeue()
    print(r.show())
