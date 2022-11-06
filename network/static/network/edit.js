function edit(id) {
    event.preventDefault();
    var content = document.querySelector(`#content${id}`);
    content.innerHTML = `
    <form id="edit-form">
        <textarea id="edit-content" name="content" rows="4" cols="60">${content.innerHTML}</textarea>
        <br>
        <button style="margin-top: 10px;" class="btn btn-primary" type="submit" onclick="submitEdit(${id})">Save</button>
    </form>`;
    document.getElementById('edit-button').disabled = true;
}
function submitEdit(id) {
    event.preventDefault();
    const content = document.querySelector('#edit-content').value;
    console.log(content);
    fetch(`/post/${id}`, {
        method: 'PUT',
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