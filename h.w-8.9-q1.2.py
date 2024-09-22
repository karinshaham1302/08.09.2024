# start

pizza_slices: int = int(input('how many pizza slices?'))
friends: int = int(input('how many friends?'))

each_one_got = pizza_slices // friends
left_over = pizza_slices % friends

print(f'each on got: {each_one_got}, left over: {left_over}')

# stop
