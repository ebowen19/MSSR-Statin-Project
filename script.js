// Get the modal
    var modal = document.getElementById("myModal");

    // Get the image and insert it inside the modal - use its "alt" text as a caption
    var modalImg = document.getElementById("img01");
    var captionText = document.getElementById("caption");
    var downloadLink = document.querySelector('.download-link');

    // Use a class to select all your images
    var images = document.querySelectorAll('.thumbnail');

    images.forEach(function(image) {
      image.onclick = function(){
        modal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;

        // Update the download link to point to the .tif file instead of the .jpg
        var tifSrc = this.src.replace(".jpg", ".tif");
        downloadLink.href = tifSrc;
      }
    });

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() { 
      modal.style.display = "none";
    }
