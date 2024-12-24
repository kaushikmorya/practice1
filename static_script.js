document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            const dataDiv = document.getElementById('data');
            dataDiv.innerHTML = data.map(item => `<p>${item.key}: ${item.value}</p>`).join('');
        });

    document.getElementById('dataForm').addEventListener('submit', event => {
        event.preventDefault();
        const formData = new FormData(event.target);
        const data = Object.fromEntries(formData.entries());

        fetch('/api/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            console.log(result.message);
            location.reload();
        });
    });
});
