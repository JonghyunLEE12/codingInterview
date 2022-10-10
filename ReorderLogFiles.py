logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

# 로그를 재정렬하라
# 로그의 가장 앞부분은 식별자
# 문자로 구성된 로그가 숫자로 구성된 로그보다 앞에온다.
# 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
# 숫자 로그는 입력 순서대로 한다.


letters , digits = [],[]
for log in logs:
    # print(log.split()[1])
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letters.append(log)

print(letters)
letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(letters + digits )