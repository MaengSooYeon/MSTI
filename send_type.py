#현재 시간과 타입의 결과를 텍스트 파일에 저장한 파일

from datetime import datetime

def sendType(typeName):

    f = open("file/result.txt",'a', encoding='utf-8')

    data = f'{typeName}\n'
    print(data)
    f.write(data)
    f.close()

