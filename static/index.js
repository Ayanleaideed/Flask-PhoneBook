// JavaScript for filtering the table based on user input
const searchInput = document.getElementById("searchInput");
const table = document.querySelector("table");
const rows = table.getElementsByTagName("tr");

searchInput.addEventListener("input", function () {
    const searchTerm = searchInput.value.toLowerCase();

    for (let i = 1; i < rows.length; i++) {
        const row = rows[i];
        const nameCell = row.getElementsByTagName("td")[0];
        const phoneCell = row.getElementsByTagName("td")[1];

        const name = nameCell.textContent.toLowerCase();
        const phone = phoneCell.textContent.toLowerCase();

        if (name.includes(searchTerm) || phone.includes(searchTerm)) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    }
});
