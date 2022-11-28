import java.util.Scanner;

public class tarea {
    public static void main(String[] argms) {
        Scanner lectura = new Scanner(System.in);

        System.out.println("Dolares a Euros: ");

        Integer valor = lectura.nextInt();

        Double euro = valor*0.98;

        System.out.println("Su nombre es: " + valor + " y su edad es: " + euro);
    }
}