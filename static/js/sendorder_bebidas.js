import { Api } from "./api_bebidas.js";

const acompList = document.getElementById("id_bebidas_1");
console.log(acompList.childElementCount);

class sendOrder {

    static async sendOrderData() {
        const acompList = document.getElementById("id_bebidas");
        const acompQty = acompList.childElementCount;
        // const acompQty = 1
        let acomps = []

        for(let i = 0; i < acompQty; i++) {
            let acomp = {
                name: document.getElementById("id_bebidas_" + i).value,
                value: document.getElementById("id_bebidas_" + i).checked
            }

            acomps.push(acomp)
        }

        
        const response = await Api.sendOrder(acomps);

        // console.log(response)
    }
}

function loadSendButtonEvent() {
    const sendButton = document.getElementById("sendOrderButton");
    
    sendButton.addEventListener("click", event => {
        // event.preventDefault()

        sendOrder.sendOrderData()
    })
}

loadSendButtonEvent()