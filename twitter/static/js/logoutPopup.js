document.addEventListener('DOMContentLoaded', function () {
    function togglePopup(event) {
      event.stopPropagation();
      var popup = document.getElementById('logoutPopup');
      popup.style.display = (popup.style.display === 'block') ? 'none' : 'block';
    }
  
    window.onclick = function (event) {
      var popup = document.getElementById('logoutPopup');
      if (popup.style.display === 'block' && !event.target.closest('.navigation__user')) {
        popup.style.display = 'none';
      }
    };
  
    var navigationUser = document.querySelector('.navigation__user');
    if (navigationUser) {
      navigationUser.addEventListener('click', togglePopup);
    }
  });
  