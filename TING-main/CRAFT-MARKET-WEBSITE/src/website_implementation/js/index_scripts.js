document.addEventListener('DOMContentLoaded', function() {
    // Access filter buttons to allow users to filter sports based on frequency
    const filterButtons = document.querySelectorAll('.filter');
    const filterButtonsContainer = document.querySelector('.filter-buttons');
    const returnButton = document.querySelector('.return-btn');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Get the desired filter value from the clicked button
            const filterValue = this.getAttribute('data-filter');
            const sports = document.querySelectorAll('.sport');

            // Get the desired filter value from the clicked button
            sports.forEach(function(sport) {
                if (filterValue === 'yearly' && sport.querySelector('figcaption').innerText === 'climbing') {
                    sport.style.display = 'block';
                } else if (filterValue === 'monthly' && sport.querySelector('figcaption').innerText === 'Yoga') {
                    sport.style.display = 'block';
                } else if (filterValue === 'weekly' && sport.querySelector('figcaption').innerText === 'Running') {
                    sport.style.display = 'block';
                } else {
                     // Hide sports that don't match the filters
                    sport.style.display = 'none';
                }
            });

            // Hide filter buttons and show the return button after a filter is applied
            filterButtonsContainer.style.display = 'none';
            returnButton.style.display = 'block';
        });
    });

    // Allow users to return to the filter options after filtering
    returnButton.addEventListener('click', function() {
        filterButtonsContainer.style.display = 'flex';
        returnButton.style.display = 'none';
    });

    // Hamburger menu functionality
    const menuIcon = document.querySelector('.menu-icon');
    const pageLinks = document.querySelector('.page-links');

    menuIcon.addEventListener('click', function() {
         // Toggle the visibility of the navigation links when the menu icon is clicked
        if (pageLinks.style.display === 'none' || pageLinks.style.display === '') {
            pageLinks.style.display = 'block';
        } else {
            pageLinks.style.display = 'none';
        }
    });

    // Provide a "back to top" button for better user navigation on long pages
    document.querySelector(".back-to-top").addEventListener("click", function() {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
      
    // Display the "back to top" button only when the user has scrolled down a certain distance
    window.onscroll = function() {
        if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
            document.querySelector(".back-to-top").style.display = "block";
        } else {
            document.querySelector(".back-to-top").style.display = "none";
        }
    };

   });
