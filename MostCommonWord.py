paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# 금지된 단어를 제외한 가장 흔하게 등장하는 단어 출력
# 대소문자 구분하지 않기
# 구두점 또한 무시
from collections import Counters

# print(paragraph.split())
paragraph = paragraph.split()

