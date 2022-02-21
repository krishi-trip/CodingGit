package cs1302.nums;

public abstract class Food {

    private String name;
    private boolean isEaten;
    private boolean isPoisonous;

    public Food(String name, boolean isPoisonous) {
        this.name = name;
        this.isPoisonous = isPoisonous;
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
