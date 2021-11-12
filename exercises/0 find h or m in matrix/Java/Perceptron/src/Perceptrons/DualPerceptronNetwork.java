package Perceptrons;

public class DualPerceptronNetwork {
    int bias = 1;
    float biasWeight = 0.5f;
    private int [] weights0 = new int[25]; //trabalhando com 5x5
    private int [] weights1 = new int[25]; //trabalhando com 5x5

    int learningRate = 1;       //Taxa de Aprendizagem

    public void train(int [] question, int [] rightAnswer){
        int [] inferedAnswer ; // tipos de resposta vistas em aula [0,0](nada), [0,1](M), [1,0](H), [1,1](nada)
        int errorRate = 1;

        while(errorRate != 0) {
            inferedAnswer = infer(question);

            errorRate = rightAnswer[0] - inferedAnswer[0] + rightAnswer[1] - inferedAnswer[1]; //verificando se a IA acertou

            for (int i = 0; i < weights0.length; i++) {
                weights0[i] = weights0[i] + learningRate * errorRate * question[i];
            }
        }
    }

    public void train(int [] [] question, int [] rightAnswer) {
        int[] inferedAnswer ; // tipos de resposta vistas em aula [0,0](nada), [0,1](M), [1,0](H), [1,1](nada)
        int [] errorRate = new int [2];errorRate[0] = 1; errorRate[1] = 1;

        while (errorRate[0] != 0 && errorRate[1] != 0) {

            inferedAnswer = infer(question);

            errorRate[0] = rightAnswer[0] - inferedAnswer[0]; //verificando se a IA acertou
            errorRate[1] = rightAnswer[1] - inferedAnswer[1];
            //System.out.println("Inferencia");
            //System.out.println(inferedAnswer[0]+", "+inferedAnswer[1]);
            //System.out.println("resposta");
            //System.out.println(rightAnswer[0]+", "+rightAnswer[1]);
            //System.out.println("error 0 and 1");
            //System.out.println(errorRate[0]+", "+errorRate[1]);

            for (int i = 0; i < question.length; i++) {
                for (int j = 0; j < question[0].length; j++) {
                    weights0[i*j] = weights0[i * j] + learningRate * errorRate[0] * question[i][j];
                }
            }

            for (int i = 0; i < question.length; i++) {
                for (int j = 0; j < question[0].length; j++) {
                    weights1[i*j] = weights1[i * j] + learningRate * errorRate[1] * question[i][j];
                }
            }
        }
    }
    public int [] infer(int [] question){
        double y = 0.0; // resultado cru da inferencia do perceptron
        int [] inferedAnswer = new int [2]; // tipos de resposta vistas em aula [0,0](nada), [0,1](M), [1,0](H), [1,1](nada)

        for (int i = 0; i < question.length; i++) {
            y += weights0[i] * question[i];
        }

        y += bias * biasWeight;

        if (y > 10){
            inferedAnswer[0] = 1;// Achou H
        }
        else if(y > 0){
            inferedAnswer[1] = 1;// Achou M
        }
        return inferedAnswer;
    }

    public int [] infer(int [] [] question){
        double [] y = new double[2]; // resultado cru da inferencia do perceptron
        int [] inferedAnswer = new int [2]; // tipos de resposta vistas em aula [0,0](nada), [0,1](M), [1,0](H), [1,1](nada)

        for (int i = 0; i < question.length; i++) {
            for (int j = 0; j < question[0].length; j++) {
                y[0] += weights0[i*j] * question[i][j];
                //System.out.println(y[0]);
            }
        }
        y[0] += bias * biasWeight;

        for (int i = 0; i < question.length; i++) {
            for (int j = 0; j < question[0].length; j++) {
                y[1] += weights1[i*j] * question[i][j];
                //System.out.println(y[1]);
            }
        }
        y[1] += bias * biasWeight;
        //System.out.println("[ " +y[0]+",  "+y[0]+ " ]");
        //printArray(weights0);
        //printArray(weights1);
        if (y[0] >= 0){
            inferedAnswer[0] = 1;// Achou H
        }

        if (y[1] >= 0){
            inferedAnswer[1] = 1;// Achou M
        }

        return inferedAnswer;
    }

    public static void printArray(int [] array){
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            if (i != array.length-1){
                System.out.print(array[i]+", ");
            }
            else{
                System.out.print(array[i]);
            }
        }
        System.out.print("]\n");
    }
}
