function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = 0;
            var content = document.getElementById("content")
            content.readOnly = true;
            var button = document.getElementById('check');
            button.form.submit();
        }
    }, 1000);
}

function start_timer() {
    var oneMinute = 60 * 1;
    display = document.querySelector('#time');
    startTimer(oneMinute, display);
    var content = document.getElementById('content');
    content.removeAttribute('readonly');
    content.focus();
    var result = document.getElementById('div-result');
    result.setAttribute("class", "invisible")    
};