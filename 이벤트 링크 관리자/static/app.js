// 간단한 JavaScript 예시
document.addEventListener('DOMContentLoaded', function() {
    // 버튼 클릭 시 처리할 이벤트 핸들러 추가 가능
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function() {
            console.log('Button clicked:', this.innerText);
        });
    });
});