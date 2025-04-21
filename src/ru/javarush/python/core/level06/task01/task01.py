# Создание множеств.
import random
# Напиши программу, которая создает 5 множеств:
# множество с 0 элементов,
# множество с 1 элементом,
# множество с 5 элементами,
# множество с 100 элементами,
# множество с 1000 элементами

# Напишите тут ваш код
def create_set(size):
    if size == 0:
        return set()
    return {random.randint(1,size) for i in range(size)}

l = [create_set(i) for i in (0, 1, 5, 100, 1000)]



'''
cards = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

cards_list = list(cards)
random.shuffle(cards_list)
print(f'Card_list = {cards_list}')
new_cards = set(cards_list)
print(f'Cards = {cards}')

print(f'New cards = {new_cards}')
print(f'Card_list = {cards_list}')

print(cards.pop())
print(cards.pop())
print(cards.pop())
print(cards.pop())
print(cards.pop())

print(f'Cards = {cards}')
'''