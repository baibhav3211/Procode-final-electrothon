// Revele on Scroll

var controller = new ScrollMagic.Controller();
var revealElements = document.getElementsByClassName("service");
                
for (var i=0; i<revealElements.length; i++) { // create a scene for each element
    new ScrollMagic.Scene({
        triggerElement: revealElements[i], // y value not modified, so we can use element as trigger as well
        offset: 50,												 // start a little later
		triggerHook: 0.9,
		})
		.setClassToggle(revealElements[i], "visible") // add class toggle
		.addTo(controller);
}
        
var nIntervId = setInterval(navColorChange, 10);
function navColorChange(){
    if($(window).scrollTop() > 10){
        $('nav').css('backgroundColor', '#f9f9f9');
    }else{
        $('nav').css('backgroundColor', 'white');
    }
};

