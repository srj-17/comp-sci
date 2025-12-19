using System.Linq;

class Voter
{
    public string Name { get; set; }
    public int Age { get; set; }
    public string Address { get; set; }
}

namespace BasicQuestions
{

    public class LinqExample
    {
        private static readonly List<Voter> _voters = new List<Voter> {
            new Voter{Name="Sita", Age=20, Address="Patan"},
            new Voter{Name="Gita", Age=16, Address="Patan"},
            new Voter{Name="Ram", Age=22, Address="Kathmandu"},
            new Voter{Name="Hari", Age=25, Address="Patan"}
        };

        public static void Demo()
        {
            Console.WriteLine("Saugat Rijal (79010255)\n");

            var result = from v in _voters
                         where v.Age > 18 && v.Address == "Patan"
                         select v.Name;

            Console.WriteLine("Eligible voters in Patan:");
            foreach (var name in result)
            {
                Console.WriteLine(name);
            }
        }
    }
}
