package Package;

import java.util.*;

public class par_contador {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int contador = 0;
        int numero = 1;

        while (true){
            String numeroString = leer.nextLine();
            numero = Integer.parseInt(numeroString);
            int resto = numero % 2;
            if (numero == 0) {
            	break;
            }
            if (resto == 0){
                System.out.println("Par");
                contador = contador +1;
            } else if (resto != 0){
                System.out.println("Impar");
            }
        }
        System.out.println("La cantidad de números pares es " + contador);
    }
}
