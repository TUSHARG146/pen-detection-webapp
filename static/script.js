document.getElementById('uploadButton').addEventListener('click', () => {
    const fileInput = document.getElementById('imageUpload');
    const uploadStatus = document.getElementById('uploadStatus');
    const formData = new FormData();

    if (!fileInput.files.length) {
        uploadStatus.textContent = 'Please select an image first.';
        uploadStatus.style.color = 'red';
        return;
    }

    uploadStatus.textContent = 'Uploading...';
    uploadStatus.style.color = 'blue';

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

document.getElementById('collectButton').addEventListener('click', () => {
    console.log("Collect button clicked.");  // Log to confirm button click
    const collectStatus = document.getElementById('collectStatus');

    collectStatus.textContent = 'Data collection started...';
    collectStatus.style.color = 'blue';

    fetch('/collect', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);  // Log to confirm data received from the backend
        collectStatus.textContent = data.message;
        collectStatus.style.color = data.success ? 'green' : 'red';
    })
    .catch(error => {
        console.error("Error:", error);  // Log errors for easier debugging
        collectStatus.textContent = 'Error during data collection.';
        collectStatus.style.color = 'red';
    });
});

document.getElementById('testButton').addEventListener('click', () => {
    const testStatus = document.getElementById('testStatus');

    testStatus.textContent = 'Testing started...';
    testStatus.style.color = 'blue';

    fetch('/test', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        testStatus.textContent = data.message;
        testStatus.style.color = data.success ? 'green' : 'red';
    })
    .catch(error => {
        testStatus.textContent = 'Error during testing.';
        testStatus.style.color = 'red';
    });
});

document.getElementById('trainButton').addEventListener('click', () => {
    const trainStatus = document.getElementById('trainStatus');
    const trainProgress = document.getElementById('trainProgress');
    const trainFill = trainProgress.querySelector('.progress-bar-fill');

    trainStatus.textContent = 'Training started...';
    trainStatus.style.color = 'blue';

    trainFill.style.width = '0%';
    trainProgress.style.display = 'block';

    fetch('/train', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        trainStatus.textContent = data.message;
        trainStatus.style.color = data.success ? 'green' : 'red';
        trainFill.style.width = data.success ? '100%' : '0%';
    })
    .catch(error => {
        trainStatus.textContent = 'Error during model training.';
        trainStatus.style.color = 'red';
        trainFill.style.width = '0%';
    });
});

document.getElementById('detectButton').addEventListener('click', () => {
    const detectStatus = document.getElementById('detectStatus');
    const detectProgress = document.getElementById('detectProgress');
    const detectFill = detectProgress.querySelector('.progress-bar-fill');

    detectStatus.textContent = 'Starting real-time detection...';
    detectStatus.style.color = 'blue';

    detectFill.style.width = '0%';
    detectProgress.style.display = 'block';

    fetch('/detect', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        detectStatus.textContent = data.message;
        detectStatus.style.color = data.success ? 'green' : 'red';
        detectFill.style.width = data.success ? '100%' : '0%';
    })
    .catch(error => {
        detectStatus.textContent = 'Error starting real-time detection.';
        detectStatus.style.color = 'red';
        detectFill.style.width = '0%';
    });
});
