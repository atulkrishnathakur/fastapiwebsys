var editorFrm =  document.getElementById('editorFrm');
 var textArea = document.getElementById("textArea");
 var textAreaCode = "";
 var akt_encode ="";
 var akt_decode="";
 editorFrm.onsubmit = function(){
     
     textAreaCode = textArea.value;
    
    akt_encode = window.btoa(textAreaCode);// window.btoa() work same as base64_encode() of php
    
    textArea.value = akt_encode; 
        
   
 };
 
 function programDecoder(){  
    akt_encode = textArea.value;
    
    akt_decode = window.atob(akt_encode); // window.atob() work same as base64_decode();
    
    textArea.value = akt_decode;
     
}

programDecoder();







  /*editorFrm.onclick = function(){  
    akt_encode = textArea.value;
    
    akt_decode = window.atob(akt_encode); // window.atob() work same as base64_decode();
    
    textArea.value = akt_decode;
     
}; 

backInCodeBtn.onclick = function(){
    
     akt_encode = textArea.value;
    
    akt_decode = window.atob(akt_encode); // window.atob() work same as base64_decode();
    
    textArea.value = akt_decode;
}; */

/*
 
   The btoa() method encodes a string in base-64.

This method uses the "A-Z", "a-z", "0-9", "+", "/" and "=" characters to encode the string.

Tip: Use the atob() method to decode a base-64 encoded string.
      
    //////////////////////////////////
    
var str = "Hello World!";
var enc = window.btoa(str);
var dec = window.atob(enc);

var res = "Encoded String: " + enc + "<br>" + "Decoded String: " + dec;
    
 */
