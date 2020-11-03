def fill_in_char(original_word, answer_word, char):
    list_original_word = list(original_word)
    count = 0
    for x in list_original_word:
        if x == char:
            answer_word[count] = x
        count = count + 1
    return answer_word


og_word = "lekeu"
ans_word = ['_', '_', 'k', '_', '_']
print(ans_word)
ans_word = fill_in_char(og_word, ans_word, 'u')
print(ans_word)
ans_word = fill_in_char(og_word, ans_word, 'l')
print(ans_word)
ans_word = fill_in_char(og_word, ans_word, 'e')
print(ans_word)