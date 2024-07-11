document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", event => {
            // Previne o comportamento padrão do formulário
            event.preventDefault();
            
            // Exemplo de validação simples
            const nome = form.querySelector("[name='nome']").value;
            if (nome.trim() === "") {
                alert("O campo 'nome' é obrigatório.");
                return;
            }

            // Se a validação passar, enviar o formulário
            form.submit();
        });
    });
});
