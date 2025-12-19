class Animal
{
    public virtual void Sound()
    {
        Console.WriteLine("Animal makes a sound");
    }
}

class Dog : Animal
{
    public override void Sound()
    {
        Console.WriteLine("Dog barks");
    }
}

class Cat : Animal
{
    public override void Sound()
    {
        Console.WriteLine("Cat meows");
    }
}

namespace BasicQuestions
{
    public class Polymorphism
    {
        public static void Demo()
        {
            Console.WriteLine("Saugat Rijal (79010255)\n");

            Animal a = new Dog();
            a.Sound();

            a = new Cat();
            a.Sound();
        }
    }

}
