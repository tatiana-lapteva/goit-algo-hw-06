
def get_subway_info(path: str) -> list:
    stations = []
    edges = []
    color_map = {}

    try:
        with open(path, 'r', encoding='utf-8') as file:
            next(file)
            for line in file:
                line = line.strip().split(",")
                stations.append(line[0]) if line[0] not in stations else None
                if line[0] not in color_map.keys():
                    color_map[line[0]] = line[1]
                if line[2] != 'None' and line[3].strip() != 'None':
                    edges.append((line[0], line[2], int(line[3])))
        return stations, edges, color_map
    except IOError:
        print("Error: could not read file " + path.name)