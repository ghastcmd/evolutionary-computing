import numpy as np

def scale(matrix: np.ndarray, final_shape: tuple):
    ret_matrix = np.zeros(final_shape, dtype=int)
    height, width = final_shape
    orig_height, orig_width = matrix.shape
    scale_width = width/orig_width
    scale_height = height/orig_height
    
    for y in range(orig_height):
        yy = int(y * scale_height)
        for x in range(orig_width):
            xx = int(x * scale_width)
            ret_matrix[yy:yy+int(scale_height+1),xx:xx+int(scale_width+1)] = matrix[y, x]

    return ret_matrix

if __name__ == '__main__':
    class Test:
        def __init__(self):
            self.num_test = 1

        def test_print(self, mat1, mat2):
            print(f'Test {self.num_test:02}: ', (mat1 == mat2).all())
            # print(mat1)
            self.num_test += 1

        def test(self, little_matrix, final_matrix):
            out_matrix = scale(little_matrix, final_matrix.shape)
        
            self.test_print(out_matrix, final_matrix)

    tt = Test()
    
    little_matrix = np.array([
        [1, 0],
        [1, 1],
    ])
    
    test_matrix = np.ones((20, 20))
    test_matrix[0:10,10:20] = 0
    
    tt.test(little_matrix, test_matrix)
    
    little_matrix = np.array([
        [0, 0],
        [1, 1]
    ])

    test_matrix = np.vstack([np.zeros((10, 20)), np.ones((10, 20))])
    
    tt.test(little_matrix, test_matrix)
    
    little_matrix = np.array([
        [0, 0],
        [1, 0]
    ])
    
    test_matrix = np.zeros((20, 20))
    test_matrix[10:20,0:10] = 1
    
    tt.test(little_matrix, test_matrix)
    
    little_matrix = np.zeros((19, 19))
    little_matrix[0:,0] = 1
    
    final_matrix = np.zeros((20,20))
    final_matrix[:19,0] = 1
    
    tt.test(little_matrix, final_matrix)
    