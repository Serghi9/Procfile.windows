import telebot
import apiai
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types = ['text'])

def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Hello, my creator!')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIHsF5bnnN2ELJahNR6yN5qqdOhOuLEAAIJAAMwoooWuOlc57D36VUYBA')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Bye, creator!')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIHsl5boLffsHCupUZNnz4PB8Oqejz_AAIHAAMwoooWvpPfI5qJaTgYBA')
    elif message.text.lower() == 'вызов рабия':
        bot.send_message(message.chat.id, 'Вызываем...')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAItK15gJXY6OKSs5edfkSEXoC2JY1vGAAK6AANReM0Ph00BlaOp5vQYBA')
    elif message.text.lower() == 'хто рабій?':
        bot.send_message(message.chat.id, 'Рабій духарной пидарас!!!')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAItKV5gI7-tPgcTg1cYGUIigjA5lVv3AAJfAANAZ3QRkR-5QNPUc8cYBA')
    elif message.text.lower() == '#похуй':
        bot.send_message(message.chat.id, 'Мені похуй, просто рабій з мусорки хавае пидар!')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAItK15gJXY6OKSs5edfkSEXoC2JY1vGAAK6AANReM0Ph00BlaOp5vQYBA')

@bot.message_handler(content_types = ['sticker'])

def sticker_id(message):
    print(message)

bot.polling()
