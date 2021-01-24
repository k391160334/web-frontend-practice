const toDOContainer=document.querySelector(".js-toDoList");
const toDoInputForm=toDOContainer.querySelector("form");
const toDoInput=toDoInputForm.querySelector("input");
const list=toDOContainer.querySelector('ul');
const TODOS_LS='toDos';
const LAST_ID_LS='lastId'
//const HIDDEN_CLS='hidden';
let toDos=[];
let lastId=0;
function init(){
  loadToDos();
  loadLastId();
  if(toDos!==null){
    toDos.forEach((toDo)=>{
      paintToDo(toDo);
    });
  }
  toDoInputForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    const toDo=createToDo(toDoInput.value);
    toDoInput.value="";
    addToList(toDo);
    saveListAtLS();
    saveLastIdAtLS();
    paintToDo(toDo);
  });
}
function addToList(toDo){
  toDos.push(toDo);
}
function saveListAtLS(){
  const list=JSON.stringify(toDos);
  localStorage.setItem(TODOS_LS,list);
}
function saveLastIdAtLS(){
  localStorage.setItem(LAST_ID_LS,lastId);
}
function loadLastId(){
  const id=localStorage.getItem(LAST_ID_LS);
  if(id===null){
    console.log('empty lastId');
    return;
  }
  lastId=parseInt(id);
}
function createToDo(text){
  const toDo={
    id:++lastId,
    text:text
  };
  return toDo;
}
function loadToDos(){
  //from LS to list
  const ls=localStorage.getItem(TODOS_LS);
  if(ls===null){
    console.log('empty ls');
    return;
  }
  toDos=JSON.parse(ls);
}
function paintToDo(toDo){
  const li=document.createElement("li");
  li.addEventListener('mouseenter',toDoShowOpts);
  li.addEventListener('mouseleave',toDoHideOpts);
  const span=document.createElement('span');
  span.innerText=toDo.text;
  const delBtn=document.createElement('button');
  delBtn.innerText='❌';
  delBtn.addEventListener('click',handleDelete);
  delBtn.classList.add(HIDDEN_CLS);
  li.appendChild(span);
  li.appendChild(delBtn);
  li.id=toDo.id;
  list.appendChild(li);
}
function toDoShowOpts(e){
  //console.log(e.target.childNodes[1]);
  const delBtn=e.target.childNodes[1];
  delBtn.classList.remove(HIDDEN_CLS);
}
function toDoHideOpts(e){
  const delBtn=e.target.childNodes[1];
  delBtn.classList.add(HIDDEN_CLS);
}
function handleDelete(e){
  const li=e.target.parentNode;
  //del from html
  list.removeChild(li);
  //del from List
  toDos=toDos.filter((toDo)=>{
    return toDo.id!==parseInt(li.id);
  });
  //save list
  saveListAtLS();
}
init();
