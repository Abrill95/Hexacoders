document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.getElementById("navbar");
    window.addEventListener("scroll", function () {
        if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    });
});




let text = document.getElementById('text');
let leaf = document.getElementById('leaf');
let hill1 = document.getElementById('hill1');
let hill4 = document.getElementById('hill4');
let hill5 = document.getElementById('hill5');

window.addEventListener('scroll',()=>{
    let value=window.scrollY;
    let maxScroll = 450;
    if (value > maxScroll) {
        value = maxScroll;
    }
    text.style.transform = `translateY(${value * 2.5}px)`; // Cambia de marginTop a transform para mayor suavidad
    leaf.style.transform = `translate(${value * 1.5}px, ${-value * 1.5}px)`;
    hill5.style.transform = `translateX(${value * 1.5}px)`;
    hill4.style.transform = `translateX(${-value * 1.5}px)`;
    hill1.style.transform = `translateY(${value}px)`;
})

document.addEventListener("DOMContentLoaded", function() {
    const bgDiv = document.querySelector(".bg-img-cover");
    const highResUrl = bgDiv.getAttribute("data-bg-url");
    const img = new Image();
    img.src = highResUrl;
    img.onload = function() {
        bgDiv.style.backgroundImage = `url(${highResUrl})`;
    };
});


document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("formulario");
    const confirmationMessage = document.getElementById("confirmationMessage");

    // Escuchar el evento de envío del formulario
    form.addEventListener("submit", function (event) {
        event.preventDefault();


        confirmationMessage.style.display = "block";
        confirmationMessage.classList.add("fadeIn");


        setTimeout(function () {
            confirmationMessage.classList.remove("fadeIn");
            confirmationMessage.classList.add("heartbeat");
        }, 600);


        setTimeout(function () {
            confirmationMessage.classList.remove("heartbeat");
            confirmationMessage.classList.add("fadeOut");

            // Ocultar el mensaje después de fadeOut y limpiar el formulario
            setTimeout(function () {
                confirmationMessage.style.display = "none";
                confirmationMessage.classList.remove("fadeOut");
                form.reset();
            }, 600);
        }, 2500);
    });
});
