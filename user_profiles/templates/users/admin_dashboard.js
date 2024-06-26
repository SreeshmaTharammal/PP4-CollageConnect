// static/users/js/admin_dashboard.js
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("add-student-form").addEventListener("submit", function (event) {
        event.preventDefault();
        const username = document.getElementById("student-username").value;
        const password = document.getElementById("student-password").value;
        const address = document.getElementById("student-address").value;

        fetch("/api/admin/add_student/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({
                username: username,
                password: password,
                address: address
            })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                alert("Student added successfully!");
            } else {
                alert("Error adding student: " + data.error);
            }
        });
    });

    document.getElementById("add-instructor-form").addEventListener("submit", function (event) {
        event.preventDefault();
        const username = document.getElementById("instructor-username").value;
        const password = document.getElementById("instructor-password").value;
        const department = document.getElementById("instructor-department").value;
        const address = document.getElementById("instructor-address").value;

        fetch("/api/admin/add_instructor/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({
                username: username,
                password: password,
                department: department,
                address: address
            })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                alert("Instructor added successfully!");
            } else {
                alert("Error adding instructor: " + data.error);
            }
        });
    });

    document.getElementById("add-course-form").addEventListener("submit", function (event) {
        event.preventDefault();
        const name = document.getElementById("course-name").value;

        fetch("/api/admin/add_course/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({
                name: name
            })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                alert("Course added successfully!");
            } else {
                alert("Error adding course: " + data.error);
            }
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
