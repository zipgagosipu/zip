from PIL import Image

import os
경로 = os.getcwd()
파일명들 = os.listdir(경로+'/images')
print(파일명들)

# img = Image.open('images/photo1.jpg')
# # img.thumbnail((300,500)) #이미지 비율을 유지한채로 예쁘게 출력댐 // 변수에 할당 안하고 그냥 써도댐
# # img.save('images/new_photo1.jpg', quality=30) #퀄리티 기본값은 75임 #PNG파일은 quantize 옵션으로 해야해서 찾아보고 해야댐 #png파일은 색상이 몇개없을때 쓰는파일
# # #progressive JPG 만들기도 가능
# #convert('L')쓰면 흑백으로 변환됨
# #crop()쓰면 이미지를 잘라줌
# img = img.thumbnail((500,2500))
# #왼쪽꺼는 왼쪽위, 오른쪽은 오른쪽 아래 좌표
# img.save('images/crop_photo1.jpg')
