#!/usr/bin/env python3

import sys

favs = { 'activity' : 'climbing',
				 'food' : 'pizza',
				 'dessert' : 'mint chip ice cream',
				 'organism' : 'kitten'
}

#print(favs['activity'])
#fav_thing = 'activity'
#print(favs[fav_thing])
#print(favs['food'])
#fav_thing = 'organism'
#print(favs[fav_thing])

usr_val = sys.argv[1]

for item in favs:
	print(f'{item}: {favs[item]}')

print(favs[usr_val])

print(f'Options: {favs.keys()}')

favs['organism'] = 'e. coli'

print(favs['organism'])

new_key = sys.argv[2]
new_val = sys.argv[3]

favs[new_key] = new_val

print(f'Updated dictionary includes new favorite: {favs}')


 
