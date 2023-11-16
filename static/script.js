function typeEffect(element, text, speed) {
    element.innerHTML = text.charAt(0)
    let i = 1;
    let interval = setInterval(function() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
        } else {
            clearInterval(interval);
        }
    }, speed);
}

function getRandomWord() {
    let outputElement = document.getElementById('output');
    outputElement.innerHTML = ""; // Clear any previous text

    fetch('/get_random_word')
        .then(response => response.text())
        .then(word => {
            typeEffect(outputElement, "Random Word: " + word, 50);
        });
}

function getSpookyFact(){
    let outputElement = document.getElementById('output');
    outputElement.innerHTML = ""; // Clear any previous text

    fetch('/get_spooky_fact')
        .then(response => response.text())
        .then(word => {
            typeEffect(outputElement, word, 50);
        });
}

function getDeath(){
    let outputElement = document.getElementById('output');
    outputElement.innerHTML = ""; // Clear any previous text

    fetch('/get_death')
        .then(response => response.text())
        .then(word => {
            typeEffect(outputElement, word, 50);
        });
}