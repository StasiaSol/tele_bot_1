import Setting_bot
import telebot
from telebot import types
from telebot.types import InlineKeyboardButton as ib

bot = telebot.TeleBot(Setting_bot.SeyKeys)
ans = ''


@bot.message_handler(commands = ['start'])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(ib('7',callback_data='7'),ib('8',callback_data='8'),ib('9',callback_data='9'),ib('x',callback_data='*'))
    keyboard.row(ib('4',callback_data='4'),ib('5',callback_data='5'),ib('6',callback_data='6'),ib('-',callback_data='-'))
    keyboard.row(ib('1',callback_data='1'),ib('2',callback_data='2'),ib('3',callback_data='3'),ib('+',callback_data='+'))
    keyboard.row(ib('0',callback_data='0'),ib('/',callback_data='/'),ib('=',callback_data='='))
    
    bot.send_message(message.chat.id,'Calculator',reply_markup=keyboard)
    
@bot.callback_query_handler(lambda call:True)
def buttons(call):
    global ans
    if call.data == '=':
        while ans[-1]=='-' or ans[-1]=='+' or ans[-1]=='*' or ans[-1]=='/':
            ans = ans[-1]
        bot.send_message(call.message.chat.id,f'Решение: {ans} = {eval(ans)}')
        #print(eval(ans))
        ans=''
    else:
        if call.data == '+' or call.data == '-' or call.data == '*'or call.data == '/':
            if ans != '' and (ans[-1]=='+' or ans[-1]=='-' or ans[-1]=='*'or ans[-1]=='/'):
                ans = ans[:-1]+call.data
            else:
                ans += call.data
        else:
            ans += call.data

bot.polling(non_stop=True)
