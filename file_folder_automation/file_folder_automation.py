import os
import shutil

TARGET_FOLDER = 'C:\\Users\\사 용 자 명 넣 는 곳\\Downloads\\'
IMAGE_EXT =  ['.jpg', '.jpeg', '.gif', '.webp', '.png']
ZIP_EXT =  ['.zip', '.rar', '7z', 'alz']

# 파일들을 다 가져와보자
for file in os.listdir(TARGET_FOLDER):
    # 이름과 확장자 분리
    name, ext = os.path.splitext(TARGET_FOLDER + file)

    if ext in IMAGE_EXT:
        if not os.path.exists(TARGET_FOLDER + '이미지'):
            os.mkdir(TARGET_FOLDER + '이미지')
        shutil.move(TARGET_FOLDER + file, TARGET_FOLDER + '이미지')

    elif ext in ZIP_EXT:
        if not os.path.exists(TARGET_FOLDER + '압축파일'):
            os.mkdir(TARGET_FOLDER + '압축파일')
        shutil.move(TARGET_FOLDER + file, TARGET_FOLDER + '압축파일')

    else:
        continue

print('정리 끝')