# import dependencies
from ast import Num
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import easyocr
import cv2
import warnings
warnings.filterwarnings('ignore')


# scale the map
# imporoves resolution
def scale(image, new_rows, new_cols):
    rows, cols = image.shape
    return [
        [image[int(rows * row / new_rows)][int(cols * col / new_cols)]
         for col in range(new_cols)] for row in range(new_rows)
    ]


def remove_spaces(line):
    return line.replace('\n', '')


# get the range of the mountain tile
def get_range(num, delimeter):
    start, end = num.split(delimeter)
    return [int(start), int(end)]


# read from ther input file
# assuming its always available
def read_from_file(filename):
    filename += '.txt'
    lines = []
    with open(filename, 'r') as data:
        [lines.append(line) for line in data.readlines()]
    return lines


# get rows and columns sizes
def get_shape(lines):
    line = remove_spaces(lines[0])
    line = line.replace('map_size=', '')
    return get_range(line, ',')


# create map
def create_map(lines):
    map_shape = get_shape(lines)
    map_data = remove_spaces(lines[2])
    mountain = lines[7].replace('Mountain', '')
    mountain = get_range(remove_spaces(mountain), '-')
    map = np.empty(map_shape, dtype=int)
    count = 0
    for i in range(map_shape[0]):
        for j in range(map_shape[1]):
            index_num = int(map_data[count: count + 3])
            count += 3
            map[i][j] = 1 if index_num >= mountain[0] else 0
    map_append = np.zeros(map_shape, dtype=int)
    map = np.append(map_append, map, axis=0)
    return map


# construct the map image
def image(map, img_name):
    # scale to get better resolution
    rows, cols = map.shape
    row_scale, colm_scale = 1024 // rows, 720 // cols
    new_rows, new_cols = rows * row_scale, cols * colm_scale
    map = scale(map, new_rows, new_cols)
    # save the created map as a picture
    img_name += '.png'
    plt.imsave(img_name, map, cmap=cm.gray, dpi=150)


# wrute solution to file
def to_file(result, filename):
    filename += '_solution.txt'
    result = result if len(result) > 1 else "0" + result
    file = open(filename, 'w')
    file.write(result)
    file.close()


# get the number from the image
def get_num(img_name):
    img_path = "./" + img_name + '.png'
    img = cv2.imread(img_path)
    reader = easyocr.Reader(['en'], gpu=False, verbose=False)
    results = reader.readtext(img, allowlist='0123456789')
    result = results[0][1]
    return result


def run():
    maps = ['map_1', 'map_2', 'map_3']
    for map in maps:
        lines = read_from_file(map)
        map_arr = create_map(lines)
        image(map_arr, map)
        num = get_num(map)
        to_file(num, map)


if __name__ == '__main__':
    run()
