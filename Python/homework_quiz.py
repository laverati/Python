from sqlite3 import connect
from random import choice


def create_quiz(cursor):
    cursor.execute("""drop table if exists quiz""")
    cursor.execute("""CREATE TABLE quiz (level int, question text, option_1 text, option_2 text, option_3 text, option_4 text, right_option int)""")
    cursor.execute("""INSERT INTO quiz VALUES 
    (1, 'Что из перечисленного является единственной оперой Бетховена?', 'Фиделио', 'Дон Жуан', 'Волшебная флейта', 'Кармен', 1), 
    (1, 'В каких жанрах не писал Бах?', 'Квартеты', 'Сонаты', 'Оперы', 'Симфонии', 3),
    (1, 'Кто по образованию Чайкоский?', 'Врач', 'Юрист', 'Композитор', 'Пианист', 2),
    (2, 'Как звали сестру Моцарта?', 'Аврора', 'Изабелла', 'Сусанна', 'Наннерль', 4),
    (2, 'Сколько актов в Щелкунчике?', '1', '2', '3', '4', 2),
    (2, 'Сколько опер у Глинки?', '4', '12', '2', '7', 3),
    (3, 'Что из перечисленного Мусоргский не писал?', 'Картинки с выставки', 'Полет шмеля', 'Борис Годунов', 'Хованщина', 2),
    (3, 'Шопен композитор какой страны?', 'Польши', 'Франции', 'России', 'Испании', 1),
    (3, 'Что из перечисленного Бах не писал?', 'ХТК', 'Рожденственская оратория', 'Свадьба Фигаро', 'Искусство фуги', 3),
    (4, 'Рахманинов был...', 'Композитором', 'Пианистом', 'Дирижером', 'Все вышеперечисленное', 4),
    (4, 'Композитором какой эпохи был Лист?', 'Барокко', 'Романтизм', 'Авангард', 'Импрессионизм', 2),
    (4, 'Композитором какой эпохи был Бах?', 'Барокко', 'Романтизм', 'Авангард', 'Импрессионизм', 1),
    (5, 'Как называлась вилла Рахманинова в Швейцарии?', 'Сантих', 'Атас', 'Сенар', 'Манис', 3),
    (5, 'Сколько опер у Римского-Корсакова?', '6', '15', '9', '21', 2),
    (5, 'Что из перечисленного писал Прокофьев?', 'Петя и Волк', '1812', 'Спящая красавица', 'Леди Макбет Мценского уезда', 1);""")

def viktorina():
    conn = connect("/home/sirius/Python/Домашние работы/викторина вопросы-ответы.db")
    cursor = conn.cursor()
    create_quiz(cursor)
    level = 1
    while level < 6:
        print("Уровень ", level, end='\n'*2)
        cursor.execute(f"SELECT * FROM quiz WHERE level = {level}")
        tuple_quiz = choice(cursor.fetchall())
        print(tuple_quiz[1], "\n\nВарианты:")
        for i in range(1, 5):
            print(i, ') ', tuple_quiz[i+1], sep='')
        answer = int(input("\nВаш ответ: "))
        if answer == tuple_quiz[6]:
            print("Ответ правильный!")
            level += 1
        else:
            print("Вы проиграли\nПравильный ответ:", tuple_quiz[tuple_quiz[6] + 1])
            break
        print("-" * 50)
    if level == 6:
        print("Победа!")
    conn.commit()
    cursor.close()
    conn.close()

viktorina()






