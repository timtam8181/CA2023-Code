# shopping_list = []
# with open('shopping.txt') as f:
#     for line in f:
#         shopping_list.append(line.strip())

# print(shopping_list)

# shows = [
#     'The Mandalorian',
#     'The Wticher',
#     'The X-Files'
# ]

# with open('tv-shows.txt', 'w') as f:
#     # f.write('\n'.join(shows))
#     for i, s in enumerate(shows):
#         f.write(f'{i + 1}. {s}\n')

item = input('What do you need to buy? ')
with open('shopping.txt', 'a') as f:
    f.write(f'\n{item}\n')