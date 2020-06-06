$(document).ready( function () {
    if(screen.width<600) {
        // row = document.getElementByClass("row");
        els = $(".col.s4");
        els.each(function () {
            $(this).attr("class", "col s12");
            // new_html = "<div class='row'><div class=" + el.innerHTML
            // new_html = "<div class='col s12'>" + el.innerHTML + "</div>";
        });
        row_el = $(".row");
        html = row_el.innerHTML;
        row_el.html(html);
    }
});
