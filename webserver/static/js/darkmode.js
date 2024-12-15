/**
 * @type {HTMLButtonElement}
 */
const toggleButton = document.getElementById('theme-toggle');
const darkModeRuleset = document.getElementById("dark-mode-ruleset");

const setCookie = (name, value, days) => {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = `${name}=${value}; ${expires}; path=/`;
};

const getCookie = (name) => {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
};

function getTheme() {
    if (localStorage.getItem('theme')) {
        return localStorage.getItem('theme');
    }
    else {
        return "light";
    }
}

function setDarkMode() {
    darkModeRuleset.disabled = false;
    localStorage.setItem("theme", "dark");
    setCookie("theme", "dark", 365);
}

function setLightMode() {
    darkModeRuleset.disabled = true;
    localStorage.setItem("theme", "light");
    setCookie("theme", "light", 365);
}

function toggleTheme() {
    if (getTheme() == "dark") {
        setLightMode()
    }
    else {
        setDarkMode()
    }
}

toggleButton.addEventListener("click", toggleTheme);
