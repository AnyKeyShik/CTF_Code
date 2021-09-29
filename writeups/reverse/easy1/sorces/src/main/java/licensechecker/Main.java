package licensechecker;

public class Main {

    public static void main(String[] argv) {

        LicenseHandler licenseHandler;

        if (argv.length != 1) {
            System.err.println("Please give me license file as argument!");
            System.exit(-1);
        }

        licenseHandler = new LicenseHandler(argv[0]);

        if (licenseHandler.check()) {
            System.out.println("It's your license!\nGreat!\nYour flag: " + licenseHandler.getLicense());
        } else {
            System.err.println("Invalid license!");
            System.exit(-1);
        }
    }
}
