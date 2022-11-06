document.addEventListener('DOMContentLoaded', function() {
    //on page load, and when form is submitted, run the post function
    document.querySelector('#post-form').onsubmit = function() {
        post();
    };
    
});
function post() {
    event.preventDefault();
    console.log('Posts');
    const content = document.querySelector('#post-content').value;
    fetch('/post', {
        method: 'POST',
        body: JSON.stringify({
            content: content
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
    }
    );
}