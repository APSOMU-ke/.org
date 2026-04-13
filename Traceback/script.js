window.addEventListener('scroll', function () {
  const header = document.querySelector('header');
  if (window.scrollY > 50) {
    header.classList.add('header-scrolled');
  } else {
    header.classList.remove('header-scrolled');
  }
});

// Stakeholder Data
const stakeholderData = {
  1: {
    title: 'Students',
    description: 'Students are the main stakeholders, APSOMU is primarily focused on promoting and advancing study of political science among students.',
    bgColor: '#f0f4ff', // Light Blue
    textColor: '#00008B', // Dark Blue
    img: 'https://via.placeholder.com/120?text=Students'
  },
  2: {
    title: 'Political Science Scholars and Practitioners',
    description: 'Association provides opportunities for students to engage with different scholars and practitioners therefore this individuas are stakeholders of the organization.',
    bgColor: '#f5f0ff', // Light Purple
    textColor: '#800080', // Purple
    img: 'https://via.placeholder.com/120?text=Scholars'
  },
  3: {
    title: 'Higher Education Institutions (MOI UNIVERSITY)',
    description: 'Association works to promote research and scholarships in the field of political science and to influence policy and contribute to the development of political science as a discipline. Therefore higher institutions are stakeholders.',
    bgColor: '#fffaf0', // Light Gold/Cream
    textColor: '#DAA520', // Golden
    img: 'https://via.placeholder.com/120?text=Institutions'
  },
  4: {
    title: 'Government and Administrative Body',
    description: 'Association may work to influence policy and contribute to the development of effective and responsive governance and therefore government and Administrative bodies are stakeholders in the organization.',
    bgColor: '#f0f0f0', // Neutral Gray
    textColor: '#333333', // Dark Gray
    img: 'https://via.placeholder.com/120?text=Government'
  },
  5: {
    title: 'Other Organizations and Institutions',
    description: "Association may Foster collaboration and partnerships with other organizations and institutions in the political science community to advance the field and promote it's mission therefore this organization are stakeholders.",
    bgColor: '#f0fff4', // Light Green hint
    textColor: '#2e7d32', // Darker Green for differentiation
    img: 'https://via.placeholder.com/120?text=Community'
  }
};

// Main Logic Handler
document.addEventListener('DOMContentLoaded', function () {
  // Slideshow Logic
  const slides = document.querySelectorAll('.slide');
  const dots = document.querySelectorAll('.dot');
  let currentSlide = 0;
  const slideInterval = 5000;
  let slideTimer;

  function updateSlides(index) {
    slides.forEach(s => s.classList.remove('active'));
    dots.forEach(d => d.classList.remove('active'));
    if (slides[index]) slides[index].classList.add('active');
    if (dots[index]) dots[index].classList.add('active');
    currentSlide = index;
  }

  function nextSlide() {
    let next = (currentSlide + 1) % slides.length;
    updateSlides(next);
  }

  window.setSlide = function (index) {
    clearInterval(slideTimer);
    updateSlides(index);
    slideTimer = setInterval(nextSlide, slideInterval);
  }

  if (slides.length > 0) {
    updateSlides(0);
    slideTimer = setInterval(nextSlide, slideInterval);
  }

  // Stakeholder Logic
  const tiles = document.querySelectorAll('.stakeholder-tile');
  const infoCard = document.getElementById('sdg-info-card');
  const infoTitle = document.getElementById('sdg-info-title');
  const infoDescription = document.getElementById('sdg-info-description');
  const infoImg = document.getElementById('stakeholder-info-img');

  tiles.forEach(tile => {
    tile.addEventListener('click', function () {
      const stakeholderId = this.getAttribute('data-stakeholder');
      const data = stakeholderData[stakeholderId];

      if (!data) return;

      // Update active state
      tiles.forEach(t => t.classList.remove('active'));
      this.classList.add('active');

      // Update info card
      infoTitle.textContent = data.title;
      infoDescription.textContent = data.description;
      infoCard.style.backgroundColor = data.bgColor;
      infoTitle.style.color = data.textColor;
      if (infoImg) infoImg.src = data.img;
    });
  });
});
