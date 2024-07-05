
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('file-upload');
    const postText = document.querySelector('.post-text');
    const shareBtn = document.querySelector('.share-btn');

    if (!fileInput || !postText || !shareBtn) {
        console.error('필수 요소를 찾을 수 없습니다.');
        return;
    }
});

// 뒤로 가기 버튼
document.querySelector('.back-btn').addEventListener('click', function() {
    window.history.back();
});