alert('I am the app.js file!')
// which html file to link to js file
//Object oriented way to design front-end 

let test = 1;

// use jquery to get values from form
//prevent default form submit
// append html to confirm button works

// add e listener
let $submitBtn = $('#submit_guess')



async function submitGuess(){
    // prevent page reload
    // send AJAX request to the server
    // need to get url.  Add full url?
    // let guess = $()

    // JSON gets passed to the server
    let response = await axios.post("/evaluateValue", {word: {guess}});
    console.log(response);
    console.log('entered submitGuess');
    return response;
}

$submitBtn.on('click', submitGuess)

function handleScore(){
    // receive score from server
    // store in local storage
    // show player score in browser
}


function timeGame(){
    // ensure game can only be played for 60s
}


function gameStats(){
    // send number of plays and high score that was stored in browser
}

