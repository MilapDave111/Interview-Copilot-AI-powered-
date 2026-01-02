const { Pool } = require('pg');
require('dotenv').config();

// Create a pool of connections (More efficient than opening/closing every time)
const pool = new Pool({
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  database: process.env.DB_NAME,
});

// Test the connection immediately
pool.connect((err, client, release) => {
  if (err) {
    return console.error('Error acquiring client', err.stack);
  }
  console.log('Database Connected Successfully!');
  release();
});

module.exports = pool;