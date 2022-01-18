#반복문으로 트리 만들기
for i in range(1, 5):
    print("*" * i)

#while문으로 작성
i = 1
while i < 5:
    print("*" * i)
    i = i +1

#트리 2개 반복
for i in range(1, 3):
    for k in range(1, 5):
        print("*" * k)

#while문으로 작성
i, k = 1, 1
while i <= 2:
    while k <= 4:
        print("*" * k)
        k = k + 1
    i = i +1
    k = 1

#등차수열 트리 만들기 (공백문자열과 별표 둘 다 만들어야 됨)
#i는 공백문자열, k는 별표
i, k = 5, 1
while i >= 0:
    print("{0}".format(" " * i, "*" * (2 * k - 1)))
    i = i - 1
    k = k + 1