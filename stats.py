def main1(book_text):
    test_list = book_text.split()
    word_count = len(test_list)
    return word_count

def char_count(book_text):
    new_book_text = book_text.lower()
    test_dict = {}
    for character in new_book_text:
        test_dict[character]=0
    for character in new_book_text:
        if character in test_dict:
            test_dict[character] +=1

    return test_dict

def sorting(test1_dict):
    test_list = []
    for key, value in test1_dict.items():
        test_list.append({"char": key, "num": value})
    def sort_on(items):
        return items["num"]
    
    test_list.sort(reverse = True, key = sort_on)
    return test_list
    


    



