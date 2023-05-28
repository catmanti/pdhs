var ctx = document.getElementById('myChart');
new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: [{%for data in population %}'{{data.ds_division}}',{% endfor %}], //loop through queryset,
    datasets: [{
        label: '# of Votes',
        data: [{%for data in population %}{{ data.population }}, {% endfor %}],
    borderWidth: 1
    }]
    },
    options: {
    plugins: {
        legend: {
            display: false,
        },
        customCanvasBackgroundColor: {
            color: 'lightGreen',
        },
    },
    scales: {
        y: {
            beginAtZero: true,
        },
    },
},
});