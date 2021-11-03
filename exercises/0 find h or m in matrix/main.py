# This exercise is to find a h or m or nothing in a 
# 5x5 matrix using the technique of neural nets

import numpy as np

def search_matrix(list, matrix):
    for mat in list:
        if (mat == matrix).all():
            return True
    return False

first = np.random.randint(0, 2, (3,5,5))
m_example = np.array(
    [
        [1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)

first[1] = m_example

# Draws a h in a 5x5 boolean matrix
# height goes from 3 to 5
# bar_width goes from 1 to 3
# bar_position goes from 1 to 3
# x_position goes from 0 to 3
# y_postion goes from 0 to 3
def create_h(height, bar_width, bar_position, x_position, y_position):
    assert height >= 3 and height <= 5
    assert bar_width >= 1 and bar_width <= 3
    assert bar_position >= 1 and bar_position < height - 1
    assert x_position >= 0 and x_position <= 5 - height
    assert y_position >= 0 and y_position < 5 - bar_width - 1

    arr = np.zeros((5,5))
    for i in range(height):
        arr[i + y_position, x_position] = 1
        arr[i + y_position, x_position + bar_width + 1] = 1

    for i in range(bar_width):
        arr[y_position + bar_position, i + x_position + 1] = 1

    return arr

# generating all possible h
h_list = []
for h in range(3, 6):
    for b in range(1, 4):
        for bp in range(1, 4):
            for xp in range(0, 4):
                for yp in range(0, 4):
                    try:
                        new_h = create_h(h, b, bp, xp, yp)
                        h_list.append(new_h)
                    except:
                        pass

h_list = np.array(h_list)
print(np.array(h_list))