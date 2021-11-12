import numpy as np

class DualPerceptronNetwork:
    bias = 1
    bias_weight = 0.5
    
    weights0 = np.zeros(25)
    weights1 = np.zeros(25)
    
    learning_rate = 1
    
    def train(self, question: np.array, right_answer: np.array):
        infered_answer = 0
        error_rate = [0,0]
        
        while error_rate != 0:
            infered_answer = self.infer(question)
            
            error_rate[0] = right_answer[0] - infered_answer[0]
            error_rate[1] = right_answer[1] - infered_answer[1]
            
            for i in range(len(self.weights0)):
                self.weights0[i] += self.learning_rate * error_rate * question[i]
    
            for i in range(len(self.weights1)):
                self.weights1[i] += self.learning_rate * error_rate * question[i]
    
    def infer(self, question: np.array):
        y = [0,0]
        infered_answer = [0,0]
        
        y[0] = np.sum(self.weights0 * question)
        y[1] = np.sum(self.weights1 * question)
        
        y += self.bias * self.bias_weight
        
        return y > 0