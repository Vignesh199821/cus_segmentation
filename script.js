const form = document.querySelector('.login-form');
form.addEventListener('submit', (e) => {
	e.preventDefault();
	const username = form.username.value;
	const password = form.password.value;
	if (username === 'demo' && password === 'demo') {
		window.location.href = 'home.html';
	}
});


// Get a reference to the "Sign Out" button
var signOutBtn = document.getElementById("sign-out-btn");

// Add a click event listener to the button
signOutBtn.addEventListener("click", function() {
  window.location.href = "index.html"; // replace "signin.html" with the actual URL of your sign-in page
});







function fileSelected(fileInput) {
    const upnm = document.getElementById('up-file-name'); // replace 'file-input' with the ID of your file input element
    const selectedFiles = fileInput.files;
    if (selectedFiles.length > 0) {
        console.log(selectedFiles[0].name)
        upnm.textContent =selectedFiles[0].name+" is selected"
        
        const fileInput = document.getElementById("file-upload");
        console.log(fileInput)
        fileInput.addEventListener("change", event => {
        const file = event.target.files[0];
        sendCSVFileToAPI(file);
        });
      return selectedFiles[0].name;
    } else {
      return null; // no file selected
    }
  }
  
/*
  async function getData() {
    const response = await fetch('http://127.0.0.1:5001/images'); // replace with the API endpoint you want to call
    const data = await response.json(); // assuming the response is in JSON format, parse it and store it in a variable
    console.log(data)
    return "done"; // return the data so it can be used by other parts of the code
  }

*/
function getData() {
    fetch('http://127.0.0.1:5001/images')
        .then(response => response.json())
        .then(images => {
            // Loop through the images array
            images.forEach((image, index) => {
                // Create a container for the image and download button
                const container = document.createElement('div');
                container.classList.add('image-container');
                // Create an image tag for each image
                const img = document.createElement('img');
                // Set the source of the image to the base64-encoded image data
                img.src = 'data:image/png;base64,' + image;
                // Add the image to the container
                container.appendChild(img);
                // Create a link tag for the download button
                const downloadLink = document.createElement('a');
                downloadLink.classList.add('download-button');
                downloadLink.download = `image${index+1}.png`;
                downloadLink.textContent = 'Download';
                downloadLink.href = 'data:application/octet-stream;base64,' + image;
                // Add the download button to the container
                container.appendChild(downloadLink);
                // Add the container to the DOM
                const divEle = document.getElementById('img_cont');
                divEle.appendChild(container);
            });
        })
        .catch(error => console.error(error));
    return 'done';
}



function sendCSVFileToAPI(csvFile) {
    console.log('sfdfvcdfvfcerc')
    // Create a FormData object to hold the CSV file
    const formData = new FormData();
    formData.append("csvFile", csvFile);
    console.log(formData)
    // Make a fetch request to the API endpoint
    fetch("http://127.0.0.1:5001/images", {
      method: "POST",
      body: formData,
    })
      .then(response => {
        // Handle the API response
        if (response.ok) {
          console.log("CSV file uploaded successfully!");
        } else {
          console.error("Error uploading CSV file:", response.statusText);
        }
      })
      .catch(error => {
        console.error("Error uploading CSV file:", error);
      });
  }
  

  
  
  function get3dplot(){
    //fetch('http://127.0.0.1:5001/get3dplots')
    getAndSaveApiResponse('http://127.0.0.1:5001/get3dplots', 'response.html');




  }


  
  function get3dplot(apiUrl, fileName) {
    const https = require('https');
    const fs = require('fs');
    https.get(apiUrl, (res) => {
      let data = '';
  
      res.on('data', (chunk) => {
        data += chunk;
      });
  
      res.on('end', () => {
        fs.writeFile(fileName, data, (err) => {
          if (err) {
            console.error(err);
            return;
          }
          console.log(`Response saved to ${fileName} file`);
        });
      });
    }).on('error', (err) => {
      console.error(err);
    });
  }
  
  // Example usage:
  getAndSaveApiResponse('https://jsonplaceholder.typicode.com/posts/1', 'response.html');
  