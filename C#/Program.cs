using System;
using System.Collections.Generic;

namespace C_
{
    // Main Class
    class Program
    {
        // This is where program runs
        static void Main(string[] args)
        {

        // Variables: DataType variableName = value;
            String name = "Vilius";
            int year = 2022;
            byte b = 255;
            double doubleNum = 1.20;
            float floatNum = 9.99F;
            bool allowed = true;
            char c = 'c';
            // Constant values
            const String lastDayOfWeek = "Sunday";

            // String Operation
            /*
            Length	A property that returns the length of the string.
            Compare()	A static method that compares two strings.
            Contains()	Determines if the string contains a specific substring.
            Equals()	Determines if the two strings have the same character data.
            Format()	Formats a string via the {0} notation and by using other primitives.
            Trim()	Removes all instances of specific characters from trailing and leading characters. Defaults to removing leading and trailing spaces.
            Split()	Removes the provided character and creates an array out of the remaining characters on either side.
            */
        
        // Collections
                //Arrays
                char[] chars = new char[10];
                chars[0] = 'a';
                chars[1] = 'b';
                string[] letters = {"A", "B", "C"};
                int[] mylist = {100, 200};
                bool[] answers = {true, false};
                
                //List
                /// requires library:  System.Collections.Generic
                List<string> names = new List<string>();
                List<Object> someObjects = new List<Object>();

            // Conditional Statements
                //If else
                if (year < 1990) {
                    Console.WriteLine("Less than 1990");
                } else if (year > 1990) {
                    Console.WriteLine("More than 1990");
                } else {
                    Console.WriteLine("It's 1990");
                }
                
                //Switch statement
                switch ("blue") {
                    case "red":
                        Console.WriteLine("I don't like that color.");
                        break;
                    case "blue":
                        Console.WriteLine("I like that color.");
                        break;
                    default:
                        Console.WriteLine("I feel ambivalent about that color.");
                        break;
                }

            // Loops
                int[] numbers = {1, 2, 3, 4, 5};

                for(int i = 0; i < numbers.Length; i++) {
                    Console.WriteLine(numbers[i]);
                }

                foreach(int num in numbers) {
                    Console.WriteLine(num);
                }
                while(true){
                    // Do somthing
                }
        
            // Functions/Methods: (const/static) DataTypeToReturn FunctionName(DataType param1, DataType param2) {Code}
                void Study(int param1, string param2){
    
                }
            
            // Classes & Objects
            /*
                class Car
                {
                string color = "red";
                    static void Main(string[] args)
                    {
                        Car myObj1 = new Car();
                        Car myObj2 = new Car();
                        Console.WriteLine(myObj1.color);
                        Console.WriteLine(myObj2.color);
                    }
                }
            */

            // Interface
                /*
                interface IAnimal 
                {
                    void animalSound(); 
                }

                class Dog : IAnimal 
                {
                    public void animalSound() 
                    {
                        Console.WriteLine("The dog says: woof woof");
                    }
                }
                */

            // Inheritance
                /*
                public class X
                {
                    public void GetDetails()
                    {
                        // Method implementation
                    }
                }
                public class Y : X
                {
                    // your class implementation
                }
                */
            // Exceptions
                try {
                // statements causing exception
                } catch( System.IndexOutOfRangeException e1 ) {
                /*
                Exception Classes
                System.IO.IOException	Handles I/O errors.
                System.IndexOutOfRangeException	Handles errors generated when a method refers to an array index out of range.
                System.ArrayTypeMismatchException	Handles errors generated when the type is mismatched with the array type.
                System.NullReferenceException	Handles errors generated from referencing a null object.
                System.DivideByZeroException	Handles errors generated from dividing a dividend with zero.
                System.InvalidCastException	Handles errors generated during typecasting.
                System.OutOfMemoryException	Handles errors generated from insufficient free memory.
                System.StackOverflowExcept
                */
                } 


        }
    }
}



