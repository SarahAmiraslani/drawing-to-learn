from datetime import datetime
import string
from collections import defaultdict


def remove_punctuation(input_str: str) -> str:
    translator = str.maketrans("", "", string.punctuation)
    return input_str.translate(translator)


def unique_word_calc(input_str: str) -> int:
    no_punct_str = remove_punctuation(input_str.lower())
    word_count = defaultdict(int)
    for word in no_punct_str.split():
        word_count[word] += 1
    return len(word_count)


def total_word_calc(input_str: str) -> int:
    no_punct_str = remove_punctuation(input_str.lower())
    return len(no_punct_str.split())


def day_of_week(date: str) -> str:
    dt = datetime.strptime(date, "%Y-%m-%d")
    return dt.strftime("%A").lower()


def time_of_day(time: str) -> str:
    dt = datetime.strptime(time, "%H:%M:%S")
    return dt.strftime("%I:%M %p").lstrip("0").lower()


if __name__ == "__main__":
    print(remove_punctuation("Hello, World!"))
    print(unique_word_calc("Hello, World! Hello, World!"))
    print(total_word_calc("Hello, World! Hello, World!"))
    print(day_of_week("2020-12-25"))
    print(time_of_day("23:59:59"))
