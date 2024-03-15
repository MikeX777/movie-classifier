from gensim.parsing.preprocessing import remove_stopwords
import os
import nltk
import string
import pysrt
from pathlib import Path
import re

stop_no_punc_directory = os.fsencode("..\\data\\script_stop_no_punc")
script_word_shift_directory = os.fsencode("..\\data\\script_word_shift")
subtitle_raw_directory = os.fsencode("..\\data\\subtitle_raw")
subtitle_clean_directory = os.fsencode("..\\data\\subtitle_clean")
subtitle_stop_no_punc_directory = os.fsencode("..\\data\\subtitle_stop_no_punc")


for file in os.listdir(stop_no_punc_directory):
    f = open(f"{os.fsdecode(stop_no_punc_directory)}\\{os.fsdecode(file)}", "r", encoding = "utf-8")
    lines = f.read()
    f.close()
    output = ""
    partial_token_amount = 0
    partial_token = ""
    word_shift = 0
    tokens = nltk.word_tokenize(lines)
    for token in tokens:
        match token:
            case "CONTINUED":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                output += f"[{word_shift}] {token} "
                word_shift = 0
            case "TITLE":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                output += f"[{word_shift}] {token} "
                word_shift = 0
            case "TRANSITION":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                output += f"[{word_shift}] {token} "
                word_shift = 0
            case "CONTINUE":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                output += f"[{word_shift}] {token} "
                word_shift = 0
            case "VO":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                output += f"[{word_shift}] {token} "
                word_shift = 0
            case "INT":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                output += f"[{word_shift}] {token} "
                word_shift = 0
            case "EXT":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                output += f"[{word_shift}] {token} "
                word_shift = 0
            case "INTERIOR":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                output += f"[{word_shift}] {token} "
                word_shift = 0
            case "EXTERIOR":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                output += f"[{word_shift}] {token} "
                word_shift = 0
            case "CLOSE":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                output += f"[{word_shift}] {token} "
                word_shift = 0
            case "ANGLE":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                partial_token = token
                partial_token_amount = 1
            case "CAMERA":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                partial_token = token
                partial_token_amount = 1
            case "CUT":
                if partial_token != "" :
                    if partial_token == "JUMP":
                        output += f"[{word_shift}] {partial_token} {token} "
                        word_shift = 0
                        partial_token = ""
                        partial_token_amount = 0
                    else:
                        word_shift += partial_token_amount
                        partial_token_amount = 0
                        partial_token = ""
                partial_token = token
                partial_token_amount = 1
            case "CAMERA":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                partial_token = token
                partial_token_amount = 1
            case "DISSOLVE":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                partial_token = token
                partial_token_amount = 1
            case "IN":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                partial_token = token
                partial_token_amount = 1
            case "FADE":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                partial_token = token
                partial_token_amount = 1
            case "JUMP":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                partial_token = token
                partial_token_amount = 1
            case "VIEW":
                if partial_token != "" :
                    word_shift += partial_token_amount
                    partial_token_amount = 0
                    partial_token = ""
                partial_token = token
                partial_token_amount = 1
            case "ON":
                if partial_token != "":
                    if partial_token == "ANGLE" or partial_token == "VIEW":
                        output += f"[{word_shift}] {partial_token} {token} "
                    else:
                        word_shift += partial_token_amount
                        partial_token = ""
                        partial_token_amount = 0
                else:
                    word_shift += 1
            case "TO":
                if partial_token != "":
                    if partial_token == "CUT" or partial_token == "DISSOLVE" or partial_token == "FADE":
                        output += f"[{word_shift}] {partial_token} {token} "
                    else:
                        word_shift += partial_token_amount
                        partial_token = ""
                        partial_token_amount = 0
                else:
                    word_shift += 1
            case "FROM":
                if partial_token != "":
                    if partial_token == "CUT":
                        output += f"[{word_shift}] {partial_token} {token} "
                    else:
                        word_shift += partial_token_amount
                        partial_token = ""
                        partial_token_amount = 0
                else:
                    word_shift += 1
            case "PANS":
                if partial_token != "":
                    if partial_token == "CAMERA":
                        output += f"[{word_shift}] {partial_token} {token} "
                    else:
                        word_shift += partial_token_amount
                        partial_token = ""
                        partial_token_amount = 0
                else:
                    word_shift += 1
            case "UP":
                if partial_token != "":
                    if partial_token == "FADE":
                        output += f"[{word_shift}] {partial_token} {token} "
                    else:
                        word_shift += partial_token_amount
                        partial_token = ""
                        partial_token_amount = 0
                else:
                    word_shift += 1
            case _:
                word_shift += 1

    f = open(f"{os.fsdecode(script_word_shift_directory)}\\{os.fsdecode(file)}", "w", encoding = "utf-8")
    f.write(output)
    f.close()


