
import hashtab
from hashtab import Hashtab as ht

from random import randint

def test_put_rand_int():
    try:
        value=randint(0,1000)
        o=ht()
        o.put(value,value+1)
        if o.take(value)==value+1: return True
    except:
        #print('test_put_rand_int:fatal error')
        pass
    return False

def test_put_some_rand_int():
    try:
        o=ht()
        some_value=[]
        for i in range(randint(0,10)):
            value=randint(0,1000)
            o.put(value,value)
            some_value.append(value)
        for value in some_value:
            if not o.take(value)==value:
                print(value,some_value)
                return False
        return True
    except:
        #print('test_put_some_rand_int:fatal error')
        #print(some_value)
        pass
    return False

def test_put_float():
    try:
        value=1/3
        o=ht()
        o.put(value,value)
        if o.take(value)==value: return True
    except:
        #print('test_put_float:fatal error')
        pass
    return False

def test_put_str():
    try:
        value='a'
        o=ht()
        o.put(value,value)
        if o.take(value)==value: return True
    except:
        #print('test_put_str:fatal error')
        pass
    return False

def test_put_list():
    try:
        value=[1,2,3]
        o=ht()
        o.put(value,value)
        if o.take(value)==value: return True
    except:
        print('test_put_list:fatal error')
        pass
    return False

def test_put_dict():
    try:
        value={1:1,'a':'a'}
        o=ht()
        o.put(value,value)
        if o.take(value)==value: return True
    except:
        print('test_put_dict:fatal error')
        pass
    return False

def test_put_set():
    try:
        value={1,2,3}
        o=ht()
        o.put(value,value)
        if o.take(value)==value: return True
    except:
        print('test_put_set:fatal error')
        pass
    return False

def test_put_tuple():
    try:
        value=(1,2,3)
        o=ht()
        o.put(value,value)
        if o.take(value)==value: return True
    except:
        #print('test_put_tuple:fatal error')
        pass
    return False

def test_put_class():
    try:
        class cl:
            def __init__(s):
                s.a='a'
        value=cl()
        o=ht()
        o.put(value,value)
        if o.take(value)==value: return True
    except:
        #print('test_put_class:fatal error')
        pass
    return False

def test_resize():
    try:
        old_size=randint(0,10)
        o=ht(old_size)
        some_value=[]
        for i in range(old_size):
            value=randint(100,1000)
            o.put(value,value)
            some_value.append(value)
        size=randint(1,20)
        o.resize(size)
        n=0
        m=0
        for value in some_value:
            if o.take(value)==value:
                n+=1
        if old_size<size:
            some_value=[]
            for value in range(size-old_size):
                o.put(value,value)
                some_value.append(value)
            for value in some_value:
                if o.take(value)==value:
                    m+=1
        if (min(old_size,size)<=n<=old_size) and (m>=size-old_size): return True
    except:
        #print('test_resize:fatal error')
        #print(some_value)
        pass
    return False

def test_remove():
    try:
        o=ht()
        try: o.rm(0)
        except:
            #print('test_remove:not_defined error')
            pass
        try: o.rm(None)
        except:
            #print('test_remove:None_type error')
            pass
        some_value=[]
        for i in range(randint(0,10)):
            value=randint(0,1000)
            o.put(value,value)
            some_value.append(value)
        value='a'
        o.put(value,value)
        o.rm(value)
        #print(value)
        if not (o.take(value)==value): return True
    except:
        #print('test_remove:fatal error')
        pass
    return False

def test_take_after_remove():
    try:
        o=ht()
        value_rm='a'
        o.put(value_rm,value_rm)
        some_value=[]
        for i in range(9):
            value=randint(0,1000)
            o.put(value,value)
            some_value.append(value)
        o.rm(value_rm)
        o.rm(None)
        for value in some_value:
            if not o.take(value)==value:
                print(value,some_value)
                return False
        return True
        #print(value)
    except:
        #print('test_take_after_remove:fatal error')
        pass
    return False
'''
list, dict, set - unsupported
int, float, str, tuple, class - supported
'''
if __name__=='__main__':
    test_funcs=[test_put_rand_int,test_put_some_rand_int,test_put_float,test_put_str,
                test_put_tuple,test_put_class,test_resize,test_remove,test_take_after_remove]
    for func in test_funcs:
        print(func())
