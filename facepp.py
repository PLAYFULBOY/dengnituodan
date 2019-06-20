#from translate import Translator
import requests
import json
from PIL import Image, ImageDraw
# https://console.faceplusplus.com.cn/documents/4888373


#调用旷视科技的人脸识别api,返回人脸的属性
def face_detect(filepath):

    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'#人脸检测url
    object_url = 'https://api-cn.faceplusplus.com/imagepp/beta/detectsceneandobject'#物体检测url
    key = 'acOJJf6exx4QlN-BjtzJ4Sgf2PnEK1af'
    secret = '0vjVEK3boUZq0w_QMN7In8LjHpK4mGv4'
    
    #data = {'api_key':key, 'api_secret':secret, 'return_landmark':'0','return_attributes':'gender,age,beauty,ethnicity,emotion,mouthstatus,skinstatus'}
    data = {'api_key':key, 'api_secret':secret, 'return_landmark':'0','return_attributes':'gender,age,beauty,ethnicity,emotion'}
    object_data = {'api_key':key, 'api_secret':secret}
    files = {'image_file': open(filepath, 'rb')}
    object_files = {'image_file': open(filepath, 'rb')}
    
    resposen = requests.post(http_url, data=data, files=files)
    resp_dict = resposen.json()
    num = len((resp_dict['faces']))
    ans = ''
    index = 0
    if 'error_message' in resp_dict:
        ans = '抱歉,服务器出现错误'
        return (ans)
    elif num == 0:#如果没有脸,则检测图像中的物体
        response_object = requests.post(object_url, data=object_data, files=object_files)
        resp_dict_object = response_object.json()
        #print (resp_dict_object)
        object_see = resp_dict_object['objects']
        #print (object_see)
        object_num = len(object_see)
        if object_num == 0:
            ans = '这是啥图呢,昵昵不知道耶~~'
        elif object_num == 1:#如果图像上只有一个物体
            ans = 'there has a ' + object_see[0]['value'] + ' in this picture~~'
        else:#如果图像上出现了多个物体
            for i in range(object_num-1): 
                ans = ans + object_see[i]['value'] + ', '
            ans = ans + object_see[object_num-1]['value']
            ans ='there has ' + ans + ' int this picture~~'
        return ans     
    else:
        for i in range(num):
            if 'attributes' in resp_dict['faces'][i].keys():
                beauty = resp_dict['faces'][i]['attributes']['beauty']['male_score'] + 15
                age = resp_dict['faces'][i]['attributes']['age']['value']
                gender = resp_dict['faces'][i]['attributes']['gender']['value']
                emotion = resp_dict['faces'][i]['attributes']['emotion']
                emotion_d = max(emotion,key = emotion.get)
                #mouthstatus = resp_dict['faces'][i]['attributes']['mouthstatus']
                #mouthstatus_d = max(mouthstatus,key = mouthstatus.get)
                #skinstatus = resp_dict['faces'][i]['attributes']['skinstatus']
                #skinstatus_d = max(skinstatus,key = skinstatus.get)
                if gender == 'Male':
                    gender = '男'
                else:
                    gender = '女'
                #class_man = resp_dict['faces'][i]['attributes']['ethnicity']['value']
                #if class_man == 'ASIAN':
                #    class_man = '亚洲人'
                #elif class_man == 'BLACK':
                #    class_man = '黑人'
                #elif class_man == 'WHITE':
                #    class_man = '白人'
                #else:
                #    class_man = '印度人'
                #情感分析
                if emotion_d == 'anger':
                    emotion_d = '你看起来有点生气哦~~'
                elif emotion_d == 'disgust':
                    emotion_d = '你好像看到什么厌恶的东西了哦~~'
                elif emotion_d == 'fear':
                    emotion_d = '你好像有点恐惧~~'
                elif emotion_d == 'happiness':
                    emotion_d = '你看起来很开心哦~~'
                elif emotion_d == 'neutral':
                    emotion_d = '你看起来很平静~~'
                elif emotion_d == 'sadness':
                    emotion_d = '你看起来有点伤心哦~~'
                else:
                    emotion_d = '你看起来有点惊讶哦~~'
                #嘴部状态分析
                #if mouthstatus_d == 'close':
                #    mouthstatus_d = '你的嘴部没有遮挡,而且是闭合的~~'
                #elif mouthstatus_d == 'open':
                #    mouthstatus_d = '你的嘴部没有遮挡,而且是张开的~~'
                #elif mouthstatus_d == 'surgical_mask_or_respirator':
                #    mouthstatus_d = '你的嘴部可能被医用口罩遮挡~~'
                #else:
                #    mouthstatus_d = '你的嘴部可能被什么东西挡住了~~'
                #皮肤状态分析
                #if skinstatus_d == 'health':
                #    skinstatus_d = '你的皮肤很健康哦~~'
                #elif skinstatus_d == 'stain':
                #    skinstatus_d = '你的皮肤可能存在色斑~~'
                #elif skinstatus_d == 'acne':
                #    skinstatus_d = '你的皮肤可能存在青春豆~~'
                #elif skinstatus_d == 'dark_circle':
                #    skinstatus_d = '你可能有黑眼圈~~'


                index = index+1
                if beauty > 100 and gender == '男':
                    ans = ans + '\n-------\n' + '性别: ' + str(gender) + '\n' + '颜值: ' + '哇,帅哥，你的颜值爆表了～～' + '\n' + '年龄: ' + str(age) + '\n' + '情绪: ' + emotion_d
                elif beauty > 100 and gender == '女':
                    ans = ans + '\n-------\n' + '性别: ' + str(gender) + '\n' + '颜值: ' + '哇,美女，你的颜值爆表了～～' + '\n' + '年龄: ' + str(age) + '\n' + '情绪: ' + emotion_d

                else:
                    ans = ans + '\n-------\n' + '性别: ' + str(gender) + '\n' + '颜值: ' + str(beauty) + '\n' + '年龄: ' + str(age) + '\n' + '情绪: ' + emotion_d

        if index == num:
            ans = '照片上有' + str(num) + '个人' + ans
            return ans
        else:
            ans = '照片上有' + str(num) + '个人,但是有' + str(num-index) + '个人脸属性无法判断' + ans
            return ans
        

if __name__ == '__main__':
    file_path = '/home/lk/python_web/WeRoBot-master/pic/22334995351335186.jpg'
    ans = face_detect(file_path)
    print(ans)
