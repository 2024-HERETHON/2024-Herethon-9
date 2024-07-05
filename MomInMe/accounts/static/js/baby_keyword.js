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

    completeBtn.addEventListener("click", function(event) {
        if (selectedKeywords.length === 0) {
            event.preventDefault();
            warningMessage.style.display = "block";
        } else {
            warningMessage.style.display = "none";
            const form = document.getElementById('keyword-form');
            selectedKeywords.forEach(keyword => {
                const input = document.createElement('input');
                input.type = 'hidden';
                input.name = 'keywords';
                input.value = keyword;
                form.appendChild(input);
            });
        }
    });
});
