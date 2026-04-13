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
    img: 'Images/stakeholder1.webp'
  },
  2: {
    title: 'Political Science Scholars and Practitioners',
    description: 'Association provides opportunities for students to engage with different scholars and practitioners therefore this individuas are stakeholders of the organization.',
    bgColor: '#f5f0ff', // Light Purple
    textColor: '#800080', // Purple
    img: 'Images/stakeholder2.webp'
  },
  3: {
    title: 'Higher Education Institutions (MOI UNIVERSITY)',
    description: 'Association works to promote research and scholarships in the field of political science and to influence policy and contribute to the development of political science as a discipline. Therefore higher institutions are stakeholders.',
    bgColor: '#fffaf0', // Light Gold/Cream
    textColor: 'green', // Green
    img: 'Images/stakeholder3.webp'
  },
  4: {
    title: 'Government and Administrative Body',
    description: 'Association may work to influence policy and contribute to the development of effective and responsive governance and therefore government and Administrative bodies are stakeholders in the organization.',
    bgColor: '#f0f0f0', // Neutral Gray
    textColor: '#333333', // Dark Gray
    img: 'Images/stakeholder4.webp'
  },
  5: {
    title: 'Other Organizations and Institutions',
    description: "Association may Foster collaboration and partnerships with other organizations and institutions in the political science community to advance the field and promote it's mission therefore this organization are stakeholders.",
    bgColor: '#f0fff4', // Light Green hint
    textColor: '#2e7d32', // Darker Green for differentiation
    img: 'Images/WhatsApp Image 2026-01-31 at 17.37.35 (1).webp'
  }
};

