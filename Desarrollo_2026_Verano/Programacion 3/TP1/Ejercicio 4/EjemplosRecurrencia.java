package TP1.Ejercicio4;

import java.util.Arrays;

public class EjemplosRecurrencia {

    /**
     * Ejercicio 4: Resolución de Recurrencias
     * Implementación de algoritmos representativos para cada caso.
     */
    public static void main(String[] args) {
        System.out.println("=== 1. SUSTRACCIÓN ===");

        // Caso 1: a = 1
        System.out.println("Caso 1 (a=1): " + sustraccionCaso1_a_Igual_1(5));
        
        // Caso 2: a > 1 (Torres de Hanoi)
        System.out.println("Caso 2 (Torres de Hanoi): Movimientos para 3 discos: " + sustraccionCaso2_TorresHanoi(3));

        // Caso 3: a < 1
        System.out.println("Caso 3 (a<1): " + sustraccionCaso3_a_Menor_1(10));


        System.out.println("\n=== 2. DIVISIÓN ===");
        
        // Caso 4: a = b^k (MergeSort simplificado - simulación de costo)
        int[] arr = {5, 3, 8, 1, 9, 2};
        System.out.println("Caso 4 (a=b^k): Ejecutando MergeSort...");
        divisionCaso4_a_Igual_bk(arr);
        System.out.println("Resultado: " + Arrays.toString(arr));

        // Caso 5: a < b^k (QuickSelect - Búsqueda k-ésimo)
        int[] arr2 = {10, 4, 5, 8, 6, 11, 26};
        int k = 3; // Buscar el 3er elemento más pequeño
        System.out.println("Caso 5 (QuickSelect - simulado): Encontrado aprox en " + divisionCaso5_QuickSelect(arr2, k) + " operaciones");

        // Caso 6: a > b^k (Multiplicación Naive: 4 llamadas)
        long x = 1234; // Simulado
        long y = 5678; // Simulado
        int n_bits = 16; 
        System.out.println("Caso 6 (Multiplicación Naive - Costo): " + divisionCaso6_MultiplicacionNaive(n_bits));
    }


    // -----------------------------------------------------
    // 1. Sustracción: T(n) = a*T(n-1) + f(n)
    // -----------------------------------------------------

    /**
     * Caso 1: a = 1
     * T(n) = T(n-1) + c
     * Complejidad: O(n)
     * Ejemplo: Suma lineal de 1 a n.
     */
    public static int sustraccionCaso1_a_Igual_1(int n) {
        if (n <= 0) return 0;
        return n + sustraccionCaso1_a_Igual_1(n - 1);
    }

    /**
     * Caso 2: a > 1
     * Ejemplo: Torres de Hanoi.
     * Recurrencia: T(n) = 2*T(n-1) + 1
     */
    public static int sustraccionCaso2_TorresHanoi(int n) {
        if (n == 1) return 1; // Mover 1 disco
        // Mover n-1, Mover 1, Mover n-1
        return sustraccionCaso2_TorresHanoi(n - 1) + 1 + sustraccionCaso2_TorresHanoi(n - 1);
    }

    /**
     * Caso 3: a < 1
     * Recurrencia: T(n) = 0.5 * T(n-1) + O(1) (En Probabilidad)
     * Ejemplo: Algoritmo Probabilístico.
     * Con probabilidad 0.5 resolvemos el problema (coste 1).
     * Con probabilidad 0.5 debemos procesar n-1 (recurrencia).
     * El tiempo ESPERADO T(n) disminuye rápidamente.
     */
    public static int sustraccionCaso3_a_Menor_1(int n) {
        if (n <= 0) return 0;
        
        // Simular lanzamiento de moneda (p=0.5)
        if (Math.random() < 0.5) {
            // Caso favorable: Resolvemos aquí y terminamos
            return 1;
        } else {
            // Caso desfavorable: Debemos recurrir
            return 1 + sustraccionCaso3_a_Menor_1(n - 1);
        }
    }


    // -----------------------------------------------------
    // 2. División: T(n) = a*T(n/b) + O(n^k)
    // -----------------------------------------------------

    /**
     * Caso 4: a = b^k
     * Parámetros: a=2, b=2, k=1 -> 2 = 2^1
     * Complejidad: O(n log n)
     * Ejemplo: Merge Sort
     */
    public static void divisionCaso4_a_Igual_bk(int[] arr) {
        if (arr.length <= 1) return;

        int mid = arr.length / 2;
        int[] left = Arrays.copyOfRange(arr, 0, mid);
        int[] right = Arrays.copyOfRange(arr, mid, arr.length);

        // a=2 llamadas
        divisionCaso4_a_Igual_bk(left);
        divisionCaso4_a_Igual_bk(right);

        merge(arr, left, right); // f(n) = O(n)
    }

    private static void merge(int[] result, int[] left, int[] right) {
        int i=0, j=0, k=0;
        while(i < left.length && j < right.length) {
            if(left[i] <= right[j]) result[k++] = left[i++];
            else result[k++] = right[j++];
        }
        while(i < left.length) result[k++] = left[i++];
        while(j < right.length) result[k++] = right[j++];
    }

    /**
     * Caso 5: a < b^k
     * Ejemplo: QuickSelect (Caso Promedio).
     * Busca el k-ésimo elemento más chico.
     * 1. Particiona el array (O(n)).
     * 2. Recurre solo en 1 lado (T(n/2)).
     * Recurrencia: T(n) = T(n/2) + O(n).
     * Complejidad: O(n).
     * (Aquí simulamos el costo computacional retornando el número de operaciones "virtuales")
     */
    public static int divisionCaso5_QuickSelect(int[] arr, int k) {
        if (arr.length <= 1) return 1;
        
        // Simular costo de Partición: O(n)
        int costoParticion = arr.length;

        // Simular recursión en SOLO UNA MITAD (a=1, b=2)
        // En QuickSelect real, vamos a izq o der, pero el tamaño es aprox n/2.
        int[] mitad = new int[arr.length / 2];
        
        return costoParticion + divisionCaso5_QuickSelect(mitad, k);
    }

    /**
     * Caso 6: a > b^k
     * Ejemplo: Multiplicación Entera Naive (Divide and Conquer).
     * Para multiplicar numero de n dígitos:
     * - Se parten en mitades (alto y bajo algo, alto y bajo otro)
     * - Se hacen 4 multiplicaciones recursivas de n/2
     * - Se combinan con sumas y shifts O(n)
     * Recurrencia: T(n) = 4*T(n/2) + O(n)
     * Complejidad: O(n^2)
     */
    public static long divisionCaso6_MultiplicacionNaive(int n_bits) {
        if (n_bits <= 1) return 1; // Multiplicación de 1 bit es O(1)

        // Costo de combinar (Suma y Shifts) -> O(n)
        long costoCombinar = n_bits;

        // 4 Multiplicaciones recursivas de mitad de tamaño
        long recursivo = 4 * divisionCaso6_MultiplicacionNaive(n_bits / 2);

        return costoCombinar + recursivo;
    }
}
