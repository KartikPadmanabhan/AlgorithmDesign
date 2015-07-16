__author__ = 'aukauk'
import Stack
from Stack import *
import os

def dectobin(n):
    s=Stack()
    while (n>0):
        m=n%2
        s.push(m)
        n=int(n/2)
    return s

if __name__=='__main__':
    decbin=list(dectobin(10).items)
    print(decbin.join())