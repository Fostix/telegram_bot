from telegram.ext import CallbackContext
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









def start_game_candies(update: Update, context: CallbackContext):
    print('text1')

    update.message.reply_text('setting games')
    game_activate = True
    update.message.reply_text(game_activate)
    print('text2')
    print(game_activate)

    return game_activate


# not on
def game_setting(update: Update, context: CallbackContext):

    update.message.reply_text('how many candies: ')
    candies = int(update.message.text)
    print(candies)
    update.message.reply_text('max take candies: ')
    max = int(update.message.text)
    print(max)
    return candies, max
    


# not on
# def input_method(update: Update, context: CallbackContext):
#     take = int(update.message.text)
#     return take





def g(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('start game!, введите сколько конфет можно ввести: ')
    max = update.message.text
    min = 1
    update.message.reply_text('введите количество конфет: ')
    candies = update.message.text
    print('text3')
    if candies > 0:
        print(candies)
        print(max)
        bot = candies % (max + min)
        candies -= bot
        update.message.reply_text(f'{candies} осталось')
        if candies < 0:
            update.message.reply_text('you lose!')
        print('text4')
        take = update.message.text
        
        print(take)
        candies -= int(take)
        update.message.reply_text(f'{candies} осталось')
        print('text5')
        if candies < 0:
            update.message.reply_text('you win!')







def start_game(update: Update, context: CallbackContext):
    update.message.reply_text('start game')


def setting(update: Update, context: CallbackContext):
    check = False
    if not check:
        update.message.reply_text('how many candies at oll?')
        candies = int(update.message.text)
        check = True
    if check:
        update.message.reply_text('max take candies: ')
        max = int(update.message.text)
        check = False
    print('candies:{}, max:{}'.format(candies, max))


def inputter(update: Update, context: CallbackContext):
    number = int(update.message.text)
    return number




def game(update: Update, context: CallbackContext):
    max = 0
    update.message.reply_text('how many candies')
    candies = int(update.message.text)
    if max == 0:
        update.message.reply_text('max take candies:')
        max = int(update.message.text)
        print('candies:{}, max:{}'.format(candies, max))





        
    
