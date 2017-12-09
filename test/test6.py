# coding:utf-8
import os
import random

password_list = [1234, 123456]


def account_login():
    password = input('Password:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed successfully!')
        account_login()
    else:
        print('Wrong password or invalid input!')
        account_login()


account_login()
for i in range(1, 10):
    for j in range(1, 10):
        print('{} X {} = {}'.format(i, j, i * j)),
        if i == j:
            print
            break

all = 1000


def aaa():
    global all
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    c = random.randrange(1, 7)
    sum = a + b + c
    if sum < 9:
        result = '小'
        all = all - 100
    else:
        result = "大"
        all = all + 100
    print str(a) + " " + str(b) + " " + str(c) + " " + result
    print all
    aaa()


aaa()


class a:
    faaa = ['1', '2', '3', '4']
