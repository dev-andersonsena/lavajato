document.addEventListener("DOMContentLoaded", function() {
    const currentDay = document.querySelector(".current-day");

    // Animação simples para realçar o dia atual
    currentDay.animate([
        // keyframes
        { transform: 'scale(1)', backgroundColor: '#00f' }, 
        { transform: 'scale(1.2)', backgroundColor: '#00f' },
        { transform: 'scale(1)', backgroundColor: '#00f' }
    ], { 
        // timing options
        duration: 1000,
        iterations: Infinity
    });
});
