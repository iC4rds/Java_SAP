package first_package;

public class plant {
	
	private String type;
	private double size;
	private boolean toxic;
	
//	public static int xyz(int a, int b) {
//		int result = a+b;
//		return result;
//	}
//	
//	public static void main(String[] args) {
//		System.out.println(xyz(18,2));
//	}
	
//	public void setAttributes(String type, double size, boolean toxic) {
//		this.type = type;
//		this.size = size;
//		this.toxic = toxic;
//	}
	
	public plant(String type, double size, boolean toxic) {
		this.type = type;
		this.size = size;
		this.toxic = toxic;
	}
	
	public void displayAttributes() {
		System.out.println(this.type);
		System.out.println(this.size);
		System.out.println(this.toxic);
	}
	
	public boolean toxic() {
		return this.toxic;
	}
	
	public static void main(String[] args) {
		plant Baum = new plant("B",20,false);
		plant Baum2 = new plant("K",2,false);
		plant Baum3 = new plant("A",10.5,true);
		Baum.displayAttributes();
		Baum2.displayAttributes();
		Baum3.displayAttributes();
	}
	
	
	
}
