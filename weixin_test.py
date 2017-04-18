#coding:utf-8
from wxpy import *
import selenium

bot=Bot(cache_path=True)
# my_friend=ensure_one(bot.search('任嘉铭'))
# tuling=Tuling(api_key='1262cb0c6de046c1aa38b6f49ec40a38')
# @bot.register(my_friend)
# def reply_my_friend(msg):
#     tuling.do_reply(msg)
# embed()
bot.file_helper.send_image('wocao.png')
