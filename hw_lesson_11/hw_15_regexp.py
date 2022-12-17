"""
Есть фрагмент текста, состоящий из предложений.
Предложение - это строка, которая начинается с большой буквы и заканчивается точкой, вопросительным или восклицательным знаком (или несколькими такими знаками).
Слова состоят только из латинских букв, разделяются отделяются пробелами или запятыми с пробелами.
Предложение может состоять из одного слова.
Составить предложение из первых слов предложений фрагмента.
Только первое слово итогового предложения должно быть с большой буквы, остальные с маленькой.
Предложение должно заканчиваться точкой.
"""
import re


def generate_sentence(text: str) -> str:
    pattern = r'(?:^|[.?!] )([A-Z][a-z]+)'
    words = re.findall(pattern, text)
    words[1:] = map(lambda word: word.lower(), words[1:])
    return " ".join(words) + "."


text_1 = "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.."
text_2 = "Hola..."

assert generate_sentence(text_1) == "Hello and who or yes claro."
assert generate_sentence(text_2) == "Hola."
