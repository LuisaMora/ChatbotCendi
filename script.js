const express = require('express')

const path = require('path')

const app = new express()

app.use(express.static(__dirname));

app.get('/', (req,res) =>{
  res.sendFile(path.resolve(__dirname, 'index.html' ))
})
app.get('/chatbot', (req,res) =>{
  res.sendFile(path.resolve(__dirname, 'chatbot.html' ))
})

app.listen(4000,() => {
  console.log("holi")
})
function show() {
    alert("Presionaste el boton del chatbotS");
  }