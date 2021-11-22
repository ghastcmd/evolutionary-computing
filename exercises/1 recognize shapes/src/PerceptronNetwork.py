import numpy as np

np.random.seed(1)

class PerceptronNetwork:
    bias = -0.5
    
    def __init__(self, input_shape: int, num: int, lr: float = 1):
        self.num_perceptrons = num
        self.learning_rate = lr
        self.weights = []
        
        for _ in range(num):
            self.weights.append(np.zeros(input_shape))
    
    def train_list(self, questions, answers, epochs: int = 1):
        assert type(questions) == np.ndarray
        assert type(answers) == np.ndarray
            
        for _ in range(epochs):
            choice = np.arange(len(questions))
            np.random.shuffle(choice)
            
            for i in choice:
                question = questions[i].flatten()
                answer = answers[i]
                self.train(question, answer)
    
    def train(self, question: np.array, right_answer: np.array):
        error_rate = np.ones(self.num_perceptrons)
        infered_answer = self.infer(question)
        
        error_rate = right_answer - infered_answer

        for weight, err_rate in zip(self.weights, error_rate):
            weight += self.learning_rate * err_rate * question
        
    
    def infer(self, question: np.array):
        y = np.zeros(self.num_perceptrons)
        question = question.flatten()
        
        for i, weight in enumerate(self.weights):
            y[i] = np.sum(weight * question) + self.bias
        
        ret_array = np.array(y >= 0, dtype=int)
        return ret_array

    def test(self, test_questions, test_answers):
        assert type(test_questions) == np.ndarray
        assert type(test_answers) == np.ndarray
        
        correct = 0
        count = 0
        for question, answer in zip(test_questions, test_answers):
            count += 1
            infered = self.infer(question)
            
            if infered.all() == answer.all():
                correct += 1
            
        print('Success rate:', (correct / count) * 100, '%')
        
    def save(self, output_path):
        with open(output_path, 'w') as fp:
            fp.write(f'{self.num_perceptrons}\n')
            fp.write(f'{self.learning_rate}\n')
            for weight in self.weights:
                out_str = ''
                for value in weight:
                    out_str += f'{value} '
                fp.write(f'{out_str}\n')
    
    def load(self, input_path):
        with open(input_path, 'r') as fp:
            self.num_perceptrons = int(fp.readline().strip())
            self.learning_rate = int(fp.readline().strip())
            self.weights = []
            for _ in range(self.num_perceptrons):
                values = fp.readline().strip().split()
                values = [float(x) for x in values]

                self.weights.append(values)