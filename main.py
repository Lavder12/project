from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Длительность чтения книг")
window.geometry("500x500")

frame = Frame(
    window,
    padx=10,
    pady=10)
frame.pack(expand=True)

kol_str = Label(
    frame,
    text="Сколько страниц в вашей книге ")
kol_str.grid(row=3, column=1)

kol_str_den = Label(
    frame,
    text="Сколько вы хотите читать в день ")
kol_str_den.grid(row=5, column=1)

kol_str_tf = Entry(
    frame,)
kol_str_tf.grid(row=4,column=1,pady =10)

kol_str_den_tf = Entry(
    frame,)
kol_str_den_tf.grid(row=6, column=1,pady = 10)

res_btn = Button(
    frame,
    text="Нажмите что бы получить результат")
res_btn.grid(row=7, column=2, pady=20)

def result_time():
    page = int(kol_str_tf.get())
    str_day = int(kol_str_den_tf.get())
    days = int(page / str_day)
    if page == 0 or page < 0:
        messagebox.showinfo('Результат', f'Ошибка,{page} не соответсвует введенныи данных')
    else:
        messagebox.showinfo('bmi-pythonguides', f'Вам понадобится{days} дней ')

res_btn = Button(
   frame,
   text='Нажмите что бы получить результат',
   command = result_time #Позволяет запустить событие с функцией при нажатии на кнопку.
)
res_btn.grid(row=7, column=2, pady=20)



window.mainloop()