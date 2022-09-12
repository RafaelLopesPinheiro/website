
var decrements = document.querySelectorAll('.btn-decrement');
var increments = document.querySelectorAll('.btn-increment');
let counter = document.querySelectorAll(".numb");

let sum = 0;
for (let i = 0; i < counter.length; i++){
        sum += parseInt(counter[i].innerHTML);
        console.log(counter[i].innerHTML)
};


decrements.forEach((decrement) => {
    decrement.addEventListener("click",function(e){
        if(sum > 0){
            e.preventDefault()
            e.target.nextElementSibling.innerHTML--;
            sum--;
        } else {
            // delete the item, etc
        }
    });
});

increments.forEach((increment) => {
    increment.addEventListener("click",function(e){
        if(sum>=4){
            increments.disabled = true;
        } else {
            e.preventDefault()
            e.target.previousElementSibling.innerHTML++;
            sum++;
        };
    });
    
});