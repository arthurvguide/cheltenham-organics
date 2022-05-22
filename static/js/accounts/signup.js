// Script to customize the standard allauth signup page
const labelUsername = document.getElementsByTagName("label")[0];
const labelEmail = document.getElementsByTagName("label")[1];
const labelPass = document.getElementsByTagName("label")[2];
const labelPassAgain = document.getElementsByTagName("label")[3];


window.onload = () => {
    labelUsername.innerHTML = "";
    labelEmail.innerHTML = "";
    labelPassAgain.innerHTML = "";
    labelPass.innerHTML = "";
};