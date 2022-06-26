function deleteNote(noteId) {
// This will take the noteId that we passed (L1)
    fetch('/delete-note', {
    // to send a request in JS, we use fetch
      method: 'POST',
      // Then send a POST request to the delete-note end point 

      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/noting";
      // After it gets a respond from the delete-note end point, it is going to reload the window
      // window.location.href = "/"; is a specific way to reload the window with a get request 
      // Hence, this means to redirect us to the homepage = refresh
    });
  }
// sending a request to the backend from JS