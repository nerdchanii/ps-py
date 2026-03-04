import sys

# 상금 전체금액의 22 제세공과금
# 나머지 수령
#
# 80%를 필요한 경비로 인정하게 되면 20% 중 22%만 제세공과금
#
# 출력
# 1번경우 2번경우
#

price = int(sys.stdin.readline().strip())

first = int(price - ((price * 22) / 100))
second = int(price - ((price * 20 / 100) * 22 / 100))

print(f"{first} {second}")
