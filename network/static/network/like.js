function like(id, like, dislike) {
    fetch(`/like/${id}`, {
        method: 'PUT',
        body: JSON.stringify({ 
            id: id
        }),
    })
    .then(res => res.json())
    .then(post => {
        int = parseInt(like);
        console.log(post);
        console.log(int);
        console.log(dislike);
        if (dislike === true) {// if the user has already liked the post and is now unliking it
            if (int === 0) { 
            // if the post reaches 0 likes, remove the heart
                document.querySelector(`#like${id}`).innerHTML =             
                `<input type="image" src="static/network/heart-empty.png" id="button-like" onclick="like(${id},${like},${false})" alt="...">
                <span id="like-count">${int}</span>`;
            }
            else {
            // if the post has more than 0 likes, keep the heart
            document.querySelector(`#like${id}`).innerHTML = 
            `<input type="image" src="static/network/heart.png" id="button-like" onclick="like(${id},${like},${false})" alt="...">
            <span id="like-count">${int}</span>`;
            }
        }
        else {
        // if the user has not liked the post and is now liking it
        int++;
        document.querySelector(`#like${id}`).innerHTML = 
        `<input type="image" src="static/network/heart.png" id="button-like" onclick="like(${id},${like},${true})" alt="...">
        <span id="like-count">${int}</span>`;
        }
    })
    console.log('Like');
}