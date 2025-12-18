using Microsoft.AspNetCore.Mvc;
using ValidatePlayer.Models;

namespace ValidatePlayer.Controllers
{
    public class PlayerController : Controller
    {
        [HttpGet]
        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Create(Player player)
        {
            ViewData["Error"] = "";

            if (!ModelState.IsValid)
            {
                ViewData["Error"] = "Invalid Information: Player couldn't be registered.";
            }

            return View(player);
        }
    }
}
