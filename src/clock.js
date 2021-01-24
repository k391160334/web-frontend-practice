const clock=document.querySelector(".js-clock");
const today=new Date();

function init(){
  const hour=today.getHours();
  const minute=today.getMinutes();
  setInterval(getTime, 1000);
}
function getTime(){
  const hour=today.getHours();
  const minute=today.getMinutes();
  const clockStr=`${hour<10?`0${hour}`:hour
                }:${
                    minute<10?`0${minute}`:minute}`;
  clock.innerText=clockStr;
}
init();
