document.addEventListener("DOMContentLoaded", function () {
    const coursesTableBody = document.querySelector("#courses-table tbody");

    fetch("/api/courses/")
        .then(response => response.json())
        .then(data => {
            data.courses.forEach(course => {
                const row = `<tr>
                    <td>${course.id}</td>
                    <td>${course.name}</td>
                </tr>`;
                coursesTableBody.innerHTML += row;
            });
        });
});

