document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("comment").addEventListener("keydown", function (event) {
        if (event.keyCode === 13 && !event.shiftKey) {
            event.preventDefault();
            document.getElementById("taskForm").submit();
        }
    });

    // Add event listener to all color picker input elements
    var colorPickers = document.querySelectorAll('input[type="color"]')
    colorPickers.forEach(function (colorPicker) {
        colorPicker.addEventListener('input', function (event) {
            console.log("Color picked:", this.value); // Debugging statement
            // When the color is picked, automatically submit the form
            this.form.submit();
        });
    });

    var checkboxClicked = document.querySelectorAll('input[type="checkbox"]')
    checkboxClicked.forEach(function (checkbox) {
        checkbox.addEventListener('input', function (event) {
            this.form.submit()
        });

    });

    var datePickers = document.querySelectorAll('input[type="text"]')
    datePickers.forEach(function (datePicker) {
        datePicker.addEventListener('input', function (event) {
            this.form.submit()
        });
    });
});




function showColorPicker(element) {
    element.querySelector('.delete-btn').style.display = 'block';
    element.querySelector('.color-picker').style.display = 'block';
}

function hideColorPicker(element) {
    element.querySelector('.delete-btn').style.display = 'none';
    element.querySelector('.color-picker').style.display = 'none';
}

// document.getElementById('colorPicker').addEventListener('input', function (event) {
//     // When the color is picked, automatically submit the form
//     this.form.submit();
// });