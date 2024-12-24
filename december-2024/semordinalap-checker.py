import enchant

def semordinalap_checker(word: str) -> bool:
    english_dictionary = enchant.Dict("en_US")
    return english_dictionary.check(word) and english_dictionary.check(word[::-1]) and word != word[::-1]

semordinalap_checker("racecar")
semordinalap_checker("tug")
semordinalap_checker("trap")
semordinalap_checker("piece")