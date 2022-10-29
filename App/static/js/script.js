/* ----------------------------------------------
# ALL SCRIPTS HERE IT WILL EXTENDS ALL THE PAGES
------------------------------------------------*/

// 1 ==> Character remaining counter
$(document).ready(function(){
    var start = 0;
    var limit = 1000;
    
    $('#message').keyup(function(){
        start = this.value.length
        if(start > limit){
            return false
        }
        else if(start == 1000){
            $('#remaining').html("Characters remaining: " + (limit - start)).css('color','red');
            swal("Opss !", "Characters limit exceeded !", "info")
        }
        else if(start > 970){
            $('#remaining').html("Characters remaining: " + (limit - start)).css('color','red');
            
        }
        else if(start < 1000){
            $('#remaining').html("Characters remaining: " + (limit - start)).css('color','black');
           
        }
        else{
            $('#remaining').html("Characters remaining: " + (limit)).css('color','black');
            
        }

    })

})


// 2 ==> Inputmask (only in PHONE i used )
$(document).ready(function() {
    
    $('.phone').inputmask("(+99) 9999999999", {"onincomplete": function() {
        
        swal("Opss !", "Incomplete phone . Please review !", "info");
        $('.phone').val("");
        return false;
        

    }})
})


