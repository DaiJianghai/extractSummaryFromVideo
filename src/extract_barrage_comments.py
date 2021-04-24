import re
from bs4 import BeautifulSoup as BS

if __name__ == '__main__':
    # with open("../input/626344429_2.xml", "r", encoding="utf-8") as f:
    #     lines = f.readlines();
    #     pattern = re.compile("^<d p=\"(.+)\">(.+)</d>")
    #     for line in lines:
    #         matcher = pattern.search(str(line))
    #         if matcher:
    #             content = matcher.group(2)
    #             with open("../output/barrage_info.txt", "a+") as f1:
    #                 f1.write(content + "\n")

    pattern = r'[0-9a-zA-Z\-\\._/?()。!！]'
    # with open("../output/OCR_info.txt", encoding="utf-8") as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         line = line.strip().split(' ')
    #         with open("../output/all_text.txt", "a+", encoding="utf-8") as f1:
    #             if len(line[1]) >= 3:
    #                 if re.sub(pattern, '', line[1]) is not None:
    #                     f1.write(re.sub(pattern, '', line[1]) + "\n")

    with open("../input/626344429_2.xml", "r", encoding="utf-8") as f:
        lines = f.readlines();
        for line in lines:
            soup = BS(line, 'html.parser')
            if len(soup.findAll('d')) == 0:
                continue
            content = soup.findAll('d')[0].text
            if content:
                print(content)
                with open("../output/all_text.txt", "a+", encoding='utf-8') as f1:
                    f1.write(re.sub(pattern, "", content) + "\n")
