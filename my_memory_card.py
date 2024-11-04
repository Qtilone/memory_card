from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QPushButton, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, answer, wrong1, wrong2, wrong3):
        self.question = question
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



app = QApplication([])
window = QWidget()
window.resize(650,450)
window.setWindowTitle('Железный блиц')

tx = QLabel('какой видеокатры не существует?')
button = QPushButton('Ответить')

ansbox = QGroupBox('Результат теста')
anstx = QLabel('')
ansres = QLabel('')

ansV = QVBoxLayout()
ansV.addWidget(ansres, alignment = Qt.AlignLeft)
ansV.addWidget(anstx, alignment = Qt.AlignCenter)

ansbox.setLayout(ansV)
ansbox.hide()

box = QGroupBox('Варианты ответов')
btn1 = QRadioButton('')
btn2 = QRadioButton('')
btn3 = QRadioButton('')
btn4 = QRadioButton('')

lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()
lineH = QHBoxLayout()

lineV1.addWidget(btn1, alignment = Qt.AlignCenter)
lineV1.addWidget(btn2, alignment = Qt.AlignCenter)
lineV2.addWidget(btn3, alignment = Qt.AlignCenter)
lineV2.addWidget(btn4, alignment = Qt.AlignCenter)

lineH.addLayout(lineV1)
lineH.addLayout(lineV2)

mine1 = QHBoxLayout()
mine2 = QHBoxLayout()
mine3 = QHBoxLayout()
mainV = QVBoxLayout()

mine1.addWidget(tx, alignment = Qt.AlignCenter)
mine2.addWidget(box)
mine3.addStretch(1)
mine3.addWidget(button, stretch = 2)
mine3.addStretch(1)
mine2.addWidget(ansbox)

mainV.addLayout(mine1, stretch = 2)
mainV.addLayout(mine2, stretch = 8)
mainV.addStretch(1)
mainV.addLayout(mine3, stretch = 1)
mainV.addStretch(1)

window.setLayout(mainV)
box.setLayout(lineH)
ansbox.setLayout(ansV)

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

def show_result():
    box.hide()
    ansbox.show()
    button.setText('Следующий вопрос')

def show_question():
    ansbox.hide()
    box.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [btn1, btn2, btn3, btn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    tx.setText(q.question)
    anstx.setText(q.answer)
    show_question()

def check_ans():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('Статистика')
        print('-Всего вопросов:', window.total)
        print('-Правильных ответов:', window.score)
        print('Рейтинг:', int(window.score/window.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверный')
            print('Статистика')
            print('-Всего вопросов:', window.total)
            print('-Правильных ответов:', window.score)
            print('Рейтинг:', int(window.score/window.total * 100), '%')

def show_correct(res):
    ansres.setText(res)
    show_result()

q_list = []
q_list2 = []

q_list.append(Question('какой видеокатры не существует?', 'rtx 6090', 'rtx 3060', 'rtx 3050', 'rtx 1070 super'))
q_list.append(Question('какой процессор самый дорогой?', 'ryzen 7 7800X', 'core i5 12400', 'core i5 13600', 'core i5 3400'))
q_list.append(Question('какая мышь самая дешёвая?', 'Razer Orochi V2', 'Logitech G Pro X', 'Logitech G502 X', 'DELL AW320M'))
q_list.append(Question('Какой компонент компьютера отвечает за обработку графики?', 'Видеокарта', ' Центральный процессор', 'Жесткий диск', 'Оперативная память'))
q_list.append(Question('Какая из следующих частей компьютера является основной для хранения данных?', 'Жесткий диск', 'Оперативная память', 'Видеокарта', 'Сетевой адаптер'))
q_list.append(Question('Какая из следующих частей компьютера отвечает за питание всех компонентов?', 'Блок питания', 'Жесткий диск', 'Центральный процессор', 'Видеокарта'))
q_list.append(Question('Какую роль выполняет материнская плата в компьютере?', ' Соединяет все компоненты', 'Обрабатывает графику', ' Питает компоненты', 'Хранит данные'))
q_list.append(Question('Какая часть компьютера временно хранит данные, с которыми работает процессор?', 'Оперативная память', 'Жесткий диск', 'Видеокарта', 'Блок питания')) 
q_list.append(Question('Какая характеристика процессора определяет, сколько инструкций он может выполнить за один такт?', ' Количество ядер', 'Тактовая частота', 'Объём кэша', 'Разрядность'))

def next_quest():
    global q_list, q_list2
    if len(q_list) > 0:
        cur_q = randint(0, len(q_list) - 1)
    else:
        cur_q = randint(0, len(q_list))
        q_list += q_list2
        q_list2 =[]
    if len(q_list) > 1:
        while window.cur_q == cur_q:
            cur_q = randint(0, len(q_list) - 1)
    window.total += 1
    quest = q_list[cur_q]
    window.cur_q = cur_q
    q_list2.append(quest)
    q_list.remove(quest)
    ask(quest)
    

def click_ok():
    if button.text() == 'Ответить':
        check_ans()
    else:
        next_quest()

button.clicked.connect(click_ok)

window.total = 0
window.score = 0
window.cur_q = randint(0, len(q_list) - 1)

next_quest()

window.setStyleSheet("background: #b55")
button.setStyleSheet("background: #caa")
box.setStyleSheet("background: #caa")
ansbox.setStyleSheet("background: #caa")


window.show()
app.exec_()