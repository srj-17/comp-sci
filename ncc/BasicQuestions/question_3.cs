using System.Linq;

class Student
{
    public int Id { get; set; }
    public int DepartmentId { get; set; }
    public string Name { get; set; }
    public string Address { get; set; }
}

namespace BasicQuestions
{
    public class LambdaExpressionExample
    {
        private static readonly List<Student> _students = new List<Student> {
            new Student{Id=1, DepartmentId=101, Name="Sita", Address="Kathmandu"},
            new Student{Id=2, DepartmentId=102, Name="Gita", Address="Patan"},
            new Student{Id=3, DepartmentId=101, Name="Ram", Address="Bhaktapur"},
            new Student{Id=4, DepartmentId=103, Name="Hari", Address="Lalitpur"}
        };

        public static void Demo()
        {
            Console.WriteLine("Saugat Rijal (79010255)\n");
            Console.WriteLine("Enter Department Id to filter: ");
            int deptId = Convert.ToInt32(Console.ReadLine());

            var filtered = _students.Where(s => s.DepartmentId == deptId);

            Console.WriteLine("\nFiltered Students:");
            foreach (var s in filtered)
            {
                Console.WriteLine($"{s.Id} {s.Name} {s.Address}");
            }

        }
    }
}
