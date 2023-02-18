document.addEventListener("DOMContentLoaded", StartAuthenticate)


function StartAuthenticate() {
    console.log('Script Auth carregado!');

    let inputName = document.getElementById('name')
    let inputEmail = document.getElementById('email_register')
    let inputPassword = document.getElementById('password')
    let inputConfirmPassword = document.getElementById('confirm_pass')

    let resetButton = document.querySelector('input[value="Limpar"]')
    
    inputEmail.addEventListener('focusout', function() {
        let emailDigitado = inputEmail.value
        FindUserByEmail(emailDigitado)
    })

    resetButton.addEventListener('click', function(event) {
        event.preventDefault()
        inputName.value = ''
        inputEmail.value = ''
        inputPassword.value = ''
        inputConfirmPassword.value = ''
    })
}


async function FindUserByEmail(email) {
    let url = `http://localhost:8000/api/v1/users/find?email=${email}`

    let user = await fetch(url)
        .then(data => data.json())
        .then(data => data)
        .catch(e => console.log(e))

    if(user) {
        let msg = `O email <strong>${email}</strong> já esta em uso`
        addFieldErrorEmailAlreadeyExists('label[for="email_register"]', msg)
    }
}


function addFieldErrorEmailAlreadeyExists(seletor, msg) {
    let label = document.querySelector(seletor)
    let span = document.createElement('span')

    // controle para não adicionar a mesma mensagem varias vezes no campo
    if(label.children.length <= 2) {
        span.classList.add('form-validation-error')
        span.innerHTML = msg 
        label.appendChild(span)

        setTimeout(() => {
            label.removeChild(span)
        }, 5000)
    }
}

