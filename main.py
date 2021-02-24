#from scan import Scan
from calc import eval_
from copy import copy
import telebot

token = "1345199084:AAFZkHcP7_4OlWAo11UHA9PPWZ6RN2JZsVw"
matrixes = {}
toCalc = ''
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    startMessage = """
Привет, ты используешь бот-калькулятор выражений с матрицами.
Пример работы с ним:
Допустим, нам надо вычислить значение выражения 3*А^2-4*tA, где А - это какая-то матрица. Чтобы вычислить значение этого выражения вы:
    1) Вводим выражение 3*A^2-4*tA
    2) Чтобы задать матрицу пишем /scan <Имя матрицы - Большая латинская буква> и в этом же сообщении вводим матрицу, например:
        /scan A
        1 2 3
        3 4 5
        5 6 7
    3) Если вдруг ошиблись, то /scan <Имя матрица> ещё раз
    4) Командой /calc запускаем вычисляторный процесс
    Команда /del сбрасывает всё всё всё
============================================
Операции в выражении:
+, -, *, /, ^
d<Имя матрицы> - определитель матрицы
t<Имя матрицы> - транспонировать матрицу
o<Имя матрицы> - обратная матрица
r<Имя матрицы> - ранг матрицы
===========================================
Правила:
ДЕЛЕНИЕ МАТРИЦ, ЭТО A*rB, а не A/B!!!
Если бот будет часто падать - я его обратно не включу))"""

    bot.send_message(message.chat.id, startMessage)



@bot.message_handler(commands=['scan'])
def scan_matrix(message):
    global matrixes
    s = message.text
    try:
        m = s[6]
        if m in matrixes:
            s = s.split('\n')[1:]
            s = ';'.join(s)
            matrixes[m] = s
            #print(matrixes[m])
        else:
            bot.send_message(message.chat.id, "Матрицы {} нет в Вашем выражении".format(m))
    except:
        pass

@bot.message_handler(commands=['calc'])
def calc_matrix(message):
    global matrixes, toCalc
    if toCalc:
        i = 0
        newTC = copy(toCalc)
        i = 0
        n = len(newTC)
        while i < n:
            if newTC[i] == "-" and (i == 0 or newTC[i-1] == "(" or newTC[i-1] == "*" or newTC[i-1] == "+" or newTC[i-1] == "/" or newTC[i-1] == "^"):
                j = copy(i)+1
                while newTC[j].isdigit():
                    j += 1
                newTC = newTC[:i]+"(0"+newTC[i:j]+")"+newTC[j:]
                i+=1
            i += 1 
        toCalc = newTC
        #print(matrixes)
        ans, nm = eval_(toCalc+'+0', matrixes)
        ans = str(ans)
        bot.send_message(message.chat.id, ans)
        print(toCalc+ " :: " + ans, nm)
        if ans != "error":
            for c in ans:
                if c.isupper() and c.isalpha():
                    n = nm[c].replace(';', '\n')
                    bot.send_message(message.chat.id, c + ' is: \n' + n)
                    print(c+" :: "+n)
        matrixes = {}
        toCalc = ''

@bot.message_handler(commands=['del'])
def del_matrix(message):
    global matrixes
    global toCalc
    matrixes = {}
    toCalc = ''

@bot.message_handler(content_types=['text'])
def send_text(message):
    global matrixes, toCalc
    s = message.text
    s.replace(' ', '')
    s.replace('\n', '')
    toCalc = s
    botAns = 'Введите: '
    for c in s:
        if c.isupper() and c.isalpha() and c not in matrixes:
            matrixes[c] = ''
            botAns += c+', '
    if botAns != 'Введите: ':
        botAns += 'при помощи /scan <Имя матрицы> а затем используйте /calc'
    else:
        botAns = '/calc - чтобы посчитать'
    bot.send_message(message.chat.id, botAns)


bot.polling()