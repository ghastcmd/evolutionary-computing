from GeneticAlgorithm import run

from NeuralNetwork import DEAD_END_ALL_SIDE_SN, CORRIDOR_ALL_SIDE_SN

if __name__ == '__main__':
    # run(100, 10, 10, 0.1)
    
    test_mat = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    
    result = DEAD_END_ALL_SIDE_SN.infer(test_mat)
    print(result)
    