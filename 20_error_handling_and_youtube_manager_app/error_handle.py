file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('chai aur python')



# Enumeration

# >>> x = ('Masala', 'Lemon', 'Ginger')
# >>> x   
# ('Masala', 'Lemon', 'Ginger')
# >>> y = enumerate(x)
# >>> y
# <enumerate object at 0x0000028046043D80>
# >>> list(y)
# [(0, 'Masala'), (1, 'Lemon'), (2, 'Ginger')]