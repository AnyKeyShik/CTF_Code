package licensechecker;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class FizzBuzzTest {

    private final FizzBuzz fb = new FizzBuzz(3);

    @Test
    @DisplayName("Not FizzBuzz")
    public void FizzBuzzNormalNumbers() {
        assertEquals("1", fb.convert(1));
        assertEquals("2", fb.convert(2));
    }

    @Test
    @DisplayName("Fizz")
    public void FizzBuzzThreeNumbers() {
        assertEquals("Fizz", fb.convert(3));
    }

    @Test
    @DisplayName("Buzz")
    public void FizzBuzzFiveNumbers() {
        assertEquals("Buzz", fb.convert(5));
    }

    @Test
    @DisplayName("FizzBuzz")
    public void FizzBuzzThreeAndFiveNumbers() {
        assertEquals("FizzBuzz", fb.convert(15));
    }
}