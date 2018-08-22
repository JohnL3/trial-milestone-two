let myAlert = true;
// used for when user clicks to close browser window
// i need to remove user from user list of other users online
window.onbeforeunload  = function(e) {
    if (myAlert === true) {
        let user = $('#username').text();
        clearScreen();
        let dialoug = 'Clearing your username from server';
        socket.emit('exitgame', user);
        e.returnValue = dialoug;
        return dialoug;
    }
    myAlert = true;
};

// basic set up of socketio and message to say its working
let socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
socket.on('connect', function(){
    socket.emit('message',{'message': 'Up and running'});
});

socket.on('message', function(msg){
      console.log(msg);
  });

// when user clicks exit game this fires exitgame and removes user from user list of all users online
$('#instruct').on('click', function(){
  let user = $('#username').text();
  console.log('USER',user);
  socket.emit('exitgame', user);
  myAlert = false;
});

//updates the view of user score for all users online
socket.on('my_score', function(json){
  let score = json.score;
  let user = json.user;
  $('.single.'+user).text(score);
});

//shows users who are online and who leave
socket.on('in_out_game', function(json){
    let online = $('#online-users');
    online.html('');
    let users = json.data;
    
    console.log('in_out_game',json.data);
    let user = Object.keys(users);
   
    for (let key in user) {
     let span =`<span class="user usr-name">`+users[user[key]].username+`</span>
        <span class="user usr-life">`+3+`</span>
        <span class="user usr-score ` + users[user[key]].username + `">`+users[user[key]].score+`</span>`;
        online.append(span);
    }

});

//shows the leaderboard
socket.on('leaders', function(json){
  console.log(json.data);
  let data = json.data;
  let lead = $('.lead');
  
  lead.html('');
  
  for (let item in data) {
    let ind = '<span class="user lead">'+(+item +1)+'</span>';
     $('#leader-board').append(ind);
    for(let val in data[item]) {
      let span = '<span class="user lead">'+data[item][val]+'</span>';
      $('#leader-board').append(span);
    }
  }
});


//***********************************************************************

// called if browser window is being closed 
function clearScreen() {
  $('#you-left').text('You closed tab, Needed to clear you from online users. If you didnt mean to leave, click quit game and rejoin.');
  $('.sqr-con').css('display','none');
  $('')
}

let window_width = $( window ).width();

//used to hide landscape orentitation on desktops 
if(window_width >1100) {
  $('#md-screen-con').removeClass('sm-screen-con');
}


$('.close-instructions').click(function(){
  $('.game-instructions').css('display','none');
});

$('#burger').click(function(){

   if($('aside').css('left') === '-245px') {
        $('aside').animate({left: '0'})
   } else {
       $('aside').animate({left: '-245px'})
   }
});

//used to overrid way media query shows page at smaller sizes
//so if desktop is small and then set to full size aside panel opens
$( window ).resize(function() {
  if($(window).width() > 657) {
	  $('aside').css('left','0');
  } else {
	  $('aside').css('left','-245px');
  }
});

 

// post subject choice to server which returns a question to be answered
$('.sqr').click(function(e){
  if(!$(this).hasClass('answered')) {
      let clickedOn = $(this).attr('id');
      $(this).css('background','#607D8B')
      console.log(clickedOn);
      let data = {"quest_id": clickedOn};
      $.ajax({
        type : 'POST',
        url : "http://question-answer-johnl3.c9users.io/questions",
        contentType: 'application/json;charset=UTF-8',
        dataType: 'json',
        data : JSON.stringify(data),
        success: function(d){
            console.log(d);
            previousData = d;
            createQA(d,clickedOn);
            $('.q-a-outer').css('display','flex');
        }
      });
  }
});

let previousData;
let answers = [];



// post answer to question to server 
$('#ans-button').click(()=>{
  
  let _id = $('.surround').attr('id');
  
  if(Object.getOwnPropertyNames(previousData).length > 2) {
    $('input:checkbox:checked').each(function() {
      answers.push($(this).val());
    });
    
    let answerData = {
      questionId: _id,
      answer: answers
    };
    if(answers.length > 0){
    console.log('answerData',answerData);
    postAnswers(answerData);
    } else {
      $('.error-msg').css('display','flex');
      setTimeout(function(){
        $('.error-msg').css('display','none');
      },3000);
    }
  } else {
    let answers = $('.ans-inp').val().split(/[\\,]\s|[\s\\,]/);
    if(answers != '') {
      let answerData = {
        'questionId': _id,
        'answer': answers
      };
      
      console.log('answerData',answerData);
      postAnswers(answerData);
    } else {
      $('.error-msg').css('display','flex');
      setTimeout(function(){
        $('.error-msg').css('display','none');
      },3000);
    }
  }
});

function postAnswers(data) {
  $.ajax({
      type : 'POST',
      url : "http://question-answer-johnl3.c9users.io/answer",
      contentType: 'application/json;charset=UTF-8',
      dataType: 'json',
      data : JSON.stringify(data),
        success: function(d){
        console.log('d',d);
        
          setTimeout(function(){
            $('.q-a-outer').css('display','none');
            $('#section-c').remove();
            if (d.msg[0].result === 'correct') {
              $('#'+d.msg[0].id).addClass('correct answered');
            } else {
              $('#'+d.msg[0].id).addClass('wrong answered');
            }
            answers = [];
          },500);
        }
    });
}

//Display question on page add required elements
function createQA(data, id) {
  
$('.surround').attr('id', id);

if (Object.getOwnPropertyNames(data).length > 2) {
  
  $('.input-ans').css('display','none');
  $('.question-a').text(data.question);
  $('.question-b').text(data.description);
 
  let divb = '<div id="section-c"></div>';

  $('.surround').append(divb);

  for(let item in data.choices) {
    let span = createAnswerElement(data.choices[item],item);
    $('#section-c').append(span);
  }

} else {
  
  $('.question-a').text(data.question);
  $('.question-b').text(data.description);
  $('.input-ans').css('display','block');
  $('.ans-inp').val('');
}

function createAnswerElement(answer,item) {
      let el =`<div class='answer'>
      <input type="checkbox" class="radio" id="radio-`+item+`" value="`+answer+`">
      <span>`+answer+`</span>
      </div>`;
      return el;
    }

}

function errorElement() {
  let el = `<div class='error-msg'><span>You must provide an answer.</span></div>`;
  $('.ans-button').append(el);
}
