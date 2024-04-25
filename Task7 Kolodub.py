#!/usr/bin/env python
# coding: utf-8

# ## Задание 7 Колодуб Елена Сергеевна

# Вывести на экран таблицу умножения (Пифагора)

# In[9]:


for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end = " ")
    print("")


# In[2]:


for i in range(1, 10):
    for j in range(1, 10):
        print("%4d" % (i * j), end="")
    print()


# In[3]:


i = 1
while i < 10:
    j = 1
    while j < 10:
        print("%4d" % (i * j), end="")
        j += 1
    print()
    i += 1


# показать на экране прямоугольник размером M на N, состоящий звездочек. Затем сделать тоже самое, но чтобы фигура внутри была пустая, остается только рамка   

# In[4]:


def print_rectangle(m ,n):
    for i in range(m):
        for j in range(n):
            print('*', end='')
        print()
 
m = int(input())
n = int(input())
print_rectangle(m , n)


# In[5]:


w = int(input("Введите ширину: "))
h = int(input("Введите высоту: "))
 
for i in range(h):
    if i == 0 or i == h - 1:
        for j in range(w):
            print('*', end=' ')
    else:
        print('*', end=' ')
        for j in range(1, w - 1):
            print(' ', end=' ')
        print('*', end=' ')
    print()


# Показать на экране равнобедренный треугольник, пользователь вносит высоту, затем тоже самое но чтобы фигура внутри была пустая, остается только рамка

# In[6]:


n = int(input('N='))
for i in range(n):
    k1 = n - 1 - i
    k2 = n - 1 + i
    for j in range(k2 + 1):
        print('O' if j >= k1 else ' ', end='')
    print()


# Определить является ли число любой разрядности палиндромом

# In[8]:


number = input("Введите число: ") 
if number == number[::-1]: 
    print("Число является палиндромом") 
else: 
    print("Число не является палиндромом")


# In[9]:


number = input("Введите число: ") 
if number == number[::-1]: 
    print("Число является палиндромом") 
else: 
    print("Число не является палиндромом")


# Написать программу, которая выводит на экран все простые числа от 2 до 10 000 000

# In[1]:


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n
    
def vers(n):
    limit = int(input())
    prime = []
    num = 2
    while not(num > limit):
        if is_prime(num):
            prime.append(num)
        num += 1
    return prime
print(*vers(1))


# Показать на экране все числа Амстронга от 0 до 10000000

# In[ ]:


print('Введите число')
N = int(input())
for x in range (1, N + 1):
    
    tmp = 0
    for i in str(x):
        tmp += int(i) ** len(str(x))
        
    if tmp == x:
        print(x)
        
print('end')


# Написать программу, которая генерирует календарь на любой год, указанный с клавиатуры

# In[ ]:


import datetime
дни = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
месяцы = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май',
          'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
print('Создатель календаря')

while True:  
    print('Введите год для календаря:')
    response = input('> ')
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

print('Пожалуйста, введите числовой год, например 2024')

while True: 
    print('Введите месяц для календаря, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Пожалуйста, введите числовой месяц, например, 4 для апреля')
        continue
        
month = int(response)
    if 1 <= месяцы <= 12:
        break
print('Введите число от 1 до 12')


def getCalendarFor(год, месяц):
    calText = ''  
    calText += ('  ' * 34) + месяцы[месяц - 1] + '  ' + str(год) + '\n'
    calText += '...Воскресенье.....Понедельник....Вторник...Среда...' \
               'Четверг...Пятница...Суббота...\n'
    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('|          ' * 7) + '|\n'

    currentDate = datetime.date(year, month, 1)

    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True: 
        calText += weekSeparator

        dayNumberRow = '' 
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)

        dayNumberRow += '|\n'  

        calText += dayNumberRow
        for i in range(3):
            calText += blankRow 

        if currentDate.month != месяц:
            break

    calText += weekSeparator
    return calText


calText = getCalendarFor(год, месяц)
print(calText)

calendarFilename = 'calendar_{}_{}.txt'.format(год, месяц)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to  ' + calendarFilename)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




