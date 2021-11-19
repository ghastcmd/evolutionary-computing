import numpy as np
import os
from PerceptronNetwork import PerceptronNetwork
from NormalScaling import scale

def scan_window(matrix, neural_network: PerceptronNetwork):
    num_shapes = 0
    for window in range(2, 21):
        for x in range(1, 20 - window):
            for y in range(1, 20 - window):
                view = matrix[y:y+window,x:x+window]
                scaled_matrix = scale(view, (20,20))
                num_shapes += neural_network.infer(scaled_matrix)

    return num_shapes

def read_training_file(path):
    ret_matrix = []
    ret_answers = []
    
    with open(path, 'r') as fp:
        mat_shape = fp.readline().strip().split(' ')
        mat_shape = tuple([int(x) for x in mat_shape])
        mat_list = []
        for _ in range(mat_shape[0]):
            line_mat = fp.readline().strip().split(' ')
            line_mat = [int(x) for x in line_mat]
            mat_list.append(line_mat)
        
        mat_list = np.array(mat_list, dtype=int).reshape(mat_shape)
        mat_list = scale(mat_list, (20,20))
        
        ret_matrix.append(mat_list)
        
        ret_answers.append(int(fp.readline().strip()))
        fp.readline()
    
    return ret_matrix, ret_answers

if __name__ == '__main__':
    
    values, answers = read_training_file('training.dat')
    
    print(values, '\n', answers)
    
    
    # network = PerceptronNetwork(20*20, 1)
    
    # if os.path.exists('shapes_network.data'):
    #     network.load('shapes_network.data')
    # else:
    #     print('You need to train the model first')
    #     exit()    


exit()

# testing the neural network

if __name__ == '__main__':
    network = PerceptronNetwork(25, 2)
    
    h = np.array([
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1
    ])
    h_answer = [1,0]
    
    m = np.array([
        1, 0, 0, 0, 1,
        1, 1, 0, 1, 1,
        1, 0, 1, 0, 1,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1
    ])
    m_answer = [0,1]
    
    null = np.zeros(25)
    null_answer = [1,1]
    
    questions = np.vstack((h, m, null))
    answers = np.vstack((h_answer, m_answer, null_answer))
    
    network.train_list(questions, answers, 20)
    
    network.test(questions, answers)