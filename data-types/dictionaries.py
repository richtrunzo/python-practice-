test_dictionary = {
  'football': 'steelers',
  'baseball': 'dodgers',
  'basketball': 'lakers'
}

'football' in test_dictionary #returns true

'soccer' in test_dictionary #returns false

test_dictionary['baseball'] # returns 'dodgers'

test_dictionary['soccer'] = 'lafc'

# ^ adds the value 'soccer' in test dictionary

list(test_dictionary) # returns ['football', 'baseball', 'basketball', 'soccer']
sorted(test_dictionary) # returns ['baseball', 'basketball', 'football', 'soccer']

del test_dictionary['soccer']

# ^ deletes 'soccer' from the dictionary - keyword del

drinks_dictionary = dict([('water', 'arrowhead'), ('milk', 'oatley'), ('beer', 'lagunitas')])

# ^ The dict() constructor builds dictionaries directly from sequences of key-value pairs.
