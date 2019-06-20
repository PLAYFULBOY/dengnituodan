import urllib.request
import werobot
from werobot.replies import ArticlesReply, Article,ImageReply,TextReply
import random

import joke

import facepp

token = 'dengnituodan1'

robot = werobot.WeRoBot(token=token)

# @robot.text 修饰的 Handler 只处理文本消息

 


@robot.subscribe
def subscribe(message):
    return '欢迎关注我呀!  你可以聊天.问天气.笑话等还可以测颜值哦~~'



def music_data():
    music_list = [
            ['童话镇','陈一发儿','https://e.coka.la/wlae62.mp3','https://e.coka.la/wlae62.mp3'],
            ['都选C','缝纫机乐队','https://files.catbox.moe/duefwe.mp3','https://files.catbox.moe/duefwe.mp3'],
            ['精彩才刚刚开始','易烊千玺','https://e.coka.la/PdqQMY.mp3','https://e.coka.la/PdqQMY.mp3'],
            ['温柔','五月天','http://music.163.com/song/386538/?userid=444850037','http://music.163.com/song/386538/?userid=444850037'],
            ['后来','刘若英','http://music.163.com/song/254574/?userid=444850037','http://music.163.com/song/254574/?userid=444850037'],
            ['大碗宽面', '吴亦凡', 'http://music.163.com/song/1359595520/?userid=121295973', 'http://music.163.com/song/1359595520/?userid=121295973'],
            ['遇见', '孙燕姿', 'http://music.163.com/song/287035/?userid=444850037','http://music.163.com/song/287035/?userid=444850037'],
            ['倒数', '邓紫棋', 'http://music.163.com/song/1299550532/?userid=444850037','http://music.163.com/song/1299550532/?userid=444850037'],
            ['岁月神偷', '金玟', 'http://music.163.com/song/28285910/?userid=444850037','http://music.163.com/song/28285910/?userid=444850037 '],
            ['烟火里的尘埃', '华晨宇', 'http://music.163.com/song/29004400/?userid=444850037', 'http://music.163.com/song/29004400/?userid=444850037'],
            ['起风了', '买辣椒', 'http://music.163.com/song/1330348068/?userid=444850037', 'http://music.163.com/song/1330348068/?userid=444850037'],
            ['来自天堂的魔鬼', '邓紫棋', 'http://music.163.com/song/36270426/?userid=444850037', 'http://music.163.com/song/36270426/?userid=444850037'],
            ['单身情歌','林志炫','http://music.163.com/song/26090160/?userid=121295973','http://music.163.com/song/26090160/?userid=121295973'],
            ['曾经的你','许巍','http://music.163.com/song/167975/?userid=121295973','http://music.163.com/song/167975/?userid=121295973'],
            ['青春万岁','潘新明','http://music.163.com/song/36921484/?userid=121295973 ','http://music.163.com/song/36921484/?userid=121295973 '],
            ['Lemon Tree','Fool\'s Garden','http://music.163.com/song/17858810/?userid=121295973','http://music.163.com/song/17858810/?userid=121295973'],
            ['青春再见','水木年华','http://music.163.com/song/26494128/?userid=121295973','http://music.163.com/song/26494128/?userid=121295973'],
            ['丁香花','唐磊','http://music.163.com/song/151985/?userid=121295973','http://music.163.com/song/151985/?userid=121295973'],
            ['贝加尔湖畔','李健','http://music.163.com/song/109998/?userid=121295973','http://music.163.com/song/109998/?userid=121295973'],
            ['沧海一声笑','张晓红','http://music.163.com/song/340868/?userid=121295973','http://music.163.com/song/340868/?userid=121295973'],
            ['探清水河(吉他版)','张云雷','http://music.163.com/song/547973474/?userid=121295973','http://music.163.com/song/547973474/?userid=121295973'],
            ['乌兰巴托的爸爸','英格玛','http://music.163.com/song/318929/?userid=121295973','http://music.163.com/song/318929/?userid=121295973'],
            ['黑猫警长','沈小岑','http://music.163.com/song/5263407/?userid=121295973','http://music.163.com/song/5263407/?userid=121295973'],
            ['我在东北玩泥巴','狂风桑','http://music.163.com/song/35288915/?userid=121295973','http://music.163.com/song/35288915/?userid=121295973'],
            ['小潘潘小峰峰-学喵叫','林憬','http://music.163.com/song/570074358/?userid=121295973','http://music.163.com/song/570074358/?userid=121295973'],
            ['Hallelujah','Alexandra','http://music.163.com/song/16432400/?userid=121295973','http://music.163.com/song/16432400/?userid=121295973'],
            ['We Don\'t Talk Anymore','Charlie Puth/Selena Gomez','http://music.163.com/song/401249910/?userid=121295973','http://music.163.com/song/401249910/?userid=121295973'],
            ['我住长江头','云の泣','http://music.163.com/song/29984349/?userid=121295973','http://music.163.com/song/29984349/?userid=121295973']
            ]
    len_list = len(music_list)
    num = random.randint(0,len_list-1)
    return music_list[num]



#@robot.filter('音乐')
#def music(message):
#    music1 = music_data()
#    return music1

#@robot.filter('李坤帅吗')
#def music(message):
#    #music1 = music_data()
#    return '李坤最帅了'
#


@robot.text
def first(message, session):
    changdu=str(len(session))
    session[changdu] = message.content
    print (message.content)
    if '王方冰' in message.content:
        ans = '听名字就知道很漂亮~~'
        return ans
    elif '李韬' in message.content:
        ans = '听名字就知道很肥~~'
        return ans
    elif '李坤' in message.content:
        ans = '嗯,我见过,很帅~~'
        return ans
    elif '音乐' in message.content or '歌' in message.content:
        music1 = music_data()
        return music1
    elif '名字' in message.content or '叫啥' in message.content:
        ans = '我叫昵昵~~'
        return ans
    elif '颜值' in message.content:
        ans = '请回复要测颜值的照片哦~~'
        return ans
    else:
        ans = joke.chat_module(message.content)
        return ans
    #print (ans)
    #print(message.content)
    

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


@robot.handler
def hello(message):
    return '0_o??'



robot.run()

 

 
