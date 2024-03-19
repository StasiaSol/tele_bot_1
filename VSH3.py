import Setting_bot
import telebot
from telebot import types
from telebot.types import InlineKeyboardButton as ib

bot = telebot.TeleBot(Setting_bot.SeyKeys)
ans = ''


@bot.message_handler(commands = ['start'])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup()
    num = [['7','8','9','*'],['4','5','6','-'],['1','2','3','+'],['0','/','=']]
    for n in num:
        if len(n)==4:
            keyboard.row(ib(n[0],callback_data=n[0]),ib(n[1],callback_data=n[1]),ib(n[2],callback_data=n[2]),ib(n[3],callback_data=n[3]))
        elif len(n)==3:
            keyboard.row(ib(n[0],callback_data=n[0]),ib(n[1],callback_data=n[1]),ib(n[2],callback_data=n[2]))
    
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
