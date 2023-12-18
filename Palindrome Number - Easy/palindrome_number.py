class Solution:
    def two_sum(self, x)->bool:
        list_x = [symbol for symbol in str(x)]
        print(list_x)
        for iter in range(int(len(list_x)/2)):
            print(list_x[iter], list_x[-1-iter])
            if list_x[iter] != list_x[-1-iter]:
                return False

        return True


if __name__ == '__main__':
    x = 123553219

    print (Solution.two_sum('_', x))