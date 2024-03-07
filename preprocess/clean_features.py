from gensim.parsing.preprocessing import remove_stopwords
import os
import string
import pysrt
from pathlib import Path
import re

stop_no_punc_directory = os.fsencode("..\\data\\script_stop_no_punc")
subtitle_raw_directory = os.fsencode("..\\data\\subtitle_raw")
subtitle_clean_directory = os.fsencode("..\\data\\subtitle_clean")
subtitle_stop_no_punc_directory = os.fsencode("..\\data\\subtitle_stop_no_punc")

baby_cleaner = re.compile("<.*?>")
cleaner = re.compile("<.*?><.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")

def cleanhtml(raw_html):
    return re.sub(cleaner, "", re.sub(baby_cleaner, "", raw_html))

#for file in os.listdir(subtitle_clean_directory):
#    f = open(f"{os.fsdecode(subtitle_clean_directory)}\\{os.fsdecode(file)}", "r", encoding = "utf-8")
#    lines = f.readlines()
#    f.close()
#    new_lines = []
#
#    for line in lines:
#        new_lines.append(line.replace("♪", ""))
#
#    f = open(f"{os.fsdecode(subtitle_clean_directory)}\\{os.fsdecode(file)}", "w", encoding = "utf-8")
#    for line in new_lines:
#        f.write(line)
#    f.close()

for file in os.listdir(subtitle_clean_directory):
    f = open(f"{os.fsdecode(subtitle_clean_directory)}\\{os.fsdecode(file)}", "r", encoding = "utf-8")
    lines = f.readlines()
    f.close()
    new_lines = []
    for line in lines:
        new_lines.append(remove_stopwords(line).translate(str.maketrans("", "", string.punctuation)))

    f = open(f"{os.fsdecode(subtitle_clean_directory)}\\{os.fsdecode(file)}", "w", encoding = "utf-8")
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

