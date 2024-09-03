// Function to save form data to local storage
function saveFormData(form, index) {
    const formData = new FormData(form);
    const formObject = {};
    formData.forEach((value, key) => {
        formObject[key] = value;
    });
    localStorage.setItem(`character_form_${index}`, JSON.stringify(formObject));
}

// Function to load form data from local storage
function loadFormData() {
    const forms = document.querySelectorAll('.card-body form');
    forms.forEach((form, index) => {
        const storedData = localStorage.getItem(`character_form_${index}`);
        if (storedData) {
            const formObject = JSON.parse(storedData);
            Object.keys(formObject).forEach(key => {
                const input = form.querySelector(`[name="${key}"]`);
                if (input) input.value = formObject[key];
            });
        }
    });
}

// Function to clear form data
function clearFormData(index) {
    localStorage.removeItem(`character_form_${index}`);
}

// Add event listeners to all input fields
document.querySelectorAll('.card-body form').forEach((form, index) => {
    form.querySelectorAll('input, textarea, select').forEach(input => {
        input.addEventListener('input', () => saveFormData(form, index));
    });

    // Clear form data on submission
    form.addEventListener('submit', () => {
        // Clear the form data from local storage
        clearFormData(index);
        // The form will submit normally
    });
});

// Load form data when the page loads
document.addEventListener('DOMContentLoaded', loadFormData);

// Clear submitted form data after page load if there's a success message
document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const submitted = urlParams.get('submitted');
    if (submitted) {
        const index = parseInt(submitted) - 1; // Assuming character numbers start from 1
        clearFormData(index);
        // Clear the form fields
        const form = document.querySelectorAll('.card-body form')[index];
        if (form) {
            form.reset();
        }
    }
});