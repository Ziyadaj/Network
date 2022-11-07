
function follow(id) {
    fetch(`/follow/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            id: id
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
        // if (result.message === 'Followed') {
        //     document.querySelector(`#follow${id}`).innerHTML = 
        //     `<button class="btn btn-primary" onclick="follow(${id})">Unfollow</button>`;
        // }
        // else {
        //     document.querySelector(`#follow${id}`).innerHTML = 
        //     `<button class="btn btn-primary" onclick="follow(${id})">Follow</button>`;
        // }
    }
    );
}