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
        writer.writerow(['Lemma',
                         'Genus',
                         'Nominativ Singular',
                         'Nominativ Plural',
                         'Akkusativ Singular',
                         'Akkusativ Plural',
                         'Dativ Singular',
                         'Dativ Plural',
                         'Genitiv Singular',
                         'Genitiv Plural'])

        # write data rows
        for row in data:
            writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                             row[7], row[8], row[9]])

        csv_file.close()

