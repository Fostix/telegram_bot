from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from bot_commands import *


updater = Updater('5139496111:AAGB9KwKmOT8coVEN8OeY1Mrjk4_Fra2KUc')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('minus', minus_command))
updater.dispatcher.add_handler(CommandHandler('root', root_command))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
updater.dispatcher.add_handler(CommandHandler('g', g))




print('server start') # не обязательно
updater.start_polling()
updater.idle()















# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,3,2,7]
# plt.plot(list)

# plt.show()












# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))













# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()











# from isOdd import isOdd

# print(isOdd(1))
# print(isOdd(4))