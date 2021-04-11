

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');



function Postlike(slug){
    console.log(slug);
    $.ajax({
        url: `/Book/${slug}/like/`,
        type:'post',
        data:{
            like:'1',
            csrfmiddlewaretoken:csrftoken
        },
        success:function(response){
            console.log(response.data);
            if (response.data == "likeC"){
                // console.log("лайк уже есть");
                let jet = $('<p class = "alreadyLiked float-right bg-primary text-warning h3 p-1" style=" text-shadow: 2px 2px #FF0000"></p>').text("Уже есть лайк")
                $('.likebuttonDiv').append(jet)
                $('.likebutton').remove()
                $('.likeCount').text(response.countLike)


            }
        }


    })
}