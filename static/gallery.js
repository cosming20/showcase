document.addEventListener("DOMContentLoaded", function () {
    // Fetch photos and videos from MongoDB database
    fetchMedia();
  });
  
  async function fetchMedia() {
    try {
      const response = await fetch("/api/media");
      const mediaData = await response.json();
  
      const mediaContainer = document.getElementById("media-container");
  
      mediaData.forEach(media => {
        if (media.type === "photo") {
          // Display photos
          const photoElement = document.createElement("img");
          photoElement.src = media.url;
          photoElement.alt = media.title;
          mediaContainer.appendChild(photoElement);
        } else if (media.type === "video") {
          // Display videos
          const videoElement = document.createElement("video");
          videoElement.src = media.url;
          videoElement.controls = true;
          mediaContainer.appendChild(videoElement);
        }
      });
    } catch (error) {
      console.error("Error fetching media:", error);
    }
  }
  