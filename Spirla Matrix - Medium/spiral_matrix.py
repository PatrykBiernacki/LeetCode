class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        solution1 = []
        rows, columns = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows-1 , 0, columns-1
        while len(solution1) < rows * columns:
            for i in range(left, right+1):
                solution1.append(matrix[top][i])
            top+=1
            for i in range(top, bottom+1):
                solution1.append(matrix[i][right])
            right-=1
            if top <= bottom:
                for i in range(right, left-1, -1):
                    solution1.append(matrix[bottom][i])
                bottom-=1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    solution1.append(matrix[i][left])
                left+=1
        return solution1

if __name__ == '__main__':
    solution1 = Solution()
    print(solution1.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(solution1.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(solution1.spiralOrder([[7],[9]]))
    print(solution1.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
