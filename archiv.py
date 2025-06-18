from json import dumps, loads

def compress(data,pilot_len=256,search_len=1000):
    data=dumps(data)#str(dumps(data))[2:-1]
    out=[]
    i=0
    while i<len(data):
        search=data[max(0,i-search_len):i]
        pilot=data[i:i+pilot_len]
        best_len=0
        best_destep=0
        best_char=data[i]
        for j in range(1,search_len):
            substr=search[-j:0]
            length=0
            while length<len(substr) and length<pilot_len and substr[length]==pilot[length]:
                length+=1
            if length>best_len:
                best_destep=j
                best_len=length
                if i+best_len>=len(data):
                    best_char=''
                else:
                    best_char=data[i+best_len]
        #if best_len>0:
        out.append((best_destep,best_len,best_char))
        i+=(1+best_len)
    return out
        
        

def decompress(compressed):
    out=[]
    for elem in compressed:
        destep,length,char=elem
        if destep==0==length:
            out.append(char)
        else:
            #
            for i in range(length):
                out.append(out[i+len(out)-destep])
            out.append(char)
    return loads(''.join(out))#bytes((''.join(out)).replace('\\',str(\)),utf8)
            

