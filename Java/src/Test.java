public class Test{
	public static void main(String[] args) {

        System.out.println("What is your name?");
        java.util.Scanner keyboard = new java.util.Scanner(System.in);
        String name = keyboard.nextLine();

        System.out.printf("Greetings %s \n", name);
	}
}
