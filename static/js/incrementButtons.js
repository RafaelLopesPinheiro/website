function incrementButton(){
    var element = document.getElementById('incrementText');
    var value = element.innerHTML;

    ++value

    if (value>4){
        document.getElementById('incrementText').innerHTML = --value
    }

    console.log(value)
    document.getElementById('incrementText').innerHTML = value;
}


function decrementButton(){
    var element = document.getElementById('incrementText');
    var value = element.innerHTML;

    --value

    if (value<0) {
        document.getElementById('incrementText').innerHTML = ++value;

    }

    document.getElementById('incrementText').innerHTML = value;


}


