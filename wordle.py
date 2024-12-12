import re
import nltk
from nltk.corpus import words


def find_matching_words(pattern: str, include: str, exclude: str) -> str:
    nltk.download("words")

    all_words = words.words()
    res = ""
    for word in all_words:
        if (
            re.match(f"^{pattern}$", word)
            and all(letter in word for letter in include)
            and all(letter not in word for letter in exclude)
        ):
            res += word + "\n"
