from gensim.parsing.preprocessing import remove_stopwords
import os
import string
import nltk
nltk.download("punkt")

ps = nltk.PorterStemmer()

script_directory = os.fsencode("..\\data\\scripts")
stop_directory = os.fsencode("..\\data\\script_stop")
stop_no_punc_directory = os.fsencode("..\\data\\script_stop_no_punc")
stemming_directory = os.fsencode("..\\data\\script_stop_stemming")


for file in os.listdir(stop_directory):
    f = open(f"..\\data\\script_stop\\{os.fsdecode(file)}", "r", encoding = "utf-8")
    lines = f.readlines()
    f.close()
    new_lines = []
    for line in lines:
        new_lines.append(line.translate(str.maketrans("", "", string.punctuation)))

    f = open(f"..\\data\\script_stop_no_punc\\{os.fsdecode(file)}", "w", encoding = "utf-8")
    for line in new_lines:
        f.write(line)
        f.write("\n")
    f.close()
#for file in os.listdir(script_directory):
#    f = open(f".\\data\\scripts\\{os.fsdecode(file)}", "r", encoding="utf-8")
#    lines = f.readlines()
#    f.close()
#    new_lines = []
#    for line in lines:
#        new_lines.append(remove_stopwords(line))

#    f = open(f".\\data\\script_stop\\{os.fsdecode(file)}", "w", encoding="utf-8")
#    for line in new_lines:
#        f.write(line)
#        f.write("\n")
#    f.close()

#for file in os.listdir(stop_directory):
#    f = open(f".\\data\\script_stop\\{os.fsdecode(file)}", "r", encoding="utf-8")
#    lines = f.readlines()
#    f.close()
#    new_lines = []
#    for line in lines:
#        tokens = nltk.word_tokenize(line)
#        stemmed_tokens = []
#        for token in tokens:
#            stemmed_tokens.append(ps.stem(token))
#        new_lines.append(" ".join(stemmed_tokens))
#    
#    f = open(f".\\data\\script_stop_stemming\\{os.fsdecode(file)}", "w", encoding="utf-8")
#    for line in new_lines:
#        f.write(line)
#        f.write("\n")

