document.addEventListener('DOMContentLoaded', function () {
  const loginModal = document.getElementById('loginModal');
  const openLogin = document.getElementById('openLogin');
  const closeLogin = document.getElementById('closeLogin');
  const errorMessages = document.querySelectorAll('.alert');

  if (errorMessages.length > 0) {
    loginModal.style.display = 'flex'; 
  }

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