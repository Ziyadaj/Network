function darkMode() {
    var element = document.body;
    element.classList.toggle("dark-mode");
    var button = document.querySelector('#button-dark');
    button.src= "static/network/sun.png";
    button.onclick = function() {
        lightMode();
    }
}
function lightMode() {
    var element = document.body;
    element.classList.toggle("dark-mode");
    var button = document.querySelector('#button-dark');
    button.src= "static/network/moon.png";
    button.onclick = function() {
        darkMode();
    }
}