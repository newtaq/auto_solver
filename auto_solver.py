import tkinter as tk
from tkinter import messagebox
import pyperclip
from customtkinter import *
from PIL import Image

from AI_analyze import solve, save_solve_into_json

set_appearance_mode("dark")

# region root
root = tk.Tk()
root.geometry("1000x300+1500+100")
root.resizable(False, True)
root.minsize(1000, 500)
root.maxsize(1000, 500)
root.title('Решатель задач по физике')
root.iconbitmap(default="icon.ico")
root.attributes('-alpha', 0.99)
root.config(bg="#404b62")
# endregion

# region main_frame
main_frame = CTkFrame(root, fg_color='gray22')
main_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
# endregion

# region program_name
program_name_label = CTkLabel(master=main_frame, text="Решатель задач по физике v2.01", width=150, height=50, corner_radius=20, font=("Courier", 30), text_color="white")
program_name_label.place(relx=0, rely=0.01)
# endregion

# region task_entry
task_entry = CTkEntry(master=main_frame, width=750, height=35, fg_color="#404b62", placeholder_text="Введите задачу по физике")
# task_entry.focus()
task_entry.place(relx=0.01, rely=0.12)


# endregion

# region paste_button
def paste_button_command():
    task_entry.delete(0, END)
    task_entry.insert(0, pyperclip.paste())


paste_button = CTkButton(master=main_frame, text='вставить', font=("Courier", 13), width=40, height=35, fg_color='#117394', hover_color='#404b62', command=paste_button_command)
paste_button.place(relx=0.78, rely=0.12)

# endregion

# region start_label
# start_label = CTkLabel(master=main_frame, font=("Courier", 13), fg_color='gray22', corner_radius=5, width=400)
# start_label.place_forget()
start_label = CTkTextbox(master=main_frame, font=("Courier", 17), fg_color='gray22', width=900, wrap=WORD)
start_label.place_forget()


# endregion

# region start_button
def start_button_command(event=None):
    start_label.delete(1.0, END)
    if solved := solve(task_entry.get()):
        if isinstance(solved, dict):
            text = "".join([f"{i}: {solved[i]}\n\n" for i in solved])
        elif isinstance(solved, str):
            text = solved

        start_label.insert(1.0, text)
        start_label.place(relx=0.02, rely=0.22)
        start_label.configure(height=350)

        save_button.place(relx=0.94, rely=0.22)
    else:
        messagebox.showerror("Ошибка", "Что-то пошло не так. Попробуйте ввести другой запрос.")


start_button = CTkButton(master=main_frame, text='  пуск  ', font=("Courier", 13), width=40, height=35, fg_color='#117394', hover_color='#404b62', command=start_button_command)
start_button.place(relx=0.865, rely=0.12)

task_entry.bind('<Return>', start_button_command)


# endregion

# region save_button
def save_button_command():
    save_solve_into_json(prompt=task_entry.get(), analyzed_prompt=start_label.get(1.0, END))

like_img = CTkImage(Image.open("heart.png"), size=(30, 30))
save_button = CTkButton(master=main_frame, image=like_img, text="", width=40, height=35, command=save_button_command, bg_color="transparent", fg_color='transparent',
                        hover_color='#404b62')
save_button.place_forget()
# endregion

root.mainloop()
