using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

public class HomeController : Controller
{
    // Public
    public IActionResult Index()
    {
        return View();
    }

    // Protected: Authentication required (login required)
    [Authorize]
    public IActionResult UserDashboard()
    {
        return View(User.Identity);
    }

    // Restricted: Only Admins
    [Authorize(Roles = "Admin")]
    public IActionResult AdminPanel()
    {
        return View();
    }
}
