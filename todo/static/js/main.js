$(function () {
    //https://www.w3schools.com/js/js_cookies.asp
    getCookie = function(cname){
        var name = cname+ "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for(var i=0; i<ca.length; i++){
            var c = ca[i];
            while(c.charAt(0) == ' '){
                c = c.substring(1);
            }
            if (c.indexOf(name) ==0){
            return c.substring(name.length, c.length);
            }
        }
        return "";
    }

    //handler for .ready()  called
    get_summary = function () {
        $.ajax({
            url: "summary"
        }).done(function (summary){
            $('#made_count').text(summary.made),
             $('#kept_count').text(summary.kept)
        })
    }

    send_response = function () {
        let val = $('#userinput').val()
        $('#userinput').parset('.from').replaceWith(`<span class="form">${val}</span>`)
        $.post("message",{message : val})
            .done(function(response) {
                $('#chat main').append(responce);
            })
            .fail(function(response){
                $('#chat main').append(response);
            })
    }

    enable_next_button = function (element) {
        $(element).next('button').prop('disabled', !$(element).val());
    }

    toogle_login_register = function () {
        if ($('#submit').attr('mode') == 'register'){
            $('#submit').attr('mode', "login");
            $('#name_input').addClass('hidden');
            $('#toggle').text('Register with us')
        }
        else{
          $('#submit').attr('mode', "register");
          $("#name_input").removeClass('hidden');
          $('#toggle').text('Have an account, Login')
        }  
    }

 

    auth_submit = function (){
        let date = {
            name: $('#name').val()
        }
    }


    getCookie = function(cname){
        var name = cname+"=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca=decodedCookie.split(';');
        for(var i=0;i<ca.length;i++){
            var c=ca[i];
            while(c.charAt(0)==' '){
                c=c.substring(1);
            }
            if(c.indexOf(name)==0){
                return c.substring(name.length,c.length);
            }
        }
        return "";
    }

    send_response = function(){
        let val=$('#')
    }
})
