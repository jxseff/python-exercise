pizzaPie = ['hawaiian', 'overload', 'pepperoni']
for pizza in pizzaPie:
    print(f"I like {pizza.title()}")
print('I really love pizza')

friend_pizzas = pizzaPie[:]
pizzaPie.append('cheesy')
friend_pizzas.append('macaroni')
print(f"My favorite pizzas are: {pizzaPie[0]}, \
{pizzaPie[1]}, {pizzaPie[2]} and {pizzaPie[3]}")
print(f"My friend's favorite pizzas are: {friend_pizzas[0]}, \
{friend_pizzas[1]}, {friend_pizzas[2]}, and {friend_pizzas[3]}")