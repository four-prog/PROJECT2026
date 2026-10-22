let time = 5;
const timer = document.getElementById("timer");

if (!timer) {
    console.log("timer not found");
} else {
    const x = setInterval(() => {
        time--;
        timer.textContent = time;

        if (time <= 0) {
            clearInterval(x);
            window.location.href = "/home";
        }
    }, 1000);
}