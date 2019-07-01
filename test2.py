import urllib.request
import werobot#微信公众号开发模块
from werobot.replies import ArticlesReply, Article,ImageReply,TextReply,VoiceReply
import random
import json
import joke#基于图另机器人的自动回复
import music#音乐推荐模块
import message_people#该模块储存等你脱单的全部信息
import facepp#人脸识别,颜值打分,物体识别
import re
token = 'dengnituodan1'

robot = werobot.WeRoBot(token=token)



#用户订阅时反馈该信息
@robot.subscribe
def subscribe(message):
    return ' 欢迎关注我呀! 我是等你脱单的昵昵\n昵昵功能如下:\n1 脱单报名\n  方式:后台回复\'报名\'或\'脱单报名\'\n2 查询往期信息\n  方式:后台回复包含期数的信息,比如:415期\n3 信息过滤\n  方式:目前支持\'地点\',\'性别\',\'学位\',\'星座\',\'专业\'五种信息过滤,每种信息具体的属性与使用方式如下:\n  \'学位\'-->[\'学士\',\'硕士\',\'博士\'],实例:学位硕士\n  \'性别\'-->[\'男\',\'女\'],实例:性别女\n  \'星座\'-->实例:星座摩羯座\n  专业-->[\'文学\',\'工学\',\'艺术\',\'医学\',\'理学\',\'MBA\',\'管理学\',\'经济学\',\'教育学\',\'法学\',\'军事学\'],实例:专业工学\n  地点-->实例:地点辽宁省\n4 颜值测评\n  方式:后台回复美照即可哦~~\n5 歌曲推送\n  方式:包含主流歌星,纯音乐,催眠曲,抖音等音乐,实例:\'我想听阿桑的歌\',\'我想睡觉\',\'来首纯音乐\',\'抖音神曲\'等,后台会随机推送相关歌曲哦~~\n\n  上述功能也支持语音回复哦(普通话>_<!!)~~'


#文字信息
@robot.text
def first(message, session):
    #changdu=str(len(session))
    #session[changdu] = message.content
    input_shuxing = message.content[0:2]#检测是否是查找属性
    number = re.sub("\D","",message.content)#基于正则化找出字符串里面的数字
    #print (input_shuxing)
    if input_shuxing in message_people.list_can:
        ans = message_people.check_message(message.content)
        #print (ans)
        return ans
    elif '音乐' in message.content or '歌' in message.content or '曲' in message.content or '睡觉' in message.content or '催眠' in message.content:
        music1 = music.music_data(message.content)
        return music1
    elif '名字' in message.content or '叫啥' in message.content:
        ans = '我叫昵昵~~'
        return ans
    elif '颜值' in message.content:
        ans = '请回复要测颜值的照片哦~~'
        return ans
    elif number in message_people.qishu_dict.keys():
        reply = ArticlesReply(message = message)
        article = Article(
                 title=message_people.qishu_dict[number]['title'],
                 description=message_people.qishu_dict[number]['description'],
                 img=message_people.qishu_dict[number]['img'],
                 url=message_people.qishu_dict[number]['url']
                )
        reply.add_article(article)
        return reply
    elif '报名' in message.content or '脱单' in message.content:
        reply = ArticlesReply(message = message)
        article = Article(
                 title='等你脱单报名~~',
                 description='等你脱单~~',
                 img='http://kan.026cgb.com/623324/177048046.jpg',
                 url='https://mp.weixin.qq.com/s/ruwj9ARcQX5tIj-B9et1FQ'
                )
        reply.add_article(article)
        return reply
    else:
        ans = joke.chat_module(message.content)
        return ans
    

# @robot.image 修饰的 Handler 只处理图片消息
@robot.image
def img(message,session):
    path = message.img
    name = "/home/lk/python_web/WeRoBot-master/pic/"+ str(message.message_id) + ".jpg"
    f = open(name,'wb')
    f.write((urllib.request.urlopen(path)).read())
    f.close()
    ans = facepp.face_detect(name)
    #changdu = str(len(session))
    #session[changdu] = message.MediaId
    #reply = ImageReply(message=message,media_id=message.MediaId)
    return ans



#处理语音消息
@robot.voice
def yuyin(message,session):
    len_res = len(message.recognition)#语音识别结果,微信自带
    res = message.recognition[0:len_res-1]
    number = re.sub("\D","",res)#基于正则化找出字符串里面的数字
    #print (number)
    print (res)
    input_shuxing = res[0:2]#检测是否是查找属性
    if input_shuxing in message_people.list_can:
        ans = message_people.check_message(res)
        return ans
    elif '音乐' in res or '歌' in res or '曲' in res or '睡觉' in res or '催眠' in res:
        music1 = music.music_data(res)
        return music1
    elif '名字' in res or '叫啥' in res:
        ans = '我叫昵昵~~'
        return ans
    elif '颜值' in res:
        ans = '请回复要测颜值的照片哦~~'
        return ans
    elif number in message_people.qishu_dict.keys():
        reply = ArticlesReply(message = message)
        article = Article(
                 title=message_people.qishu_dict[number]['title'],
                 description=message_people.qishu_dict[number]['description'],
                 img=message_people.qishu_dict[number]['img'],
                 url=message_people.qishu_dict[number]['url']
                )
        reply.add_article(article)
        return reply
    elif '报名' in res or '脱单' in res:
        reply = ArticlesReply(message = message)
        article = Article(
                 title='等你脱单报名~~',
                 description='等你脱单~~',
                 img='http://kan.027cgb.com/623324/177048046.jpg',
                 url='https://mp.weixin.qq.com/s/ruwj9ARcQX5tIj-B9et1FQ'
                )
        reply.add_article(article)
        return reply
    else:
        ans = joke.chat_module(res)
        return ans

#处理位置信息
@robot.location
def position(message,session):
    ans = '已收到你的位置信息,昵昵马上来救你~~'
    return ans

#处理链接信息
def link(message,session):
    ans = '不知道这是一个什么链接呢~~'
    return ans


@robot.handler
def hello(message):
    return '0_o??'


robot.run()

 

 
