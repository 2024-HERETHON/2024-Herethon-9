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
    });
});
