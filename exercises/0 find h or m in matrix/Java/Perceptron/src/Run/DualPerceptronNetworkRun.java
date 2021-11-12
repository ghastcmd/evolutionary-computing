package Run;

import Perceptrons.DualPerceptronNetwork;
public class DualPerceptronNetworkRun {
    public static void run(){
        System.out.println("Matriz H");
        int [] [] matrixH = new int [5] [5];
        int [] answerH = new int [2]; answerH[0] = 1;
        for (int i = 0; i < matrixH.length; i++) {
            for (int j = 0; j < matrixH[0].length; j++) {
                if(j==0||j==4){
                    matrixH[i][j] = 1;
                }
                if(i==2){
                    matrixH[i][j] = 1;
                }
            }
        }
        printMatrix(matrixH);

        System.out.println();
        System.out.println("Matriz M");
        int [] [] matrixM = new int [5] [5];
        int [] answerM = new int [2]; answerM[1] = 1;
        for (int i = 0; i < matrixM.length; i++) {
            for (int j = 0; j < matrixM[0].length; j++) {
                if(j==0||j==4){
                    matrixM[i][j] = 1;
                }
            }
        }
        matrixM[2][2]=1;matrixM[1][1]=1;matrixM[1][3]=1;
        printMatrix(matrixM);

        System.out.println("Matriz nula");
        int [] [] matrixNull = new int [5] [5];
        int [] answerNull = new int [2]; answerNull[0] = 1; answerNull[1] = 1;
        printMatrix(matrixNull);

        DualPerceptronNetwork network = new DualPerceptronNetwork();
        for (int i = 0; i<2; i++){
            network.train(matrixH, answerH);

            network.train(matrixM, answerM);

            network.train(matrixNull, answerNull);
        }
        printArray(network.infer(matrixH));
        printArray(network.infer(matrixM));
        printArray(network.infer(matrixNull));
    }

    public static void printMatrix(int [] [] matrix){
        for (int i = 0; i < matrix.length; i++) {
            System.out.print("[");
            for (int j = 0; j < matrix[0].length; j++) {
                if (j != matrix[0].length-1){
                    System.out.print(matrix[i][j]+", ");
                }
                else{
                    System.out.print(matrix[i][j]);
                }
            }
            System.out.print("]\n");
        }
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
