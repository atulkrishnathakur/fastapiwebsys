var frmcntr = document.getElementById("sgnup-cntr");
var frm = document.getElementById("sgnupfrm");
var userName = document.getElementById("username");
var email = document.getElementById("email");
var mobile = document.getElementById("mobile");
var pwd = document.getElementById("pwd");
var cpwd = document.getElementById("cpwd");
var dobDay = document.getElementById("dobDay");
var dobMonth = document.getElementById("dobMonth");
var dobYear = document.getElementById("dobYear");
var country = document.getElementById("country");
var gender = document.getElementById("gender");
var genrow = document.getElementById("genrow");
var male = document.getElementById("gen1");
var female = document.getElementById("gen2");
var agreerow = document.getElementById("agreerow");
var agr = document.getElementById("agr");
var smt = document.getElementById("smt");
var rst = document.getElementById("rst");
var namePtr = /^[a-zA-Z ]+$/;
var emailPtr =  /^[^.""''@ ][a-zA-Z0-9!#$%&'*+-/=?^_`{|}~]{1,64}[^.""'' ][@]{1}[a-zA-Z0-9\-]+[.]{1}[a-zA-Z]{2,}$/;//email patter created by atul


var mobilePtr = /^[789]{1}[0-9]{9}$/;
var pwdPtr = /^[a-zA-Z0-9~!@#$%^&*)(-_+=/*?.,<>`;:'"]{9,18}$/;
var countryPtr = /^[a-zA-Z ]+$/;



userName.onfocus = function(){
     var vbox = document.getElementById("vbox1");
     vbox.style.display="block";
     
};
userName.onkeyup = function(){
     var vboxa = document.getElementById("vbox1a"); 
     var vboxb = document.getElementById("vbox1b");
     var vboxc = document.getElementById("vbox1c");
     if(userName.value !== ""){
      vboxa.className = "fa fa-check"; 
     }
     else if(userName.value === ""){
      vboxa.className = "fa fa-times";
      vboxa.style.fontSize = "25px";
     
     }
     if(userName.value.match(namePtr)){
      vboxb.className = "fa fa-check"; 
      
     }
     else if(!userName.value.match(namePtr)){
      vboxb.className = "fa fa-times";
      vboxb.style.fontSize = "25px";
      
     }
    
    var uname = document.getElementById("username");
    var namestr = uname.value;
    var len = namestr.length;
    
    for(var i = 0; i< len; i++){
        if(namestr[i]===" " && namestr[i+1]===" "){
            vboxc.className = "fa fa-times";
            vboxc.style.fontSize = "25px";
            
            break;
            
        }
        else{
            vboxc.className = "fa fa-check";
        }
    }
    
};

userName.onblur = function(){
     var vbox = document.getElementById("vbox1");
     vbox.style.display="none";
};


email.onfocus = function(){
     var vbox = document.getElementById("vbox2");
     vbox.style.display="block";
     
};
email.onkeyup = function(){
     var vboxa = document.getElementById("vbox2a"); 
     var vboxb = document.getElementById("vbox2b");
     if(email.value !== ""){
      vboxa.className = "fa fa-check"; 
     }
     else if(email.value === ""){
      vboxa.className = "fa fa-times";
      vboxa.style.fontSize = "25px";
      
     }
     if(email.value.match(emailPtr)){
      vboxb.className = "fa fa-check"; 
      
     }
     else if(!email.value.match(emailPtr)){
      vboxb.className = "fa fa-times";
      vboxb.style.fontSize = "25px";
      
      
     }
     
};

email.onblur = function(){
     var vbox = document.getElementById("vbox2");
     vbox.style.display="none";
};

mobile.onfocus = function(){
     var vbox = document.getElementById("vbox3");
     vbox.style.display="block";
     
};
mobile.onkeyup = function(){
     var vboxa = document.getElementById("vbox3a"); 
     var vboxb = document.getElementById("vbox3b");
     if(mobile.value !== ""){
      vboxa.className = "fa fa-check"; 
     }
     else if(mobile.value === ""){
      vboxa.className = "fa fa-times";
      vboxa.style.fontSize = "25px";
      
     }
     if(mobile.value.match(mobilePtr)){
      vboxb.className = "fa fa-check"; 
      
     }
     else if(!mobile.value.match(mobilePtr)){
      vboxb.className = "fa fa-times";
      vboxb.style.fontSize = "25px";
      
     
     }
     
};

mobile.onblur = function(){
     var vbox = document.getElementById("vbox3");
     vbox.style.display="none";
};


pwd.onfocus = function(){
     var vbox = document.getElementById("vbox4");
     vbox.style.display="block";
     
};
pwd.onkeyup = function(){
     var vboxa = document.getElementById("vbox4a"); 
     var vboxb = document.getElementById("vbox4b");
     if(pwd.value !== ""){
      vboxa.className = "fa fa-check"; 
     }
     else if(pwd.value === ""){
      vboxa.className = "fa fa-times";
      vboxa.style.fontSize = "25px";
      
     }
     if(pwd.value.match(pwdPtr)){
      vboxb.className = "fa fa-check"; 
      
     }
     else if(!pwd.value.match(pwdPtr)){
      vboxb.className = "fa fa-times";
      vboxb.style.fontSize = "25px";
      
     
     }
     
};

pwd.onblur = function(){
     var vbox = document.getElementById("vbox4");
     vbox.style.display="none";
};



cpwd.onfocus = function(){
     var vbox = document.getElementById("vbox5");
     vbox.style.display="block";
     
};
cpwd.onkeyup = function(){
     var vboxa = document.getElementById("vbox5a"); 
     var vboxb = document.getElementById("vbox5b");
     if(cpwd.value !== ""){
      vboxa.className = "fa fa-check"; 
     }
     else if(cpwd.value === ""){
      vboxa.className = "fa fa-times";
      vboxa.style.fontSize = "25px";
      
     }
     
     
     if(cpwd.value === pwd.value){
      vboxb.className = "fa fa-check"; 
      
     }
     else if(cpwd.value !== pwd.value){
      vboxb.className = "fa fa-times";
      vboxb.style.fontSize = "25px";
     }
     
};

cpwd.onblur = function(){
     var vbox = document.getElementById("vbox5");
     vbox.style.display="none";
};

rst.onclick = function(){
    var rstcnf = confirm("Want to reset form? ");
     if(rstcnf===false){
        return false; 
     }
};
frm.onsubmit = function(){
    var smtcnf = confirm("Want submit form?");
    if(smtcnf===true){
         if(userName.value===""){
             return false;
         }
         else if(!userName.value.match(namePtr)){
           
          return false;  
        }
      if(email.value === ""){
          return false;
      }
      else if(!email.value.match(emailPtr)){
         return false;  
      }
      
      if(mobile.value === ""){
          return false;
      }
      else if(!mobile.value.match(mobilePtr)){
        return false;   
      }
      
     if(pwd.value === ""){
         return false;
     } 
     else if(!pwd.value.match(pwdPtr)){
       return false;  
     }
     
     
     
     if(cpwd.value === ""){
         return false;
     }
     else if(cpwd.value !== pwd.value){
       return false;  
     }
     
        
    } 
    
    else{
         
        return false;
    }
};