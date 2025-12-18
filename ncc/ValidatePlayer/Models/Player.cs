using System.ComponentModel.DataAnnotations;

namespace ValidatePlayer.Models
{
    public class Player
    {
        public int Id { get; set; }

        [Required(ErrorMessage = "First name cannot be null.")]
        [StringLength(
                15,
                ErrorMessage = "First Name must have length more than 5 and less than 15",
                MinimumLength = 5
        )]
        public string FirstName { get; set; }

        [Required(ErrorMessage = "Last name cannot be null.")]
        public string LastName { get; set; }

        [EmailAddress(ErrorMessage = "Not a valid email address")]
        public string Email { get; set; }

        [MaxLength(15, ErrorMessage = "Maximum length for team name is 15")]
        public string Team { get; set; }
    }
}
