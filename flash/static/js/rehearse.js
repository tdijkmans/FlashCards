var visibleCard = 0;
var cardSide = "QuestionSide";

function showCard(){
  $(".rehearse_card").hide();
  $(".card-title-question").hide();
  $(".card-text-answer").hide();
  $(".rehearse_card:eq(" + visibleCard + ")").show();
  $(".card-title-question").show();
  }

showCard();

function flipCard(){
  if(cardSide == "QuestionSide"){
      cardSide = "AnswerSide";
      $(".card-title-question").hide();
      $(".card-text-answer").show();
      console.log("show Q")
    }else{
      $(".card-title-question").show();
      $(".card-text-answer").hide();
      console.log("show A");
      cardSide = "QuestionSide"  
      }

    }


function showNextCard(){
  if(visibleCard == $(".rehearse_card").length-1){
    visibleCard = 0;
  }else{
    visibleCard++;
  }
  showCard();
}


function showPrevCard(){
  if (visibleCard == 0){
    visibleCard = $(".rehearse_card").length-1;
  }else{
    visibleCard--;
  }
  showCard();
}
