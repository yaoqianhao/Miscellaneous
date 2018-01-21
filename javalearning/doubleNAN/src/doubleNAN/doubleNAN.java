package doubleNAN;

public class doubleNAN{
	public static void main(String[] args) {
		double tmp1,tmp2=1,tmp3;
		double tt=0;
		tmp1=0/tt;
		//tmp2="asd";
		tmp3=Math.sqrt(-1);
		System.out.println(tmp1);
		System.out.println(tmp2);
		System.out.println(tmp3);
		if(Double.isNaN(tmp1))
			System.out.println("tmp1 is NaN");
		if(Double.isNaN(tmp2))
			System.out.println("tmp2 is NaN");
		if(Double.isNaN(tmp3))
			System.out.println("tmp3 is NaN");
		double tmplog=10;
		System.out.println(Math.log(tmplog));
		int x=123456;
		double nx=x;
		System.out.println(nx);
		
	}
}