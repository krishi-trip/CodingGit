package cs1302.practice;

public abstract class Food {

    private String name;

    public Food(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String newName) {
        name = newName;
    }

    public String toString() {
        String msg = "Name: " + name;

        return msg;
    }

}
