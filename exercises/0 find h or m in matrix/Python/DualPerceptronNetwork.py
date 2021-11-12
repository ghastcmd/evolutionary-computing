import numpy as np

np.random.seed(1)

class DualPerceptronNetwork:
    bias = 0.5
    
    weights0 = np.zeros(25)
    weights1 = np.zeros(25)
    
    learning_rate = 1
    
    def train_list(self, questions: np.array, answers: np.array, epochs: int):
        choice = np.arange(len(questions))
        np.random.shuffle(choice)
        
        for _ in range(epochs):
            for i in choice:
                question = questions[i].flatten()
                answer = answers[i]
                self.train(question, answer)
    
    def train(self, question: np.array, right_answer: np.array):
        error_rate = np.ones(2)
        infered_answer = self.infer(question)
        
        error_rate = right_answer - infered_answer

        self.weights0 += self.learning_rate * error_rate[0] * question
        self.weights1 += self.learning_rate * error_rate[1] * question
        
    
    def infer(self, question: np.array):
        y = np.zeros(2)
        question = question.flatten()
        
        y[0] = np.sum(self.weights0 * question)
        y[1] = np.sum(self.weights1 * question)
        
        for value in y:
            value += self.bias
        
        ret_array = np.array(y >= 0, dtype=int)
        return ret_array