from os import system
import telebot
import time
from botsToken import token #yours bot token! (token = "<token>")

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])

def handle_text(message):
    if message.text == "get":
    	system("wget -qO- ipinfo.io/ip > result")
    	time.sleep(2)
    	f = open('result','r')
    	for line in f:
    		ip = line
    	bot.send_message(message.from_user.id, line)
    
    
def main():
	bot.polling(none_stop=True, interval=0)

if __name__ == "__main__":
	main()

