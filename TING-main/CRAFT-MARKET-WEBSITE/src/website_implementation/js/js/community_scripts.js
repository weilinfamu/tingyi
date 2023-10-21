document.addEventListener("DOMContentLoaded", function() {
    // 1. Toggle Visibility
    const toggleNavButton = document.getElementById('toggleNavButton');
    const sideMenu = document.querySelector('.flex-side-menu');

    toggleNavButton.addEventListener('click', function() {
        sideMenu.classList.toggle('visible');
    });

    // 2. Highlight Active Link
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navLinks.forEach(innerLink => innerLink.classList.remove('active'));
            link.classList.add('active');
        });
    });
});

// Sample data for activities
const activityData = {
    
    football: {
       
        heading: "Football Activities",
        activities: [
            {
                title: "Football Tournament - Paddington",
                description: "Compete in a local football tournament",
                location: "Paddington 2021"
            },

            {
                title: "American Football Tournament - Dundas",
                description: "Compete in a local gridiron football tournament",
                location: "Dundas 2117"
            },

            {   title: "Football Camp - Paddington",
                description: "Participate in a local football camp to enhance football skills and socialize with other players",
                location: "Paddington, London, W2"
                
            }
            
            // ... other football activities ...
        ]
    },
    basketball: {
       
        heading: "Basketball Activities",
        activities: [
            {
                title: "Basketball League - Alexandria",
                description: "Join the local basketball league",
                location: "Alexandria 2015"
            },
            // ... other basketball activities ...
            {
                title: "Club Coach Course - Brookvale",
                description: "Enhance your coaching skills in this course",
                location: "Brookvale 2100"
            },
            {
                title: "Senior Representative Trials - Alexandria",
                description: "Participate in the NBL1 & Youth League Trials conducted by Sydney Comets for the year 2024.",
                location: "53-57 Maddox St, Alexandria, NSW 2015",
            }
        ]
    },
    tennis: {
      
        heading: "Tennis Activities",
        activities: [
            {
                title: "Tennis Championship - Bondi",
                description: "Compete in the Bondi Tennis Championship",
                location: "Bondi 2026"
            },
            {
                title: "Tennis Lessons - Haberfield",
                description: "Learn tennis at The Ark Tennis Centre",
                location: "Haberfield 2045"
            },
            {
                title: "Various Tennis Competitions - Australia",
                description: "Engage in level-based playing opportunities provided by Tennis Australia's 2023 Competitive Play Calendar",
                location: "Locations vary across Australia"
            }
            // ... other tennis activities ...
        ]
    },
    golf: {
       
        heading: "Golf Activities",
        activities: [
            {
                title: "Golf Tournament - Randwick",
                description: "Participate in a local golf tournament",
                location: "Randwick 2031"
            },
            // ... other golf activities ...
            {
                title: "Golf Championship - Rosebery",
                description: "Compete in a local golf championship",
                location: "Rosebery 2018"
            }
        ]
    },
    cycling: {
      
        heading: "Cycling Activities",
        activities: [
            {
                title: "Cycling Marathon - Parramatta",
                description: "Ride through scenic routes in the cycling marathon",
                location: "Parramatta 2150"
            },
            // ... other cycling activities ...
            {
                title: "Cycling Adventure - Narrabeen",
                description: "Enjoy an 8.4-km ride around Narrabeen Lagoon",
                location: "Narrabeen 2101"
            }
        ]
    },
    extremeSports: {
        
        heading: "Extreme Sports Activities",
        activities: [
            {
                title: "Extreme Sports Festival - Western Sydney",
                description: "Enjoy a day of adrenaline-pumping activities",
                location: "Western Sydney 2759"
            },
            // ... other extreme sports activities ...
            {
                title: "Whitewater Rafting - Western Sydney",
                description: "Get your adrenaline pumping with whitewater rafting",
                location: "Western Sydney 2759"
            }
        ]
    },
    running: {
       
        heading: "Running Activities",
        activities: [
            {
                title: "Sydney Half Marathon - CBD",
                description: "Run through Sydney’s central business district",
                location: "Sydney 2000"
            },
            // ... other running activities ...
            {
                title: "Trail Run - Centennial Park",
                description: "Discover wilderness trails in Centennial Park",
                location: "Centennial Park 2021"
            }
        ]
    },
    yoga: {
       
        heading: "Yoga Activities",
        activities: [
            {
                title: "Yoga Retreat - Darlinghurst",
                description: "Relax and rejuvenate at a yoga retreat",
                location: "Darlinghurst 2010"
            },
            // ... other yoga activities ...
            {
                title: "Outdoor Yoga - Hyde Park",
                description: "Relax and stretch with outdoor yoga in Hyde Park",
                location: "Sydney 2000"
            }
        ]
    },
    climbing: {
       
        heading: "Climbing Activities",
        activities: [
            {
                title: "Climbing Competition - St Peters",
                description: "Test your climbing skills in a friendly competition",
                location: "St Peters 2044"
            },
            // ... other climbing activities ...
            {
                title: "Rock Climbing - Villawood",
                description: "Experience indoor rock climbing at Sydney Indoor Climbing Gym",
                location: "Villawood 2163"
            }
        ]
    }
};



document.querySelectorAll('.group').forEach(group => {
    group.addEventListener('click', function() {
        const activityType = this.getAttribute('data-activity');
        updateLatestActivity(activityData[activityType]);
    });
});

function updateLatestActivity(data) {
    const latestActivity = document.getElementById('latestActivity');
    let activityListHTML = '';

    data.activities.forEach(activity => {
        activityListHTML += `
            <li>
                <h3>${activity.title}</h3>
                <p>${activity.description}</p>
                <p>${activity.location}</p>
            </li>
        `;
    });

    latestActivity.innerHTML = `
        <h2>${data.heading}</h2>
        <ul class="activity-list">
            ${activityListHTML}
        </ul>
    `;
}
