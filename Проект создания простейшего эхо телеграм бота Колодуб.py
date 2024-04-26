#!/usr/bin/env python
# coding: utf-8

# #Проект-создание простешего телеграм-бота Колодуб

# In[14]:


pip install pytelegrambotapi


# In[ ]:


import telebot
bot = telebot.TeleBot('6772746876:AAHeAwNKjDo17wAEIovxbx55Z3AjGFN7D9M')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
bot.polling(none_stop=True, interval=0)


#  t.me/elenakolodub888_bot
#  ![image.png](attachment:image.png)

# In[ ]:




