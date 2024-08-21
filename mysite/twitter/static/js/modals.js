document.addEventListener('DOMContentLoaded', function () {
    const signupModal = document.getElementById('signupModal');
    const loginModal = document.getElementById('loginModal');
    const openSignup = document.getElementById('openSignup');
    const openLogin = document.getElementById('openLogin');
    const closeSignup = document.getElementById('closeSignup');
    const closeLogin = document.getElementById('closeLogin');
  
    openSignup.addEventListener('click', function () {
      signupModal.style.display = 'block';
    });
  
    openLogin.addEventListener('click', function () {
      loginModal.style.display = 'block';
    });
  
    closeSignup.addEventListener('click', function () {
      signupModal.style.display = 'none';
    });
  
    closeLogin.addEventListener('click', function () {
      loginModal.style.display = 'none';
    });
  
    window.addEventListener('click', function (event) {
      if (event.target == signupModal) {
        signupModal.style.display = 'none';
      } else if (event.target == loginModal) {
        loginModal.style.display = 'none';
      }
    });
  });
  