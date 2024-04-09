const section = document.getElementById('features7-6');

// Adiciona a classe para tornar a seção visível após 2 segundos
setTimeout(() => {
    section.classList.add('section-visible');
    // Remove o loading container
    document.querySelector('.loading-container').remove();
}, 1500);