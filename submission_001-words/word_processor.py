import functools

    #REFERENCES: Prof.Rego &Fahima

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)

words = "These are indeed interesting, an obvious understatement, times. What say you?"
   

def convert_to_word_list(text):
    """
        THIS FUNCTION REMOVES ALL SPECIAL CHARACTERS AND MAKES ALL LETTERS LOWERCASE
    """
    
    text_list = split(",?:;. ", text.lower())
    new_text_list = list(filter(None,text_list))
    return new_text_list


def words_longer_than(length, text):
    """
        CHECKS LENGTH OF WORDS IN CONVERTED LIST
    """

    text_list = convert_to_word_list(words)
    new_text_list = list(filter(lambda words: len(words) > length, text_list))
    return new_text_list
#print(words_longer_than(10,words))    

def words_lengths_map(text):
    """
        MAPS OUT LENGTH OF EACH WORD
    """    
    new_list = [len(x) for x in convert_to_word_list(text)]
    my_dict = {k:new_list.count(k) for k in sorted(new_list)}
    return my_dict

#print(words_lengths_map(words))

def letters_count_map(text):
    """
        MAPS OUT THE LETTERS OF THE STRING
    """

    text = convert_to_word_list(text)
    text = ''.join(text)
    new_list = [x for x in text]
    alpha = [letter for letter in list(map(chr,range(97,123)))]
    my_dict = {k:new_list.count(k) for k in sorted(alpha)}
    return my_dict
#print(letters_count_map(words))

def most_used_character(text):

    """
        CHECK FOR THE LETTER THAT IS REPEATED THE MOST
    """

    count = letters_count_map(text)
    print(count)
    # for x,y in count:
    #     print(x)
    numbers = max(count, key = count.get)
    if not text:
        return None
    else:
        return(numbers)

print(most_used_character(words))            