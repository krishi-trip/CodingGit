# To compile all of my files

echo "Compiling Food.java"
javac -d bin src/cs1302/nums/Food.java

echo "Compiling Fruit.java"
javac -d bin -cp bin src/cs1302/nums/Fruit.java

echo "Compiling Apple.java"
javac -d bin -cp bin src/cs1302/nums/Apple.java

echo "Compiling FoodTester.java"
javac -d bin -cp bin src/cs1302/nums/FoodTester.java

echo ""

echo "Running FoodTester.java"

echo ""
java -cp bin cs1302.nums.FoodTester
