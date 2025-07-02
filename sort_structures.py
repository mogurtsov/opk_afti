class Queue_Stack:
    def __init__(s,limit=0):
        s.data=[]
        s.limit=limit
    def put(s,data):
        s.data.append(data)
        assert not 0<s.limit<len(s.data)
    def take_queue(s,flags=''):
        try:
            if 's' in flags: return s.data[0]
            return s.data.pop(0)
        except:
            return None
    def take_stack(s,flags=''):
        try:
            if 's' in flags: return s.data[-1:]
            return s.data.pop(-1)
        except:
            return None
    def dict(s):
        out={}
        for i in s.data:
            out[i[0]]=i[1]
        return out
    def len(s):
        return len(s.data)

from random import seed, randint

def hash_func(value,size):
    seed(value)
    return randint(0,size-1)

class Hashtab:
    def __init__(s,size=10,flags='',func=hash_func):
        s.size=size
        s.keys=[None]*s.size
        s.data={}
        s.func=func
        s.flags=flags
        
    def put(s,key,data):
        if key==None or data==None: return None
        adr=s.func(key,s.size)
        old=adr
        while not (s.keys[adr]==None and not (str(adr) in s.data)):
            if s.keys[adr]==key:
                if 'r' in s.flags:
                    s.data[str(adr)]=data
                    return None
                else:
                    return key
            adr+=1
            if adr==s.size: adr=0
            if adr==old: return key  
        s.keys[adr]=key
        s.data[str(adr)]=data
        
    def take(s,key=None):
        if key==None: return None
        adr=s.func(key,s.size)
        old=adr
        while not (s.keys[adr]==key):
            adr+=1
            if adr==s.size: adr=0
            if adr==old: return None
        return s.data[str(adr)]
    
    def rm(s,key):
        if key==None: return None
        adr=s.func(key,s.size)
        old=adr
        while not (s.keys[adr]==key):
            adr+=1
            if adr==s.size: adr=0
            if adr==old: return None
        s.data[str(adr)]=None
        s.keys[adr]=None
