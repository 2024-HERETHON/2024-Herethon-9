document.addEventListener('DOMContentLoaded', function () {
    const keywordButtons = document.querySelectorAll('.keywords button');
    const completeButton = document.getElementById('complete-btn');

    keywordButtons.forEach(button => {
        button.addEventListener('click', function () {
            this.classList.toggle('selected');
        });
    });

    completeButton.addEventListener('click', function () {
        window.location.href = '../home.html';
    });
});
