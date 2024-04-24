#!/usr/bin/env python
# coding: utf-8

# ## Задание 6 Колодуб Елена Сергеевна

# Вывести горизонтальную линию из звездочек, кол-во задает пользователь

# In[69]:


numbers = input().split() 
for i in numbers: 
    print('*' * int(i))


# С клавиатуры вводится число любой разрядности, нужно перевернуть это число в обратном порядке

# In[70]:


n1 = int(input("Введите целое число: "))

digit = n1 % 10
n2 = digit
n1 = n1 // 10
while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit
print('Обратное число:', n2)


# Написать игру "Угадай число". Пользователь мысленно загадывает число от 0 до 1000, компьютер отгадывает его за минимальное количество попыток 

# In[71]:


from random import randint as rn
def game():
    n=rn(int(input('\tот\n')),int(input('\tдо\n')))
    p=int(input('\tпопытки\n'))
    for i in range(p):
        if int(input())==n:
            print('\tвы выиграли\n')
            return
    print('\tвы проиграли\n')
game()
f=input('\tещё раз?\n')
if f=='да':
    game()
else:
    print('\tпока\n')


# In[ ]:


import random
while True:
    Min = int(input("Минимальное число для угадывания: "))
    Max = int(input("Максимальное число для угадывания: "))
    trying = int(input("Количество попыток: "))
    num = random.randint(Min,Max)
    y = 1
    x = int(input("Я загадал число от " + str(Min) + " до "+ str(Max) + ", попробуй его угадать!\n"))
    while y < trying and x!=num:
        if x == num:
            break
        elif x>num:
            print("Извини, но твоё число немного больше нужного...")
            x = int(input("Попробуешь Ещё раз?\n"))
            y+=1
        elif x<num:
            print("Нет, не угадал, твоё число поменьше моего будет))")
            x = int(input("Попробуешь Ещё раз?\n"))
            y+=1
    if x!=num:
        print("Ты не смог угадать число", num,"за " + trying  +" попыток")
    else:
        print("Поздравляю! Ты отгадал число с", y,"попытки")
    import os
    def commander(cmd):
        print(cmd)
        os.system('cls')
    if __name__ == '__main__':
        cmd = input()
        commander(cmd)


# In[ ]:




