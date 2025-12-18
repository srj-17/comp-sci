var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();

var app = builder.Build();

app.MapControllerRoute(
    name: "default",
    pattern: "api/{controller=Products}/{action=GetAll}/{id?}")
    .WithStaticAssets();

app.Run();
