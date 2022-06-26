const usrContainer=document.querySelector(".js-usrName");
const usrInputForm=usrContainer.querySelector("form");
const usrInput=usrInputForm.querySelector("input");
const mouseEvent=usrContainer.querySelector(".mouseEvent");
const greeting=mouseEvent.querySelector(".greeting");
const delOpt=mouseEvent.querySelector(".deleteOpt");

const USR_NAME_LS='usrName';
const HIDDEN_CLS='hidden';
function init(){
  if(getFromLS(USR_NAME_LS)===null){
    usrInputForm.addEventListener('submit',handleSubmit);
    waitForInput();
  }else{
    paintGreeting();
  }
  const delBtn=delOpt.querySelector("button");
  delBtn.addEventListener('click',(e)=>{
    removeFromLs(USR_NAME_LS);
    waitForInput();
  });
}
function handleSubmit(e){
  e.preventDefault();
  saveAtLS(usrInput.value);
  usrInput.value="";
  paintGreeting();
}
function waitForInput(){

  mouseEvent.classList.add(HIDDEN_CLS);
  usrInputForm.classList.remove(HIDDEN_CLS);
}

function removeFromLs(key){
  localStorage.removeItem(key);
}
function saveAtLS(text){
  localStorage.setItem(USR_NAME_LS,text);
}
function getFromLS(key){
  return localStorage.getItem(key);
}
function paintGreeting(){
  mouseEvent.classList.remove(HIDDEN_CLS);
  usrInputForm.classList.add(HIDDEN_CLS);
  const loadedUserName=getFromLS(USR_NAME_LS);
  const greetStr=`Welcome back, ${loadedUserName}`;
  greeting.innerText=greetStr;
  mouseEvent.addEventListener('mouseover',usrNameShowOpts);
  mouseEvent.addEventListener('mouseout',usrNameHideOpts);
}
function usrNameShowOpts(e){
  greeting.classList.add("hidden");
  delOpt.classList.remove("hidden");
}
function usrNameHideOpts(e){
  greeting.classList.remove("hidden");
  delOpt.classList.add('hidden');
}
init();
