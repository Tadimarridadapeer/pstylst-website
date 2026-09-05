// Intersection Observer for section animations
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.section-fade').forEach((section) => {
    observer.observe(section);
});

// Navbar blending effect on scroll
const navbar = document.getElementById('navbar');
const navLogo = document.getElementById('navbar-logo');
const navLinks = navbar.querySelectorAll('.nav-link');
const navCta = document.getElementById('nav-cta');
const navMobileBtn = document.getElementById('mobile-menu-btn');
const navEyebrow = document.getElementById('nav-eyebrow');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('bg-[#FDFBF7]/95', 'backdrop-blur-md', 'border-b', 'border-[#E5E5E5]', 'shadow-sm', 'py-4');
        navbar.classList.remove('py-6', 'text-white');
        navbar.classList.add('text-brand-black');
        
        if (navLogo) navLogo.src = '/assets/pstylst logo black.png';
        if (navMobileBtn) navMobileBtn.classList.replace('text-white', 'text-brand-black');
        if (navEyebrow) navEyebrow.classList.replace('border-white/20', 'border-brand-border');
        if (navCta) {
            navCta.classList.add('border-brand-black', 'hover:bg-brand-black', 'hover:text-white', 'text-brand-black');
            navCta.classList.remove('border-white', 'hover:bg-white', 'hover:text-brand-black', 'text-white');
        }
    } else {
        navbar.classList.remove('bg-[#FDFBF7]/95', 'backdrop-blur-md', 'border-b', 'border-[#E5E5E5]', 'shadow-sm', 'py-4', 'text-brand-black');
        navbar.classList.add('py-6', 'text-white');
        
        if (navLogo) navLogo.src = '/assets/pstylst logo white.png';
        if (navMobileBtn) navMobileBtn.classList.replace('text-brand-black', 'text-white');
        if (navEyebrow) navEyebrow.classList.replace('border-brand-border', 'border-white/20');
        if (navCta) {
            navCta.classList.remove('border-brand-black', 'hover:bg-brand-black', 'hover:text-white', 'text-brand-black');
            navCta.classList.add('border-white', 'hover:bg-white', 'hover:text-brand-black', 'text-white');
        }
    }
});
