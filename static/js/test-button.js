
let increments = document.getElementsByClassName('btn-increment');
let decrements = document.getElementsByClassName('btn-decrement');
let counter = document.querySelectorAll(".numb");

for (let j=0; j<counter.length; j++){
    let value = counter[j].innerHTML
    console.log(value)
    
for (let i=0; i < increments.length; i++){
    increments[i].addEventListener("click", function() {
        value++;
        counter[j].innerHTML = value;
        console.log(counter)
        });
    }
    
    for (let i=0; i < decrements.length; i++){
    decrements[i].addEventListener("click", function() {
        value--;
        // console.log(counter);
        counter[j].innerHTML = value;
    });
    }
}

// let value = counter[0].innerHTML // iterate over array [0],[1]

// console.log(value);

// for (let i=0; i < increments.length; i++){
// increments[i].addEventListener("click", function() {
//     value++;
//     counter[i].innerHTML = value;
//     console.log(counter)
//     });
// }

// for (let i=0; i < decrements.length; i++){
// decrements[i].addEventListener("click", function() {
//     value--;
//     // console.log(counter);
//     counter[i].innerHTML = value;
// });
// }