import re
texts = ['でレンタル HD(高画質) ￥ 500',
    'で購入　　HD(高画質) ￥ 2,500',
    'Buy SD £5.99',
    'Buy SD £14.99',
    'HD ausleihen EUR 3,99',
    'HD kaufen EUR 11,99',
    'Buy Movie HD $19.99',
    '$1,200.84'
]
curword = r'(?:USD|GBP|EUR|JPY|CHF|SEK|DKK|NOK|SGD|HKD|AUD|TWD|NZD|CNY|KRW|INR|CAD|VEF|EGP|THB|IDR|PKR|MYR|PHP|MXN|VND|CZK|HUF|PLN|TRY|ZAR|ILS|ARS|CLP|BRL|RUB|QAR|AED|COP|PEN|CNH|KWD|SAR)'
cursymbol = r'[$\u00A2-\u00A5\u058F\u060B\u07FE\u07FF\u09F2\u09F3\u09FB\u0AF1\u0BF9\u0E3F\u17DB\u20A0-\u20C0\uA838\uFDFC\uFE69\uFF04\uFFE0\uFFE1\uFFE5\uFFE6\U00011FDD-\U00011FE0\U0001E2FF\U0001ECB0]'
num = r'\d+(?:[.,]\d+)*'
pattern = re.compile(fr'(?:\b{curword}|{cursymbol})\s*({num})|({num})\s*(?:{curword}\b|{cursymbol})')
# print(fr'(?:\b{curword}|{cursymbol})\s*({num})|({num})\s*(?:{curword}\b|{cursymbol})')

for text in texts:
    m = pattern.search(text)
    if m:
        result = m.group(1) or m.group(2)
        print(result)