// Main Logic Handler
document.addEventListener("DOMContentLoaded", function () {
  // --- Mobile Menu Toggle Logic ---
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const mobileDrawer = document.getElementById('mobile-drawer');
  const menuText = document.querySelector('.menu-text');
  const hamburgerIcon = document.querySelector('.hamburger-icon');
  const closeIcon = document.querySelector('.close-icon');

  if (mobileBtn && mobileDrawer) {
    mobileBtn.addEventListener('click', function() {
      const isActive = mobileDrawer.classList.toggle('active');
      
      if (isActive) {
        // Menu is open
        menuText.textContent = '';
        hamburgerIcon.style.display = 'none';
        closeIcon.style.display = 'block';
      } else {
        // Menu is closed
        menuText.textContent = 'Menu';
        hamburgerIcon.style.display = 'block';
        closeIcon.style.display = 'none';
      }
    });
  }

  // Header Scroll Effect
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

  // Initialize individual tile colors from stakeholderData
  tiles.forEach(tile => {
    const stakeholderId = tile.getAttribute('data-stakeholder');
    const data = stakeholderData[stakeholderId];
    if (data) {
      const titleEl = tile.querySelector('.stakeholder-title');
      if (titleEl) {
        titleEl.style.color = data.textColor;
      }
      const mobileDescP = tile.querySelector('.mobile-description p');
      if (mobileDescP) {
        mobileDescP.style.borderLeftColor = data.textColor;
        mobileDescP.style.backgroundColor = data.bgColor;
      }
    }
  });

  tiles.forEach(tile => {
    tile.addEventListener('click', function () {
      const stakeholderId = this.getAttribute('data-stakeholder');
      const data = stakeholderData[stakeholderId];

      if (!data) return;

      // Check if we are in mobile view (matching the CSS breakpoint)
      if (window.innerWidth <= 768) {
        const isAlreadyExpanded = this.classList.contains('expanded');
        
        // Collapse all others first (Accordion behavior)
        tiles.forEach(t => t.classList.remove('expanded'));
        
        // Toggle current one
        if (!isAlreadyExpanded) {
          this.classList.add('expanded');
        }
      } else {
        // Desktop behavior: Update active state and info card
        tiles.forEach(t => t.classList.remove('active'));
        this.classList.add('active');

        // Update info card
        infoTitle.textContent = data.title;
        infoDescription.textContent = data.description;
        infoCard.style.backgroundColor = data.bgColor;
        infoTitle.style.color = data.textColor;
        if (infoImg) infoImg.src = data.img;
      }
    });
  });

  // Stakeholders Scroll Animation (Staggered 3D Scale-Reveal)
  const stakeholderObserverOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const stakeholderObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const gridTiles = entry.target.querySelectorAll('.sdg-tile');
        gridTiles.forEach((gridTile, index) => {
          if (gridTile.revealTimeout) clearTimeout(gridTile.revealTimeout);
          gridTile.revealTimeout = setTimeout(() => {
            gridTile.classList.add('reveal');
          }, index * 100); // 100ms stagger delay
        });
      } else {
        const gridTiles = entry.target.querySelectorAll('.sdg-tile');
        gridTiles.forEach(gridTile => {
          if (gridTile.revealTimeout) clearTimeout(gridTile.revealTimeout);
          gridTile.classList.remove('reveal');
        });
      }
    });
  }, stakeholderObserverOptions);

  const stakeholderGrid = document.querySelector('.stakeholder-grid');
  if (stakeholderGrid) {
    stakeholderObserver.observe(stakeholderGrid);
  }

  // Executives Scroll Animation (Staggered 3D Scale-Reveal)
  const executivesObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const gridTiles = entry.target.querySelectorAll('.executive-card');
        const viewportCenterX = window.innerWidth / 2;
        const viewportCenterY = window.innerHeight / 2;

        gridTiles.forEach((gridTile, index) => {
          const rect = gridTile.getBoundingClientRect();
          const tileCenterX = rect.left + rect.width / 2;
          const tileCenterY = rect.top + rect.height / 2;

          // Distance from the viewport center exactly
          const dx = viewportCenterX - tileCenterX;
          const dy = viewportCenterY - tileCenterY;

          gridTile.style.setProperty('--dx', `${dx}px`);
          gridTile.style.setProperty('--dy', `${dy}px`);

          // Form the Lotus bud in the center
          gridTile.classList.add('stacked');

          // Bloom simultaneously after a short pause to see the bud!
          if (gridTile.revealTimeout) clearTimeout(gridTile.revealTimeout);
          gridTile.revealTimeout = setTimeout(() => {
            gridTile.classList.add('reveal');
          }, 400); // 400ms pause to observe the clustered bud
        });
      } else {
        const gridTiles = entry.target.querySelectorAll('.executive-card');
        gridTiles.forEach(gridTile => {
          if (gridTile.revealTimeout) clearTimeout(gridTile.revealTimeout);
          gridTile.classList.remove('reveal', 'stacked');
        });
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  const executivesGrid = document.querySelector('.executives-grid');
  if (executivesGrid) {
    executivesObserver.observe(executivesGrid);
  }

  // National Arena Sticky Scroll Observer
  const naObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal');
      } else {
        // Optional: Remove class if you want them to animate out when scrolling past
        // We'll reset it to allow smooth replay when scrolling up/down
        entry.target.classList.remove('reveal');
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

  document.querySelectorAll('.na-item').forEach(item => {
    naObserver.observe(item);
  });

  // Mission & Vision Observer
  const mvObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
      } else {
        entry.target.classList.remove('in-view');
      }
    });
  }, { threshold: 0.2, rootMargin: '0px 0px -50px 0px' });

  document.querySelectorAll('.mv-block').forEach(block => {
    mvObserver.observe(block);
  });
});

// Executive Lightbox Functions
function openExecutiveLightbox(imgSrc) {
  const lightbox = document.getElementById('executive-lightbox');
  const lightboxImg = document.getElementById('executive-lightbox-img');
  if (lightbox && lightboxImg) {
    lightbox.style.display = 'flex';
    lightboxImg.src = imgSrc;
  }
}

function closeExecutiveLightbox(event) {
  if (event.target.classList.contains('lightbox') || event.target.classList.contains('close-lightbox')) {
    document.getElementById('executive-lightbox').style.display = 'none';
  }
}
