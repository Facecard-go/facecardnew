function jijietu() {
    $.ajax({
        type:"POST",
        url:"/exercise.py",
        success:callbackFunc
    });
}
function callbackFunc(response) {
    console.log(response);

}
jijietu('data to process');