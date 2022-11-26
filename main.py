from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3

conn = None
cursor = None
nomer = None

app = QApplication([])
ui = uic.loadUi("inter.html")
ui.setWindowTitle('БД о пользователях.')
ui.show()

def create():
    global conn, cursor
    file_name, ok = QInputDialog.getText(ui, "Создать БД", "Название БД: ")
    if ok and file_name != "":        
        conn = sqlite3.connect(file_name)
        cursor = conn.cursor()
        cursor.execute(''' DROP TABLE IF EXISTS my_table ''')
        cursor.execute(''' CREATE TABLE IF NOT EXISTS my_table (
                            id INTEGER,
                            name VARCHAR,
                            login VARCHAR,
                            password VARCHAR,
                            email VARCHAR ) ''')

def add_info():
    global cursor
    id = ui.lineEdit_2.text()
    name = ui.lineEdit_3.text()
    login = ui.lineEdit_4.text()
    password = ui.lineEdit_5.text()
    email = ui.lineEdit_6.text()
    cursor.executemany('''INSERT INTO my_table (id, name, login, password, email) VALUES (?,?,?,?,?)''', [(id, name, login, password, email)])

def read_info():
    global cursor, conn
    cursor.execute(''' SELECT * FROM my_table ''')
    x = cursor.fetchall()
    ui.listWidget.clear()
    for i in x:
        for ii in i:
            ui.listWidget.addItem(str(ii))
        ui.listWidget.addItem('***')

def open():
    global conn, cursor
    file_name, ok = QInputDialog.getText(ui, "Подключиться к БД", "Название БД: ")
    if ok and file_name != "":
        conn = sqlite3.connect(file_name)
        cursor = conn.cursor()

def close():
    global conn, cursor
    conn.commit()
    cursor.close()
    conn.close()

ui.pushButton_2.clicked.connect(create)
ui.pushButton.clicked.connect(add_info)
ui.pushButton_3.clicked.connect(read_info)
ui.pushButton_4.clicked.connect(open)
ui.pushButton_5.clicked.connect(close)

app.exec_()