from ctypes.wintypes import tagRECT
import os
import numpy
from PIL import Image

IMAGE_EXT = ['.jpg', '.jpeg', '.webp', '.png', '.gif']

DESTINATION = 'image_size_automation\images\small'
TARGET = 'image_size_automation\images'

if not os.path.exists(DESTINATION):
    print('small 폴더 생성')
    os.mkdir(DESTINATION)

for file in os.listdir(TARGET):
    name, ext = os.path.splitext(file)

    if ext in IMAGE_EXT:
        # 이미지 열기
        img_path = os.path.join(TARGET, file)
        img = Image.open(img_path)

        # 이미지 크기 수정
        width = int(img.width * 0.5)
        height = int(img.height * 0.5)
        resize = img.resize((width, height))

        # 이미지 편집
        save_path = os.path.join(DESTINATION, file)
        resize.save(save_path)

