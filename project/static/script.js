function clearCheckboxes() {
    const checkboxes = document.querySelectorAll('.student-check');

    checkboxes.forEach((checkbox) => {
        checkbox.checked = false;
    });
}
function showLoading(){

    // Show full-screen loader
    document.getElementById("loading-screen").style.display = "flex";

    // Simulate loading for 3 seconds
    setTimeout(function(){

        // Redirect to another page
        window.location.href = "";

        // OR hide the loader instead:
        // document.getElementById("loading-screen").style.display = "none";

    },3000);
}