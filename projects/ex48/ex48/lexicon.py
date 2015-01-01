directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat')
stops = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')

def scan(sentence):
    words = sentence.split();
    result = []
    for w in words:
        if w in directions:
            result.append(('direction', w))
        elif w in verbs:
            result.append(('verb', w))
        elif w in stops:
            result.append(('stop', w))
        elif w in nouns:
            result.append(('noun', w))
        else:
            n = convert_numbers(w);
            if n == None:
                result.append(('error', w))
            else:
                result.append(('number', n))
    return result

def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None
