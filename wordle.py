import re
import nltk
from nltk.corpus import words


def find_matching_words(pattern: str, include: str, exclude: str) -> str:
    
    nltk.download("words", quiet=True)

    all_words = set(word.lower() for word in words.words())  # יצירת סט ישירות

    if include is None:
        include = ""
    if exclude is None:
        exclude = ""
    res = ""   

    print(include, pattern, exclude, "ergfdssssssssewfrdseafrgvtF")
    all_words = words.words()
    res = ""
    for word in all_words:
        if (
            re.match(f"^{pattern}$", word)
            and all(letter in word for letter in include)
            and all(letter not in word for letter in exclude)
        ):
            res += word + "\n"
    return res

# def find_matching_words(pattern, include: str = "", exclude: str = "") -> None:
#     res: str = ""
#     with open(r"/usr/share/dict/words", "r") as word_file:
#         for line in word_file:
#             word: str = line.strip().lower()
#             if (
#                 re.match(f"^{pattern}$", word)
#                 and word.isalpha()
#                 and all(letter in word for letter in include)
#                 and all(letter not in word for letter in exclude)
#             ):
#                 res += word + "\n"
#     return res
