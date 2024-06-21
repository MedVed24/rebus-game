from tkinter import *
from tkinter.messagebox import showinfo, askyesno
import random
import time
from PIL import ImageTk
import game_points
import tips_logic
import os
import pyglet


num_level = 0 #Номер уровня
answer = ''
num_click = 0


def new_game_start(event):
    confirm = askyesno(title="Новая игра", message="Хотите начать новую игру?")
    if confirm:
        l_file = open("config.txt", "w")
        l_file.write("0")
        game_points.__points = 0
        l_file.close()
        fun_start(event)
    else:
        return


def save_current_level_to_file():
    global num_level
    l_file = open("config.txt", "w")
    l_file.write(str(num_level)+"\n")
    l_file.close()


def fun_start(event):
    global num_level, list_answer, num_click
    but_x = []
    but_y = []
    but = []

    if os.path.isfile("config.txt"):
        l_file = open("config.txt", "r")
        num_level = int(l_file.readlines()[0])
        l_file.close()
    else:
        save_current_level_to_file()
    def f_k(event, num_but):  # Обработка события нажатия кнопки
        #global but_x, but_y, but
        global answer
#        ent.insert(END, but[num_but]['text'])
        if but_y[num_but] == 530:
            return
        answer += but[num_but]['text']
        num_ans = len(answer) - 1
        new_x[num_but] = 50*num_ans + 100
        but_y[num_but] = 530
        but[num_but].place(x=new_x[num_but], y=530)
        #        game.itemconfig(but[num_but], y=580)
        if answer == list_answer[num_level]:
            label1['text'] = "Верно"
            label1['foreground'] = "green"
            game.update()

            game_points.points_up()  # Баллы

            time.sleep(3)
            new_level()

    def delete_t(event): # Функция очистки ответа
        global answer
        answer = ''
        for i in range(count_but):
            new_x[i] = 50 * i + 100
            but_x[i] = 50 * i + 100
            but_y[i] = 480
            but[i].place(x=new_x[i], y=480)
        for i in range(count_b[num_level], count_but):
            but[i].place_forget()
        #ent.delete(0, END)

    def new_level():
        global num_level, answer, num_click
        num_click = 0
        label_tips['text'] = ''
        label_points['text'] = game_points.__points

        num_level += 1
        save_current_level_to_file()
        label1['text'] = ""
#        ent.delete(0, END)
        if num_level > len(list_answer) - 1: # Завершение игры
#           label1['text'] = 'Игра окончена'
            showinfo(title="Завершение игры", message="Игра окончена")
#            game.update()
            time.sleep(3)
            return

        game.title("Игра " + str(num_level + 1) + " уровень")
        photo[0]['image'] = list_img[num_level][0]
        photo[1]['image'] = list_img[num_level][1]
        photo[2]['image'] = list_img[num_level][2]
        photo[3]['image'] = list_img[num_level][3]
        for i in range(count_but):
            but[i]['text'] = ''
            new_x[i] = 50 * i + 100
            but_x[i] = 50 * i + 100
            but_y[i] = 480
            but[i].place(x=new_x[i], y=480)
        #    game.itemconfig(but[i], text=list_letters[num_level][i])
        for i in range(count_b[num_level]):
            but[i]['text'] = list_letters[num_level][i]
        answer = ""
        for i in range(count_b[num_level], count_but):
            but[i].place_forget()

    game = Toplevel()
    game.geometry('800x600+0+50')
    game.title("Игра "+str(num_level)+" уровень")
    but_press = 0
    num_but = 0
    abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    list_letters = []
    count_but = 15
    label_tips = Label(game, text='', font=10)
    label_tips.place(x=620, y=350)

    def update_tips_text(text):
        label1['text'] = text

    def update_points_text(points):
        label_points['text'] = points

    def show_tips():
        global num_click
        if num_click > len(list_answer[num_level])-1:
            return
        label_tips['text'] += list_answer[num_level][num_click]
        num_click += 1

    but_tips = Button(game, text='Подсказка 10б', width=12, height=2, font="Arial 12", fg='green')
    but_tips.place(x=650, y=300)
    but_tips.bind('<ButtonPress>', lambda event: tips_logic.on_tips_button_click(
        event=event,
        num_tips_click=num_click,
        len_answer=len(list_answer[num_level]),
        label_text=lambda text: update_tips_text(text),
        label_points=lambda points: update_points_text(points),
        show_tips=lambda: show_tips()
    ))

    for i in range(len(list_answer)):
        ansi = list_answer[i]
        count_but0 = count_b[i]
        for j in range(count_but0 - len(list_answer[i])):
            ansi = ansi + abc[random.randint(0, len(abc) - 1)]
        ## Преобразуем строку в список
        list_ansi = list(ansi)
        # Перемешиваем список
        random.shuffle(list_ansi)
        list_letters.append(list_ansi)
    count_but = 15

    label1 = Label(game, font=("Arial", 30))
    label1.place(x=100, y=50)

    photo=[]
    photo.append('')
    photo[0] = Label(game, image=list_img[num_level][0], width=150, height=150)
    photo[0].place(x=100, y=100)

    photo.append('')
    photo[1] = Label(game, image=list_img[num_level][1], width=150, height=150)
    photo[1].place(x=300, y=100)

    photo.append('')
    photo[2] = Label(game, image=list_img[num_level][2], width=150, height=150)
    photo[2].place(x=100, y=300)

    photo.append('')
    photo[3] = Label(game, image=list_img[num_level][3], width=150, height=150)
    photo[3].place(x=300, y=300)

    label_points = Label(game, text=game_points.__points, font=("Arial", 20))
    label_points.place(x=200, y=20)

    label_p = Label(game, text="Баллы:", font=("Arial", 20))
    label_p.place(x=100, y=20)

    ## Создание набора кнопок
    old_x = [0 for i in range(count_but)]
    new_x = [0 for i in range(count_but)]
    for i in range(0, count_but):
        but.append(Button(game, text='', width=4, height=2))
        but[i].bind('<ButtonPress>', lambda event, par1=i: f_k(event, par1))
        but_x.append(0)
        but_y.append(0)
        but_x[i] = 50*i + 100
        old_x[i] = 50*i + 100
        but_y[i] = 480
        but[i].place(x=but_x[i], y=but_y[i])
    for i in range(0, count_b[num_level]):
        but[i]['text'] = list_letters[num_level][i]

    for i in range(count_b[num_level], count_but):
        but[i].place_forget()

    del_b = Button(game, text='Очистить', width=10, height=2, font='Arial 12', fg='red')
    del_b.place(x=520, y=300)
    del_b.bind('<ButtonPress>', delete_t)

