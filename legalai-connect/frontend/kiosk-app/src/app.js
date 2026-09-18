const problem = document.getElementById("problem");
const result = document.getElementById("result");

document.getElementById("demo").addEventListener("click", () => {
  const text = problem.value.trim();
  if (!text) {
    result.hidden = false;
    result.textContent = "தயவுசெய்து உங்கள் பிரச்சினையை சொல்லுங்கள்.";
    return;
  }

  result.hidden = false;
  result.innerHTML = `
    <strong>முதல் படி</strong><br><br>
    உங்கள் பிரச்சினையை மேலும் புரிந்துகொள்ள சில தகவல்கள் தேவை.
    சம்பவம் நடந்த தேதி, இடம் மற்றும் உங்களிடம் உள்ள ஆதாரங்களைத் தயார் வைத்துக் கொள்ளுங்கள்.
    <br><br>
    <strong>Demo note:</strong> இது ஒரு prototype response. Production பதில் அதிகாரப்பூர்வ ஆதாரங்களிலிருந்து மட்டுமே உருவாக்கப்பட வேண்டும்.
  `;
});

document.getElementById("clear").addEventListener("click", () => {
  problem.value = "";
  result.hidden = true;
});
