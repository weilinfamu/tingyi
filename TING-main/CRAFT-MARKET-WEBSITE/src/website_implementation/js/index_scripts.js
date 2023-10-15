document.querySelectorAll('.filter').forEach(button => {
    button.addEventListener('click', function() {
        let filterValue = this.getAttribute('data-filter');
        
        // Here, you can use the filterValue to show/hide or adjust the content
        // based on the selected filter. This is just a basic example, and you'd
        // need to define what should happen for each filter type.
        
        if (filterValue === 'yearly') {
            // Show/hide or adjust content for yearly
        } else if (filterValue === 'monthly') {
            // Show/hide or adjust content for monthly
        } else if (filterValue === 'weekly') {
            // Show/hide or adjust content for weekly
        }
    });
});
