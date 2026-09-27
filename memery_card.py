from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QApplication, QMessageBox,
                             QRadioButton, QHBoxLayout, QPushButton, QGroupBox, QButtonGroup)
from random import shuffle, randint

class questions:
    def __init__(self, question1, right_answer, wrong1, wrong2, wrong3):
        self.question1 = question1
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(questions('Кто создатель 67?', 'Газан', 'Влад а4', 'ReadlySQ', 'Арсен'))
questions_list.append(questions('Кто создатель майнкрафт?', 'Гудж', 'Роналду', 'Месси', 'Глент'))
questions_list.append(questions('Кто создатель звездные войны?', 'Джордж Лукас', 'Неймар', 'Турпал', 'Вася со двора'))
questions_list.append(questions('Кто создатель футбола?', 'Эбенезер Кобб Морли', 'Мишаня', 'Фифа', 'Кобяков'))
questions_list.append(questions('Кто создатель баскетбол?', 'Джеймс Нейсмит ', 'Влад', 'Джейс смит', 'Сигма'))
questions_list.append(questions('Кто создатель 67?', 'Газан', 'Влад а4', 'ReadlySQ', 'Арсен'))
questions_list.append(questions('Кто создатель майнкрафт?', 'Гудж', 'Роналду', 'Месси', 'Глент'))
questions_list.append(questions('Кто создатель звездные войны?', 'Джордж Лукас', 'Неймар', 'Турпал', 'Вася со двора'))
questions_list.append(questions('Кто создатель Роблокс?', 'Эрик Кассел', 'Роналдо9', 'Джеф класи', 'Рививи'))
questions_list.append(questions('Кто создатель питон?', 'Гвидо ван Россум', 'Ярик', 'Ламин ямаль', 'Дембеле'))

def show_result():
    group_line.hide()
    AnsGroupBox.show()
    button.setText('Следуюший вопрос')

def show_question():
    AnsGroupBox.hide()
    group_line.show()
    button.setText('Ответить')
    GroupBox.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    GroupBox.setExclusive(True)

def ask(q):
    shuffle(answers)
    question.setText(q.question1)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правда')
        win.score += 1
        print(f"Статистика\n-Всего вопросов: {win.total}\n-Правильных ответов {win.score}")
        print("Рейтинг:", win.score / len(list) - 1 * 100)
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Не правда')
        print("Рейтинг:", win.score / len(list) - 1 * 100)
def next_question():
    win.total +=1

    print(f"Статистика\n-Всего вопросов: {win.total}\n-Правильных ответов {win.score}")

    cur_quest = randint(0, len(list) - 1)

    q = list[win.cur_quest]
    ask(q)

    q = questions_list[win.cur_quest]
    ask(q)

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

app = QApplication([])
win = QWidget()
win.resize(600, 400)
win.setWindowTitle('Карточки для запоменания')

# Устанавливаем фон с градиентом от LimeGreen до GreenYellow
win.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 LimeGreen, stop:1 GreenYellow);")

question = QLabel('Сколько будет 2+2?')
button = QPushButton('Ответить')

rbtn1 = QRadioButton('4')
rbtn2 = QRadioButton('3')
rbtn3 = QRadioButton('315')
rbtn4 = QRadioButton('67')

answers = [rbtn1, rbtn2, rbtn3, rbtn4]
GroupBox = QButtonGroup()
GroupBox.addButton(rbtn1)
GroupBox.addButton(rbtn2)
GroupBox.addButton(rbtn3)
GroupBox.addButton(rbtn4)

group_line = QGroupBox('Варианты ответа')

main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()

line1.addWidget(rbtn1)
line1.addWidget(rbtn2)
line2.addWidget(rbtn3)
line2.addWidget(rbtn4)
main_line.addLayout(line1)
main_line.addLayout(line2)
group_line.setLayout(main_line)

AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('Правда/Неправда')
lb_correct = QLabel('Сам верный ответ')

ans_group_line = QVBoxLayout()
ans_group_line.addWidget(lb_result, alignment=(Qt.AlignTop | Qt.AlignLeft))
ans_group_line.addWidget(lb_correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(ans_group_line)

gline = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(question, alignment=Qt.AlignCenter)
line2.addWidget(group_line)
line2.addWidget(AnsGroupBox)
line3.addStretch(2)
line3.addWidget(button, stretch=2)
line3.addStretch(2)

AnsGroupBox.hide()
gline.addLayout(line1, stretch=2)
gline.addLayout(line2, stretch=8)
gline.addStretch(1)
gline.addLayout(line3, stretch=2)
gline.addStretch(1)
gline.addSpacing(5)
win.setLayout(gline)

button.clicked.connect(click_ok)

win.score = 0
win.total = 0
next_question()


win.show()
app.exec()
