// Add event listener to login form submit button
document.querySelector('.login-form button').addEventListener('click', (e) => {
    e.preventDefault();
    // Add animation to login form
    document.querySelector('.login-form').classList.add('animate');
    // Add delay to simulate login process
    setTimeout(() => {
        // Remove animation from login form
        document.querySelector('.login-form').classList.remove('animate');
        // Simulate login success
        alert('Login successful!');
    }, 2000);
});

// Add animation to navbar on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});