import random


def noun():
    ''' эта функция возвращает случайное существительное;
    у неё нет аргументов '''
    nouns = ['squirrel', 'chipmunk', 'elephant', 'mushroom', 'banana', 'book']
    return random.choice(nouns)


def adverb():
    ''' эта функция возвращает случайное наречие; у неё нет аргументов '''
    nouns = ['aggressively', 'loudly', 'slowly', 'proudly', 'dangerously']
    return random.choice(nouns)


def intensifier(adv):
    ''' эта функция добавляет к наречию adv наречие-модификатор
     и возвращает результат'''
    intensifiers = ['quite', 'rather', 'very', 'enough']
    random_intensifier = random.choice(intensifiers)
    if random_intensifier == 'enough':
        result = adv + ' ' + random_intensifier
    else:
        result = random_intensifier + ' ' + adv
    return result


def adjective(word):
    ''' эта функция добавляет к слову word случайное прилагательное слева
    и возвращает результат '''
    adjectives = ['big', 'little', 'brown', 'red', 'yellow',
                  'nasty', 'wonderful', 'fascinating', 'ordinary']
    return random.choice(adjectives) + ' ' + word


def verb_of_thought(subj):
    ''' эта функция добавляет к существительному subj какой-то глагол мысли
     в 3 л. ед. ч. и возвращает результат'''
    verbs = ['thinks', 'knows', 'is convinced', 'believes']
    return subj + ' ' + random.choice(verbs)


def verb_transitive(subj, obj):
    ''' эта функция берёт два слова, subj и obj, и делает их подлежащим
     и дополнением какого-то переходного глагола в форме без -s '''
    verbs = ['eat', 'throw', 'frighten', 'drink', 'kill', 'launch']
    return subj + ' ' + random.choice(verbs) + ' ' + obj


def random_sentence():
    ''' random_sentence() -- это функция, которая возвращает готовое
     случайно составленное предложение. У неё вообще нет аргументов,
     поэтому после её названия пишутся пустые скобки. '''
    sentence = verb_of_thought(adjective(noun())) + ' that '\
                + verb_transitive(adjective(noun() + 's'), noun() + 's') +\
               ' ' + intensifier(adverb()) + '.'
    # с помощью \ можно переносить длинные строки кода
    return sentence


def main():
    '''Это главная функция, из неё вызывается всё остальное'''
    text = random_sentence()
    print(text)

# А вот тут начинается основной код (вне функций). Из одной строчки. :)
if __name__ == '__main__':
    main()
