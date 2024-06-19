document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("loginForm").addEventListener("submit", function(event) {
        var username = document.querySelector('input[name="username"]').value;
        var password = document.querySelector('input[name="password"]').value;
        if (!username || !password) {
            event.preventDefault();
            alert("Please fill in both fields.");
        }
    });

    document.getElementById("signupForm").addEventListener("submit", function(event) {
        var username = document.querySelector('input[name="username"]').value;
        var password1 = document.querySelector('input[name="password1"]').value;
        var password2 = document.querySelector('input[name="password2"]').value;
        var email = document.querySelector('input[name="email"]').value;
        if (!username || !password1 || !password2 || !email) {
            event.preventDefault();
            alert("Please fill in all fields.");
        }
        if (password1 !== password2) {
            event.preventDefault();
            alert("Passwords do not match.");
        }
        const form = new FormData(event.target);
        fetch('{% url "signup" %}', {
            method: 'POST',
            body: form,
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = '{% url "employee_dashboard" %}';
            } else {
                alert('Invalid form data. Please check the form and try again.');
            }
        });
    });
});