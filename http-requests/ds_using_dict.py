ab = {
'Swaroop': 'swaroop@swaroopch.com',
'Larry': 'larry@wall.org',
'Matsumoto': 'matz@ruby-lang.org',
'Spammer': 'spammer@hotmail.com'
}
#print("Swaroop's address is", ab['Swaroop'])
print(ab.keys)

del ab['Spammer']
#print(ab)
#print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
ab['Guido'] = 'guido@python.org'
#print(ab)

