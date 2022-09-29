export class Api {

    static baseUrl = "http://127.0.0.1:8000/";
    static header = {
        "Content-Type": "application/json",
        "X-CSRFToken": localStorage.getItem("CSRFToken"),
        
    };
    

    static async sendOrder(data) {
        const url = this.baseUrl + "quentinhas/" + window.location.href.split('/')[4];
        // var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        // console.log(csrftoken)
        const requestData = {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": localStorage.getItem("CSRFToken")
            },
            url: url,
            
        };
        console.log(requestData)
        return await fetch(url, requestData).then(res => res.json());
    }
}


