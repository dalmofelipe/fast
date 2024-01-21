document.addEventListener("DOMContentLoaded", StartIndexPage)


function StartIndexPage() {
    console.log('Script IndexPage carregado!');

    let smallTime = document.getElementById('time')
    smallTime.innerHTML = new Date().toLocaleString('pt-BR')

    setInterval(() => {
        smallTime.innerHTML = new Date().toLocaleString('pt-BR')
    }, 1000)
}
