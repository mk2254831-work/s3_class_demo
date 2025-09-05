const form = document.getElementById('searchForm');
const tableBody = document.querySelector('#resultsTable tbody');
let flightsData = [];

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
        from_city: document.getElementById('fromCity').value,
        to_city: document.getElementById('toCity').value,
        start_date: document.getElementById('startDate').value,
        end_date: document.getElementById('endDate').value
    };

    const res = await fetch('/search', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });

    flightsData = await res.json();
    displayFlights(flightsData);
});

function displayFlights(flights) {
    tableBody.innerHTML = '';
    flights.forEach(f => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${f.airline_name}</td>
            <td>${f.from}</td>
            <td>${f.to}</td>
            <td>${f.departure}</td>
            <td>${f.arrival}</td>
            <td>${f.fare}</td>
        `;
        tableBody.appendChild(row);
    });
}

// Sorting
document.getElementById('sortFare').addEventListener('click', () => {
    const sorted = flightsData.sort((a, b) => a.fare - b.fare);
    displayFlights(sorted);
});

document.getElementById('sortDate').addEventListener('click', () => {
    const sorted = flightsData.sort((a, b) => new Date(a.departure) - new Date(b.departure));
    displayFlights(sorted);
});