const http = require('http');
const {spawn} = require('child_process');

const hostname = '127.0.0.1';
const port = 4040;

const readings = [];
const sensor = spawn('python', ['obd_sensors.py']);

sensor.stdout.on('data', function(data) {
    readings.push(data);
})

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  res.write(`<a>${readings[readings.length-1]}</a>`);
  res.end();
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});







