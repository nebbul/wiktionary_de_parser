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
found_lemmas = []
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


def nullcheck(s):
    s = s if s is not None else ''
    return s


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

        # skip duplicates
        if lemma in found_lemmas: continue
        # skip abbreviations
        if lemma.isupper(): continue

        # print(lemma)

        genus = record['flexion'].get('Genus')
        if genus == 'm': genus = 0
        elif genus == 'f': genus = 1
        elif genus == 'n': genus = 2
        else: continue # skip if there is no article
        # print(genus)

        flex_list = []
        for flexion in wanted_flexions:
            flex = nullcheck(record['flexion'].get(flexion))
            flex_list.append(flex)
            # print(flexion + ': ' + flex)

        # if missing BOTH nominative sing. and plural we skip the word completely
        if flex_list[0] is '' and flex_list[1] is '': continue

        # column values
        tmp_list = [lemma, genus, flex_list[0], flex_list[1], flex_list[2], flex_list[3], flex_list[4],
                    flex_list[5], flex_list[6], flex_list[7]]
        # print(tmp_list)
        my_list.append(tmp_list)

        # store the lemmas so we can check against duplicates and skip them
        found_lemmas.append(lemma)

        countFound += 1
        # print("-----")

        # count += 1
        # if count > 49:
        #    break

endTime = datetime.now()

print('Words found: ' + str(countFound) + ' out of ' + str(countTotal) + ' entries')
print('---- PARSING DONE -----')
print('---- WRITING CSV START -----')
WriteCSV.output(my_list)
print('---- WRITING CSV DONE -----')
print('Execution time: ' + str(endTime - startTime))
print('---- SCRIPT DONE -----')
