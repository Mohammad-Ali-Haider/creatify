document.addEventListener('DOMContentLoaded', (event) => {
    const theme = localStorage.getItem('theme') || 'dark';
    setTheme(theme);
    document.getElementById('theme').value = theme;
});

function setTheme(theme) {
    const themeStylesheet = document.getElementById('theme-stylesheet');
    if (theme === 'light') {
        themeStylesheet.href = "/static/css/light.css";
    } else {
        themeStylesheet.href = "/static/css/dark.css";
    }
    localStorage.setItem('theme', theme);
}

function changeTheme(theme) {
    setTheme(theme);
}
