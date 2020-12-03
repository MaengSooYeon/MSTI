#현재 시간과 타입의 결과를 텍스트 파일에 저장
from datetime import datetime
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

typeName = "woody"     #결과 넘어갈때 값 추가하고 페이지 넘어가기

f = open("file/result.txt",'a', encoding='utf-8')
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
data = f'MSTI TYPE: {typeName}\t\t Test TIME: {now}\n'
f.write(data)
f.close()