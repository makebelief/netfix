// Form validation
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                } else {
                    field.classList.remove('error');
                }
            });

            if (!isValid) {
                event.preventDefault();
                alert('Please fill in all required fields');
            }
        });
    });
});

// Dynamic datetime validation
const datetimeInputs = document.querySelectorAll('input[type="datetime-local"]');
datetimeInputs.forEach(input => {
    input.addEventListener('change', function() {
        const selectedDate = new Date(this.value);
        const now = new Date();
        
        if (selectedDate < now) {
            alert('Please select a future date and time');
            this.value = '';
        }
    });
});
