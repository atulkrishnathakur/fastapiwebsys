

var repeat = document.getElementById("repeat");

var programBox = document.getElementsByClassName("program-box");
var programBoxInner = document.getElementsByClassName("program-box-inner");
var outputIframe = document.getElementsByClassName("output-iframe");
var i = 0;
repeat.onclick = function(){
    
    if(i===0){
    programBox[0].style.width="49%";
    programBox[0].style.float="left";
    programBox[0].style.height="100%";
    programBoxInner[0].style.height="400px";
   
    programBoxInner[0].style.overflow="auto";
    programBox[1].style.width="49%";
    programBox[1].style.float="right";
    programBox[1].style.height="100%";
    programBoxInner[1].style.height="400px";
    
    i++;
}
else if(i===1){
  location.reload();
  i--;
}

};

