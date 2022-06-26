const weatherContainer=document.querySelector('.js-weather');
const weather=weatherContainer.querySelector('.weather');
const place=weatherContainer.querySelector('.place');
const API_KEY='a1cfa3171179e182f6c77b500b2372f9';
const LOCAL_COORDS_LS='localCoords';
let longitude
function init(){
  const loadedCoords=getGeoFromLS();
  if(loadedCoords!==null){
    const parsedCoords=JSON.parse(loadedCoords);
    getWeather(parsedCoords);
  }else{
    const coords=navigator.geolocation.getCurrentPosition(handleSuccess,handleError);
  }
}

function getGeoFromLS(){
  return localStorage.getItem(LOCAL_COORDS_LS);
}
function getWeather(coords){
  const long=coords.long;
  const lat=coords.lat;
  fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${long}&appid=${API_KEY}&units=metric`
  ).then((res)=>{
    return res.json();
  }).then((json)=>{
    const temperature=json.main.temp;
    const placeName=json.name;
    weather.innerText=`${temperature}°C`;
    place.innerText=placeName;
});
}

function handleSuccess(loca){
  const coords={
    long:loca.coords.longitude,
    lat:loca.coords.latitude
  }
  localStorage.setItem(LOCAL_COORDS_LS,JSON.stringify(coords));
  getWeather(coords);
}
function handleError(err){
}
init();
