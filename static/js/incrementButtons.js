

var decrements = document.querySelectorAll('.decrement');
var increments = document.querySelectorAll('.increment');
let counter = document.querySelectorAll(".qty-input");


let sum = 0;
for (let i = 0; i < counter.length; i++){
        sum += parseInt(counter[i].innerHTML);
        console.log(sum)
}


decrements.forEach((decrement) => {
    decrement.addEventListener("click",function(e){
        if(sum > 0 && e.target.nextElementSibling.innerHTML > 0){
            e.target.nextElementSibling.innerHTML--;
            sum--;
            
            for (let i = 0; i < increments.length; i++){
                increments[i].disabled = false;
            }
            if (sum == 0){
                for (let i = 0; i < decrements.length; i++){
                    decrements[i].disabled = true;
                }    
            }
            console.log(sum)
        } 
    });
});


increments.forEach((increment) => {
    increment.addEventListener("click",function(e){
        if(sum < 4){
            sum++;
            e.target.previousElementSibling.innerHTML++;
            for (let i = 0; i < decrements.length; i++){
                decrements[i].disabled = false;
            }
            if (sum == 4){
                for (let i=0; i < increments.length; i++){
                    increments[i].disabled = true;
                }
            }

            console.log(sum)
        } 
    });
    
});




