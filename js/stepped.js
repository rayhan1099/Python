const a=4000;
if (a>=5000){
    const discount=a*10/100;
    const payamount=a-discount;
    console.log(payamount);
}
else if(a>2500){
    const discount=a*5/100;
    const payamount=a-discount;
    console.log(payamount)
}
else{
    console.log("You did not get any kind of discount")
}
const age=12;
age>=18?console.log("Vot dite parba"):console.log("Tumi vot dite parbana");
const isleader=false;
a=isleader===true?price>1000?price/2:0:price+200;