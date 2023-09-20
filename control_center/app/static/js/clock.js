function updateClock() {
    const now = new Date();
    const timeString = now.toLocaleTimeString();
    document.getElementById('liveClock').textContent = timeString;
}

setInterval(updateClock, 1000);
updateClock(); // Initial call to display the time immediately
