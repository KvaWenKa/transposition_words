from tkinter import *
from tkinter import messagebox

def button_click():
    spl_str = (entry_str.get()).split()
    if len(spl_str) == 0:
        messagebox.showwarning("Ошибка", "Ввод пустой строки")
        return
    try:
        first = int(entry_first_str.get()) - 1
        end = int(entry_end_str.get()) - 1
        if(first < 0 or first > end or end > len(spl_str)-1):
            messagebox.showerror("Ошибка", "Ошибка диапазона")
            return
    except:
        messagebox.showerror("Ошибка", "Ошибка ввода")
        return
    new_str = " ".join(spl_str[first:end+1])
    if len(spl_str[:first]) > 0:
        new_str += " " + " ".join(spl_str[:first])
    if len(spl_str[end+1:]) > 0:
        new_str += " " + " ".join(spl_str[end+1:])

    label3.config(text=new_str)

root = Tk()
root.title("Перестановка слов")
root.geometry("600x200")
root.config(bg="#dce0ce")

entry_str = StringVar()
textbox1 = Entry(textvariable=entry_str,borderwidth=1, relief="solid", width="50", font = "5")
textbox1.place(relx=.5, rely=.1, anchor="c")

entry_first_str = StringVar()
label1 = Label(text="C", bg="#dce0ce", width = "10", font = "5")
label1.place(relx=.1, rely=.3, anchor="c")
textbox2 = Entry(textvariable=entry_first_str, width="5", font = "5")
textbox2.place(relx=.2, rely=.3, anchor="c")

entry_end_str = StringVar()
label2 = Label(text="ПО", bg="#dce0ce", width = "10", font = "5")
label2.place(relx=.5, rely=.3, anchor="c")
textbox3 = Entry(textvariable=entry_end_str, width="5", font = "5")
textbox3.place(relx=.6, rely=.3, anchor="c")

btn = Button(text="OK", background ="#dcdcdc", width="5", font="5", command=button_click)
btn.place(relx=.8, rely=.3, anchor="c")

label3 = Label(borderwidth=1, relief="solid", bg="#dce9ce", width = "50", font = "5")
label3.place(relx=.5, rely=.6, anchor="c")

root.mainloop()
