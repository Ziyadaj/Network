
function getLikes(id) {
    fetch(`/like/${id}`, {
        method: 'POST',
        body: JSON.stringify({ id }),
    })
    .then(res => res.json())
    .then(post => {
        document.querySelector('#likes').innerHTML = post.likes;
    })
    console.log('Like');
}