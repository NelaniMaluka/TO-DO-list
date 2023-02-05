import tkinter
from tkinter import *

root=Tk()
root.title("To-Do-List")
root.geometry("500x650+500+100")
root.resizable(False,False,)

task_list=[]

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    
    #If there is an entry in the task_entry BOX then it gets added the entry to the tasklist.txt file
    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR)) #collecting the selected task
    
    if task in task_list:           #checking if the task is in the tasklist.txt file and deleting it
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete( ANCHOR)

def openTaskFile():
    #checks for the existence of the tasklist.txt file and shows the contents in the listbox
    try:
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END , task)
    #if the tasklist.txt file doesnt exits then it gets created
    except:
        file= open("tasklist.txt", "w")
        file.close()

#Icon image
Image_icon= PhotoImage(file="img/task.png")
root.iconphoto(False,Image_icon)

#Top bar image
TopImage= PhotoImage(file="img/topbar.png")
Label(root,image=TopImage).pack()

dockerImage = PhotoImage(file="img/dock.png")
Label(root,image=dockerImage,bg="#32405b").place(x=80,y=25)

noteImage = PhotoImage(file="img/task.png")
Label(root, image=noteImage,bg="#32405b").place(x=390,y=20)

heading= Label(root,text= "ALL TASKS", font="arial 20 bold", fg="white",bg="#32405b")
heading.place(x=170,y=20)


frame= Frame(root,width=500,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 15", bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()


button= Button(frame,text="Add Task", font="areial 20 bold", width=8, bg="#5a95ff", fg="#fff", bd= 1, command=addTask)
button.place(x=360,y=0)


frame1= Frame(root,bd=3,width=700, height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1, font=("arial", 12), width=50, height=16, bg="#32405b",fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side= RIGHT, fill= BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()
    
#Delete Icon
Delete_icon=PhotoImage(file="img/delete.png")
Button(root,image=Delete_icon,bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)


root.mainloop()


















