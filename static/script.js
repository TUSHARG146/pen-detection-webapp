document.getElementById('uploadButton').addEventListener('click', () => {
    const fileInput = document.getElementById('imageUpload');
    const uploadStatus = document.getElementById('uploadStatus');
    const formData = new FormData();

    if (!fileInput.files.length) {
        uploadStatus.textContent = 'Please select an image first.';
        uploadStatus.style.color = 'red';
        return;
    }

    formData.append('file', fileInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        uploadStatus.textContent = data.message;
        uploadStatus.style.color = data.success ? 'green' : 'red';
    })
    .catch(error => {
        uploadStatus.textContent = 'Error uploading image.';
        uploadStatus.style.color = 'red';
    });
});

document.getElementById('trainButton').addEventListener('click', () => {
    const trainStatus = document.getElementById('trainStatus');

    fetch('/train', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        trainStatus.textContent = data.message;
        trainStatus.style.color = data.success ? 'green' : 'red';
    })
    .catch(error => {
        trainStatus.textContent = 'Error during model training.';
        trainStatus.style.color = 'red';
    });
});

document.getElementById('detectButton').addEventListener('click', () => {
    const detectStatus = document.getElementById('detectStatus');

    fetch('/detect', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        detectStatus.textContent = data.message;
        detectStatus.style.color = data.success ? 'green' : 'red';
    })
    .catch(error => {
        detectStatus.textContent = 'Error starting real-time detection.';
        detectStatus.style.color = 'red';
    });
});
