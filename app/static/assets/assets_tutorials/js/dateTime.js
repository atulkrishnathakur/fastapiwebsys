
	 
	     var watch = document.getElementById("watch");
	     
	      
              
                 setInterval(sabblaWatch,1000);
		    
              

         
	   function sabblaWatch(){
	   
	      
	       var dt = new Date();
	                 
	                 var sec = dt.getSeconds();
                
			var mn = dt.getMinutes();
			var hrs = dt.getHours();
	                
	      watch.innerHTML = hrs+" : "+mn+" : "+sec;
	   }
	
        
        
        
        var showdate = document.getElementById("showdate");
        
        setInterval(sabblaDate,1000);
        
        function sabblaDate(){
	   var dt = new Date();
           var d = dt.getDate();
           var m = dt.getMonth();
           var day = dt.getDay();
           var y = dt.getFullYear();
          
          
          
          switch(day){
               case 0:
                day="Sun";
               break;
               
               case 1:
                day="Mon";
               break;
               
               case 2:
                day="Tue";
               break;
               
               case 3:
                day="Wed";
               break;
               
               case 4:
                day="Thu";
               break;
               
               case 5:
                day="Fri";
               break;
               
               case 6:
                day="Sat";
               break;
                              
           }
          
          showday.innerHTML = day; 
           
           
           switch(m){
               case 0:
                m="Jan";
               break;
               
               case 1:
                m="Feb";
               break;
               
               case 2:
                m="Mar";
               break;
               
               case 3:
                m="Apr";
               break;
               
               case 4:
                m="May";
               break;
               
               case 5:
                m="Jun";
               break;
               
               case 6:
                m="Jul";
               break;
               
               case 7:
                m="Aug";
               break;
               
               case 8:
                m="Sep";
               break;
               
               case 9:
                m="Oct";
               break;
               
               case 10:
                m="Nov";
               break;
               
               case 11:
                m="Dec";
               break;
               
               
               
           }
           
           
           showdate.innerHTML = d+" "+m+", "+y;
           
        }
      
