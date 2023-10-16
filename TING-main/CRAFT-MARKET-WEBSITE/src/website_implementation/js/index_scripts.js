document.addEventListener('DOMContentLoaded', function() {
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

            // 隐藏筛选按钮的容器并显示返回按钮
            filterButtonsContainer.style.display = 'none';
            returnButton.style.display = 'block';
        });
    });

    returnButton.addEventListener('click', function() {
        // 显示筛选按钮的容器并隐藏返回按钮
        filterButtonsContainer.style.display = 'flex';
        returnButton.style.display = 'none';
    });
});
