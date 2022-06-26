const clock=document.querySelector(".js-clock");

function init(){
  setInterval(getTime, 1000);
}
function getTime(){
  const today=new Date();
  const hour=today.getHours();
  const minute=today.getMinutes();
  const clockStr=`${hour<10?`0${hour}`:hour
                }:${
                    minute<10?`0${minute}`:minute}`;
  clock.innerText=clockStr;
}
init();
