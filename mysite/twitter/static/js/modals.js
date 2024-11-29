document.addEventListener('DOMContentLoaded', function () {
  const loginModal = document.getElementById('loginModal');
  const openLogin = document.getElementById('openLogin');
  const closeLogin = document.getElementById('closeLogin');

  openLogin.addEventListener('click', function () {
    loginModal.style.display = 'flex';
  });

  closeLogin.addEventListener('click', function () {
    loginModal.style.display = 'none';
  });

  window.addEventListener('click', function (event) {
    if (event.target == loginModal) {
      loginModal.style.display = 'none';
    }
  });
});
