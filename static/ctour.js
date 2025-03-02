const steps = [
    {
      mapSrc: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2833.839093102827!2d-123.2813823!3d44.5637807!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54c040b24f771007%3A0xffcf65b4dc9883f!2sReser%20Stadium!5e0!3m2!1sen!2sus!4v1611965645455!5m2!1sen!2sus", // Example map URL
      description: "Step 1: Welcome to the Memorial Union.",
      audioSrc: "./static/memorial_union.mp3",
      imgSrc: "./static/mu.jpg",
      title: "Memorial Union"
    },
    {
      mapSrc: "https://www.google.com/maps/embed?pb=EXAMPLE2", // Example map URL
      description: "Step 2: This is Reser Stadium.",
      audioSrc: "./static/reser_stadium.mp3",
      imgSrc: "./static/reser.jpg",
      title: "Reser Stadium"
    }
  ];
  
  let currentStep = 0;
  
  // DOM elements
  const map = document.getElementById("map");
  const description = document.getElementById("tour-description");
  const title = document.getElementById("tour-title");
  const img = document.getElementById("tour-img");
  const audio = document.getElementById("audio");
  const prevButton = document.getElementById("prev");
  const nextButton = document.getElementById("next");
  
  // Function to update the step content
  function updateStep() {
      map.src = steps[currentStep].mapSrc;
      description.textContent = steps[currentStep].description;
      title.textContent = steps[currentStep].title;
      img.src = steps[currentStep].imgSrc;
      img.load()
      audio.src = steps[currentStep].audioSrc;
      audio.load();
  }
  
  // Event listeners for Prev and Next buttons
  prevButton.addEventListener("click", () => {
      if (currentStep > 0) {
          currentStep--;
          updateStep();
      }
  });
  
  nextButton.addEventListener("click", () => {
      if (currentStep < steps.length - 1) {
          currentStep++;
          updateStep();
      }
  });
  
  // Initialize with the first step
  updateStep();
  