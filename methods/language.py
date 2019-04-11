import re

# sprachcodes
# https://de.wiktionary.org/wiki/Hilfe:Sprachcodes
sprachcodes = {
    'abchasisch': 'ab',
    'afar': 'aa',
    'afrikaans': 'af',
    'akan': 'ak',
    'albanisch': 'sq',
    'altkirchenslawisch': 'cu',
    'amharisch': 'am',
    'anishinabe': 'oj',
    'arabisch': 'ar',
    'aragonesisch': 'an',
    'aramäisch': 'arc',
    'armenisch': 'hy',
    'aserbaidschanisch': 'az',
    'assamesisch': 'as',
    'avestisch': 'ae',
    'awarisch': 'av',
    'aymara': 'ay',
    'bambara': 'bm',
    'banyumasan': 'by',
    'baschkirisch': 'ba',
    'baskisch': 'eu',
    'bengalisch': 'bn',
    'bihari': 'bh',
    'birmanisch': 'my',
    'bislama': 'bi',
    'bokmål': 'nb',
    'bosnisch': 'bs',
    'bretonisch': 'br',
    'bulgarisch': 'bg',
    'chamorro': 'ch',
    'chichewa': 'ny',
    'chinesisch': 'zh',
    'cree': 'cr',
    'deutsch': 'de',
    'dhivehi': 'dv',
    'dzongkha': 'dz',
    'dänisch': 'da',
    'englisch': 'en',
    'esperanto': 'eo',
    'estnisch': 'et',
    'ewe': 'ee',
    'fidschi': 'fj',
    'finnisch': 'fi',
    'französisch': 'fr',
    'friesisch': 'fy',
    'fula': 'ff',
    'färöisch': 'fo',
    'galicisch': 'gl',
    'ganda': 'lg',
    'georgisch': 'ka',
    'griechisch': 'el',
    'grönländisch': 'kl',
    'guaraní': 'gn',
    'gujarati': 'gu',
    'gälisch': 'gd',
    'haitianisch': 'ht',
    'hausa': 'ha',
    'hebräisch': 'he',
    'herero': 'hz',
    'hindi': 'hi',
    'hiri': 'motu,ho',
    'indonesisch': 'id',
    'interlingua': 'ia',
    'interlingue': 'ie',
    'inuktitut': 'iu',
    'inupiaq': 'ik',
    'irisch': 'ga',
    'isixhosa': 'xh',
    'isizulu': 'zu',
    'isländisch': 'is',
    'italienisch': 'it',
    'japanisch': 'ja',
    'javanisch': 'jv',
    'jiddisch': 'yi',
    'kannada': 'kn',
    'kanuri': 'kr',
    'kasachisch': 'kk',
    'kaschmirisch': 'ks',
    'katalanisch': 'ca',
    'khmer': 'km',
    'kikuyu': 'ki',
    'kiluba': 'lu',
    'kinyarwanda': 'rw',
    'kirgisisch': 'ky',
    'kirundi': 'rn',
    'komi': 'kv',
    'kongo': 'kg',
    'koreanisch': 'ko',
    'kornisch': 'kw',
    'korsisch': 'co',
    'kroatisch': 'hr',
    'kuanyama': 'kj',
    'kurdisch': 'ku',
    'laotisch': 'lo',
    'latein': 'la',
    'lateinisch': 'la',
    'lettisch': 'lv',
    'limburgisch': 'li',
    'lingala': 'ln',
    'litauisch': 'lt',
    'luxemburgisch': 'lb',
    'madagassisch': 'mg',
    'malaiisch': 'ms',
    'malayalam': 'ml',
    'maltesisch': 'mt',
    'manx': 'gv',
    'maori': 'mi',
    'marathi': 'mr',
    'marshallesisch': 'mh',
    'mazedonisch': 'mk',
    'mongolisch': 'mn',
    'nauruisch': 'na',
    'navajo': 'nv',
    'ndonga': 'ng',
    'nepalesisch': 'ne',
    'niederländisch': 'nl',
    'nord': 'ndebele,nd',
    'norwegisch': 'no',
    'nynorsk': 'nn',
    'okzitanisch': 'oc',
    'oriya': 'or',
    'oromo': 'om',
    'ossetisch': 'os',
    'pali': 'pi',
    'pandschabi': 'pa',
    'paschtu': 'ps',
    'persisch': 'fa',
    'polnisch': 'pl',
    'portugiesisch': 'pt',
    'quechua': 'qu',
    'rumänisch': 'ro',
    'russisch': 'ru',
    'rätoromanisch': 'rm',
    'samisch': 'se',
    'samoanisch': 'sm',
    'sango': 'sg',
    'sanskrit': 'sa',
    'sardisch': 'sc',
    'schwedisch': 'sv',
    'serbisch': 'sr',
    'sesotho': 'st',
    'setswana': 'tn',
    'shona': 'sn',
    'sindhi': 'sd',
    'singhalesisch': 'si',
    'siswati': 'ss',
    'slowakisch': 'sk',
    'slowenisch': 'sl',
    'somali': 'so',
    'spanisch': 'es',
    'suaheli': 'sw',
    'sundanesisch': 'su',
    'swahili': 'sw',
    'süd': 'ndebele,nr',
    'tadschikisch': 'tg',
    'tagalog': 'tl',
    'tahitianisch': 'ty',
    'tamilisch': 'ta',
    'tatarisch': 'tt',
    'telugu': 'te',
    'thailändisch': 'th',
    'tibetisch': 'bo',
    'tigrinya': 'ti',
    'tongaisch': 'to',
    'tschechisch': 'cs',
    'tschetschenisch': 'ce',
    'tschuwaschisch': 'cv',
    'tsonga': 'ts',
    'turkmenisch': 'tk',
    'twi': 'tw',
    'türkisch': 'tr',
    'uigurisch': 'ug',
    'ukrainisch': 'uk',
    'ungarisch': 'hu',
    'urdu': 'ur',
    'usbekisch': 'uz',
    'venda': 've',
    'vietnamesisch': 'vi',
    'volapük': 'vo',
    'walisisch': 'cy',
    'wallonisch': 'wa',
    'weißrussisch': 'be',
    'wolof': 'wo',
    'yi': 'ii',
    'yoruba': 'yo',
    'zhuang': 'za',
}


def init(title, text, record):
    match_lang = re.search(r'=== ?{{Wortart\|[^}|]+\|([^}|]+)(?:\|[^}|]+)*}}', text)
    if not match_lang:
        return False

    lang_lang = match_lang.group(1) if match_lang.group(1) else match_lang.group(2)
    lang_lang = lang_lang.lower()

    if lang_lang not in sprachcodes:
        return False

    return sprachcodes[lang_lang]
