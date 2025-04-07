document.addEventListener('click', (e) => {
    const collapsibleTitle = e.target.closest("[data-collapsible]");

    if (collapsibleTitle) {
        const content = collapsibleTitle.nextElementSibling;
        const arrow = collapsibleTitle.querySelector('.arrow');
        
        content.style.display = content.style.display === "block" ? "none" : "block";
        arrow.textContent = arrow.textContent === "▼" ? "▲" : "▼";
    }
});
