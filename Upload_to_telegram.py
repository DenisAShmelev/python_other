import time
import pyautogui
from tkinter import filedialog as fd
import pyperclip

pyautogui.PAUSE = 0.5

print('''
1. Вписываешь комманду "open".
2. Выбираешь файлы которые необходимо загрузить.
3. Переходишь в телеграм жмёшь ctrl+O, вставляешь в строку пути к папке сочетанием клавиш ctrl+V.
4. Возвращаешься в программу. Вводишь комманду "start"
5. После этого есть 5 секунд чтобы перенести курсор внутрь окна телеграм в строку канал в который необходимо произвести загрузку.
6. Ждёшь

Комманды:
open, открыть - открыть диалог выбора файлов
start, старт - запустить выполнение скрипта

''')
command = input("command:")
g = []
t = []
f = 0

if command.lower() == "open" or command.lower() == "открыть":
    f = fd.askopenfilenames()
    e = f[0].rfind("/")
    e1 = f[0][:e]
    print(e1)
    e2 = pyperclip.copy(e1)

    for i in range(0, len(f)):
        w = f[i].rfind("/")
        r = f[i].rfind(".")
        g.append(f[i][w+1:])
        t.append(f[i][w+1:r])
        print(g[i])

    command = input("command:")

if command.lower() == "start" or command.lower() == "старт":
    time.sleep(3)
    for i in range(0, len(f)):
        pyautogui.hotkey('ctrl', 'o')
        pyperclip.copy(g[i])
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
        pyperclip.copy(t[i])
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
        print("DONE -", g[i])
    print("Загрузка закончена")
    pyautogui.alert('Загрузка закончена')
    command = input("")
