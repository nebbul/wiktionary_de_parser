import re


def remove_tags(text):
    # remove <!-- --> comments
    text = re.sub(r'(<!--.+(?=-->)-->)', ' ', text)
    # remove <ref></ref> tags
    text = re.sub(r'(<ref>.+(?=</ref>)</ref>)', ' ', text)
    # replace superimposition tag with a ^
    text = text.replace('<sup>', '^')
    text = text.replace('</sup>', '')
    text = text.replace('<sub>', '')
    text = text.replace('</sub>', '')

    # trim
    text = text.strip()

    return text


def clean_text(text):
    text = text.replace('{{Bedeutungen}}\n', '')
    text = text.replace(':[1]', '')
    text = text.replace('\'', '')
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace('{', '')
    text = text.replace('}', '')
    text = text.replace('K|', '')
    text = text.replace('K|', '')
    text = text.replace('„', '\"')
    text = text.replace('“', '\"')
    text = text.replace('|t2=_|', '')
    text = text.replace('|', '/')
    text = text.replace(':1a', '')
    text = text.replace('ISO 8601; ; ', '')
    text = text.replace('ISO 8601;', '')
    text = text.replace('#', '')
    text = text.replace(' m/', ' ')
    text = text.replace('^1 ', ' ')
    text = text.replace(' ^2 ', ' ')

    # trim
    text = text.strip()

    return text


def polish_text(text):
    if text.endswith(';'):
        text = text.replace(';', '')
    if not text.endswith('.'):
        text = text + '.'

    # uppcase first letter
    text = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), text, 1)

    # remove excess whitespace
    text = re.sub(' +', ' ', text)

    text = text.replace('Va./', 'Veraltet,')
    text = text.replace('Va. /', 'Veraltet,')
    text = text.replace('Va.', 'Veraltet,')
    text = text.replace('kPl./', 'kein Plural,')
    text = text.replace('KPl.', 'kein Plural,')
    text = text.replace('Ugs./', 'Umgangssprachlig,')
    text = text.replace('(ugs.)', '(Umgangssprachlig)')

    return text


def init(title, text, current_record):
    """
{{Bedeutungen}}
:[1] {{K|Finanzwesen}} Geldinstitut für Finanzdienstleistungen
:[2] ein [[Glücksspiellokal]]; auch eine der Spielparteien kann als ''Bank'' bezeichnet werden (beim Roulette gewinnt die Bank, wenn keine der gesetzten Kombinationen fällt), oder auch ein zentraler Vorrat, der selbst nicht am Wettstreit teilnimmt, kann so bezeichnet werden (beispielsweise der Vorrat an Straßen, Häusern und Hotels, die beim Monopoly bisher noch von keinem Mitspieler gekauft wurden)

"""
    text = remove_tags(text)

    match_firstline = re.search(r'({{Bedeutungen}}\n[^\n]+)', text)
    if match_firstline:
        first_line = match_firstline.group(1)
        # print(first_line)

        cleaned_text = clean_text(first_line)

        polished_text = polish_text(cleaned_text)

        # print(first_line)
        meaning = polished_text
    else:
        meaning = ''
    #if not match_firstline:
    #    return False



    return {
        'meaning': meaning
    }
