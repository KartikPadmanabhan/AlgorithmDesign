__author__ = 'aukauk'
class Queue:

    def __init__(self):
        self.items=[]

    def push(self,element):
        self.items.insert(0,element)

    def pop(self):
        self.items.pop()


if __name__=='__main__':
    a=Queue()
    a.push(10)
    a.push(13)
    a.push(12)
    a.push(15)
    a.push(14)
    a.pop()
    print(a.items)