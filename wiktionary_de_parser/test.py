import os
import sys
from bz2file import BZ2File
#from __init__ import Parser
from wiktionary_de_parser import Parser

from wiktionary_de_parser.write_csv import WriteCSV
from datetime import datetime

# add parent dir to PATH
sys.path.insert(1, os.path.join(sys.path[0], '..'))

bzfile_path = 'E:/Work/UnityProjects/DeutschCompanion/data/dewiktionary-20190601-pages-meta-current.xml.bz2'
bz = BZ2File(bzfile_path)
collection = set()
my_list = []
#found_lemmas = []
startTime = datetime.now()

countFound = 0
countTotal = 0

wanted_flexions = [
    'Nominativ Singular',
    'Nominativ Plural',
    'Akkusativ Singular',
    'Akkusativ Plural',
    'Dativ Singular',
    'Dativ Plural',
    'Genitiv Singular',
    'Genitiv Plural',
]

print('---- SCRIPT START -----')
print('---- PARSING START -----')

for record in Parser(bz):
    countTotal += 1
    if 'language' not in record or record['language'] != 'Deutsch':
        continue

    if 'lemma' in record and 'flexion' in record and 'pos' in record:
        if 'Substantiv' not in record['pos']:
            continue

        # print(record['pos'])

        lemma = record['lemma']

        # skip abbreviations
        if lemma.isupper(): continue
        # skip some weird words
        if lemma.startswith('-'): continue
        # skip some more weird words
        if lemma.startswith('Benutzer Diskussion:'): continue
        if lemma.startswith('Benutzer:'): continue

        genus = record['flexion'].get('Genus')
        if genus == 'm': genus = 0
        elif genus == 'f': genus = 1
        elif genus == 'n': genus = 2
        else: continue  # skip if there is no article
        # print(genus)

        ipa = record['ipa']

        flex_list = []
        for flexion in wanted_flexions:
            flex = record['flexion'].get(flexion)
            flex_verify = flex if flex is not None else ''
            flex_list.append(flex_verify)
            # print(flexion + ': ' + flex)

        # if missing BOTH nominative sing. and plural we skip the word completely
        if flex_list[0] is '' and flex_list[1] is '': continue

        # get meaning "Bedeutungen"
        meanings = record['meaning']
        #print(meanings)

        # get examples "Beispiele"
        examples = record['example']
        #print(lemma)
        #print(meanings)
        #print(examples)

        # get translations
        translations = record['translation']
        t = []
        for key in translations.keys():
            t.append(record['translation'].get(key))

        #print('---------')
        # column values
        tmp_list = [lemma, genus, ipa, flex_list[0], flex_list[1], flex_list[2], flex_list[3], flex_list[4],
                    flex_list[5], flex_list[6], flex_list[7], meanings, examples,
                    t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9],
                    t[10], t[11], t[12], t[13], t[14], t[15], t[16], t[17], t[18], t[19],
                    t[20], t[21]]
        # print(tmp_list)
        my_list.append(tmp_list)

        countFound += 1
        # print("-----")

        #if countFound > 5000:
        #    break

endTime = datetime.now()

print('Words found: ' + str(countFound) + ' out of ' + str(countTotal) + ' entries')
print('---- PARSING DONE -----')
print('---- WRITING CSV START -----')
WriteCSV.output(my_list)
print('---- WRITING CSV DONE -----')
print('Execution time: ' + str(endTime - startTime))
print('---- SCRIPT DONE -----')
