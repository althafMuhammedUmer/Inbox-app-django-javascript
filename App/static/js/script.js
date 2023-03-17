/* ----------------------------------------------
# ALL SCRIPTS HERE IT WILL EXTENDS ALL THE PAGES
------------------------------------------------*/

// 1 ==> Character remaining counter
$(document).ready(function () {
  var start = 0;
  var limit = 1000;

  $("#message").keyup(function () {
    start = this.value.length;
    if (start > limit) {
      return false;
    } else if (start == 1000) {
      $("#remaining")
        .html("Characters remaining: " + (limit - start))
        .css("color", "red");
      swal("Opss !", "Characters limit exceeded !", "info");
    } else if (start > 970) {
      $("#remaining")
        .html("Characters remaining: " + (limit - start))
        .css("color", "red");
    } else if (start < 1000) {
      $("#remaining")
        .html("Characters remaining: " + (limit - start))
        .css("color", "black");
    } else {
      $("#remaining")
        .html("Characters remaining: " + limit)
        .css("color", "black");
    }
  });
});

// 2 ==> Inputmask (only in PHONE i used )
$(document).ready(function () {
  $(".phone").inputmask("(+91) 9999999999", {
    onincomplete: function () {
      swal("Opss !", "Incomplete phone . Please review !", "info");
      $(".phone").val("");
      return false;
    },
  });
});

// 3 ===> (Script to get DATE AND TIME real time)
setInterval(function () {
  var date = new Date();
  $("#clock").html(
    (date.getHours() < 10 ? "0" : "") +
      date.getHours() +
      ":" +
      (date.getMinutes() < 10 ? "0" : "") +
      date.getMinutes() +
      ":" +
      (date.getSeconds() < 10 ? "0" : "") +
      date.getSeconds()
  );
}, 500);

// 4 ===> (Script to update the page always at 0:00)
function autoRefresh(hours, minute, seconds) {
  var now = new Date(),
    then = new Date();
  then.setHours(hours, minute, seconds, 0);
  if (then.getTime() < now.getTime()) {
    then.setDate(now.getDate() + 1);
  }
  var timeout = then.getTime() - now.getTime();
  setTimeout(function () {
    window.location.reload(true);
  }, timeout);
}
autoRefresh(0, 0, 0);

// 5 ==== script to accept until 2mb 'upload file'
$("input[type='file']").on("change", function () {
  if (this.files[0].size > 2000000) {
    //   alert("Please upload file less than 2MB. Thanks!!");
    swal("Attention !", "Maximum allowed size is 2mb", "info");
    $(this).val("");
  }
});

// 6) script to close offcanvas when the logout button is clicked
// $(document).ready(function(){
//     jQuery('#offcanvasRight, .offcanvas-body, a').click(function(){
//         console.log($(this).attr('href'));
//         jQuery('.offcanvas').offcanvas('hide');
//     });
// });

//7) script to show empty message and hide content
$(document).ready(function(){
    var verify = $('#checked_td').length;

    if (verify == 0){
        $(".hide").css('display', 'none');
        $('#msg').text("No message found");
        $('#refresh').html('<i class="fas fa-sync-alt fa-3x"></i>')
    }

});

// 8) script to get time running at realtime
setInterval(function() {
    var date = new Date();
    $('#clock, #mini-clock').html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" +
        (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" + 
        (date.getSeconds() < 10 ? '0' : '') + date.getSeconds() + ":" 
    );
}, 500); 

// 9) script to update the page always at (0:00)
function autoRefresh(h,m,s){
    var now = new Date(), then = new Date();
    then.setHours(h,m,s,0);
    if (then.getTime() < now.getTime()){
        then.setDate(now.getDate() + 1 );
    }
    var timeout = (then.getTime() - now.getTime());

    setTimeout(function() {
        window.location.reload(true);
    }, timeout);
}


