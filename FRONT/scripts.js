// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://127.0.0.1:5000/Montpellier/stations/ODYSSEUM', true)

request.onload = function () {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)

  if (request.status >= 200 && request.status < 400) {
    data.forEach((index) => {
      console.log(index)
    })
  } else {
    console.log('error')
  }
}

// Send request
request.send()

