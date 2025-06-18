import archiv
import hashtab
import datetime
#from random import sample, randint
#import render
#import queue
tab=hashtab.Hashtab(100)
with open('doc.txt', 'r', encoding='utf-8') as f:
    doc=''.join(f.readlines())
current_time=datetime.datetime.now()

main=True
while main:
    inp=input("")
    if inp in ['help','/help','']:
        print(doc,'\n')
        print('commands:\nput, exit')
    elif inp=='put':
        tab.put(current_time.minute,input("Заметка:\n"))
    elif inp=='time':
        pass
    elif inp=='exit':
        main=False
