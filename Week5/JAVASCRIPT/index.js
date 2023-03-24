
//let age =0
let msg =""

function add_numbers(num1, num2)
{
    return num1 + num2
}
console.log("Javascriot console testing")
document.getElementById("confirm_btn").onclick=function check_age(){
console.log("Button clicked!")
    var age=document.getElementById("age").innerHTML.valueOf()
    console.log(age)

if(age<=18){
    msg= "You are not allowed" 
    document.getElementById("get_in").innerHTML=msg

}else{
    msg ="Welcome to the club"
    document.getElementById("get_in").innerHTML=msg
}

