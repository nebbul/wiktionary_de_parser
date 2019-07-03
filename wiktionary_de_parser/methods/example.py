import re


def remove_tags(text):
    # remove <!-- --> comments
    text = re.sub(r'(<!--.+(?=-->)-->)', ' ', text)
    # remove <ref></ref> tags
    text = re.sub(r'(<ref>.+(?=</ref>)</ref>)', ' ', text)
    text = re.sub(r'(<ref name = ".*">.+(?=</ref>)</ref>)', ' ', text)
    text = re.sub(r'(<ref name= ".*">.+(?=</ref>)</ref>)', ' ', text)
    # remove tags
    text = re.sub(r'(<span style=".*">)', '', text)
    text = re.sub(r'(</span>)', '', text)
    text = re.sub(r'(<ref name=".*">.+(?=</ref>)</ref>)', ' ', text)
    text = re.sub(r'(<ref name=".*"/>)', ' ', text)
    text = re.sub(r'(<ref name=".*"/>)', ' ', text)
    text = re.sub(r'(<ref name=".*" />)', ' ', text)
    text = re.sub(r'(<ref name=.*>)', ' ', text)
    text = re.sub(r'(<ref name = .*>)', ' ', text)
    text = re.sub(r'(<ref name = ".*">)', ' ', text)
    text = re.sub(r'(<ref name = ".*"/>)', ' ', text)
    text = re.sub(r'(<ref name = ".*" />)', ' ', text)
    text = re.sub(r'(<ref name= ".*" />)', ' ', text)
    text = re.sub(r'(<ref name =".*" />)', ' ', text)
    text = re.sub(r'(<REF>.+(?=</REF>)</REF>)', ' ', text)
    text = text.replace('<sup>', '^')
    text = text.replace('</sup>', '')
    text = text.replace('<sub>', '')
    text = text.replace('</sub>', '')
    text = text.replace('<small>', '')
    text = text.replace('</small>', '')
    text = text.replace('<big>', '')
    text = text.replace('</big>', '')
    text = text.replace('<code>', ' ')
    text = text.replace('</code>', ' ')
    text = text.replace('<math>', ' ')
    text = text.replace('</math>', ' ')
    text = text.replace('<nowiki>', ' ')
    text = text.replace('<nowiki/>', ' ')
    text = text.replace('<nowiki />', ' ')
    text = text.replace('</nowiki>', ' ')
    text = text.replace('<ref>', ' ')
    text = text.replace('<br />', ' ')
    text = text.replace('<!--', '')

    # trim
    text = text.strip()

    return text


def clean_text(text):
    text = text.replace('{{Beispiele}}\n', '')
    text = text.replace(':[1]', '')
    text = text.replace('\'', '')
    text = text.replace('[1, 2]', '')
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace('{', '')
    text = text.replace('}', '')
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
    text = text.replace('(– – υ υ)', '')
    text = text.replace('(– υ – υ – – –)', '')
    text = text.replace('& nbsp;', '')
    text = re.sub(r'(/t.*=_/)', '/', text)
    text = re.sub(r'(/t.*=;/)', '/', text)
    text = re.sub(r'(/A=.*)', '', text)
    text = text.replace('/ft=', ',')
    text = text.replace('(w:', '(')
    text = text.replace('…', '...')

    # trim
    text = text.strip()

    return text


def polish_text(text):
    if text.endswith(';') or text.endswith(':'):
        text = text[:-1]
    if not text.endswith('.') and not text.endswith('?') and not text.endswith('!') and not text.endswith('"'):
        text = text + '.'
    if text.startswith(':'):
        text = text[1:] # 71602
    if text == '.':
        text = ''

    # uppcase first letter
    text = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), text, 1)

    # remove excess whitespace
    text = re.sub(' +', ' ', text)

    text = text.replace('Va./', 'Veraltet,')
    text = text.replace('Va. /', 'Veraltet,')
    text = text.replace('Va.', 'Veraltet,')
    text = text.replace('*Veraltet,:.', 'Veraltet,')
    text = text.replace('*Veraltet,', 'Veraltet,')
    text = text.replace('kPl./', 'kein Plural,')
    text = text.replace('KPl.', 'kein Plural,')
    text = text.replace('Ugs./', 'Umgangssprachlig,')
    text = text.replace('(ugs.)', '(Umgangssprachlig)')
    text = text.replace('/; ugs./:.', '(Umgangssprachlig)')
    text = text.replace('ugs./,', '(Umgangssprachlig)')
    text = text.replace('*Ugs.', '(Umgangssprachlig)')
    text = text.replace(' :', ':')
    text = text.replace(' ,', ',')

    if text.endswith(','):
        text = text[:-1]
        text = text + '.'

    text = text.replace('Beispiele fehlen.', '')
    text = text.replace('Beispiele fehlen/spr=.', '')
    text = text.replace('Beispiele fehlen/spr=de.', '')
    text = text.replace('Beispiele fehlen/spr=Deutsch.', '')
    text = text.replace('Beispiele fehlen/spr=Deutsch.', '')
    text = text.replace('Beispiele fehlen/spr=en.', '')
    text = text.replace('Beispiele fehlen/spr=it.', '')

    text = text.strip()

    return text


def init(title, text, current_record):
    """
{{Bedeutungen}}
:[1] {{K|Finanzwesen}} Geldinstitut für Finanzdienstleistungen
:[2] ein [[Glücksspiellokal]]; auch eine der Spielparteien kann als ''Bank'' bezeichnet werden (beim Roulette gewinnt die Bank, wenn keine der gesetzten Kombinationen fällt), oder auch ein zentraler Vorrat, der selbst nicht am Wettstreit teilnimmt, kann so bezeichnet werden (beispielsweise der Vorrat an Straßen, Häusern und Hotels, die beim Monopoly bisher noch von keinem Mitspieler gekauft wurden)

"""
    text = remove_tags(text)

    match_firstline = re.search(r'({{Beispiele}}\n[^\n]+)', text)
    if match_firstline:
        first_line = match_firstline.group(1)
        # print(first_line)

        cleaned_text = clean_text(first_line)

        polished_text = polish_text(cleaned_text)

        #if 'Beispiele fehlen' in text:
        #    example = ''
        #else:
        example = polished_text
    else:
        example = ''

    return {
        'example': example
    }
