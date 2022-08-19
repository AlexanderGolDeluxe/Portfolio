function show_more(element) {
    let isEngText = element.textContent.startsWith("Show")
    let needToShowMore = (
        element.textContent == "Посмотреть всё" ||
        element.textContent == "Show more"
    );
    document.querySelectorAll(".js-show-more").forEach(
        item => item.hidden = !needToShowMore
    );
    if (needToShowMore) {
        if (isEngText) element.textContent = "Show less";
        else element.textContent = "Показать меньше";
    }
    else {
        if (isEngText) element.textContent = "Show more";
        else element.textContent = "Посмотреть всё";
    }
}