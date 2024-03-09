import fitz

def getAns(path):
    pdf = fitz.open(path)
    page = pdf[11]
    text = page.get_text("text")
    text_list = text.split()
    ch = []
    ph = []
    ma = []
    l = len(text_list)
    i = 0
    while i < l:
        if text_list[i] == 'CHEMISTRY':
            while text_list[i] != 'PHYSICS':
                for x in text_list[i]:
                    if 'A' <= x <= 'D' and text_list[i-1].strip('.').isnumeric():
                        ch.append(x)
                i = i+1
        i = i + 1
    i = i-1
    i = 0
    while i < l:
        if text_list[i] == 'PHYSICS':
            while text_list[i] != 'MATHEMATICS':
                for x in text_list[i]:
                    if 'A' <= x <= 'D' and text_list[i-1].strip('.').isnumeric():
                        ph.append(x)
                i = i+1
                if i == l:
                    break
        i = i + 1
        if i == l:
            break

    i = 0
    while i < l:
        if text_list[i] == 'MATHEMATICS':
            while text_list[i] != 'FITJEE':
                for x in text_list[i]:
                    if 'A' <= x <= 'D' and text_list[i-1].strip('.').isnumeric():
                        ma.append(x)
                i = i+1
                if i == l:
                    break
        i = i + 1
        if i == l:
            break
    res = {}
    res['ma'] = ma
    res['ch'] = ch
    res['ph'] = ph
    return res
    print(len(ch))


