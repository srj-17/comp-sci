using Microsoft.AspNetCore.Mvc;
using SimpleProductApi.Models;


namespace SimpleProductApi.Controllers
{
    public class ProductsController : ControllerBase
    {

        private readonly List<Product> _products = new List<Product>
        {
            new Product { Id = 1, Name = "Laptop", Price = 999.99m },
            new Product { Id = 2, Name = "Mouse", Price = 25.50m },
            new Product { Id = 3, Name = "House", Price = 100000.50m }
        };

        public IActionResult GetAll()
        {
            return Ok(_products);
        }
    }
}
