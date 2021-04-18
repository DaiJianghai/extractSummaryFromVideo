from aip import AipOcr
import os


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def process(frame_path, app_id, api_key, secret_key):
    # 初始化AipFace对象
    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # 定义参数变量
    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
    }

    files = os.listdir(frame_path)
    for file in files:
        # 调用通用文字识别接口
        result = aipOcr.basicGeneral(get_file_content(frame_path + file), options)
        print(result)
        words_result = result['words_result']
        li = []
        for i in range(len(words_result)):
            print(words_result[i]['words'])
            li.append(words_result[i]['words'])
        with open("ocr_res.txt", "a+") as f:
            for i in range(len(li)):
                f.write(file + " " + li[i] + "\n")


if __name__ == '__main__':
    APP_ID = '24017114'
    API_KEY = 'yceEmCN2iRh2k6BmGL6FcEbe'
    SECRET_KEY = 'HZxAZ8o3pXqDplflDtzHwQtidtAkVu7R'
    key_frame_path = r'../output/key_frames/'
    process(key_frame_path, APP_ID, API_KEY, SECRET_KEY)
