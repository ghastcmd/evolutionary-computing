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

if __name__ == '__main__':
    network = PerceptronNetwork(20*20, 1)
    
    if os.path.exists('shapes_network.data'):
        network.load('shapes_network.data')
    else:
        print('You need to train the model first')
        exit()    


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