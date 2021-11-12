import numpy as np

class DualPerceptronNetwork:
    bias = 1
    bias_weight = 0.5
    
    weights0 = np.zeros(25)
    weights1 = np.zeros(25)
    
    learning_rate = 1
    
    def train(self, question: np.array, right_answer: np.array):
        error_rate = np.ones(2)
        
        while error_rate.any() != 0:
            infered_answer = self.infer(question)
            
            error_rate[0] = right_answer[0] - infered_answer[0]
            error_rate[1] = right_answer[1] - infered_answer[1]

            self.weights0 += self.learning_rate * error_rate[0] * question
            self.weights1 += self.learning_rate * error_rate[1] * question
        
    
    def infer(self, question: np.array):
        y = np.array([0,0])
        
        y[0] = np.sum(self.weights0 * question)
        y[1] = np.sum(self.weights1 * question)
        
        y[0] += self.bias * self.bias_weight
        y[1] += self.bias * self.bias_weight
        
        ret_array = np.array(y >= 0, dtype=int)
        return ret_array