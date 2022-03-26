from telegram.ext import CallbackContext
import datetime
from spy import *
import emoji
import math




def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('{} Hello'.format(emoji.emojize(':wave:')))




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


# candies = 27
# def start_game_candies(update: Update, context: CallbackContext):
#     update.message.reply_text('setting games')
#     game_activate = True
#     return game_activate


# def game_setting(update: Update, context: CallbackContext):

#     update.message.reply_text('how many candies: ')
#     candies = int(update.message.text)

#     update.message.reply_text('max take candies: ')
#     max = int(update.message.text)
#     return candies, max
    





# def g(update: Update, context: CallbackContext, candies, max):
#     log(update, context)
#     update.message.reply_text('start game!, введите сколько конфет можно ввести: ')
#     max = update.message.text
#     min = 1
#     update.message.reply_text('введите количество конфет: ')
#     candies = update.message.text
#     if candies > 0:
#         bot = candies % (max + min)
#         candies -= bot
#         update.message.reply_text(f'{candies} осталось')
#         if candies < 0:
#             update.message.reply_text('you lose!')
#         take = update.message.text
#         print(take)
#         candies -= int(take)
#         update.message.reply_text(f'{candies} осталось')
#         if candies < 0:
#             update.message.reply_text('you win!')
        
    