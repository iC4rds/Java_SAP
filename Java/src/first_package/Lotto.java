package first_package;

import java.util.Scanner;

public class Lotto {
	public static void main(String[] args) {
		int treffer = 0;
		int gesamt = 0;
		int[] L = new int[6];
		int[] l = new int[6];
		Scanner scanner = new Scanner(System.in);
		System.out.println("Bitte geben sie 6 Zahlen an: ");
		for(int i = 0; i<L.length; i++) {
			L[i] = scanner.nextInt();
		}
		scanner.close();
		for(int i = 0; i<l.length; i++) {
			l[i] = random();
			System.out.println(l[i]);
		}
		for(int i=0; i<l.length; i++) {
			for(int j = 0; j<L.length; j++) {
				if(l[i] == L[j]) {
					treffer = L[j];
				}
			}
			if(treffer!=0) {
				System.out.println("Die Zahl " + treffer + " war ein treffer!");
				treffer = 0;
				gesamt++;
			}
		}
		if(gesamt !=6) {
			System.out.println("Insgesamt hattest du " + gesamt + " treffer!");
		}
		else {
			System.out.println("Du hast im Lotto gewonnen");
		}
	}
	public static int random() {
		return (int)((Math.random())*49+1);
	}
}
