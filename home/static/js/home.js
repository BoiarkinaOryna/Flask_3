let text = document.querySelector(".text")
let button = document.querySelector(".buttonSend")
let form = document.querySelector(".review")
let buttonAnother = document.querySelector(".buttonSendAnother")

console.log('button = ', button)
if (button != null){
    button.addEventListener(
        type = 'click',
        listener = function(){
            document.cookie = 'review_sended = true'
            console.log("1 document.cookie =", document.cookie)
        }
    )
}

console.log('buttonAnother = ', buttonAnother)
if (buttonAnother != null){
    buttonAnother.addEventListener(
        type = 'click',
        listener = function(){
            document.cookie = "review_sended = false"
            console.log("2 document.cookie =", document.cookie)
            text.textContent = 'Оновіть, будь ласка, сторінку'
            buttonAnother.style.display = "none"
        }
    )
}