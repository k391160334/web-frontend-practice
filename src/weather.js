const API_KEY='a1cfa3171179e182f6c77b500b2372f9';
let longitude
function init(){
  const coords=navigator.geolocation.getCurrentPosition(handleSuccess,handleError);

}
function getWeather(long,lat){
  fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${long}&appid=${API_KEY}&units=metric`
  ).then((res)=>{
    return res.json();
  }).then((json)=>{
    console.log(json);
});
}

function handleSuccess(loca){
  console.log(loca);
  getWeather(loca.coords.longitude,loca.coords.latitude);
}
function handleError(err){
  console.log(err);
}
init();
