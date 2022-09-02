# https://leetcode.com/problems/roman-to-integer/
# https://leetcode.com/problems/integer-to-roman/
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = []
        i = 0
        while i < len(s):
            if i < len(s) - 1:
                if roman_numbers[s[i]] > roman_numbers[s[i + 1]]:
                    n.append(roman_numbers[s[i]])
                elif roman_numbers[s[i]] < roman_numbers[s[i + 1]]:
                    n.append(roman_numbers[s[i + 1]] - roman_numbers[s[i]])
                    i += 1
                elif roman_numbers[s[i + 1]]:
                    n.append(roman_numbers[s[i]])
            else:
                n.append(roman_numbers[s[i]])
            i += 1
        return sum(n)

    def intToRoman(self, num: int) -> str:
        roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = []
        s = []
        while num > 0:
            n.append(num % 10)
            num //= 10
        n.reverse()
        print(n)
        for i in range(len(n) - 1):
            for k, v in roman_numbers.items():
                if v == n[i]:
                    s.append(roman_numbers[k])
        return str(s).replace(', ', '')


if __name__ == '__main__':
    # print(Solution().romanToInt('MCMXCIV'))
    # print(Solution().romanToInt('LVIII'))
    # print(Solution().romanToInt('III'))
    print(Solution().intToRoman(1994))
    print(Solution().intToRoman(58))
    print(Solution().intToRoman(3))
