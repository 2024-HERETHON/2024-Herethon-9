document.addEventListener("DOMContentLoaded", function () {
  var wave = document.getElementById("wave");
  var percentage = document.getElementById("percentage");
  var title = document.getElementById("title");
  var subtitle = document.getElementById("subtitle");
  var percent = 0;

  function incrementPercentage() {
    if (percent <= 100) {
      percentage.innerText = percent + "%";
      wave.style.transform = `translateY(${100 - percent}%)`;

      if (percent === 70) {
        subtitle.innerText = "거의 다 완료 되었어요.";
      }

      if (percent === 100) {
        title.innerHTML = "우리에게 꼭 맞는 제품을<br>찾았어요!";
        subtitle.innerText = "메인페이지로 이동합니다.";
        setTimeout(function () {
          window.location.href = "../home/home.html";
        }, 2000);
      }

      percent++;
      setTimeout(incrementPercentage, 100); // Adjust this value for speed
    }
  }

  incrementPercentage();
});
