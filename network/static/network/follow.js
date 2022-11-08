function follow(id) {
    fetch(`/follow/${id}`, {
        method: 'POST',
        body: JSON.stringify({
            id: id
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
        
        if (result.message === 'Follow successful.') {
            let button = document.querySelector('#button-follow');
            button.textContent = 'Unfollow';
        }
        else if (result.message === 'Unfollow successful.') {
            let button = document.querySelector('#button-unfollow');
            button.textContent = 'Follow';
        }
        else if (result.error === 'Cannot follow yourself.') {
            alert('You cannot follow yourself.');
        }
        
    });
}