from stats import main1
from stats import char_count
from stats import sorting

import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content


def main():
    contents1 = get_book_text(sys.argv[1])
    print(contents1)


def main2():
    with open(sys.argv[1]) as f:
        tri = f.read()
    test = main1(tri)
    print(f"{test} words found in the document")



def main3():
    with open(sys.argv[1]) as f:
        jam = f.read()
    test_new = char_count(jam)
    for key, value in test_new.items():
        print(f"{repr(key)}: {value}")


def main4():
    print(f"Analyzing book found at {sys.argv[1]}")

    with open(sys.argv[1]) as f:
        data = f.read()
    count = main1(data)
    print(f"Found {count} total words")

    character_count = char_count(data)
    sorted_characters = sorting(character_count)
    for t in sorted_characters:
        if t["char"].isalpha() == True:
            print(f"{t['char']}: {t['num']}")
main4() 


    



    




    