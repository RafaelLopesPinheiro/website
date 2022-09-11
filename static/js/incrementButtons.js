

function incrementButton(arg){
        
        var element = document.getElementById(arg);
        var value = element.innerHTML;
        var button = document.getElementsByClassName('btn-success');
        var quant = document.getElementsByClassName('qty-input');
        var value2 = quant[0].innerHTML;


        console.log(value2);
        console.log(element);
        let sum = 1;
        for (let i = 0; i < quant.length; i++){
                sum += parseInt(quant[i].innerHTML);
        };

        console.log(sum);
        
        
        if (sum>=4){
                // quant.innerHTML = value++;
                element.innerHTML = value++; 
                for(let i = 0; i < button.length; i++) {
                        button[i].disabled = true;
                }
            } else{             
                value++;
            }
        element.innerHTML = value ;

}




function decrementButton(arg){
        var element = document.getElementById(arg);
        var button = document.getElementsByClassName('btn-success');
        var value = element.innerHTML;

        
        if (value<1) {
                element.innerHTML = value;
            } else {
                for(let i = 0; i < button.length; i++) {
                        button[i].disabled = false;
                        
                }

                value--;

            }
        

        console.log(value);
        element.innerHTML = value;
        
        }
        
        

