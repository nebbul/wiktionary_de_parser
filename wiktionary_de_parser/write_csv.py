import unicodecsv as csv
import os


class WriteCSV:
    @staticmethod
    def output(data):
        output_path = 'output'
        output_file = os.path.join(output_path, 'output.csv')

        # create folder if it doesnt exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # create file if it doesn't exist
        csv_file = open(output_file, 'wb')
        writer = csv.writer(csv_file, encoding='utf-8', delimiter=',')

        # write header
        writer.writerow(['Index',
                         'Lemma',
                         'Genus',
                         'Nominativ Singular',
                         'Nominativ Plural',
                         'Akkusativ Singular',
                         'Akkusativ Plural',
                         'Dativ Singular',
                         'Dativ Plural',
                         'Genitiv Singular',
                         'Genitiv Plural',
                         'Meaning'
                         'ca',  # Catalan / català
                         'hr',  # Croatian / hrvatski
                         'cs',  # Czech / čeština
                         'da',  # Danish / dansk
                         'nl',  # Dutch / Nederlands
                         'en',  # English / English
                         'fi',  # Finnish / suomi
                         'fr',  # French / français
                         'hu',  # Hungarian / magyar
                         'is',  # Icelandic / íslenska
                         'it',  # Italian / italiano
                         'la',  # Latin / Latina
                         'lv',  # Latvian / latviešu
                         'no',  # Norweigan / norsk
                         'pl',  # Polish / polski
                         'pt',  # Portuguese / português
                         'ro',  # Romanian / română
                         'sk',  # Slovak / slovenčina
                         'sl',  # Slovenian / slovenščina
                         'es',  # Spanish / español
                         'sv',  # Swedish / svenska
                         'tr',  # Turkish / Türkçe
                         ])

        # write data rows
        rows_sorted = sorted(data, key=lambda x: x[0].lower())

        index = 0
        for row in rows_sorted:
            writer.writerow([index, row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                             row[7], row[8], row[9], row[10],
                             row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19],
                             row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29],
                             row[30], row[31], row[32]])
            index += 1

        csv_file.close()

