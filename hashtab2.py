from random import seed, randint

def hash_func(value,size):
    seed(value)
    return randint(0,size-1)

class Hashtab:
    def __init__(s,size,func1=hash_func,func2=lambda value,size: hash_func(value,size)+1):#hash_func(hash_func(value,size),size)):
        s.size=size
        s.keys1=[None]*s.size
        s.keys2=[None]*s.size
        s.data1={}
        s.data2={}
        s.func1=func1
        s.func2=func2
        s.bad=0
    def put(s,key,data):
        if key==None: return None
        adr1=s.func1(key,s.size)
        if s.keys1[adr1] == None:
            s.keys1[adr1]=key
            s.data1[adr1]=data
        else:
            adr2=s.func2(key,s.size)
            if s.keys2[adr2] == None:
                s.keys2[adr2]=key
                s.data2[adr2]=data
            else:
                old=(s.keys1[adr1],s.data1[adr1])
                s.keys1[adr1]=key
                s.data1[adr1]=data
                print(*old)
                s.bad+=1
                if s.bad>s.size:
                    assert False
                s.put(*old)

a=Hashtab(5)
a.put(1,1)
a.put(2,2)
a.put(3,3)
a.put(4,4)
a.put(5,5)
a.put(6,6)
a.put(7,7)
