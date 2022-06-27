
async function personaAgregaMensaje() {
    
    const input = document.getElementById("userin")
    const mensaje = input.value;
    var respuesta = "";
    const options = {
        mode: "no-cors",
        method: 'POST',
        "headers": {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        "body": { "mensaje": mensaje }
    };

    await fetch(`http://localhost:4000/response?mensaje=${mensaje}`, {
            method : 'POST', 
            mode: "no-cors",
            })
        
    .then(async response => {
                    console.log(response)
                    console.log("--------------")
                    if (!response.ok) {
    
                        // throw Error(response.status);
                    }else{
                        respuesta = await fetch("./data.json")
                        .then(async response => {
                            return await response.json().then(mensajito => {
                                                            console.log(mensajito)
                                                            return mensajito
                                                            // respuesta = mensajito
                                                            }
                                )
                        })
                    }
                    
                })
    .catch(e => {
                    console.log(e);
                });
        input.value = ""
        const div3 = document.createElement("div");
        div3.className = "media media-chat media-chat-reverse"

        const img2 = document.createElement("img")
        img2.className = "avatar2"
        img2.src = "https://img.icons8.com/color/344/gender-neutral-user.png"
        img2.alt = "... sd"

        const p2 = document.createElement("p")
        p2.textContent = mensaje

        const div4 = document.createElement("div");
        div4.className = "media-body"

        div3.insertAdjacentElement("beforeend", img2)
        div3.insertAdjacentElement("beforeend", div4)

        div4.insertAdjacentElement("beforeend", p2)

        const app2 = document.querySelector("#chat-content");
        app2.insertAdjacentElement("beforeend", div3)
        botAgregaMensaje(respuesta);
    

}
function botAgregaMensaje(mensajeBot) {
    // chat del chatbot-----------------------
    const div1 = document.createElement("div");
    div1.className = "media media-chat"

    const img = document.createElement("img")
    img.className = "avatar"
    img.src = "https://img.icons8.com/color/344/bmo.png"
    img.alt = "..."
    const p1 = document.createElement("p")
    p1.textContent = mensajeBot

    const div2 = document.createElement("div");
    div2.className = "media-body"

    div1.insertAdjacentElement("beforeend", img)
    div1.insertAdjacentElement("beforeend", div2)

    div2.insertAdjacentElement("beforeend", p1)
    // div2.insertAdjacentHTML("beforeend","<p>holi esto es una prueba che </p>")


    const app = document.querySelector("#chat-content");
    app.insertAdjacentElement("beforeend", div1)
    // app.insertAdjacentHTML("beforeend",'<div class="media media-chat"> <img class="avatar" src="https://img.icons8.com/color/36/000000/administrator-male.png" alt="..." <div class="media-body"> <p>holi esto es una prueba che </p> <p class="meta"><time datetime="2018">00:10</time></p> </div> </div>')

}
// const botonEnviar = document.querySelector(".boton_personalizado")
// export default personaAgregaMensaje;