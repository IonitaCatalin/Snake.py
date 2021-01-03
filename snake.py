import json
import sys

from core.app import App


def import_configuration(filename):
    try:
        file_desc = open(filename, 'r')
        content = ""
        while chunk := file_desc.read(1024):
            content += chunk
        return json.loads(content)
    except IOError as exception:
        print(f'Missing initialization file {filename}')
        exit(1)


if __name__ == '__main__':
    configuration = import_configuration(sys.argv[1])
    rounds = None
    map_width = None
    map_height = None
    player_height = None
    player_width = None
    obstacles = list()

    if 'rounds' in configuration:
        rounds = int(configuration["rounds"])
    else:
        print('Missing "rounds" from the initialization file')
        exit(1)

    if 'map' in configuration:
        if 'width' not in configuration['map'] or 'height' not in configuration['map']:
            print('Malformed input for "map" field')
            exit(1)
        else:
            map_width = int(configuration['map']['width'])
            map_height = int(configuration['map']['height'])
    else:
        print('Missing "map" from the initialization file')
        exit(1)
    if 'player' in configuration:
        if 'width' not in configuration['player'] or 'height' not in configuration['player']:
            print('Malformed input for "player" field')
            exit(1)
        else:
            player_width = int(configuration['player']['width'])
            player_height = int(configuration['player']['height'])
    else:
        print('Missing "player" value from the initialization file')
        exit(1)
    if 'obstacles' in configuration:
        for value in configuration['obstacles']:
            if 'x' not in configuration['obstacles'][value] or 'y' not in configuration['obstacles'][value]:
                print('Malformed input for "obstacles" field')
            else:
                obstacles.append(
                    [int(configuration['obstacles'][value]['x']),int(configuration['obstacles'][value]['y'])])
    else:
        print('No obstacles found!')

    main = App(rounds, map_width, map_height, player_width, player_height, obstacles)
    main.execute()
