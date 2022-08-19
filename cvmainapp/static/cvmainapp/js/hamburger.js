const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".site-navigation");

document.querySelectorAll(".nav-item-link, .link-change-lang").forEach(
    n => n.addEventListener("click", () => {
        navMenu.classList.remove("show");
        hamburger.classList.remove("is-active");
    })
)


function show_nav_menu(element) {
    navMenu.classList.toggle("show");
    element.classList.toggle("is-active");
}
