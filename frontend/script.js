const express = require('express')
const path = require('path')
const axios = require('axios')
const app = new express()

app.use(express.static(__dirname));

app.get('/', (req, res) => {
  res.sendFile(path.resolve(__dirname, 'index.html'))
})
app.get('/chatbot', (req, res) => {
  res.sendFile(path.resolve(__dirname, 'chatbot.html'))
})

app.get('/response', (req, res) => {
  axios.get('http://localhost:5050/chatbot/entrenar').then(resp => {
    console.log(resp.data);
  });
})

app.post('/response', async (req, resp) => {
  const mensaje = req.query.mensaje;
  console.log(mensaje)
  const options = {
    mode: "no-cors",
    method: 'POST',
    "headers": {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    "body": { "mensaje": mensaje }
  };
  await axios({
    method: 'post',
    url: `http://localhost:5050/chatbot/${mensaje}`,
    data: {
      mensaje: 'HOLIWIS'
    },
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then((response) => {
    console.log(response.status);
    resp.sendStatus(200);
  }, (error) => {
    console.log(error);
  });
  // await fetch(`http://localhost:5050/chatbot/${mensaje}`, options)
  //   .then(response => {
  //     console.log(response)
  //     console.log("--------------")
  //     if (!response.ok) {

  //       throw Error(response.status);
  //     }
  //     console.log(response.json)
  //   })
  //   .catch(e => {
  //     console.log(e);
  //   });
  
})

app.listen(4000, () => {
  console.log("holi")
})
function show() {
  alert("Presionaste el boton del chatbotS");
}
