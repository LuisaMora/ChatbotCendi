
async function personaAgregaMensaje() {
    const input = document.getElementById("userin")
    const mensaje = input.value;
    const options = {
        mode: "no-cors",
        method: 'POST',
        "headers": {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        "body": { "mensaje": mensaje }
    };
    if (mensaje) {

        // fetch(`http://localhost:5050/chatbot/${mensaje}`, {
        //     mode: "no-cors",
        //     headers : {
        //         'Content-Type': 'application/json'
        //     },
        //     method : 'POST', 
        //     body : JSON.stringify( {  
        //         'mensaje' : 'Holi'
        //     })
        // })
        // .then(function (response){ 
        //     console.log(response.json())
        //     if(response.ok) {  

        //         response.json() 
        //         .then(function(response) {
        //             console.log(response)
        //         });
        //     }
        //     else {
        //         throw Error('Something went wrong');
        //     }
        // })
        // .catch(function(error) {
        //     console.log(error);
        // });
        // $.post("http://127.0.0.1:5050/chatbot",
        //     {
        //         id: 1,
        //         title: "What is AJAX",
        //         body: JSON.stringify({'mensaje':"Holitas"})
        //     },
        //     function (data, status) {
        //         if (status === "success") {
        //             console.log("Post successfully created!")
        //         }
        //     },
        //     "json")
        // $.ajax({
        //     type : 'POST',
        //     url : "http://127.0.0.1:5050/chatbot",
        //     contentType: 'application/json;charset=UTF-8',
        //     data : {'mensaje':"Holitas"}
        //   })
        await fetch(`http://localhost:5050/chatbot/${mensaje}`, options)
            .then(response => {
                console.log(response)
                console.log("--------------")
                if (!response.ok) {

                    throw Error(response.status);
                }
                console.log(response.json)
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
        botAgregaMensaje();
    }

}
function botAgregaMensaje() {
    // chat del chatbot-----------------------
    const div1 = document.createElement("div");
    div1.className = "media media-chat"

    const img = document.createElement("img")
    img.className = "avatar"
    img.src = "https://img.icons8.com/color/344/bmo.png"
    img.alt = "..."
    const p1 = document.createElement("p")
    p1.textContent = "holi esto es una prueba che "

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