

var decrements = document.querySelectorAll('.decrement');
var increments = document.querySelectorAll('.increment');
let counter = document.querySelectorAll(".qty-input");
let value = counter.innerHTML;


let sum = 0;
for (let i = 0; i < counter.length; i++){
        sum += parseInt(counter[i].innerHTML);
        console.log(sum)
}


decrements.forEach((decrement) => {
    decrement.addEventListener("click",function(e){
        if(sum > 0){
            e.preventDefault();
            e.target.nextElementSibling.innerHTML--;
            sum--;
            for (let i=0; i < increments.length; i++){
            increments[i].disabled = false;
            }
            console.log(sum)
        } else {
            e.target.nextElementSibling.innerHTML;
            e.preventDefault();
        };
    });
});


increments.forEach((increment) => {
    increment.addEventListener("click",function(e){
        if(sum>=4){
                e.preventDefault()
                e.target.previousElementSibling.innerHTML;
                for (let i=0; i < increments.length; i++){
                        increments[i].disabled = true;
                }
        } else {
            e.preventDefault()
            sum++;
            e.target.previousElementSibling.innerHTML++;
            console.log(sum)
        };
    });
    
});





// OLD VERSION WITH ONCLICK ARGUMENT //

// function incrementButton(arg){
        
//         var element = document.getElementById(arg);
//         var value = element.innerHTML;
//         var button = document.getElementsByClassName('btn-success');
//         var quant = document.querySelectorAll('.qty-input');

        
//         // console.log(element);
//         let sum = 1;
//         for (let i = 0; i < quant.length; i++){
//                 sum += parseInt(quant[i].innerHTML);
//         };

//         // console.log(sum);
        
        
//         if (sum>=4){
//                 // quant.innerHTML = value++;
//                 element.innerHTML = value++; 
//                 for(let i = 0; i < button.length; i++) {
//                         button[i].disabled = true;
//                 }
//             } else{             
//                 value++;
//             }
//         element.innerHTML = value ;

// }




// function decrementButton(arg){
//         var element = document.getElementById(arg);
//         var button = document.getElementsByClassName('btn-success');
//         var value = element.innerHTML;

        
//         if (value<1) {
//                 element.innerHTML = value;
//             } else {
//                 for(let i = 0; i < button.length; i++) {
//                         button[i].disabled = false;
                        
//                 }

//                 value--;

//             }
        

//         console.log(value);
//         element.innerHTML = value;
        
//         }
        
        

