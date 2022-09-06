function incrementButton(id){
    var element = document.getElementsByClassName(id);
    var value = element.innerHTML;
    console.log(element)
    

    if (value>3){
        document.getElementById(id).innerHTML = value
    } else{
        value++
    }
    
    
    console.log(value)
    document.getElementById(id).innerHTML = value;
}


function decrementButton(){
    var element = document.getElementById('id_acompanhamentos_0');
    var value = element.innerHTML;

    --value

    if (value<0) {
        document.getElementById('id_acompanhamentos_0').innerHTML = ++value;

    }

    document.getElementById('id_acompanhamentos_0').innerHTML = value;

    console.log(value)
}


// function test(){
//     var string = ''
//     for (var i=0; i<=10; i++){
//         string += "<p id='opcao_"+i+"'>TESTANDO O LOOP</p>"
        
//     }
//     document.getElementById('f'),innerHTML = string
// }
