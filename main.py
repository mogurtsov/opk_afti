from archive import *
from sort_structures import *
import tkinter as tk
import datetime

def d_time(flags='hm',char=':'):
    out=''
    current_time=datetime.datetime.now()
    if 'Y' in flags:
        year=str(current_time.year)
        out+=f'{year}{char}'
    if 'M' in flags:
        month= '' if len(str(current_time.month))>1 else '0'
        month+=str(current_time.month)
        out+=f'{month}{char}'
    if 'D' in flags:
        day= '' if len(str(current_time.day))>1 else '0'
        day+=str(current_time.day)
        out+=f'{day}{char}'
    if 'W' in flags:
        l=['пн','вт','ср','чт','пт','сб','вс']
        week_day=l[current_time.weekday()]
        out+=f'{week_day}{char}'
    if 'h' in flags:
        hour= '' if len(str(current_time.hour))>1 else '0'
        hour+=str(current_time.hour)
        out+=f'{hour}{char}'
    if 'm' in flags:
        minute= '' if len(str(current_time.minute))>1 else '0'
        minute+=str(current_time.minute)
        out+=f'{minute}{char}'
    if 's' in flags:
        second= '' if len(str(current_time.second))>1 else '0'
        second+=str(current_time.second)
        out+=f'{second}{char}'
    out=out[:-1]
    return out

def main_menu():
    button_add.place(x=200,y=50)
    button_take.place(x=200,y=110)
    button_exit.place(x=200,y=170)

def back_from_add():
    main_menu()
    entry.delete(0,'end')
    entry.pack_forget()
    button_enter.place_forget()
    button_back_add.place_forget()

def back_from_take():
    main_menu()
    entry.delete(0,'end')
    entry.pack_forget()
    listbox.destroy()
    scrollbar.destroy()
    button_find.place_forget()
    button_back_take.place_forget()
    label.pack_forget()
    try:
        button_rm.place_forget()
        button_view.place_forget()
    except: pass

def add_menu():
    button_add.place_forget()
    button_take.place_forget()
    button_exit.place_forget()
    entry.pack(padx=0,pady=0)
    button_enter.place(x=200,y=50)
    button_back_add.place(x=200,y=110)

def take_menu():
    button_add.place_forget()
    button_take.place_forget()
    button_exit.place_forget()
    take_list_upd(list(queue.dict())[::-1])
    entry.pack(padx=0,pady=0)
    button_find.place(x=200,y=50)
    button_back_take.place(x=200,y=110)
    label.pack()
    #last_point=None

#last_point=None
queue=Queue_Stack()

def take_list_upd(lt):#list
    global listbox, scrollbar
    try:
        listbox.destroy()
        scrollbar.destroy()
    except: pass
    lt=tk.StringVar(value=lt)
    listbox=tk.Listbox(listvariable=lt)
    listbox.pack(side='left', fill='both')
    scrollbar=tk.Scrollbar(orient='vertical',command=listbox.yview)
    scrollbar.pack(side='right', fill='y')
    listbox['yscrollcommand']=scrollbar.set
    listbox.bind('<<ListboxSelect>>',select)

def find_hash():
    i=set(tab.keys)
    i.remove(None)
    i=list(i)
    if entry.get()=='':
        label['text']=i
    #take_list_upd(list(i))
    button_find.place_forget()
    button_rm.place(x=200,y=50)
    button_view.place(x=200,y=170)
    #last_point=''

def rm():
    #global last_point
    tab.rm(entry.get())
    i=set(tab.keys)
    i.remove(None)
    i=list(i)
    label['text']=i
    if entry.get()=='queue':
        while queue.len()>0:
            queue.take_stack()
        take_list_upd([])

def view():
    #global last_point
    label['text']=tab.take(entry.get())

def enter():
    enter_time=d_time('hms')
    queue.put((enter_time,entry.get()))
    #entry.delete(0,'end')

def select(event):
    global label
    try:
        label['text']=queue.data[::-1][listbox.curselection()[0]][1]
        #label['text']=tab.take(listbox.get(listbox.curselection()))
    except: pass

def save_exit():
    tkwindow.title('saving...')
    while queue.len()>0:
        i=queue.take_queue()
        tab.put(i[0],i[1])
    out=[compress(tab.keys),compress(tab.data)]
    file=open('keys.txt','w')
    file.write(dumps(out[0]))
    file.close()
    file=open('data.txt','w')
    file.write(dumps(out[1]))
    file.close()
    tkwindow.title('saved')
    exit()

tab=Hashtab(100)
try:
    file=open('keys.txt','r')
    i=file.read()
    file.close()
    tab.keys=decompress(loads(i))
    file=open('data.txt','r')
    i=file.read()
    file.close()
    tab.data=decompress(loads(i))
except: pass
try:
    file=open('keys.txt','r')
    i=file.read()
    file.close()
    tab.keys=decompress(loads(i))
    file=open('data.txt','r')
    i=file.read()
    file.close()
    tab.data=decompress(loads(i))
except: pass
tkwindow=tk.Tk()
tkwindow.geometry('700x300')
button_add=tk.Button(text='Add',command=add_menu,width=10,height=3)
button_take=tk.Button(text='Take',command=take_menu,width=10,height=3)
button_exit=tk.Button(text='Save&Exit',command=save_exit,width=10,height=3)
entry=tk.Entry()
entry1=tk.Entry()
label=tk.Label(text='',wraplength=200,justify='left',bg='gray',width=30,height=60)
button_enter=tk.Button(text='Enter',command=enter,width=10,height=3)
button_back_add=tk.Button(text='Back',command=back_from_add,width=10,height=3)
button_find=tk.Button(text='Find',command=find_hash,width=10,height=3)
button_rm=tk.Button(text='Remove',command=rm,width=10,height=3)
button_view=tk.Button(text='View',command=view,width=10,height=3)
button_back_take=tk.Button(text='Back',command=back_from_take,width=10,height=3)
main_menu()
tkwindow.mainloop()
