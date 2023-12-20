class Solution:
    def __init__(self) -> None:
        pass

    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            raise Exception("Zero is not acceptable divisor")    
        non_negative = 1
        if dividend < 0:
            non_negative *= -1
            dividend *= -1
        if divisor < 0:
            non_negative *= -1  
            divisor *= -1

        quotient = len(range(0, dividend-divisor+1, divisor))
        
        if quotient >= 2**31-1 and non_negative == 1:
            return 2**31-1
        if quotient >= 2**31 and non_negative == -1:
            return -2**31
        return quotient * non_negative


if __name__ == '__main__':
    solution1 = Solution()
    print(solution1.divide(-2147483648, 1))
    print(solution1.divide(2147483647, -1))
