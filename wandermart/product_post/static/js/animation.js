document.addEventListener("DOMContentLoaded", function() {
    let images = document.querySelectorAll(".hero-image");

    images.forEach((image, index) => {
        setTimeout(() => {
            image.classList.remove("hidden");
            image.style.animation = index % 2 === 0 ? "throwLeft 1.5s ease-out forwards" : "throwRight 1.5s ease-out forwards";
        }, index * 200);
    });
});
