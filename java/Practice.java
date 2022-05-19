public class Practice {
    public static void main (String[] args) {
        printRow(10);
    } // Main

    public static void printRow(int num) {
        if (num == 0) {
            return;
        }
        printRow(num-1);
        printCol(num-1);
        System.out.println();
    } // printRow

    public static void printCol(int num) {
        if(num==0) {
            return;
        } 
        System.out.print("*");
        printCol(num-1);
    } // printCol
} // Practice
