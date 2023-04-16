import tkinter as tk
from tkinter import *
import customtkinter

import pyperclip

from SOLVE import solve_problem

# region root
root = tk.Tk()
root.geometry("300x200")
root.geometry("1000x500+1500+100")
root.resizable(False, True)
root.minsize(1000, 500)
root.maxsize(1000, 1000)
root.title('Решатель задач по физике')
root.iconbitmap(default="icon.ico")
# root.attributes("-toolwindow", True)
root.attributes('-alpha', 0.95)
root.config(bg="gray")
# endregion

# region frame_1
frame = customtkinter.CTkFrame(root, fg_color='#d7d7d7')
frame.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)  # Задаем размер и положение фрейма
# endregion

# region label_1
label = customtkinter.CTkLabel(frame, text=" Решатель задач по физике v 1.0: alpha ", font=("Courier", 16), bg_color="gray22")
label.place(x=10, y=10) # Задаем отступ от верхнего края фрейма
# endregion

# region Entry_1
ENTRY = customtkinter.CTkEntry(frame, font=("Arial", 12), width=720)
ENTRY.place(x=10, y=50)  # Задаем отступ от надписи
ENTRY.insert(0, '*Пример задачи*')
ENTRY.focus()
# endregion

# region button_paste
def button_paste():
    try:
        ENTRY.delete(0, len(ENTRY.get()))
        ENTRY.insert(0, pyperclip.paste())
    finally: ...

BTN_PASTE = customtkinter.CTkButton(frame, text="Вставить", command=button_paste, font=("Courier", 12), width=100, fg_color='gray', hover_color='gray22')
BTN_PASTE = BTN_PASTE.place(x=750, y=50)

# endregion

# region button_start
frame_GIVEN = customtkinter.CTkFrame(frame, fg_color='gray22', height=0, width=0)
frame_GIVEN.place(x=10, y=90)

frame_FIND = customtkinter.CTkFrame(frame, fg_color='gray22', height=0, width=0)


BASE = {'given:': [], 'find:': []}
def button_start():
    try:
        BASE = solve_problem(ENTRY.get())
        print(BASE)
        hei_given = len(BASE['given:'])
        hei_find = len(BASE['find:'])
        wdth = len(str(max([i[0] for i in BASE['given:']])))

        frame_GIVEN.configure(height=hei_given*30, width=wdth*12 + 30)

        lbl_given = customtkinter.CTkLabel(frame_GIVEN, text="".join([f'{i[0]}\n' for i in BASE['given:']]), font=("Courier", 20)).place(x=10, y=10)

        frame_FIND.place(x=10, y=hei_given * 30 + 100)
        frame_FIND.configure(height=hei_find * 30, width=wdth*12 + 30)
    except: ...

BTN_START = customtkinter.CTkButton(frame, text="Пуск", command=button_start, font=("Courier", 12), width=100, fg_color='gray', hover_color='gray22')
BTN_START.place(x=860, y=50)



# endregion




root.mainloop()
