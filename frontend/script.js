// Espera a página carregar completamente
document.addEventListener("DOMContentLoaded", () => {
  const generateBtn = document.getElementById("generateBtn");
  const passwordField = document.getElementById("password");
  const copyBtn = document.getElementById("copyBtn");

  generateBtn.addEventListener("click", async () => {
    const length = document.getElementById("length").value;
    const upper = document.getElementById("upper").checked;
    const lower = document.getElementById("lower").checked;
    const digits = document.getElementById("digits").checked;
    const symbols = document.getElementById("symbols").checked;

    try {
      // Faz a requisição para o back-end Flask
      const response = await fetch(`http://127.0.0.1:5000/generate?length=${length}&upper=${upper}&lower=${lower}&digits=${digits}&symbols=${symbols}`);
      const data = await response.json();

      // Exibe a senha no campo
      passwordField.textContent = data.password;
    } catch (error) {
      passwordField.textContent = "❌ Erro ao gerar senha. Verifique se o servidor está rodando.";
      console.error("Erro ao chamar API:", error);
    }
  });

  // Copiar senha ao clicar no botão 📋
  copyBtn.addEventListener("click", () => {
    const password = passwordField.textContent;
    if (password && password !== "Clique no botão acima") {
      navigator.clipboard.writeText(password);
      copyBtn.textContent = "✅ Copiado!";
      setTimeout(() => (copyBtn.textContent = "📋 Copiar"), 2000);
    }
  });
});
