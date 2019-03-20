#project 2 (Japanese tokenizer) by Ell Buscemi 3.13.19
#there are some "" characters in the wordlist, not sure what they're supposed to be so
#just got rid of them for now

import sys
import re

file_name = "in.txt"#sys.argv[1]
out_file_name = "out.txt"#sys.argv[2]
dictionary_file_name = "japanese_wordlist.txt"

with open(file_name, 'r', encoding='utf-8') as file:
    with open(out_file_name, 'w', encoding='utf-8') as fixed_file:
        with open(dictionary_file_name, 'r', encoding='utf-8') as dictionary:
            x = dictionary.read()
            wordDictionary = re.findall(r'^.+$', x, re.MULTILINE)
            y = file.read()
            linesToTokenize = re.findall(r'.+$', y, re.MULTILINE)

            tokenized = ""
            for line in linesToTokenize:
                lineLocal = line

                while True:
                    foundMatch = False

                    if lineLocal in wordDictionary:
                        print("found match: " + lineLocal)
                        tokenized += (lineLocal + " ")
                        line = line[len(lineLocal):len(line)]
                        lineLocal = line
                        foundMatch = True
                        #break

                    if len(lineLocal) == 1:
                        print("found single character: " + lineLocal)
                        tokenized += (lineLocal + " ")
                        line = line[len(lineLocal):len(line)]
                        lineLocal = line
                        foundMatch = True
                        #break

                    if lineLocal == "":
                        break

                    if foundMatch == False:
                        lineLocal = lineLocal.rstrip(lineLocal[(len(lineLocal)-1)])
                        print("no match, stripping rightmost character: "+ lineLocal)

                if line == "":
                    tokenized += "\n"
                    print("tokenized: " + tokenized)

            fixed_file.write(tokenized)
