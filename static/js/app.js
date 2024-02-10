document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("comment").addEventListener("keydown", function (event) {
        if (event.keyCode === 13 && !event.shiftKey) {
            event.preventDefault();
            document.getElementById("taskForm").submit();
        }
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

const colorPickerInput = document.querySelector('.color-picker-input');
const checkbox = document.getElementById('flexCheckDefault');
const textInput = document.querySelector('input[type="text"]');

colorPickerInput.addEventListener('input', function () {
    const color = this.value;
    checkbox.style.backgroundColor = color;
    textInput.style.backgroundColor = color;
});