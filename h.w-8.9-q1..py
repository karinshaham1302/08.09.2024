# start

friends_of_danny: int = int(input('how many friends came to danny?'))
slice_of_pizza: int = int(input('how many slices of pizza are order?'))
print(f'how much each friends received? {slice_of_pizza // 4}')

if slice_of_pizza % 4 != 0:
    print(f'how many are left {slice_of_pizza % 4}')

# stop
