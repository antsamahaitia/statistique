document.addEventListener('DOMContentLoaded', () => {
  const generalBtn = document.getElementById('general');
  const defenseBtn = document.getElementById('defense');
  const attaqueBtn = document.getElementById('attaque');
  const dataDisplay = document.getElementById('dataDisplay');

  generalBtn.addEventListener('click', () => {
    fetchData('/api/generale');
  });

  defenseBtn.addEventListener('click', () => {
    fetchData('/api/defense');
  });

  attaqueBtn.addEventListener('click', () => {
    fetchData('/api/attaque');
  });

  function fetchData(endpoint) {
    fetch(`http://localhost:3001${endpoint}`)
      .then(response => response.json())
      .then(data => {
        const tableHTML = generateTableHTML(data);
        dataDisplay.innerHTML = tableHTML;
      })
      .catch(error => console.error('Error fetching data:', error));
  }

  function generateTableHTML(data) {
    // Ajoutez votre logique pour générer le tableau HTML à partir des données JSON
    let generatedHTML = '<table><thead><tr>';
    for (const key in data[0]) {
      generatedHTML += `<th>${key}</th>`;
    }
    generatedHTML += '</tr></thead><tbody>';

    data.forEach(row => {
      generatedHTML += '<tr>';
      for (const key in row) {
        generatedHTML += `<td>${row[key]}</td>`;
      }
      generatedHTML += '</tr>';
    });

    generatedHTML += '</tbody></table>';
    return generatedHTML;
  }
});
