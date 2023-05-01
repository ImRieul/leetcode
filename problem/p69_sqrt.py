# x(n+1) = (x(n) + a / x(n)) / 2
#
# 여기서 a는 제곱근을 구하려는 수이고,
# x(0)은 임의의 초기값입니다.
# 이 공식에서 x(n)은 n번째 반복에서의 근사값을 나타내며,
# x(n+1)은 n+1번째 반복에서의 근사값을 나타냅니다.
import math


class Solution:
    # def mySqrt(self, x: int) -> int:
    def square_root(self, a):
        default_num = 0.1

        x1 = (default_num + a / default_num) / 2
        while abs(x1 - default_num) > 1:
            default_num = x1
            x1 = (default_num + a / default_num) / 2
        return math.floor(x1)