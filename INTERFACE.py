import json
import tkinter as tk
import pyperclip
from customtkinter import *

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
root.attributes('-alpha', 0.95)
root.config(bg="gray")
# endregion

# region frame_main (white)
frame_main = CTkFrame(root, fg_color='#d7d7d7')
frame_main.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)  # Задаем размер и положение фрейма
# endregion

# region config
CONFIG = {}


def update_config():
    global CONFIG
    with open('CONFIG.json', 'r') as read_config:
        CONFIG = json.load(read_config)


# endregion

update_config()

# region label_program_name
program_name = f' Решатель задач по физике: {CONFIG["CONFIG_NAME"][:30]}... '
label_program_name = CTkLabel(frame_main, text=program_name, font=("Courier", 16), bg_color="gray22")
label_program_name.place(x=10, y=10)  # Задаем отступ от верхнего края фрейма


# endregion

# region button_config
def button_config():
    try:
        file_path = filedialog.askopenfilename()
        with open(file_path, "r") as new_config:
            new_config_data = json.load(new_config)
        with open("CONFIG.json", "w") as old_config:
            json.dump(new_config_data, old_config)
        update_config()
        program_name = f' Решатель задач по физике: {CONFIG["CONFIG_NAME"][:30]}... '
        label_program_name.configure(text=program_name)
        btn_config.place(x=len(program_name) * 9 + 90)
    except json.decoder.JSONDecodeError:
        ...


btn_config = CTkButton(frame_main, text="Загрузить конфигурацию", command=button_config, font=("Courier", 12), width=200, fg_color='gray', hover_color='gray22')
btn_config.place(x=len(program_name) * 9 + 90, y=10)
# endregion

# region entry_task
entry_task = CTkEntry(frame_main, font=("Arial", 12), width=720)
entry_task.place(x=10, y=50)  # Задаем отступ от надписи
entry_task.insert(0, 'Найти скорость если время за которое прошло тело равно 5 секунд за 20 метров')
entry_task.focus()


# endregion

# region button_paste
def button_paste():
    entry_task.delete(0, len(entry_task.get()))
    entry_task.insert(0, pyperclip.paste())


btn_paste = CTkButton(frame_main, text="Вставить", command=button_paste, font=("Courier", 12), width=100, fg_color='gray', hover_color='gray22')
btn_paste.place(x=750, y=50)
# endregion

# region button_start
frame_given = CTkFrame(frame_main, fg_color='gray22', height=0, width=0)
frame_given.place(x=10, y=90)
frame_find = CTkFrame(frame_main, fg_color='gray22', height=0, width=0)
frame_find.place(x=10, y=0)


def button_start():
    tid, dia = solve_problem(entry_task.get(), out_mode='data_dict, data_into_answer')

    # region creating frame_given, frame_find
    giv_height = len(tid['given:']) * 30
    find_height = len(tid['find:']) * 30
    maxwid = max([len(i) for i in entry_task.get().split() + list(tid['given:'].keys()) + list(tid['find:'].keys())]) * 20
    frame_given.configure(height=giv_height, width=maxwid)
    frame_find.configure(height=find_height, width=maxwid)
    frame_find.place(y=giv_height + find_height + 70)
    # endregion

    given_text = "".join([f'{i}: {tid["given:"][i]["value"]}, {tid["given:"][i]["measure"]}\n' for i in tid['given:']])
    label_given = CTkLabel(frame_given, text=given_text, font=("Courier", 12))
    label_given.place(x=10, y=10)
    find_text = "".join([f'{i}: {tid["find:"][i]}\n' for i in tid['find:']])
    label_find = CTkLabel(frame_find, text=find_text, font=("Courier", 12))
    label_find.place(x=10, y=6)


button_start = CTkButton(frame_main, text="Пуск", command=button_start, font=("Courier", 12), width=100, fg_color='gray', hover_color='gray22')
button_start.place(x=860, y=50)

# endregion
if __name__ == '__main__':
    root.mainloop()
