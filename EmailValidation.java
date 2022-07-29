import java.util.Scanner;

public class EmailValidation implements EmailAdapter {

    Scanner input = new Scanner(System.in);

    @Override
    public boolean isValidEmail(String email) {

        String expressInvalid = "^(?=.{1,64}@)[A-Za-z0-9_-]+(\\.[A-Za-z0-9_-]+)*@"
                + "[^-][A-Za-z0-9-]+(\\.[A-Za-z0-9-]+)*(\\.[A-Za-z]{2,})$";

        return email.matches(expressInvalid);
    }

    public void emailClient() {
        System.out.println("Type your e-mail!");
        String email = input.next();

        if (isValidEmail(email)) {
            System.out.println("E-mail is valid!");
        } else {
            System.out.println("E-mail is invalid!");
        }
    }

}
