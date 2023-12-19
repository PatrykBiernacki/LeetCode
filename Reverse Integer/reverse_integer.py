class Solution:
    def __init__(self) -> None:
        pass
        
    def reverse(self, x: int) -> int:
        'Solution with str.'
        if  x <= -2**31 or x >= 2**31-1:
            return 0
        non_negative = 1
        if x < 0:
            non_negative = -1
            x *= -1
        y = str(x)[::-1]
        y = int(y)*non_negative
        if y <= -2**31 or y >= 2**31-1:
            return 0
        return y

    def reverse_no_str(self, x: int) -> int:
        'Solution does not use strings.'
        if x <= -2**31 or x >= 2**31-1:
            return 0
        non_negative = 1
        if x < 0:
            non_negative = -1
            x *= -1
        y=0
        while x != 0:
            modulo = x % 10
            y += modulo
            if y <= -2**31 or y >= 2**31-1:
                return 0
            x -= modulo
            if x == 0:
                break
            y *= 10
            x /= 10
        return int(y * non_negative)


if __name__ == '__main__':
    solution1 = Solution()
    print(solution1.reverse(x=15342469))
    print(solution1.reverse(x=-21473648))