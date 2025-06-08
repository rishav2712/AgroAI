// Agro AI Basic JavaScript - by Human 💡

document.addEventListener("DOMContentLoaded", function () {
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", function () {
            const submitButton = form.querySelector("input[type='submit']");
            if (submitButton) {
                submitButton.value = "Please wait...";
                submitButton.disabled = true;
            }
        });
    });

    console.log("Agro AI script loaded ✅");
});
