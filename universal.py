# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:25:46 2021

@ismoiljamshid: Hometasks

"""
 -*- coding: utf-8 -*-
"""
Fri Jun  4 10:49:17 2021

@ismoiljamshid: Vazifalar
"""

#%%
import math
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton, QLineEdit

class Hometask(QWidget):
    def __init__(self):
        super().__init__()
        
        #asosiy layoutlar
        self.v_box = QVBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        
        #label, yozuv kiritish uchun panel
        self.label = QLineEdit()
        
        #barcha buttonlar
        self.button_p = QPushButton("Polindrome")
        self.button_c = QPushButton("Calculate")
        self.button_f = QPushButton("Factorial")
        self.button_fib = QPushButton("Fibonacci")
        self.button_clear = QPushButton("<-X")
        self.button_clearall = QPushButton("Clear")
                                           
        #gorizontal qatordagi tugmalarni qo'yib chiqamiz                                   
        self.h_box1.addWidget(self.button_p)
        self.h_box1.addWidget(self.button_c)
        
        self.h_box2.addWidget(self.button_f)
        self.h_box2.addWidget(self.button_fib)
        
        self.h_box3.addWidget(self.button_clearall)
        self.h_box3.addWidget(self.button_clear)
        
        #vertical qatordagi tugmalarni qo'yib chiqamiz
        self.v_box.addWidget(self.label)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        
        #buttonlarga funkksiyalarni ulab chiqamiz
        self.button_p.clicked.connect(lambda: self.label.setText(self.polindrome(self.label.text())))
        self.button_c.clicked.connect(lambda: self.calculator(self.label.text()))
        self.button_f.clicked.connect(lambda: self.label.setText(self.factorial_number(self.label.text())))
        self.button_fib.clicked.connect(lambda: self.label.setText(self.fibbonacci(self.label.text())))
        self.button_clear.clicked.connect(lambda: self.clear(self.label.text()))
        self.button_clearall.clicked.connect(lambda: self.clearall(self.label.text()))
        
        self.setLayout(self.v_box)

	#barcha funksiyalarni yozib chiqamiz
    def factorial_number(self, number):
        number = int(number)
        # math kutubxonasidagi factorial funksiyasidan foydalanish
        return str(math.factorial(number))
    
    def fibbonacci(self, number):
        number = int(number)
        number1, number2, fnumber = 0, 1, 0
        # agar foydalanuvchi 1 yoki 0 ni kiritsa, javob aniq 
        count = 0
        l = list()
        if number <= 0:
            return "Please enter positive integer"
        elif number == 1:
            return "0"
        #fibonacci hisoblanishi
        else:
            #while orqali C tilidagi "for"ni yasab olamiz
            while count <= number: #ushbu kod son berilgan raqamga tenglashmaguncha davom etadi
                l.append(fnumber) #har hisoblashda raqamni listga joylashtirib ketamiz
                fnumber = number1 + number2 #fnumber o'zgaruvchisi factorial raqamni o'z ichiga oladi
                #raqamlarni yangilab olamiz 
                number1 = number2 
                number2 = fnumber
                count += 1
            return str(l)
    def polindrome(self, word):
        #stringning [::1] ko'rinishida yozilsa butun so'zni qaytaradi, shuni -1 qilib qo'yilsa teskarisini qaytaradi
        if word == word[::-1]:
            return f"This word <{word}> is polindrome"
        else:
            return f"<{word}> is not polindrome"
    def calculator(self, order):
        self.label.setText(str(eval(order)))
    
    def clear(self, equation):
        self.label.setText(equation[:-1])
    
    def clearall(self, word):
        self.label.setText("")
app = QApplication(sys.argv)
win = Hometask()
win.setGeometry(500,200,300,150)
win.show()
app.exec_() 
