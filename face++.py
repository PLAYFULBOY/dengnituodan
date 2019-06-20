import requests
import json
from PIL import Image, ImageDraw
# https://console.faceplusplus.com.cn/documents/4888373



def face_detect():

    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    key = 'acOJJf6exx4QlN-BjtzJ4Sgf2PnEK1af'
    secret = '0vjVEK3boUZq0w_QMN7In8LjHpK4mGv4'
    filepath = '2.jpg'
    
    data = {'api_key':key, 'api_secret':secret, 'return_landmark':'0','return_attributes':'gender,age,beauty,ethnicity'}
    files = {'image_file': open(filepath, 'rb')}
    
    resposen = requests.post(http_url, data=data, files=files)
    resp_dict = resposen.json()
    beauty = resp_dict['faces'][0]['attributes']['beauty']['male_score']
    age = resp_dict['faces'][0]['attributes']['age']['value']
    gender = resp_dict['faces'][0]['attributes']['gender']['value']
    class_man = resp_dict['faces'][0]['attributes']['ethnicity']['value']
    
    
    ans = 'gender: ' + str(gender) + '\n' + '颜值打分: ' + str(beauty) + '\n' + '年龄: ' + str(age) + '\n' + '所属人种: ' + class_man
    print (ans)
    #print('gender: ' + str(gender) + '\n' + '颜值打分: ' + str(beauty) + '\n' + '年龄: ' + str(age) + '\n' + '所属人种: ' + class_man) 
    if 'error_message' in resp_dict:
        return('这是人类吗?')
    else:
        return ans
        #faces = resp_dict['faces']
        #faceName = len(faces)
        #im = Image.open(filepath)
        #draw = ImageDraw.Draw(im)

        #for i in range(faceName):
        #    face_rectangle = faces[i]['face_rectangle']
        #    width = face_rectangle['width']
        #    top = face_rectangle['top']
        #    left = face_rectangle['left']
        #    height = face_rectangle['height']
        #    start = (left, top)
        #    end = (left+width, top+height)

        #    draw.rectangle([start, end], outline='red')
        #im.show()


if __name__ == '__main__':
    ans = face_detect()
    print (ans)
