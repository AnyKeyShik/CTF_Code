package licensechecker;

import com.google.common.annotations.VisibleForTesting;

public class FizzBuzz {

    private final Integer seed;

    public FizzBuzz(int seed) {
        this.seed = seed;
    }

    public void run() {
        for (int i = seed; i < seed * 2; i++) {
            System.out.println(convert(i));
        }
    }

    protected String convert(int fizzBuzz) {

        if (fizzBuzz % 15 == 0) {
            return "FizzBuzz";
        }
        if (fizzBuzz % 3 == 0) {
            return "Fizz";
        }
        if (fizzBuzz % 5 == 0) {
            return "Buzz";
        }
        return String.valueOf(fizzBuzz);
    }
}
