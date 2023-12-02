
def my_function_to_run(input):
    total = 0
    enumerated_games = enumerate(input.split("\n"))
    for game_index, game in enumerated_games:
        game_max_red = 0
        game_max_green = 0
        game_max_blue = 0
        
        collection = game.split(";")
        collection_validity = set()
        for index, pull in enumerate(collection):
           colors = parse(pull, index)
           print(colors)
           for i in range (len(colors)):
               if i == 0 and colors[i] > game_max_red:
                  game_max_red = colors[i]
               if i == 1 and colors[i] > game_max_green:
                  game_max_green = colors[i]
               if i == 2 and colors[i] > game_max_blue:
                  game_max_blue = colors[i]
        total += game_max_red * game_max_green * game_max_blue 
    return total


def parse(pull, index):
    color_group = str(pull).split(",")

    if index == 0:
        color_group = pull.split(":")[1].split(",")

    color_group_is_valid = set()
    max_red = 0
    max_green = 0
    max_blue = 0

    for index in range(len(color_group)):
        
        color_number_pair = color_group[index]
        [number, color] = color_number_pair.strip().split(" ")
        number = int(number)
        redcheck = number > max_red and color == "red"
        greencheck = number > max_green and color == "green"
        bluecheck = number > max_blue and color == "blue"

        if (redcheck):
            max_red = number
        if (bluecheck):
            max_blue = number
        if (greencheck):
            max_green = number
    return [max_red, max_green, max_blue]
    # return list(color_group_is_valid)