#    ent = Entry(game, width=20, font=('Arial', 12)) ## Поле ввода
#    ent.place(x=100, y=550)



def fun_desc(event):
    descr = Tk()
    descr.geometry('800x600+0+50')
    descr.title("Описание игры")
    text_descr = "Это очень увлекательная и затягивающая игра, в которой нужно угадывать слова по "\
    "четырем картинкам, связанные с ними. Некоторые уровни очень сложные и заставят вас поломать голову.\n"\
    "Игра подходит для любителей кроссвордов, сканвордов, загадок, ребусов и логических игр.\n"\
    "Кроме того, игра помогает развивать мозг, память и внимание."
    text1 = Text(descr, height=25, width=70, padx=20, font='Georgia 30', wrap=WORD)
    text1.insert(1.0, text_descr)
    text1.pack()
    descr.update()

def fun_shop(event):
    option = Tk()
    option.geometry('800x600+0+50')
    option.title("Магазин")

    label_balance = Label(option, text="Ваш баланс:", font=("Arial", 20))
    label_balance.place(x=0, y=0)

    label_points = Label(option, text=game_points.__points, font=("Arial", 20))
    label_points.place(x=170, y=0)


menu=Tk()
menu.geometry('790x700+0+50')
menu.title("4 фото одно слово")
list_img = []

#with open("answers2.txt", "r", encoding="utf8") as file:
#    list_answer = file.read().splitlines()

#with open("count_b.txt", "r", encoding="utf8") as file:
#    count_but = file.read().splitlines()
file = open('answers.txt', 'r', encoding="utf8")
list_answer = []
count_b = []
for line in file:
    a, b = line.split()
    list_answer.append(a)
    count_b.append(int(b))


#file = open('answers.txt', 'r')
#list_answer = file.readlines()
#print(list_answer)
#list_answer = ['ГРИБ', 'ЗИМА', 'СОБАКА', 'КОМПЬЮТЕР']
for n in range(len(list_answer)):
    list_img.append([0, 0, 0, 0])
    for k in range(4):
        file_name = 'i' + str(n+1) + str(k+1) + '.jpeg'
        list_img[n][k] = ImageTk.PhotoImage(file=file_name)

imgm = ImageTk.PhotoImage(file='menuimg.jpeg')

lblm = Label(menu, image=imgm, width=790, height=770)
lblm.pack()

new_game = Button(menu, width=40, height=3, text='Новая игра')
new_game.place(x=250, y=370)
new_game.bind('<ButtonPress>', new_game_start)

start = Button(menu, width=40, height=3, text='Продолжить')
start.place(x=250, y=430)
start.bind('<ButtonPress>', fun_start)

desc = Button(menu, width=40, height=3, text='Описание') ##Описание кнопки описания
desc.place(x=250, y=490)
desc.bind('<ButtonPress>', fun_desc)

opt = Button(menu, width=40, height=3, text='Магазин') ##Описание кнопки настройки
opt.place(x=250, y=550)
opt.bind('<ButtonPress>', fun_shop)

menu.mainloop()
