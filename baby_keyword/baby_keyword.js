<<<<<<< HEAD
document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.keywords button');

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            button.classList.toggle('selected');
        });
    });

    const completeBtn = document.getElementById('complete-btn');
    completeBtn.addEventListener('click', function () {
        window.location.href = '../me_keyword/me_keyword.html';
=======
document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".keywords button");
    const completeBtn = document.getElementById("complete-btn");
    const warningMessage = document.getElementById("warning-message");
    let selectedKeywords = [];

    buttons.forEach(button => {
        button.addEventListener("click", function() {
            if (selectedKeywords.includes(this.textContent)) {
                this.style.backgroundColor = "";
                this.style.color = "#8B4513";
                selectedKeywords = selectedKeywords.filter(keyword => keyword !== this.textContent);
            } else {
                this.style.backgroundColor = "#FFD700";
                this.style.color = "white";
                selectedKeywords.push(this.textContent);
            }
        });
    });

    completeBtn.addEventListener("click", function() {
        if (selectedKeywords.length === 0) {
            warningMessage.style.display = "block";
        } else {
            warningMessage.style.display = "none";
            window.location.href = "loading.html";
        }
>>>>>>> 6deec216c17cf4dd52160539da0fd8eb5eb16fbe
    });
});
