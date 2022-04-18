import java.util.function.*;

public class ExampleDriver {
    public static void main(String[] args) {
	Example e = new Example();


	Supplier<Example> se = () -> new Example();
	BiFunction<Example, Double, Double> bf = (Example ex, Double num) -> ex.cubeIt(num);
	BinaryOperator<Double> bo = (a, b) -> Example.times(a, b);
	//	UnaryOperator<Double> uf = (Example ex, Double num) -> ex.cubeIt(num);
    }
}
