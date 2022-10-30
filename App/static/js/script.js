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

// 3 ===> (Script to get DATE AND TIME real time)
setInterval(function() {
    var date = new Date();
    $('#clock').html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" +
        (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" +
        (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()

    );
}, 500);


// 4 ===> (Script to update the page always at 0:00)
function autoRefresh(hours, minute, seconds){
    var now = new Date(), then = new Date();
    then.setHours(hours, minute, seconds, 0);
    if(then.getTime() < now.getTime()) {
        then.setDate(now.getDate() + 1);

    }
    var timeout = (then.getTime() - now.getTime());
    setTimeout(function() {
        window.location.reload(true)

    }, timeout);

}
autoRefresh(0,0,0)



