def is_pangram(sentence):
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    sentence_without_whitespace_lowercase=sentence.lower().replace(" ", "")
    for x in sentence:
        if x not in all_letters:
            return False
    return True

