interface IFather
{
    void ShowFather();
}

interface IMother
{
    void ShowMother();
}

class Child : IFather, IMother
{
    public void ShowFather()
    {
        Console.WriteLine("From IFather.");
    }
    public void ShowMother()
    {
        Console.WriteLine("From IMother");
    }
}

namespace BasicQuestions
{
    public class MultipleInheritance
    {
        public static void Demo()
        {
            Console.WriteLine("Saugat Rijal (79010255)\n");

            Child c = new();
            c.ShowFather();
            c.ShowMother();
        }
    }

}
