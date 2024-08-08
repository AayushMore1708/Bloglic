document.addEventListener('DOMContentLoaded', function () {
    const addButton = document.getElementById('add-comment-button');
    if (addButton) {
        addButton.addEventListener('click', function () {
            const form = document.getElementById('add-comment-form');
            if (form) {
                if (form.style.display === 'none') {
                    form.style.display = 'block';
                } else {
                    form.style.display = 'none';
                }
            }
        });
    }
});