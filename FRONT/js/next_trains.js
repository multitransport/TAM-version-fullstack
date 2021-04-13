var parameters = location.search.substring(1).split("&");
var town;
var station;
for (let step=0; step<parameters.length; step++){
  if (parameters[step].split("=")[0] === "town"){
    town = parameters[step].split("=")[1]
  }else{
    station = parameters[step].split("=")[1]
  }
}


const app = document.getElementById('root')

const container = document.createElement('div')
container.setAttribute('class', 'container')

app.appendChild(container)

// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://0.0.0.0:5000/'+town+'/stations/'+station, true)
request.onload = function () {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)

  if (request.status >= 200 && request.status < 400) {
    

    data.forEach((transport) => {
    
     // Create a div with a card class
     const card = document.createElement('div')
     card.setAttribute('class', 'card')
 
     // Create an h1 and set the text content to the film's title
     const h2 = document.createElement('h2')
     h2.textContent = 'Arrêt : ' + transport[0][1] + ' - Destination : ' + transport[0][2] + ' - Ligne : ' + transport[0][0]
    

  
    // Create a p and set the text content to the film's description
    const resultOne = document.createElement('p')
    const resultTwo = document.createElement('p')
    const resultThree = document.createElement('p')

    if (typeof transport[1][0] !== "undefined") {
      resultOne.textContent = transport[1][0]
    }else{
      resultOne.textContent = "Service terminé"
    }

    if (typeof transport[1][1] !== "undefined") {
      resultTwo.textContent = transport[1][1]
    }else{
      resultTwo.textContent = "Service terminé"
    }

    if (typeof transport[1][2] !== "undefined") {
      resultThree.textContent = transport[1][2]
    }else{
      resultThree.textContent = "Service terminé"
    }



    // Append the cards to the container element
    container.appendChild(card)

    // Each card will contain an h1 and a p
    card.appendChild(h2)
    card.appendChild(resultOne)
    card.appendChild(resultTwo)
    card.appendChild(resultThree)
    })
  } else {
  const errorMessage = document.createElement('marquee')
  errorMessage.textContent = `Gah, it's not working!`
  app.appendChild(errorMessage)
  }
}

// Send request
request.send()
à