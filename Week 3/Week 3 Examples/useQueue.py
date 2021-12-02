from queueInClass import *

def useQueue():
    'use a queue'
    q = queue()
    try:
        q.dequeue()
    except DequeueExcept as e:
        print(e)
