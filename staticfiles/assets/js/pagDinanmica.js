function showSection() {
    const section = document.getElementById('features-section');
    section.classList.remove('hidden');
    section.classList.add('visible');
}

setTimeout(showSection, 2000); // Tempo em milissegundos (2000ms = 2 segundos)