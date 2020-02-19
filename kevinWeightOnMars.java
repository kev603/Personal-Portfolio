/* This program gets the user input weight and the 
 * converts it into the equivalent weight on Mars
 * in order to do so it uses the following formula
 * Weight on the Mars = Weight on Earth / 9.81 * 3.711
 */

import java.util.Scanner;//imports Scanner from java.util so we can use user input

public class kevinWeightOnMars {

	public static void main(String[] args) {
	
		//this is the greeting string
		System.out.println("Welcome to Program that tells the weight on Mars");

		//this is the string that asks the user what to input
		System.out.println("Now please enter the weight in pounds you wish to convert");
		
		Scanner input = new Scanner(System.in);//it uses scanner to create an input variable

		double wghtEarth = input.nextDouble();//here is creating a second variable with the value of the scanner input 
		//here the final answer is converted to an integer so it can be rounded
		int wghtMars = (int)( wghtEarth / 9.81 * 3.711);//this is the variable that gets the calculated weight on Mars
												//after using the given formula to do so	
		//this is the final string that tells the user the converted equivalent weight on Mars
		System.out.println("The equivalent weight on Mars is " + wghtMars + "Lbs");

	}

}
