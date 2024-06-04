document.getElementById('csvFileInput').addEventListener('change', handleFileSelect, false);

function handleFileSelect(event) {
    const file = event.target.files[0];
    if (!file) {
        return;
    }

    const reader = new FileReader();
    reader.onload = function(e) {
        const contents = e.target.result;
        displayCSV(contents);
    };
    reader.readAsText(file);
}

function displayCSV(contents) {
    const lines = contents.split('\n');
    const table = document.getElementById('csvTable');
    table.innerHTML = '';

    lines.forEach((line, index) => {
        const row = table.insertRow();
        const cells = line.split(',');
        cells.forEach(cell => {
            const cellElement = document.createElement(index === 0 ? 'th' : 'td');
            cellElement.textContent = cell;
            row.appendChild(cellElement);
        });
    });
}
