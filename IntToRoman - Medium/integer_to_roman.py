class Solution:

    def intToRoman_if(self, num: int) -> str:
        roman_num = ''
        while num > 0:
            if num >= 1000:
                roman_num += 'M'
                num -= 1000
            elif num >= 900:
                roman_num += 'CM'
                num -= 900
            elif num >= 500:
                roman_num += 'D'
                num -= 500
            elif num >= 400:
                roman_num += 'CD'
                num -= 400   
            elif num >= 100:
                roman_num += 'C'
                num -= 100
            elif num >= 90:
                roman_num += 'XC'
                num -= 90
            elif num >= 50:
                roman_num += 'L'
                num -= 50        
            elif num >= 40:
                roman_num += 'XL'
                num -= 40    
            elif num >= 10:
                roman_num += 'X'
                num -= 10        
            elif num >= 9:
                roman_num += 'IX'
                num -= 9 
            elif num >= 5:
                roman_num += 'V'
                num -= 5        
            elif num >= 4:
                roman_num += 'IV'
                num -= 4 
            else:
                roman_num += 'I'
                num -= 1   

        return roman_num


if __name__ == '__main__':
    solution1 = Solution()
    print(solution1.intToRoman(3))
    print(solution1.intToRoman(117))
    print(solution1.intToRoman(1000))