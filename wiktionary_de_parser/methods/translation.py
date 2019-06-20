import re
#from translate import Translator

# todo: use translator package to translate words that are not present on wiktionary (limited data)
# todo: probably weird licenses
# todo: Google API [??]
# todo: Microsoft API [pay per char, 2M free per day]
# todo: MyMemory [anon:1000 words/day, register:10000 words/day)
# todo: https://github.com/terryyin/translate-python

wanted_languages = [
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
]


def init(title, text, current_record):
    """
                 '==== {{Übersetzungen}} ====\n'
                 '{{Ü-Tabelle|Ü-links=\n'
                 '*{{en}}: [1] {{Ü|en|free rider}}\n'
                 '*{{fi}}: [1] {{Ü|fi|siipeilijä}}, {{Ü|fi|vapaamatkustaja}}\n'
                 '*{{fr}}: [1] {{Ü|fr|profiteur}}\n'
                 '|Ü-rechts=\n'
                 '*{{it}}: [1] {{Ü|it|scroccone}} {{m}}\n'
                 '*{{es}}: [1] {{Ü|es|}}\n'
                 '}}\n'
                 '\n'
    """

    translation = {}


    # find all translation languages
    """
    test = re.finditer(r'{{Ü\|(.*?)\|(.*?)}}', text)
    for t in test:
        t_found = t.group(1).strip()
        print(t_found)
        #print('------')
    """

    for language in wanted_languages:
        search_translation = re.search(r'{{Ü\|' + language + r'\|(.*?)}}', text)
        if search_translation:
            found_translation = search_translation.group(1).strip()
            if len(found_translation) > 0:
                translation[language] = found_translation
            else:
                translation[language] = ''
        else:
            translation[language] = ''

    return {
        'translation': translation
    }
