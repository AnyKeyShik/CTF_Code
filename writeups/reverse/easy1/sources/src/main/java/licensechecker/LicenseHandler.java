package licensechecker;

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class LicenseHandler {

    private final Cryptor cryptor;
    private final String licenseFile;
    private byte[] encryptedLicense;

    public LicenseHandler(String licenseFile) {
        this.licenseFile = licenseFile;
        cryptor = new Cryptor();
    }

    public boolean check() {
        readLicense();

        return cryptor.hash(encryptedLicense);
    }

    public String getLicense() {
        return cryptor.decrypt(encryptedLicense);
    }

    private void readLicense() {
        try {
            var reader = new DataInputStream(new FileInputStream(licenseFile));
            int nBytesToRead = reader.available();

            if (nBytesToRead > 0) {
                encryptedLicense = new byte[nBytesToRead];

                if (reader.read(encryptedLicense) == -1) {
                    throw new IOException();
                }
            }
        } catch (FileNotFoundException e) {
            System.err.println("License file not found! :c");
            System.exit(-1);
        } catch (IOException e) {
            System.err.println("Can't read license file! :c");
            System.exit(-1);
        }
    }
}
