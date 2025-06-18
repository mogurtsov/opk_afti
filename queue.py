#очередь
class Queue:
    def __init__(s):
        s.data=[]
    def put(s,data):
        s.data.append(data)
    def take(s):
        return s.data.pop(0)
'''
class Queue:
    pass

def put(s,data):
    try:
        s.data.append(data)
    except:
        s.data=[]
        
def take(s):
    try:
        return s.data.pop(0)
    except:
        return None
'''

#стек
class Stack:
    def __init__(s,limit=0):
        s.data=[]
        s.limit=limit
    def put(s,data):
        s.data.append(data)
        assert not 0<s.limit<len(s.data)
    def take(s):
        return s.data.pop(-1)
'''
class Stack:
    pass

def put(s,data):
    try:
        s.data.append(data)
    except:
        s.data=[]
    try:
        assert not 0<s.limit<len(s.data)
    except:
        s.limit=0
        
def take(s):
    try:
        return s.data.pop(-1)
    except:
        return None
'''
