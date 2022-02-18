package cs1302.nums;

public abstract class Food {

    private String name;
    private boolean isEaten;

    public Food(String name) {
        this.name = name;
        this.isEaten = false;
    }

    public String getName() {
        return name;
    }

    public void setName(String newName) {
        name = newName;
    }

    public void eat() {
        isEaten = true;
    }

    public boolean hasBeenEaten() {
        return isEaten;
    }

    public String toString() {
        String msg = "Name: " + name + "\n" +
            "isEaten: " + isEaten;

        return msg;
    }

}
