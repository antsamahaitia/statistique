const mysql = require('mysql');

let connection;

function createConnection() {
   connection = mysql.createConnection({
      host: 'localhost',
      user: 'root',
      password: 'root',
      database: 'footStat',
   });

   // Gestion des erreurs lors de la connexion
   connection.connect((err) => {
      if (err) {
         console.error('Erreur de connexion à la base de données : ', err);
         throw err;
      } else {
         console.log('Connexion à la base de données établie');
      }
   });

   // Gestion des erreurs lors de la déconnexion
   connection.on('error', (err) => {
      console.error('Erreur de connexion à la base de données : ', err);
      if (err.code === 'PROTOCOL_CONNECTION_LOST') {
         console.log('Reconnexion à la base de données...');
         // Vérifier si la connexion n'est pas déjà en cours avant de réessayer
         if (!connection.connecting) {
            createConnection(); // Réessayer la connexion
         }
      } else {
         throw err;
      }
   });
}

// Ne pas appeler connection.connect ici

// Créer la première connexion
createConnection();

module.exports = connection;
