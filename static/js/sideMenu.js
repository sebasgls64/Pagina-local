document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.getElementById("sidebar");
    const logoArea = document.querySelector(".logo-area");

    logoArea.addEventListener("click", () => {
        sidebar.classList.toggle("collapsed");
    });
});
