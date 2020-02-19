import java.util.Scanner;//imports scanner for it to be able to be used 
public class speedFineCalculator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		System.out.println("\"Welcome to program that calculates the speeding ticket\"\n");//welcome string 
		
		System.out.println("Please enter the Speed Limit of the zone:");//asks for the speed limit of the road
		Scanner limit = new Scanner(System.in);
		double spdLimt = limit.nextDouble();//its a double 
		
		System.out.println("Please enter Speed of the vehicle in mph:");//asks for the speed at which the vehicle was going
		Scanner speed = new Scanner(System.in);
		double spd = speed.nextDouble();
		
		System.out.println("State [Y,y] for Construction or School Zone \nState [N,n] for Regular Zone:");//asks to say yes or no if there was a special zone or a regular zone
		Scanner zone = new Scanner(System.in);
		char zoneType = zone.next().charAt(0);//the char function is used to get the characters [Y,y,N,n]
		
		boolean cOrSZone = false;//boolean that if == true, means there was a special zone
		boolean overLimt = false;//boolean that if == true, means that the car was speeding
		
		//condition for determining if there was a special zone or no
		if(zoneType == 'Y' || zoneType == 'y')//condition needed to be met for it to == true
			cOrSZone = true;
		else if(zoneType == 'N' || zoneType == 'n')
			cOrSZone = false;
		
		//condition for determining if car is speeding
		if(spd > spdLimt)
			overLimt = true;
		else
			overLimt = false;
		
		//prices for the tickets
		double ticketA = 119.00;
		double ticketB = 169.00;
		double ticketC = 219.00;
		double ticketD = 289.00;
	
		
		if(overLimt == true) {//if the car was speading
			double spdDiff = spd - spdLimt;//finds the difference to determine how much was the car over the limit or under the limit
			if(cOrSZone == true) {//if both, car is speeding and in a special zone
				if(spdDiff < 10) {
					ticketA *= 2;//the tickets get doubled
					System.out.println("Your ticket is $" + ticketA);
					System.out.println("Slow Down. !");
				}
				else if(spdDiff >= 10 && spdDiff < 15) {
					ticketB *= 2;
					System.out.println("Your ticket is $" + ticketB);
					System.out.println("Drive with caution. !");
				}
				else if(spdDiff >= 15 && spdDiff < 20) {
					ticketC *= 2;
					System.out.println("Your ticket is $" + ticketC);
					System.out.println("You are over speeding. !");
				}
				else if(spdDiff >= 20 && spdDiff < 30) {
					ticketD *= 2;
					System.out.println("Your ticket is $" + ticketD);
					System.out.println("You are in Danger zone. !");
				}
				else if(spdDiff > 30) {
					System.out.println("See ya in court. !!");
				}
			}else if(cOrSZone == false) {//if the car was speeding but in a regular zone
				if(spdDiff < 10) {
					ticketA = 119.00;
					System.out.println("Your ticket is $" + ticketA);
					System.out.println("Slow Down. !");
				}
				else if(spdDiff >= 10 && spdDiff < 15) {
					ticketB = 169.00;
					System.out.println("Your ticket is $" + ticketB);
					System.out.println("Drive with caution. !");
				}
				else if(spdDiff >= 15 && spdDiff < 20) {
					ticketC = 219.00;
					System.out.println("Your ticket is $" + ticketC);
					System.out.println("You are over speeding. !");
				}
				else if(spdDiff >= 20 && spdDiff < 30) {
					ticketD = 289.00;
					System.out.println("Your ticket is $" + ticketD);
					System.out.println("You are in Danger zone. !");
				}
				else if(spdDiff > 30)
					System.out.println("See ya in court. !!");
			}
			}else {
			System.out.println("You are at the speed limit");//if the car was at the speed limit
		}
		
		System.out.println("Goodbye!!");//final string 
		
		
		
		
		
		
	
		
		
		
	}

}
