#!/usr/bin/env python
# coding: utf-8

# ## Задание 3 Колодуб Елена Сергеевна

# Марафонец прошел S км со скоростью V км/с (расстояние и скорость вводятся с клавиатуры). Определить сколько времени он был в пути ч, мин, с?  

# In[8]:


S = float (input('Введите расстояние, км: '))
V = float (input('Введите скорость км/c: '))
tc=S/V
tч=((S/V)/3600)
tмин=((S/V)/60)
print(tc)
print(tч)
print(tмин)


# Пользователь вводит с клавиатуры два дробных числа, вывести на экран суммы целых и дробных частей  

# In[14]:


lst=float (input('Введите первое число: ')), float (input('Введите второе число: '))
def rounding(lst):
    integer = [int(x) for x in lst]
    fractional = [x - integer[i] for i, x in enumerate(lst)]
    return sum(integer), round(sum(fractional), 2)
print(rounding(lst))


# In[ ]:




