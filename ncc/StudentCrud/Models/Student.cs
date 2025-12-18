namespace StudentCrud.Models
{
    public class Student
    {
        public int Id { get; set; }
        public required string FirstName { get; set; }
        public required string LastName { get; set; }
        public string Email { get; set; }
        public DateTime EnrollmentDate { get; set; } = DateTime.Now;
    }
}
