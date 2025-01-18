document.addEventListener("DOMContentLoaded", function() {
    const products = document.querySelectorAll("li");
    if (products.length > 0) {
        products.forEach((product, index) => {
            // Adiciona um evento de hover para destacar o produto
            product.addEventListener("mouseenter", () => {
                product.style.backgroundColor = "#e0f7fa";
                product.style.transform = "scale(1.02)";
                product.style.transition = "all 0.2s ease-in-out";
            });

            product.addEventListener("mouseleave", () => {
                product.style.backgroundColor = "#fff";
                product.style.transform = "scale(1)";
            });
        });
    }
});
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    // Mensagem de confirmação ao tentar sair sem salvar
    let formModified = false;
    form.addEventListener("input", () => {
        formModified = true;
    });

    window.addEventListener("beforeunload", (event) => {
        if (formModified) {
            event.preventDefault();
            event.returnValue = "Você tem alterações não salvas. Deseja sair mesmo assim?";
        }
    });

    // Notificação ao salvar alterações
    form.addEventListener("submit", (event) => {
        alert("Alterações salvas com sucesso!");
    });
});