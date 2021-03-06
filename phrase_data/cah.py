import json

data = {
    'cah' : {
        'template' : ['{black_card}'],

        'black_card' : [],
        'white_card' : [],
    }
}

with open('phrase_data/against-humanity/source/cards.json') as card_file:
    all_cards = json.loads(card_file.read())
    for card in all_cards:
        if card['numAnswers'] is 0:
            if card['text'][-1] == '.' and card['text'][-2] != '.':
                card['text'] = card['text'][:-1]
            data['cah']['white_card'].append(card['text'])
        else:
            if card['text'].count('_') != card['numAnswers']\
                    and card['text'][-1] != '?':
                print(card)
            elif card['text'][-1] == '?':
                data['cah']['black_card'].append(card['text'] + ' ' + '{white_card}')
            else:
                modified = card['text'].replace('_', '{white_card}')
                data['cah']['black_card'].append(modified)
