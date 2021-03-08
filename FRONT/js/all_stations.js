var parameters = location.search.substring(1).split("=");
<<<<<<< HEAD
town = unescape(parameters[1]);
=======
city = unescape(parameters[1]);
document.getElementById("town").innerHTML = city
>>>>>>> 0d530d7b7e789633725b0b139744f60ddddbe7e6

const app = document.getElementById('root')

const container = document.createElement('div')
container.setAttribute('class', 'container')

app.appendChild(container)

// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()
request.responseType = 'json'
// Open a new connection, using the GET request on the URL endpoint

<<<<<<< HEAD
request.open('GET', "http://127.0.0.1:5000/"+town+"/stations", true)
=======
request.open('GET', "http://127.0.0.1:5000/"+city+"/stations", true)
>>>>>>> 0d530d7b7e789633725b0b139744f60ddddbe7e6


request.onload = function () {
  // Begin accessing JSON data here
  var data = request.response;
  console.log(data)

  if (request.status >= 200 && request.status < 400) {
<<<<<<< HEAD

     // Create a div with a card class
     const card = document.createElement('div')
     card.setAttribute('class', 'card')
 
     // Create an h1 and set the text content to the film's title
     const h2 = document.createElement('h2')
     h2.textContent = town
     card.appendChild(h2)
     

    data.forEach((station) => {

    const a = document.createElement('a')
    a.setAttribute('href', 'next_trains.html?town='+town+ '&'+ 'station='+station)
    a.setAttribute('id', station)
    
    // Create a p and set the text content to the film's description
    const p = document.createElement('p')
    p.textContent = station
    

    // Append the cards to the container element
    container.appendChild(card)
    
    // Each card will contain an h1 and a p
    a.appendChild(p)
    card.appendChild(a)
      
=======
      // Create a div with a card class
      const card = document.createElement('div')
      card.setAttribute('class', 'card')
  
      // Create an h1 and set the text content to the film's title
      const h2 = document.createElement('h2')
      h2.textContent = city
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
>>>>>>> 0d530d7b7e789633725b0b139744f60ddddbe7e6
    })
  } else {
  const errorMessage = document.createElement('marquee')
  errorMessage.textContent = `Gah, it's not working!`
  app.appendChild(errorMessage)
  }
}

// Send request
request.send()


