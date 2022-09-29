import { Api } from "./api.js";

class sendOrder {

    static async sendOrderData() {
        const acompList = document.getElementById("acomp_list");
        const acompQty = acompList.childElementCount;

        let acomps = []

        for(let i = 0; i < acompQty; i++) {
            let acomp = {
                amount: document.getElementById("acomp_qty_" + i).innerHTML,
                name: document.getElementById("acomp_name_" + i).innerHTML
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
        event.preventDefault()

        sendOrder.sendOrderData()
    })
}
console.log(window.location.href.split('/')[4])
loadSendButtonEvent()