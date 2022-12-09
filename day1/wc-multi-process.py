import pathlib
from multiprocessing import Pool


def get_word_counts(file_path):
    wc = dict()
    with open(file_path) as f:
        data = f.read()
        words = data.split()

        for word in words:
            if word in wc:
                wc[word] += 1
            else:
                wc[word] = 1

    return wc


word_count = dict()
NUM_PROCESSES = 4 # we have 12 logical cores in laptop
NUM_FILES = 60  # there are 60 files in total but change this if want to process lower files

with Pool(NUM_PROCESSES) as mexecutor:
    files = [f for f in pathlib.Path("../data/").glob("*.txt")]
    # change the number of files processed
    files = files[:NUM_FILES]
    for wc in mexecutor.imap_unordered(get_word_counts, files):
        for word in wc:
            word_count[word] = word_count.get(word, 0) + wc[word]

list_wc_freq = []

for k in word_count:
    list_wc_freq.append((word_count[k], k))


list_wc_freq = sorted(list_wc_freq, reverse=True)

# print the top 10 results
for val, word in list_wc_freq[:10]:
    print(word, val)
    