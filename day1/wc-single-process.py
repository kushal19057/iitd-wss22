import os

def get_word_counts(book_path):
    global word_count
    with open(book_path) as f:
        data = f.read()
        words = data.split()
        
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1


DATA_PATH = "../data/"

book_paths = []
for book_name in os.listdir(DATA_PATH):
    book_paths.append(DATA_PATH + book_name.strip())

# print(book_paths)

word_count = dict()

for book_path in book_paths:
    get_word_counts(book_path)

list_wc_freq = []

for k in word_count:
    list_wc_freq.append((word_count[k], k))


list_wc_freq = sorted(list_wc_freq, reverse=True)

# print the top 10 results
for val, word in list_wc_freq[:10]:
    print(word, val)