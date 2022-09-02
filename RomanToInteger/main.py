# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = []
        i = 0
        while i < len(s):
            if i < len(s) - 1:
                # if
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


if __name__ == '__main__':
    print(Solution().romanToInt('MCMXCIV'))
    print(Solution().romanToInt('LVIII'))
    print(Solution().romanToInt('III'))
