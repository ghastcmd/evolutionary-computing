import numpy as np
from PerceptronNetwork import PerceptronNetwork

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