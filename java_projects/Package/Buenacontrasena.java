package Package;

import java.util.*;

public class Buenacontrasena {
  public static void main(String[] args) {
    Scanner contrasena = new Scanner(System.in);
    int contador = 0;
    String aux = "";

    aux = contrasena.nextLine();
    if (aux.length() < 8 || aux.length() > 16) {
      contador++;
    } else if (!contieneMayuscula(aux)) { /* Negamos la respuesta para saber si no hay mayúsculas */
      contador++;
    } else if (!contieneNumero(aux)) {
      contador++;
    }
    if (contador == 0){
      System.out.println("Buena contraseña cruck.");
    }
    else {
      System.out.println("Mira máquena, cagaste.");
    }
    contrasena.close();
  }

  static Boolean contieneMayuscula(String comprobar) { /* Comprueba caracter por caracter si es letra mayúscula */
    for (int i = 0; i < comprobar.length(); i++) { /* la longitud es el límite hasta el que contamos */
      if (Character.isUpperCase(comprobar.charAt(i))) {
        return true;
      }
    }
    return false;
  }

  static Boolean contieneNumero(String comprobar) { /* Comprueba caracter por caracter si es un número */
    for (int i = 0; i < comprobar.length(); i++) {
      if (Character.isDigit(comprobar.charAt(i))) {
        return true;
      }
    }
    return false;
  }
}
