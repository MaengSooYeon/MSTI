#테스트 결과를 텍스트 파일에 저장

def sendType(typeName):
    f = open("file/result.txt",'a', encoding='utf-8')

    data = f'{typeName}\n'
    # print(data)
    f.write(data)
    f.close()