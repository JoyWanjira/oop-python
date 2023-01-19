shoplist=['apple','mango','carrot','banana']
print('i have', len(shoplist), 'items to purchase')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

shoplist.sort()
print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])
olditem= shoplist[0]
print("i bought the", olditem)
del shoplist[0]
print("my shopping list is now", shoplist)