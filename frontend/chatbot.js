// const div1 = document.createElement('<div class="media media-chat"> <img class="avatar" src="https://img.icons8.com/color/36/000000/administrator-male.png" alt="..." <div class="media-body"> <p>holi esto es una prueba che </p> <p class="meta"><time datetime="2018">00:10</time></p> </div> </div>');
// chat del chatbot
const div1 = document.createElement("div");
div1.className="media media-chat"

const img = document.createElement("img")
img.className="avatar"
img.src="https://img.icons8.com/color/344/bmo.png"
img.alt="..."
const p1 = document.createElement("p")
p1.textContent="holi esto es una prueba che "

const div2 = document.createElement("div");
div2.className="media-body"

div1.insertAdjacentElement("beforeend",img)
div1.insertAdjacentElement("beforeend",div2)

div2.insertAdjacentElement("beforeend",p1)
// div2.insertAdjacentHTML("beforeend","<p>holi esto es una prueba che </p>")


const app = document.querySelector("#chat-content");
app.insertAdjacentElement("beforeend",div1)
// app.insertAdjacentHTML("beforeend",'<div class="media media-chat"> <img class="avatar" src="https://img.icons8.com/color/36/000000/administrator-male.png" alt="..." <div class="media-body"> <p>holi esto es una prueba che </p> <p class="meta"><time datetime="2018">00:10</time></p> </div> </div>')

// chat de la persona
const div3 = document.createElement("div");
div3.className="media media-chat media-chat-reverse"

const img2 = document.createElement("img")
img2.className="avatar2"
img2.src="https://img.icons8.com/color/344/gender-neutral-user.png"
img2.alt="... sd"
const p2 = document.createElement("p")
p2.textContent="Hola wenas joven "

const div4 = document.createElement("div");
div4.className="media-body"

div3.insertAdjacentElement("beforeend",img2)
div3.insertAdjacentElement("beforeend",div4)

div4.insertAdjacentElement("beforeend",p2)
// div2.insertAdjacentHTML("beforeend","<p>holi esto es una prueba che </p>")


const app2 = document.querySelector("#chat-content");
app2.insertAdjacentElement("beforeend",div3)
