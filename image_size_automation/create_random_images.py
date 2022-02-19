# pip install pandas pillow
import os
import numpy
from PIL import Image

TARGET = 'image_size_automation/images'

if not os.path.exists(TARGET):
    print('images 폴더 생성!!!!!!!!')
    os.mkdir(TARGET)

for i in range(1, 20 + 1):
    filename = f'{i}.jpg'

    # 3차원 rgb 랜덤 배열 생성
    rgb_array = numpy.random.rand(720, 1080, 3) * 255

    # 이미지 생성
    image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')

    # 이미지 저장
    image.save(os.path.join(TARGET, filename))

    # 이미지를 닫아준다.
    image.close()