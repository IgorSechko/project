
// Функция ymaps.ready() будет вызвана, когда
// загрузятся все компоненты API, а также когда будет готово DOM-дерево.
ymaps.ready(init);
var Circles = [null, null, null];
var curPlace = null;
function init() {
	myMap = new ymaps.Map("map", {
		center: [55.00, 37.00],
		zoom: 4,
		controls: ['rulerControl', 'zoomControl', 'typeSelector', 'fullscreenControl']
	});
	var button = new ymaps.control.Button({ data: { content: 'Добавить / снять выделение' }, options: { maxWidth: 200 } });
	button.events.add('click', function (e) {
		var pixels = document.getElementsByClassName("ymaps-2-1-77-scaleline")[0].style.width;
		var distance = document.getElementsByClassName("ymaps-2-1-77-scaleline__label")[0].innerHTML;
		var factor = 1000;
		if (!distance.includes("км")) {
			factor = 1;
		}
		var widthInMeters = factor * 750 * parseInt(distance, 10) / parseInt(pixels, 10);
		var radius = widthInMeters / 7;
		if (!Circles[curPlace - 1]) {
			Circles[curPlace - 1] = new ymaps.Circle([
				myMap.getCenter(),
				radius
			], {}, {
				fillColor: "#007BFF33",
				strokeColor: "#007BFF",
				strokeOpacity: 0.8,
				strokeWidth: 4
			});
			myMap.geoObjects.add(Circles[curPlace - 1]);
			Circles[curPlace - 1].editor.startEditing();
		} else {
			myMap.geoObjects.remove(Circles[curPlace - 1]);
			Circles[curPlace - 1] = null;
		}
	});
	myMap.controls.add(button);
}
function makeCircleVisible() {
	if (Circles[curPlace - 1]) {
		myMap.geoObjects.add(Circles[curPlace - 1]);
		Circles[curPlace - 1].editor.startEditing();
	}
}
function setCurPlace(arg) {
	curPlace = arg;
}
function nullCurPlace() {
	curPlace = null;
}
function saveData() {
	place_x = document.getElementsByName(`place${curPlace}_x`)[0];
	place_y = document.getElementsByName(`place${curPlace}_y`)[0];
	place_radius = document.getElementsByName(`place${curPlace}_radius`)[0];
	if (Circles[curPlace - 1]) {
		place_x.value = Circles[curPlace - 1].geometry.getCoordinates()[0].toString();
		place_y.value = Circles[curPlace - 1].geometry.getCoordinates()[1].toString();
		place_radius.value = Circles[curPlace - 1].geometry.getRadius().toString();
		myMap.geoObjects.remove(Circles[curPlace - 1]);
	} else {
		place_x.value = "";
		place_y.value = "";
		place_radius.value = "";
	}
	nullCurPlace();
}





//   function handleDataformSubmit(event){
//     event.preventDefault()
//     const myForm = event.target //thr form element
//     const myCard = new Card(myForm)
//     // for(let [name, value] of myCard) {
//     //   alert(`${name} = ${value}`); 
//     // }
//     console.log(myCard)
//     const url = myForm.getAttribute("action")
//     const method = myForm.getAttribute("method")
//     const xhr = new XMLHttpRequest()
//     const responseType = "json"
//     xhr.responseType = responseType
//     xhr.open(method, url)
//     xhr.send(myCard)
//   }
//   const formcreateEl = document.getElementById("dataform-form")
//   formcreateEl.addEventListener("submit",handleDataformSubmit)