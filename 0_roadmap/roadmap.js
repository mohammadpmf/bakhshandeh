function myFunction(text) {
    navigator.clipboard.writeText(text);
    var tooltip = document.getElementById(text);
    tooltip.innerHTML = `${text} کپی شد.`;
}
  

function outFunc(text) {
    var tooltip = document.getElementById(text);
    tooltip.innerHTML = "برای کپی کردن کلیک کنید";
}