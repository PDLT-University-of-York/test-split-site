// initial toggle buttons must have the class 'closed'

// grab items
const allDetails = document.querySelectorAll("details");
const allToggles = document.querySelectorAll(".toggle")

// function to open all details
const openDetails = () => {
        allDetails.forEach(detail => detail.setAttribute("open", true));
        allToggles.forEach((toggle) => {
            toggle.classList.remove("closed");
            toggle.classList.add("open");
            toggle.innerHTML = "Close all sections"
        });
}

// function to close all details
const closeDetails = () => {
    allDetails.forEach(detail => detail.removeAttribute("open"));
    allToggles.forEach((toggle) => {
        toggle.classList.remove("open");
        toggle.classList.add("closed");
        toggle.innerHTML = "Open all sections"
    });
}

// function for toggle button
const toggleDetailsOpenClosed = () => {
    allToggles[0].classList.contains("closed") ? openDetails() : closeDetails();        
}

// add event listener on toggle buttons
allToggles.forEach(toggle => {
    toggle.addEventListener("click", toggleDetailsOpenClosed);
})