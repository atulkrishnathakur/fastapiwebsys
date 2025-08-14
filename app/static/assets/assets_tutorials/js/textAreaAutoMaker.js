var ttrlTextArea = document.getElementsByClassName("ttrl-textarea");
 
function aktTextArea(textAreaObj){
    textAreaObj.style.cssText="height:auto; padding-bottom:25px;";
    textAreaObj.style.cssText = 'height:' + textAreaObj.scrollHeight + 'px';
}


function aktTextAreaOnLoad(){

	let ttrlTextAreaEle = document.getElementsByClassName("ttrl-textarea");
	
	for(let i=0;i < ttrlTextAreaEle.length; i++){
    ttrlTextAreaEle[i].style.cssText="height:auto; padding-bottom:25px;";
    ttrlTextAreaEle[i].style.cssText = 'height:' + ttrlTextAreaEle[i].scrollHeight + 'px;';
	}
}

 
 /*var textarea = document.querySelector('#ttrl-textarea');

textarea.addEventListener('keydown', autosize);
             
function autosize(){
  var el = this;
  setTimeout(function(){
    el.style.cssText = 'height:auto; padding:0';
    // for box-sizing other than "content-box" use:
    // el.style.cssText = '-moz-box-sizing:content-box';
    el.style.cssText = 'height:' + el.scrollHeight + 'px';
  },0);
}*/