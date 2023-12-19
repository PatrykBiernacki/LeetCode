class Solution:
    def __init__(self) -> None:
        pass
    def palindrome_number(self, x)->bool:
        list_x = [symbol for symbol in str(x)]
        for iter in range(int(len(list_x)/2)):
            if list_x[iter] != list_x[-1-iter]:
                return False

        return True


if __name__ == '__main__':
    solution1 = Solution()
    print(solution1.palindrome_number(x=123553219))
    print(solution1.palindrome_number(x=121))
    print(solution1.palindrome_number(x=12321))
    print(solution1.palindrome_number(x=-121))