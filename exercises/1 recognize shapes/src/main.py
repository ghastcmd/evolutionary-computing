import numpy as np
import os
from PerceptronNetwork import PerceptronNetwork
from NormalScaling import scale

def scan_window(matrix, neural_network: PerceptronNetwork):
    num_shapes = 0
    for window in range(3, 21):
        for x in range(1, 20 - window):
            for y in range(1, 20 - window):
                view = matrix[y:y+window,x:x+window]
                scaled_matrix = scale(view, (20,20))
                prediction = neural_network.infer(scaled_matrix)
                num_shapes += prediction

    return num_shapes

def read_training_file(path):
    ret_matrix = []
    ret_answers = []
    
    with open(path, 'r') as fp:
        while True:
            start_read = fp.readline()
            if start_read == '':
                break
            elif start_read == '\n':
                while start_read == '\n':
                    start_read = fp.readline()
            
            mat_shape = start_read.strip().split(' ')
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
    
    return np.array(ret_matrix), np.array(ret_answers)

if __name__ == '__main__':
    network = PerceptronNetwork(20*20, 1)
    
    if os.path.exists('shapes_network.data'):
        network.load('shapes_network.data')
    else:
        if os.path.exists('training.vv'):
            values = read_training_file('training.vv')
            questions, answers = values
        else:
            print('Need to have a training file')
            exit()
        network.train_list(questions, answers, 11)
        network.save('shapes_network.data')
        network.test(questions, answers)
    
    
    input_matrix = np.zeros((20,20))
    
    input_matrix = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ])
    
    # input_matrix = scale(np.array([
    #     [1, 0, 1],
    #     [1, 1, 1],
    #     [1, 1, 1],
    # ]), (20, 20))
    
    print(input_matrix)
    
    num_shapes = scan_window(input_matrix, network)
    print(f'There is {num_shapes} horizontal rectangles in the matrix')


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