import java.util.function.IntFunction;

public class Test {

    public static <T> T[] makeArray(IntFunction<T[]> gen, int length) {
	return gen.apply(length);
    }

    public static void main(String[] args) {

	IntFunction<String[]> sgen = len -> new String[len];
	String[] sa = Test.makeArray(sgen, 1);

	//IntFunction<Character[]> cgen = new Character[len];
	//Character[] ca = Test.makeArray(cgen, 4);

	Integer[] ia = Test.makeArray(len -> new Integer[len], 6);

	for (int i = 0 ; i < sa.length ; i++) {
	    System.out.println("Index " + i + ": " + sa[i]);
	}

	System.out.println();

	for (int i = 0 ; i < ia.length ; i++) {
	    System.out.println("Index " + i + ": " + ia[i]);
	}
    }
}
