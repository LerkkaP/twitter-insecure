document.addEventListener('DOMContentLoaded', function () {
    const signupModal = document.getElementById('signupModal');
    const loginModal = document.getElementById('loginModal');
    const openSignup = document.getElementById('openSignup');
    const openLogin = document.getElementById('openLogin');
    const closeSignup = document.getElementById('closeSignup');
    const closeLogin = document.getElementById('closeLogin');
  
    openSignup.addEventListener('click', function () {
      signupModal.style.display = 'flex';
    });
  
    openLogin.addEventListener('click', function () {
      loginModal.style.display = 'flex';
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

    switchToSignup.addEventListener('click', function (event) { 
      event.preventDefault();
      loginModal.style.display = 'none';
      signupModal.style.display = 'flex';
    });

    switchToSignIn.addEventListener('click', function (event) { 
      event.preventDefault(); 
      loginModal.style.display = 'flex';
      signupModal.style.display = 'none';
    });
  });
  