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
function comment(id) {
    var card = document.querySelector(`#comments${id}`);
    if (card.style.display === 'none') {
        card.style.display = 'block';
    }
    else {
    card.style.display = 'none';
    }
}
function submitComment(id) {
    event.preventDefault();
    const content = document.querySelector(`#comment-content${id}`).value;
    fetch(`/comment/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            comments: content
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
    });
}
function showMore(id) {
    const btnText = document.getElementById(`show-more${id}`);
    const hidecontent = document.querySelector(`#content${id}`);
    const content = document.querySelector(`#uncontent${id}`);
    hidecontent.innerHTML = content.innerHTML;
    if (content.style.overflow === 'hidden') {
        content.style.overflow = 'visible';
    }
    btnText.innerHTML = "Show Less";
    btnText.onclick = function() {
        showLess(id);
    }
}
function showLess(id) {
    const btnText = document.getElementById(`show-more${id}`);
    const hidecontent = document.querySelector(`#content${id}`);
    const content = document.querySelector(`#uncontent${id}`);
    hidecontent.innerHTML = content.innerHTML.slice(0, 280) + '...';
    content.style.overflow = 'hidden';
    btnText.innerHTML = "Show More";
    btnText.onclick = function() {
        showMore(id);
    }
}