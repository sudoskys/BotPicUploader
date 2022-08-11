# encoding: utf-8
from telebot import logger
import telebot
import os
import time
import random
import requests
import joblib
import time
joblib.dump("on", 'life.pkl')
import linecache

#====================================================

def get_line_count(filename):
    count = 0
    with open(filename, 'r') as f:
        while True:
            buffer = f.read(1024 * 1)
            if not buffer:
                break
            count += buffer.count('\n')
    return count

def tail (files,line_count=3):
    linecache.clearcache()
    lines=[]
    line_count=0
    line_sum = get_line_count(files)
    # print(linecache.getline(files,line_count+1-TailLine))
    # print('总数: ', line_sum)
    lines.append("总数："+str(line_sum)+"\n")
    # line_count = line_count - 29
    if line_sum>10:
       line_sum=10
    for i in range(line_sum):
        last_line = linecache.getline(files,line_sum+1-line_count)
        # last_line = linecache.getline(files,line_count)
        line_count += 1
        if last_line:
           lines.append(last_line)
    strs="".join(lines)
    return strs if strs else "None"


#=============================================================
import random


class test(object):
    def __init__(self):
        self.headers_from_data = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Cache-Control': 'max-age=0',
            # 'Content-Type': 'multipart/form-data; boundary=c0c46a5929c2ce4c935c9cff85bf11d4',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            # 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3LnZpa2FjZy5jb20iLCJpYXQiOjE2NDU3Njc1NTUsIm5iZiI6MTY0NTc2NzU1NSwiZXhwIjoxNjYxOTI0MzU1LCJkYXRhIjp7InVzZXIiOnsiaWQiOiIyMjg5NzIifX19.-Duz6GCClfr8xYVgCYclYndkRyoRuuHx_xbJ9OiWtrk',
        }
    def upload(self,fileName):
        # if Now==sys._getframe().f_code.co_name:
             import requests
             target="返回了"
             return target
"""
             try:
                response = requests.post(url=url, files=files, data=data)
                codes=response.status_code
             except:
                codes=000
             if codes==200:
               if response.json().get("flag")==1:
                  target=response.json().get("data")
               else:
                  target=False
             else:
               target=False
             return target
"""


class launchPhoto(object):
    def __init__(self):
       self.num=random.randint(0,len(rocket)-1)
    def send(self,obj,sFile):
        if not len(rocket)==0:
           url=rocket[(self.num)].upload(sFile)
           if not url:
                rocket.pop(self.num)
                # url=obj.send(obj,sFile)
           else:
             return url
        else:
           url="无可用上传源"
           return url
#=======================================================================================


class CallingCounter(object):
    def __init__ (self):
        pass
    def get(self, key):
        key=str(key)+time.strftime("%Y-%m-%d-%H",time.localtime())
        if not hasattr(self,'count'):
           self.count = dict()
        if key in self.count:
            self.count[key] += 1
        else:
            self.count[key] = 0
        return self.count[key]


def getRoot():
    import os
    return os.getcwd() + '/Pic/'


def getID():
    c = random.randint(2, 546)
    ID = str(int(time.time()) * int(c) - int(c))
    return ID


def dealFile(info):
    if hasattr(info, 'file_name'):
       name = os.path.splitext()[-1]
    else:
       name='.jpg'
    roads = getRoot() + getID() + name
    down_file = bot.download_file(info.file_path)
    with open(roads, 'wb') as new_file:
           new_file.write(down_file)
    return roads


def workPhoto(userID,fileID, road):
    sender=launchPhoto()
    url=sender.send(sender,road)
    return url

#------------------------------------


count=CallingCounter()
bot = telebot.TeleBot("54340198xxxxxxxxxxxxxxY4Fo")
isExist = os.path.exists(getRoot())
if not isExist:
    os.makedirs(getRoot())



def Upload(userID,Name,fileID):
      come=""
      if life():
        file_info = bot.get_file(fileID)
        road=dealFile(file_info)
        target = workPhoto(userID,fileID, road)
        os.remove(road)
        come=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+" - "+str(Name)+"-"+str(userID)+" - "+target
        print(come)
        with open("run.log", 'a+') as f:
             f.write(come+'\n')   #加\n换行显示
      else:
        target="Bot sleeping,please wait for some time"
      return target


def life():
   try:
     if joblib.load('life.pkl')=="on":
        return True
     else:
        return False
   except Exception as e:
        print("Wrong:life.pkl do not exist"+str(e))
        return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "发送单张图片，我将上传并返回链接..")


@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "由支持的图床服务.")


@bot.message_handler(content_types=['text'])
def send_about(message):
    userID = message.from_user.id
    if str(userID)=="5275155445":
       # bot.reply_to(message, "主人你好！")
       # msg = bot.reply_to(message, '主人你好！指令控制！')
       # bot.register_next_step_handler(msg, process_command_step)
       try:
        chat_id = message.chat.id
        command = message.text
        if command=="off":
            joblib.dump("off", 'life.pkl')
            msg = bot.reply_to(message, 'success！')
        if command=="on":
            joblib.dump("on", 'life.pkl')
            msg = bot.reply_to(message, 'success！')
        if command=="show":
            #somes=tail(r'./run.log',7)
            somes=len(rocket)
            msg = bot.reply_to(message, somes)
       except Exception as e:
            bot.reply_to(message, "Wrong:"+str(e))


@bot.message_handler(content_types=['photo'])
def gotPhoto(message):
    userID = message.from_user.id
    Name=message.from_user.first_name
    if count.get(userID)<30:
      fileID = message.photo[-1].file_id
      target=Upload(userID,Name,fileID)
      bot.reply_to(message, target)
    else:
      bot.reply_to(message, "Sorry,too many photo upload this hour!")
      # bot.reply_to(message, str(message))


@bot.message_handler(content_types=['document'])
def gotFile(message):
    userID = message.from_user.id
    Name=message.from_user.first_name
    if count.get(userID)<30:
      if message.document:
         file_size = message.document.file_size
         if 'image' in str(message.document.mime_type)or  'gif' in str(message.document.mime_type):
            pngis=True
         if file_size<10485760 and pngis:
           types = message.document.mime_type
           fileID = message.document.file_id
           target=Upload(userID,Name,fileID)
           bot.reply_to(message, target)
         else:
           bot.reply_to(message, '超出上传范围，文件过大:TOO LARGE')
    else:
      bot.reply_to(message, "Sorry,too many photo upload this hour!")


rocket = [test()]
bot.infinity_polling()

# 请使用nohup运行
