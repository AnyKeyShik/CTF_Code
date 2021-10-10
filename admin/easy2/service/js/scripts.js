/*!
* Start Bootstrap - Grayscale v7.0.3 (https://startbootstrap.com/theme/grayscale)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
*/
//
// Scripts
//

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    console.log("V2VsY29tZSBhYm9hcmQuIFlvdXIgc2VjcmV0IHBocmFzZSBpcyAiaHlwZXJpb24iLiBNYXliZSB5b3Ugd2lsbCBuZWVkIHRoaXM6IC0tLS1bLS0+KysrKys8XT4uLS0tLS0tLisrKysuLS0uKysrWy0+KysrPF0+LlstLS0+KzxdPi0uKytbLT4rKys8XT4uWy0tLT4rPF0+LS0uK1stPisrKzxdPi4tLS0tLS0tLS0uWy0tLT4rPF0+KysuKysrKysuLS0tLlstLS0tLS0+KzxdPi5bLS0tPisrPF0+KysrKysuWy0+KysrKys8XT4rKysuWy0+KysrPF0+Ky4rKysrKy4tLS0tLlstLS0tLT4rKzxdPisuK1stLS0tLT4rPF0+LisrWy0tLS0+KzxdPisrLgo=");

});
