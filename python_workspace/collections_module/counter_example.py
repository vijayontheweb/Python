from collections import Counter
num_list = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4]
num_counter = Counter(num_list)
print(f'Num Counter : {num_counter}')
print(f'Num Counter values : {num_counter.values}')
mixed_list = ['vijay', 'vijay', 'vijay', 4, 4, 5, 6, 6, 6]
mixed_counter = Counter(mixed_list)
print(f'Mixed Counter : {mixed_counter}')
sentence = 'How many times does each word show up in this sentence with a word'
sentence_array = sentence.split(' ')
sentence_counter = Counter(sentence_array)
print(f'Sentence Counter : {sentence_counter}')
letters = 'sdkjlfjlsdkfsdfoiwroir'
letter_counter = Counter(letters)
print(f'Letter Counter : {letter_counter}')
print(f'2 Most common from Letter Counter : {letter_counter.most_common(2)}')
