using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using Microsoft.EntityFrameworkCore;
using StudentCrud.Models;

namespace StudentCrud.Controllers;

public class StudentController : Controller
{
    private readonly ApplicationDbContext _context;

    public StudentController(ApplicationDbContext context)
    {
        _context = context;
    }

    public IActionResult Index()
    {
        return View();
    }

    // Read
    [HttpGet]
    public async Task<ActionResult<IEnumerable<Student>>> Get()
    {
        var students = await _context.Students.ToListAsync();
        return View(students);
    }

    [HttpGet]
    public IActionResult Create()
    {
        return View();
    }

    // Create
    [HttpPost]
    public async Task<IActionResult> Create(Student student)
    {
        if (ModelState.IsValid)
        {

            _context.Add(student);
            await _context.SaveChangesAsync();
            // return to index if student submitted
        }
        return RedirectToAction(nameof(Get));
    }

    [HttpGet]
    public async Task<IActionResult> Update(int? id)
    {
        if (id == null)
        {
            return NotFound();
        }

        var student = await _context.Students.FindAsync(id);

        if (student == null)
        {
            return NotFound();
        }

        return View(student);
    }

    // Update
    [HttpPost]
    public async Task<IActionResult> Update(int id, Student student)
    {
        if (id != student.Id) return NotFound();

        if (ModelState.IsValid)
        {
            try
            {
                _context.Students.Update(student);
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!StudentExists(student.Id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }
            return RedirectToAction(nameof(Get));
        }

        return RedirectToAction(nameof(Get));
    }

    [HttpPost]
    public async Task<IActionResult> Delete(int id)
    {
        var student = await _context.Students.FindAsync(id);
        if (student != null)
        {
            _context.Students.Remove(student);
        }

        await _context.SaveChangesAsync();

        return RedirectToAction(nameof(Get));
    }


    private bool StudentExists(int id)
    {
        return _context.Students.Any(e => e.Id == id);
    }
}
