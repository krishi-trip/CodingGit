package cs1302.nums;

public class FoodTester {
    public static void main(String[] args) {

        Food a = new Fruit("Banana");
        Fruit b = new Apple();

        System.out.println(a);
        System.out.println(b);

        a.eat();

        System.out.println(a);

    }

}
