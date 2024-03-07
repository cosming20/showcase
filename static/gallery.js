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
      const mediaElement = document.createElement(media.type === "photo" ? "img" : "video");
      mediaElement.src = `/media/${media._id}`;
      mediaElement.alt = media.title;
      mediaContainer.appendChild(mediaElement);
    });
  } catch (error) {
    console.error("Error fetching media:", error);
  }
}
