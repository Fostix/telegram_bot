from email import message
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters
import datetime
from spy import *
from emoji import emojize
import math




def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('{} Hello'.format(emojize(':wave:', use_aliases=True)))




def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help')


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

    
def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text # берёт сообщение пользователя и положит в переменную
    print(msg)
    items = msg.split() # /sum 123 321
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')


def minus_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    item = msg.split()
    x = int(item[1])
    y = int(item[2])
    update.message.reply_text(f'{x} - {y} = {x-y}')


def root_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('{}'.format(math.sqrt(int(update.message.text.split()[1]))))



def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)



def number_of_candies(update: Update, context: CallbackContext):
    update.message.reply_text('Введите количество конфет: !')
    return update.message.text

candies = 27


def g(update: Update, context: CallbackContext):
    global candies
    log(update, context)
    update.message.reply_text('start game!')
    max = 7
    min = 1
    if candies > 0:
        candies -= int(update.message.text)
        update.message.reply_text(f'{candies} осталось')
        if candies == 0:
            update.message.reply_text('you win!')
            candies = number_of_candies(CommandHandler('g', g))
        bot = candies % (max + min)
        candies -= bot
        update.message.reply_text(f'{candies} осталось bot')
        if candies == 0:
            update.message.reply_text('you lose!')
            candies = number_of_candies(CommandHandler('g', g))


