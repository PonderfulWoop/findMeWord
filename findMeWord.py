import requests

url = "https://api.datamuse.com/words"

def findMeaningSimilar(s, max_ret = 5):
    params = {'ml' : s, 'max' : max_ret}
    r = requests.get(url = url, params = params)
    data = r.json()

    for x in data:
        print(x['word'])

def findWordsStartingWith(b, max_ret = 5):
    if len(b) > 1:
        return 'Enter a Character!!!'
    params = {'sp' : b+'*', 'max' : max_ret}
    r = requests.get(url = url, params = params)
    data = r.json()

    for x in data:
        print(x['word'])

def findWordsSoundingLike(s, max_ret = 5):
    params = {'sl' : s, 'max' : max_ret}
    r = requests.get(url = url, params = params)
    data = r.json()
    for x in data:
        print(x['word'])

def findWordsRhymingTo(s, max_ret = 5):
    params = {'rel_rhy' : s, 'max' : max_ret}
    r = requests.get(url = url, params = params)
    data = r.json()

    for x in data:
        print(x['word'])

def findWordsSpelledLike(s, max_ret = 5):
    params = {'sp' : s, 'max' : max_ret}
    r = requests.get(url = url, params = params)
    data = r.json()

    for x in data:
        print(x['word'])

while(True):
    print('------------------------------------')
    print('1. Find Words of similar meaning')
    print('2. Find Words starting with')
    print('3. Find Words sounding like')
    print('4. Find Words Rhyming to')
    print('5. Find Words spelled like')
    print('6. Exit')
    print('------------------------------------')
    x = input('Enter Choice: ')
    if int(x) is 1:
        str_inp = input('Enter Words/Expression: ')
        max_ret = input('Enter number of results: ')
        print('------------------------------------')
        print('Results: ')
        if max_ret is '':
            findMeaningSimilar(str_inp)
        else:
            findMeaningSimilar(str_inp, int(max_ret))
        print('------------------------------------')
        input('press enter to continue')
    elif int(x) is 2:
        str_inp = input('Enter a Character: ')
        max_ret = input('Enter number of results: ')
        print('------------------------------------')
        print('Results: ')
        if max_ret is '':
            findWordsStartingWith(str_inp)
        else:
            findWordsStartingWith(str_inp, int(max_ret))
        print('------------------------------------')
        input('press enter to continue')
    elif int(x) is 3:
        str_inp = input('Enter a Word: ')
        max_ret = input('Enter number of results: ')
        print('------------------------------------')
        print('Results: ')
        if max_ret is '':
            findWordsSoundingLike(str_inp)
        else:
            findWordsSoundingLike(str_inp, int(max_ret))
        print('------------------------------------')
        input('press enter to continue')
    elif int(x) is 4:
        str_inp = input('Enter a Word: ')
        max_ret = input('Enter number of results: ')
        print('------------------------------------')
        print('Results: ')
        if max_ret is '':
            findWordsRhymingTo(str_inp)
        else:
            findWordsRhymingTo(str_inp, int(max_ret))
        print('------------------------------------')
        input('press enter to continue')
    elif int(x) is 5:
        str_inp = input('Enter a Word: ')
        max_ret = input('Enter number of results: ')
        print('------------------------------------')
        print('Results: ')
        if max_ret is '':
            findWordsSpelledLike(str_inp)
        else:
            findWordsSpelledLike(str_inp, int(max_ret))
        print('------------------------------------')
        input('press enter to continue')
    else:
        break

print('Thank you for using findMeWord!')
