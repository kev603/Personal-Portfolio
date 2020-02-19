import java.util.Scanner;
public class twoDigitLotteryStr {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		System.out.println("Welcome to Two-Digit lottery program");
		
		System.out.println("Enter a two-digit number");
		
		Scanner input = new Scanner(System.in);//scanner for an input 
		
		String guessNumStr = input.nextLine();//the user's input number
		
		boolean validGuess = false;//boolean variable that == true if the user inputs a number of 2 digits
		
		int inNumLen = guessNumStr.length();//finds the length of the input string
		
		
		if(inNumLen < 2 || inNumLen > 2)
			validGuess = false;
		else if(inNumLen == 2)//length must == 2 in order to be valid
			validGuess = true;
		
		if(validGuess == true)//if the number is valid
		{
			double lotRand = Math.random();//method for finding a random number between 0-1
			
			int lotNum = (int)(lotRand* 90 + 10.0);//then the number is passed through a formula to make it from 0-100
			
			//converting the random lottery number to a string
			String lotNumStr = String.valueOf(lotNum);
			
			String lotX = lotNumStr.substring(0,1);//gives the first digit of the string lottery number
			String lotY = lotNumStr.substring(1);//gives the second digit of the string lottery number
			String guessX = guessNumStr.substring(0,1);//1st digit of the user's number
			String guessY = guessNumStr.substring(1);//2nd digit of the user's number
			
		if(guessNumStr.equals(lotNumStr)) {//perfect match
			System.out.println("You won $10,000!!!");
		}
		
		else if(lotX.equals(guessY) && lotY.equals(guessX)) {
			System.out.println("You mathched the nombers in the wrong order \n"
					+ "You won $3,000!!!");
		}
		else if((lotX.equals(guessX)) || (lotX.equals(guessY)) || (lotY.equals(guessX)) || (lotY.equals(guessY)))
		{
			System.out.println("You matched at least one of the digits \n"
					+ "You Won $1,000!!!");
		}
		else
		{
			System.out.println("You did not matched any number \n"
					+ "You lost.");
		}
		}
		else
			System.out.println("Invalid input.");//if the number is invalid
			
		
		
		
	}

}
