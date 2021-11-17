import numpy as np

def scale(matrix: np.ndarray, final_shape: tuple):
    ret_matrix = np.zeros(final_shape, dtype=int)
    height, width = final_shape
    orig_height, orig_width = matrix.shape
    scale_width = int(width/orig_width)
    scale_height = int(height/orig_height)
     
    for y in range(int(height/scale_height)):
        yy = int(y * scale_height)
        for x in range(int(width/scale_width)):
            xx = int(x * scale_width)
            ret_matrix[yy:yy+scale_height,xx:xx+scale_width] = matrix[y, x]

    return ret_matrix
    
if __name__ == '__main__':
    mat = np.array([
        [1, 0],
        [1, 1],
    ])
    
    final_matrix = scale(mat, (20,20))
    
    test_matrix = np.ones((20, 20))
    test_matrix[0:10,10:20] = 0
    print('Test 01: ', (final_matrix == test_matrix).all())