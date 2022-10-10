# 파이썬 다운 방식
s = ['h','e','l','l','o']

def pythonic(s):
    s.reverse()
    return s

print(f'pythonic : {pythonic(s)}')


# 투 포인터 사용
# 투 포인터 => 2개의 포인터를 이용해 범위를 조정해 가며 최적 해를 구한다.
s = ['h','e','l','l','o']

def reverseString(s):
    left , right = 0 , len(s)-1
    while True:
        if left >= right :
            break
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1

reverseString(s)
print(f'reverseString : {s}')


# 슬라이싱 사용
s = ['h','e','l','l','o']

def slicing(s):
    s = s[::-1]
    return s


print(f'slicing : {slicing(s)}')
