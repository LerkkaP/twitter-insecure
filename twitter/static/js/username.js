document.addEventListener('DOMContentLoaded', () => {
    const usernames = document.querySelectorAll('.username');

    usernames.forEach(username => {
        username.addEventListener('click', function(event) {
            event.preventDefault();

            const userId = this.getAttribute('data-user-id');

            window.location.href = `/profile/${userId}`;
        });
    });
});