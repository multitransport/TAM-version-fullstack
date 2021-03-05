const app = document.getElementById('root')

const container = document.createElement('div')
container.setAttribute('class', 'container')

app.appendChild(container)

// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()
request.responseType = 'json'
// Open a new connection, using the GET request on the URL endpoint

request.open('GET', 'http://127.0.0.1:5000/Montpellier/stations', true)




request.onload = function () {
  // Begin accessing JSON data here
  var data = request.response;
  console.log(data)

  if (request.status >= 200 && request.status < 400) {

    // Create a div with a card class
    const card = document.createElement('div')
    card.setAttribute('class', 'card')

    // Create an h1 and set the text content to the film's title
    const h2 = document.createElement('h2')
    h2.textContent = "Montpellier (ou nom de ville)"
    card.appendChild(h2)
    const p = document.createElement('p')
    

    data.forEach((station) => {
  
    // Create a p and set the text content to the film's description
    const p = document.createElement('p')
    p.textContent = station
    

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

