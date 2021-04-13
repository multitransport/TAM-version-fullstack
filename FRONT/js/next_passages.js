var parameters = location.search.substring(1).split("&");
var town;
var station;
var line;
var destination;
for (let step=0; step<parameters.length; step++){
  if (parameters[step].split("=")[0] === "town"){
    town = parameters[step].split("=")[1]
  }else if (parameters[step].split("=")[0] === "station"){
    station = parameters[step].split("=")[1]
  }else if (parameters[step].split("=")[0] === "line"){
    line = parameters[step].split("=")[1]
  }else{
    destination = parameters[step].split("=")[1]
  }
}


const app = document.getElementById('root')

const container = document.createElement('div')
container.setAttribute('class', 'container')

app.appendChild(container)

// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://0.0.0.0:5000/'+town+'/next/?line='+line+'&station='+station+'&destination='+destination, true)
request.onload = function () {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)

  if (request.status >= 200 && request.status < 400) {

    // Create a div with a card class
    const card = document.createElement('div')
    card.setAttribute('class', 'card')

    // Create an h1 and set the text content to the film's title
    const h2 = document.createElement('h2')
    h2.textContent = 'Arrêt : ' + data[0][1] + ' - Destination : ' + data[0][2] + ' - Ligne : ' + data[0][0]
    card.appendChild(h2)
    const p = document.createElement('p')
    

    data.forEach((transport) => {
  
    // Create a p and set the text content to the film's description
    const p = document.createElement('p')
    p.textContent = String(transport[3])
    

    // Append the cards to the container element
    container.appendChild(card)

    // Each card will contain an h1 and a p
    
    card.appendChild(p)
      
    })
  } else {
  const errorMessage = document.createElement('marquee')
  errorMessage.textContent = `Gah, it's not working!`
  app.appendChild(errorMessage)
  }
}

// Send request
request.send()
