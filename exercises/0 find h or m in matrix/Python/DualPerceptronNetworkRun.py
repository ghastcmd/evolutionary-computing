from DualPerceptronNetwork import *

def run():
    matrix_H = np.array([
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1
    ])
    answer_H = [1,0]
    print('Matrix H\n', matrix_H)
    
    matrix_M = np.array([
        1, 0, 0, 0, 1,
        1, 1, 0, 1, 1,
        1, 0, 1, 0, 1,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1
    ])
    answer_M = [0,1]
    print('Matrix H\n', matrix_M)
    
    matrix_null = np.zeros(25, dtype=int)
    answer_null = [1,1]
    print('Matrix null\n', matrix_null)
    
    network = DualPerceptronNetwork()
    
    network.train(matrix_H, answer_H)
    network.train(matrix_M, answer_M)
    network.train(matrix_null, answer_null)
    
    print('this is after the print')
    
    print(network.infer(matrix_H))
    print(network.infer(matrix_M))
    print(network.infer(matrix_null))