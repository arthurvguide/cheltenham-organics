// Script to customize the standard allauth password reset page
const labelUsername = document.getElementsByTagName("label")[0];
const labelPass = document.getElementsByTagName("label")[1];

window.onload = () => {
    labelUsername.innerHTML = "";
    labelPass.innerHTML = "";
};
