const chat = document.getElementById("chat");
const messageInput = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");


function adicionarMensagem(remetente, mensagem) {

    const message = document.createElement("div");

    message.classList.add("message");

    if (remetente === "user") {
        message.classList.add("user");
    } else {
        message.classList.add("bot");
    }

    const content = document.createElement("div");

    content.classList.add("message-content");

    const nome = document.createElement("strong");

    nome.textContent = remetente === "user"
        ? "Você"
        : "PokeAssist";

    const texto = document.createElement("p");

    texto.textContent = mensagem;

    content.appendChild(nome);
    content.appendChild(texto);

    message.appendChild(content);

    chat.appendChild(message);

    chat.scrollTop = chat.scrollHeight;
}


async function enviarMensagem() {

    const mensagem = messageInput.value.trim();

    if (!mensagem) {
        return;
    }

    adicionarMensagem("user", mensagem);

    messageInput.value = "";

    sendButton.disabled = true;
    messageInput.disabled = true;

    try {

        const resposta = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                mensagem: mensagem
            })

        });

        if (!resposta.ok) {
            throw new Error("Erro ao comunicar com o servidor.");
        }

        const dados = await resposta.json();

        adicionarMensagem(
            "bot",
            dados.resposta
        );

    } catch (erro) {

        console.error(erro);

        adicionarMensagem(
            "bot",
            "Desculpe, ocorreu um erro ao processar sua mensagem."
        );

    } finally {

        sendButton.disabled = false;
        messageInput.disabled = false;

        messageInput.focus();
    }
}


sendButton.addEventListener(
    "click",
    enviarMensagem
);


messageInput.addEventListener(
    "keydown",
    function (event) {

        if (event.key === "Enter") {
            enviarMensagem();
        }

    }
);