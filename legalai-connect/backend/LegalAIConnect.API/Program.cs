var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => Results.Ok(new {
    service = "LegalAI Connect",
    status = "prototype",
    message = "Tamil-first legal information and navigation service"
}));

app.MapPost("/api/guidance", (GuidanceRequest request) =>
{
    var risk = request.Text.Contains("danger", StringComparison.OrdinalIgnoreCase)
        ? "emergency"
        : "guided";

    return Results.Ok(new {
        caseId = "DEMO-" + DateTime.UtcNow.ToString("yyyyMMddHHmmss"),
        language = request.Language ?? "ta-IN",
        risk,
        guidance = "Prototype response. Production responses must be generated from approved legal sources and reviewed according to the safety policy.",
        escalationRecommended = risk != "guided"
    });
});

app.Run();

record GuidanceRequest(string Text, string? Language);
