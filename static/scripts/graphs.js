const COLOURS = [
    '#225a86',
    '#991825',
    '#784c1b',
    '#222d73',
    '#a8170d',
    '#af320c',
    '#1881ae',
    '#00532d',
    '#313638',
    '#1b527b',
    '#2e913b',
]

function pie_chart(id, prepare_data, label_cb) {
    const chart = document.getElementById(id)
    fetch(chart.dataset.url)
        .then(res => res.json())
        .then(prepare_data)
        .then(data => {
            if (data.labels.length === 0) {
                chart.classList.add('hidden')
                const noDataWarning = document.createElement('p')
                noDataWarning.innerText = 'No data'
                chart.parentElement.appendChild(noDataWarning)
                chart.parentElement.classList.add('no-data')
                return
            }

            const ctx = chart.getContext('2d')
            const callbacks = {}
            if (label_cb) callbacks.label = label_cb
            new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Income',
                        data: data.data,
                        backgroundColor: COLOURS,
                    }],
                },
                options: {
                    responsive: true,
                    tooltips: { callbacks },
                },
            })
        })
}
