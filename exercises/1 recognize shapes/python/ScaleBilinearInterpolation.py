import numpy as np

simple_matrix = np.array([
    [1, 0],
    [1, 1],
], dtype=int)

view_matrix = np.zeros((10, 10))

scale = view_matrix.shape[0] / simple_matrix.shape[0]

def bilinear_interpolation(x, y, points, check = False):
    (x1, y1, q11), (_x1, y2, q12), (x2, _y1, q21), (_x2, _y2, q22) = points

    if check:
        if x1 != _x1 or x2 != _x2 or y1 != _y1 or y2 != _y2:
            raise ValueError('points do not form a rectangle')
        if not x1 <= x <= x2 or not y1 <= y <= y2:
            raise ValueError('(x, y) not within the rectangle')

    return (q11 * (x2 - x) * (y2 - y) +
            q21 * (x - x1) * (y2 - y) +
            q12 * (x2 - x) * (y - y1) +
            q22 * (x - x1) * (y - y1)
           ) / ((x2 - x1) * (y2 - y1) + 0.0)

def make_points(dim, scale):
    points = []
    for x in range(dim + 1):
        final = False
        if x == dim:
            final = True

        pos_x = int(x * scale)
        
        points.append((pos_x, 0, simple_matrix[0, x - final]))
    
    for y in range(dim):
        for x in range(dim+1):
            final = False
            if x == dim:
                final = True
            
            pos_x = int(x * scale)
            pos_y = int(y * scale + scale - 1)
        
            points.append((pos_x, pos_y, simple_matrix[y, x - final]))
    
    return np.array(points).reshape((dim+1,dim+1,3))

points = make_points(simple_matrix.shape[0], scale)
print(points)

def get_point_block(x, y, points):
    ret_points = []
    
    ret_points.append(points[y, x])
    ret_points.append(points[y+1, x])
    ret_points.append(points[y, x+1])
    ret_points.append(points[y+1, x+1])
    
    return ret_points

original_shape = view_matrix.shape[0]
block_shape = original_shape / scale
block_shape = int(block_shape)
block_scale = int(scale)

for bb_y in range(block_shape):
    for bb_x in range(block_shape):
        p_list = get_point_block(bb_x, bb_y, points)
        print(p_list)

        for i in range(block_scale):
            x = int(bb_x * scale + i)
            for j in range(block_scale):
                y = int(bb_y * scale + j)
                
                view_matrix[y, x] = bilinear_interpolation(x, y, p_list)

print(view_matrix)
print(np.array((view_matrix>0.3), dtype=int))

zero = np.zeros((5,5))

points = [(0,0,1),(0,4,1),(4,0,0),(4,4,1)]
for y in range(5):
    for x in range(5):
        zero[y, x] = bilinear_interpolation(x, y, points)
        
print(zero)
print(np.array(zero>0.75, dtype=int))

print(zero.T)