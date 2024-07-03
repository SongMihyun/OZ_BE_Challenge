function updateDateTime() {
    const now = new Date();

    // 날짜 구성 요소 추출
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0'); // 월은 0부터 시작하므로 +1
    const day = String(now.getDate()).padStart(2, '0');

    // 시간 구성 요소 추출
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');

    // 날짜와 시간을 "YYYY-MM-DD HH:MM:SS" 형식으로 결합
    const currentDateTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;

    // HTML 요소에 현재 날짜와 시간 설정
    document.getElementById('current-datetime').textContent = currentDateTime;
}

// 페이지가 로드될 때 날짜와 시간을 업데이트하고, 1초마다 업데이트
document.addEventListener('DOMContentLoaded', (event) => {
    updateDateTime();
    setInterval(updateDateTime, 1000);
});


// 다크모드
function toggleTheme() {
    const modal = document.getElementById('exampleModal');
    const currentTheme = modal.getAttribute('data-bs-theme');

    if (currentTheme === 'light') {
      modal.setAttribute('data-bs-theme', 'dark');
    } else {
      modal.setAttribute('data-bs-theme', 'light');
    }
  }


// 회원가입 팝업창

function openJoin() {
    // 새 창을 열 때 사용할 URL
    var url = 'join.html';

    // 새 창 열기 (URL, 창 이름, 창 속성)
    var newWindow = window.open(url, '_blank', 'width=800,height=800');
    
    // 팝업 차단을 우회할 수 없는 경우에 대비한 대체 처리
    if (!newWindow || newWindow.closed || typeof newWindow.closed === 'undefined') {
      alert('팝업 차단 기능이 활성화되어 있을 수 있습니다. 팝업 창을 허용해 주세요.');
    }
  }
