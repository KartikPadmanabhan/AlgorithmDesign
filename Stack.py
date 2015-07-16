class Stack:

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()


if __name__=='__main__':
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(5)
    s.pop()
    s.push('a')
    print(s.items)

