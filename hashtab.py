
from random import seed, randint

def hash_func(value,size):
    seed(value)
    return randint(0,size-1)

class Hashtab:
    def __init__(s,size=10,func=hash_func):
        s.size=size
        s.keys=[None]*s.size
        s.data={}
        s.func=func
        
    def put(s,key,data):
        if key==None: return None
        adr=s.func(key,s.size)
        old=adr
        while not (s.keys[adr]==None and not (adr in s.data)):
            adr+=1
            if adr==s.size: adr=0
            if adr==old: return key
            if s.keys[adr]==key:
                s.data[adr]=data
                return None
        s.keys[adr]=key
        s.data[adr]=data
        #print('q',value,s.func(value,s.size),s.size)
        
    def take(s,key=None):
        if key==None: return None
        adr=s.func(key,s.size)
        old=adr
        while not (s.keys[adr]==key):
            adr+=1
            #print('take step')
            if adr==s.size: adr=0
            if adr==old: return None
        return s.data[adr]
        #print('q',value,s.func(value,s.size),s.size)
    
    def rm(s,key):
        if key==None: return None
        adr=s.func(key,s.size)
        s.data[adr]=None
        s.keys[adr]=None
        
    def foreach(s,func):
        for i in s.data.keys():
            if i==None: continue
            s.data[i]=func(s.data[i])
        
    def resize(s,size):
        o=Hashtab(size)
        for key in s.keys: o.put(key,s.take(key))
        s.size=o.size
        s.keys=o.keys
        s.data=o.data


if __name__=='__main__':
    o=Hashtab(20)
    o.put(0,0)
    print(o.take(0))
    o.foreach(lambda x: x+1)
    print(o.take(0))    
    o.resize(5)
    for i in range(50):
        a=hash_func(i,5)
        if a==0: print(i)
