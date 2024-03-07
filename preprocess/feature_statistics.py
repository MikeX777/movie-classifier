from gensim.parsing.preprocessing import remove_stopwords
import os
import nltk
nltk.download("punkt")

ps = nltk.PorterStemmer()

script_directory = os.fsencode(".\\data\\scripts")
stop_directory = os.fsencode(".\\data\\script_stop")
stemming_directory = os.fsencode(".\\data\\script_stop_stemming")


minimum_words = 50000
minimum_unique_words = 50000
maximum_words = 0
maximum_unique_words = 0
sum_words = 0
sum_unique_words = 0
average_words = 0
average_unique_words = 0
vocab_dict = dict()
top_5 = dict()
top_5_i = 0

average_min_vs_unique = 0
average_max_vs_unique = 0
average_average_vs_unique = 0

for file in os.listdir(stemming_directory):
    f = open(f".\\data\\script_stop_stemming\\{os.fsdecode(file)}", "r", encoding="utf-8")
    lines = f.read()
    f.close()
    tokens = nltk.word_tokenize(lines)
    features_stats = dict()
    for token in tokens:
        if token in features_stats:
            features_stats[token] += 1
        else:
            features_stats[token] = 1
        if token in vocab_dict:
            vocab_dict[token] += 1
        else:
            vocab_dict[token] = 1
    if len(tokens) < minimum_words:
        minimum_words = len(tokens)
    if len(tokens) > maximum_words:
        maximum_words = len(tokens)
    if len(features_stats.keys()) < minimum_unique_words:
        minimum_unique_words = len(features_stats.keys())
    if len(features_stats.keys()) > maximum_unique_words:
        maximum_unique_words = len(features_stats.keys())

    sum_words += len(tokens)
    sum_unique_words += len(features_stats.keys())

average_words = sum_words / len(os.listdir(stemming_directory))
average_unique_words = sum_unique_words / len(os.listdir(stemming_directory))
    
for file in os.listdir(stop_directory):
    f = open(f".\\data\\script_stop_stemming\\{os.fsdecode(file)}", "r", encoding="utf-8")
    lines = f.read()
    f.close()
    tokens = nltk.word_tokenize(lines)
    features_stats = dict()
    for token in tokens:
        if token in features_stats:
            features_stats[token] += 1
        else:
            features_stats[token] = 1
    
    if top_5_i < 5:
        top_5[os.fsdecode(file)] = f"Max vs Unique: {maximum_words / len(features_stats.keys())}, Min vs Unique: {minimum_words / len(features_stats.keys())}, Average vs Unique: {average_words / len(features_stats.keys())}"
        top_5_i += 1
    average_max_vs_unique += maximum_words / len(features_stats.keys())
    average_min_vs_unique += minimum_words / len(features_stats.keys())
    average_average_vs_unique += average_words / len(features_stats.keys())

average_max_vs_unique = average_max_vs_unique / len(os.listdir(stemming_directory))
average_min_vs_unique = average_min_vs_unique / len(os.listdir(stemming_directory))
average_average_vs_unique = average_average_vs_unique / len(os.listdir(stemming_directory))

print(f"Max Number of words: {maximum_words}")
print(f"Minimum Number of words: {minimum_words}")
print(f"Number of unique words: {len(vocab_dict)}")
print()
print(f"Maximum Unique Words per Script: {maximum_unique_words}")
print(f"Minimum Unique Words per Script: {minimum_unique_words}")
print(f"Average Unique Words per Script: {average_unique_words}")
print()
print(f"Averaged Minimum Number of Words per Unique Words of Movie: {average_min_vs_unique}")
print(f"Averaged Maximum Number of Words per Unique Words of Movie: {average_max_vs_unique}")
print(f"Averaged Average Number of Words per Unique Words of Movie: {average_average_vs_unique}")

for mk in top_5:
    print(f"Movie: {mk}, {top_5[mk]}")
    print()
    


