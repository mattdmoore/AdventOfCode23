import re

impossible = set()
min_bag_powers = []
bag = {'red': 12, 'green': 13, 'blue': 14}
with open('input.txt') as games:
    for game in games:

        game_id = int(re.findall('Game (\d*)', game)[0])
        bag_power = 1
        for colour, total in bag.items():

            # Part 1
            cubes = [int(c) for c in re.findall('(\d*) ' + colour, game)]
            if any([c > total for c in cubes]):
                impossible.add(game_id)

            # Part 2
            bag_power *= max(cubes)

        min_bag_powers.append(bag_power)
    possible = {*range(1, game_id + 1)}.difference(impossible)

    # Result
    print(sum(possible), sum(min_bag_powers))

