document.addEventListener('DOMContentLoaded', function() {
    // Existing filter functionality
    const filterButtons = document.querySelectorAll('.filter');
    const filterButtonsContainer = document.querySelector('.filter-buttons');
    const returnButton = document.querySelector('.return-btn');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filterValue = this.getAttribute('data-filter');
            const sports = document.querySelectorAll('.sport');

            sports.forEach(function(sport) {
                if (filterValue === 'yearly' && sport.querySelector('figcaption').innerText === 'climbing') {
                    sport.style.display = 'block';
                } else if (filterValue === 'monthly' && sport.querySelector('figcaption').innerText === 'Yoga') {
                    sport.style.display = 'block';
                } else if (filterValue === 'weekly' && sport.querySelector('figcaption').innerText === 'Running') {
                    sport.style.display = 'block';
                } else {
                    sport.style.display = 'none';
                }
            });

            filterButtonsContainer.style.display = 'none';
            returnButton.style.display = 'block';
        });
    });

    returnButton.addEventListener('click', function() {
        filterButtonsContainer.style.display = 'flex';
        returnButton.style.display = 'none';
    });

    // Hamburger menu functionality
    const menuIcon = document.querySelector('.menu-icon');
    const pageLinks = document.querySelector('.page-links');

    menuIcon.addEventListener('click', function() {
        if (pageLinks.style.display === 'none' || pageLinks.style.display === '') {
            pageLinks.style.display = 'block';
        } else {
            pageLinks.style.display = 'none';
        }
    });
    window.onscroll = function() {
        if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
            document.querySelector(".back-to-top").style.display = "block";
        } else {
            document.querySelector(".back-to-top").style.display = "none";
        }
    };

   });
