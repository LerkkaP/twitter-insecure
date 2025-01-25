document.addEventListener('DOMContentLoaded', () => {
    const textarea = document.getElementById('post-textarea');

    function adjustTextareaHeight() {
        textarea.style.height = 'auto';
        textarea.style.height = textarea.scrollHeight + 'px';
    }

    textarea.addEventListener('input', adjustTextareaHeight);

    adjustTextareaHeight();
});
