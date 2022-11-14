function make_currency_label(t, d) {
    return ` ${d.labels[t.index]}: £${(d.datasets[t.datasetIndex].data[t.index] / 100).toFixed(2)}`;
}

function prepare_data(data) {
    const result = { labels: [], data: [] };
    for (const key in data) {
        result.labels.push(key);
        result.data.push(data[key]);
    }
    return result;
}