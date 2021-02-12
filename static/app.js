//Object oriented way to design front-end 
//Is it necessary to return something in a function?

let $submitForm = $('#submit-form');
let $body = $('body');
let $messages = $('#messages');
let $score = $('#score');
let $time = $('#time');
let $gamesPlayed = $('#game-count')


async function submitGuess(evt){
    //Submits word on form and makes post request to server

    evt.preventDefault();

    let time = Number($time.eq(0).text());
    if(time === 0){
        return;
    }
    
    let $word = $('#guess').val();
    $submitForm.trigger('reset');

    let response = await axios.post("http://127.0.0.1:5000/evaluatedValue", {"word": $word});

    return await guessResult(response, $word);
};

$submitForm.on('submit', submitGuess)

async function guessResult(result, word){
    //Updates DOM with guess result for the user

    let message; 
    let guessFeedback = result.data.result;

    if(guessFeedback === "ok"){
        message = "Good Guess!";
        incrementScore(word)

    }else if(guessFeedback === "not-word"){
        message = "Guess was not a word!";
    }else{
        message = "Guess does not exist on board!";
    }

    $messages.eq(0).text(`${message}`);
    return;
}

function incrementScore(word){
    //increments score based on the word length
    let pointValue = word.length;
    let currentScore = Number($score.eq(0).text());
    let newScore = currentScore + pointValue;

    $score.eq(0).text(`${newScore}`);
    return;
}

async function timer(){
    //Counts down until 0 then checks for high score with the server

    let currentTime = Number($time.eq(0).text());
    let updatedTime = currentTime - 1;
    let score = Number($score.eq(0).text());

    if(updatedTime===-1){
        clearInterval(countdown);

        let response = await axios.post(`http://127.0.0.1:5000/gameEnd`, {"score": `${score}`});

        return response.data;
    }
    return $time.eq(0).text(`${updatedTime}`);
}

let countdown = setInterval(timer, 1000)

