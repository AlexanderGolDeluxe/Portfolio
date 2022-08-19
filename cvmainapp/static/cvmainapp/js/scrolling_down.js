const firstScreenBlock = document.querySelector(".first-screen-wrapper");


function scroll_down() {
    window.scroll({
        top: firstScreenBlock.scrollHeight,
        behavior: "smooth"
    })
}