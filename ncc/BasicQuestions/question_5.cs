namespace BasicQuestions
{
    public class ExceptionHandling
    {
        public static void Demo()
        {
            Console.WriteLine("Saugat Rijal (79010255)\n");

            try
            {
                Console.Write("Enter product price: ");
                double price = Convert.ToDouble(Console.ReadLine());
                Console.WriteLine($"You entered price: {price}");
            }
            catch (FormatException)
            {
                Console.WriteLine("Invalid Input: Only Numbers are allowed for price!");
            }
        }
    }
}
