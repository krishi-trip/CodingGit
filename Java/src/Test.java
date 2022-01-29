/*
 * Test.java
 *
 * A java environment to practice java skills and test java code
 *
 */

import java.util.*;

public class Test{
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        String name = "";

        System.out.println("What is your name?");

        try {
            name = keyboard.nextLine();
        }
        catch (InputMismatchException ime) {
            System.out.println("That is not a string");
        }
        catch (NullPointerException npe) {
            System.out.println("You didn't enter your name");
        }

        System.out.printf("Greetings %s \n", name);
    }
}
