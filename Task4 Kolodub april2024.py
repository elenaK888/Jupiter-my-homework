#!/usr/bin/env python
# coding: utf-8

# ## Задание 4 Колодуб Елена Сергеевна

# Вывести число и определить четное оно или нет

# In[21]:


number = int(input("Введите число: "))
if number % 2==0:
    print("Это чётное число")
else:
    print("Это НЕчётное число")


# Ввести три числа и определить наименьшее среди них

# In[22]:


a=int(input())
b=int(input())
c=int(input())
if a>b>c:
   print(c)
elif a<b<c:
    print(a)
else:
    print(b)


# Реализовать калькулятор. Вводятся 2 любых вещественных числа в переменных a и b. Необходимо вывести на экран меню с пунктами
# 1. a+b 
# 2. a-b 
# 3. a*b
# 4. a/b
# 5. a%b
# При выборе соотвествующего пункта должна быть проверка на нуль

# In[29]:


x = int(input()) 
y = int(input()) 
znak = input() 
if(znak == "+"): 
    print(x+y) 
elif(znak == "-"): 
    print(x-y) 
elif(znak == "*"): 
    print(x*y) 
elif(znak == "%"): 
    print(x*y) 
elif(znak == "/" and y != 0): 
    print(x/y) 
elif(znak == "**"): 
    print(x**y) 
else: 
    print("Ошибка")


# In[ ]:





# In[ ]:




