def intToRoman(num):
        """
        :type num: int
        :rtype: str
        """
        string = ""
        if num >= 1000:
            thousands = num // 1000
            num %= 1000
            if thousands == 4:
                string += 'IM'
            else:
                for i in range(thousands):
                    string += 'M'
        if num >= 500:
            hundies = num // 100
            num %= 100
            if hundies == 9:
                string += 'CM'
            else:
                string += 'D'
                for i in range(hundies - 5):
                    string += 'C'
        elif num >= 100:
            hundies = num // 100
            num %= 100
            if hundies == 4:
                string += 'CD'
            else:
                for i in range(hundies):
                    string += 'C'

        if num >= 50:
            tens = num // 10
            num %= 10
            if tens == 9:
                string += 'XC'
            else:
                string += 'L'
                for i in range(tens - 5):
                    string += 'X'
        elif num >= 10:
            tens = num // 10
            num %= 10
            if tens == 4:
                string += 'XL'
            else:
                for i in range(tens):
                    string += 'X'
        
        if num == 9:
            string += 'IX'
        elif num >= 5:
            num -= 5
            string += 'V'
            for i in range(num):
                string += 'I'
        elif num == 4:
            string += 'IV'
        else:
            for i in range(num):
                string += 'I'
        
        return string

print(intToRoman(3749))
print(intToRoman(58))
print(intToRoman(1995))