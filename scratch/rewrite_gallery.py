import codecs

with codecs.open(r"c:\Users\victor\3D Objects\APSOMU\gallery.html", "r", "utf-8") as f:
    content = f.read()

# 1. New Main block
new_main = """
    <main>
        <!-- Section 1: Members (Expanding Style) -->
        <section id="members" class="gallery-section style2-section">
            <div class="category-header">
                <h2>Our Members</h2>
                <p>The Heart of APSOMU</p>
                <button class="download-btn" onclick="downloadCollection(galleryData['Members'], 'APSOMU_Members')">
                    <i class="fas fa-download"></i> Download Selection
                </button>
            </div>
            <div class="options" id="members-wrapper">
                <!-- Dynamic Options -->
            </div>
        </section>

        <!-- Section 2: Launching (Fullscreen Story Style) -->
        <section id="launching" class="gallery-section style3-section">
            <div class="main-slider swiper launch-swiper-main">
                <div class="swiper-wrapper" id="launching-main-wrapper">
                    <!-- Dynamic Slides -->
                </div>
            </div>
            <div class="style3-content">
                <h1 id="launching-title">Association Launch</h1>
                <p id="launching-desc">Witness the beginning of a structured platform for students.</p>
            </div>
            <div class="style3-controls">
                <div class="style3-btn launch-prev"><i class="fas fa-arrow-left"></i></div>
                <div class="style3-btn launch-next"><i class="fas fa-arrow-right"></i></div>
                <button class="download-btn" onclick="downloadCollection(galleryData['Launching'], 'APSOMU_Launch')"
                    style="width: auto; height: 50px; border-radius: 25px; padding: 0 25px; margin-top: 0;">
                    <i class="fas fa-download"></i>
                </button>
            </div>
            <div class="thumb-container">
                <div class="thumb-slider swiper launch-swiper-thumb">
                    <div class="swiper-wrapper" id="launching-thumb-wrapper">
                        <!-- Dynamic Thumbs -->
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 3: Public Lecture (Curved Style) -->
        <section id="lecture" class="gallery-section style1-section" style="background: #111; color: #fff;">
            <div class="category-header">
                <h2>Prof. PLO Lumumba Public Lecture</h2>
                <p>Ethical Leadership & Governance Insights</p>
                <button class="download-btn" onclick="downloadCollection(galleryData['Public Lecture'], 'Public_Lecture')">
                    <i class="fas fa-download"></i> Download Selection
                </button>
            </div>
            <div class="swiper lecture-swiper">
                <div class="swiper-wrapper" id="lecture-wrapper">
                    <!-- Dynamic Slides -->
                </div>
                <div class="swiper-pagination"></div>
            </div>
        </section>

        <!-- Section 4: County Assembly (Curved Style) -->
        <section id="county-visit" class="gallery-section style1-section" style="background: #000; color: #fff;">
            <div class="category-header">
                <h2>County Assembly Visit</h2>
                <p>Bridging Theory and Practice</p>
                <button class="download-btn" onclick="downloadCollection(galleryData['County Assembly'], 'County_Assembly')">
                    <i class="fas fa-download"></i> Download Selection
                </button>
            </div>
            <div class="swiper county-swiper">
                <div class="swiper-wrapper" id="county-wrapper">
                    <!-- Dynamic Slides -->
                </div>
                <div class="swiper-pagination"></div>
            </div>
        </section>

        <!-- Section 5: AGM (Fullscreen Story Style) -->
        <section id="agm" class="gallery-section style3-section">
            <div class="main-slider swiper agm-swiper-main">
                <div class="swiper-wrapper" id="agm-main-wrapper">
                    <!-- Dynamic Slides -->
                </div>
            </div>
            <div class="style3-content">
                <h1 id="agm-title">Annual General Meeting</h1>
                <p id="agm-desc">Evaluating progress and transitioning leadership.</p>
            </div>
            <div class="style3-controls">
                <div class="style3-btn agm-prev"><i class="fas fa-arrow-left"></i></div>
                <div class="style3-btn agm-next"><i class="fas fa-arrow-right"></i></div>
                <button class="download-btn" onclick="downloadCollection(galleryData['AGM'], 'APSOMU_AGM')"
                    style="width: auto; height: 50px; border-radius: 25px; padding: 0 25px; margin-top: 0;">
                    <i class="fas fa-download"></i>
                </button>
            </div>
            <div class="thumb-container">
                <div class="thumb-slider swiper agm-swiper-thumb">
                    <div class="swiper-wrapper" id="agm-thumb-wrapper">
                        <!-- Dynamic Thumbs -->
                    </div>
                </div>
            </div>
        </section>

    </main>
"""

# Replace <main> block
main_start = content.find("<main>")
main_end = content.find("</main>") + 7
content = content[:main_start] + new_main + content[main_end:]

# Now replace the <script> block
script_start = content.find("<script>", content.find("<!-- Swiper JS -->"))
script_end = content.find("</body>")

new_script = """<script src="js/gallery-data.js"></script>
    <script>
        // Use galleryData imported prior for the various sections.
        
        /* 1. Members (Expanding Style) */
        const membersData = galleryData['Members'] || [];
        const membersWrapper = document.getElementById('members-wrapper');
        membersData.forEach((imgSrc, idx) => {
            const option = document.createElement('div');
            option.className = `option ${idx === 0 ? 'active' : ''}`;
            // Encode the string properly for the URL so spaces don't break CSS backgorund-image
            const safeImgSrc = encodeURI(imgSrc);
            option.style.backgroundImage = `url('${safeImgSrc}')`;
            option.innerHTML = `<div class="shadow"></div>`;
            membersWrapper.appendChild(option);
            
            option.addEventListener("click", () => {
                if (option.classList.contains("active")) {
                    openLightbox(imgSrc);
                } else {
                    document.querySelectorAll("#members-wrapper .option").forEach(o => o.classList.remove("active"));
                    option.classList.add("active");
                    option.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
                }
            });
        });

        /* 2. Launching (Fullscreen Story) */
        const launchData = galleryData['Launching'] || [];
        const launchMain = document.getElementById('launching-main-wrapper');
        const launchThumb = document.getElementById('launching-thumb-wrapper');
        
        launchData.forEach(imgSrc => {
            const safeImgSrc = encodeURI(imgSrc);
            const slide = document.createElement('div');
            slide.className = 'swiper-slide';
            slide.style.backgroundImage = `url('${safeImgSrc}')`;
            launchMain.appendChild(slide);

            const thumb = document.createElement('div');
            thumb.className = 'swiper-slide';
            thumb.style.backgroundImage = `url('${safeImgSrc}')`;
            launchThumb.appendChild(thumb);
        });

        const launchThumbsSwiper = new Swiper(".launch-swiper-thumb", { spaceBetween: 15, slidesPerView: 3, freeMode: true, watchSlidesProgress: true });
        new Swiper(".launch-swiper-main", {
            effect: "fade", loop: true, thumbs: { swiper: launchThumbsSwiper },
            navigation: { nextEl: ".launch-next", prevEl: ".launch-prev" },
            on: {
                slideChange: function () {
                    document.getElementById('launching-desc').textContent = `Moment ${this.realIndex + 1} of APSOMU's grand launch event.`;
                }
            }
        });

        /* 3. Public Lecture (Curved Swiper) */
        const lectureData = galleryData['Public Lecture'] || [];
        const lectureWrapper = document.getElementById('lecture-wrapper');
        lectureData.forEach((imgSrc, idx) => {
            const safeImgSrc = encodeURI(imgSrc);
            const slide = document.createElement('div');
            slide.className = 'swiper-slide style1-slide';
            slide.onclick = () => openLightbox(imgSrc);
            slide.innerHTML = `<img src="${safeImgSrc}" alt="Lecture Image ${idx+1}">`;
            lectureWrapper.appendChild(slide);
        });

        new Swiper(".lecture-swiper", {
            effect: "coverflow", grabCursor: true, centeredSlides: true, slidesPerView: "auto",
            coverflowEffect: { rotate: 50, stretch: 0, depth: 100, modifier: 1, slideShadows: true },
            pagination: { el: ".lecture-swiper .swiper-pagination" },
            initialSlide: 2
        });

        /* 4. County Assembly (Curved Swiper) */
        const countyData = galleryData['County Assembly'] || [];
        const countyWrapper = document.getElementById('county-wrapper');
        countyData.forEach((imgSrc, idx) => {
            const safeImgSrc = encodeURI(imgSrc);
            const slide = document.createElement('div');
            slide.className = 'swiper-slide style1-slide';
            slide.onclick = () => openLightbox(imgSrc);
            slide.innerHTML = `<img src="${safeImgSrc}" alt="County Assembly Image ${idx+1}">`;
            countyWrapper.appendChild(slide);
        });

        new Swiper(".county-swiper", {
            effect: "coverflow", grabCursor: true, centeredSlides: true, slidesPerView: "auto",
            coverflowEffect: { rotate: 50, stretch: 0, depth: 100, modifier: 1, slideShadows: true },
            pagination: { el: ".county-swiper .swiper-pagination" },
            initialSlide: 2
        });

        /* 5. AGM (Fullscreen Story) */
        const agmData = galleryData['AGM'] || [];
        const agmMain = document.getElementById('agm-main-wrapper');
        const agmThumb = document.getElementById('agm-thumb-wrapper');
        
        agmData.forEach(imgSrc => {
            const safeImgSrc = encodeURI(imgSrc);
            const slide = document.createElement('div');
            slide.className = 'swiper-slide';
            slide.style.backgroundImage = `url('${safeImgSrc}')`;
            agmMain.appendChild(slide);

            const thumb = document.createElement('div');
            thumb.className = 'swiper-slide';
            thumb.style.backgroundImage = `url('${safeImgSrc}')`;
            agmThumb.appendChild(thumb);
        });

        const agmThumbsSwiper = new Swiper(".agm-swiper-thumb", { spaceBetween: 15, slidesPerView: 3, freeMode: true, watchSlidesProgress: true });
        new Swiper(".agm-swiper-main", {
            effect: "fade", loop: true, thumbs: { swiper: agmThumbsSwiper },
            navigation: { nextEl: ".agm-next", prevEl: ".agm-prev" },
            on: {
                slideChange: function () {
                    document.getElementById('agm-desc').textContent = `Highlight ${this.realIndex + 1} from our Annual General Meeting.`;
                }
            }
        });

        // Batch Download Function Updated for Arrays
        async function downloadCollection(filesArray, zipFilename) {
            if (!filesArray || filesArray.length === 0) {
                alert("No files to download in this category.");
                return;
            }

            const zip = new JSZip();
            const folder = zip.folder(zipFilename);
            const btn = event.currentTarget;
            const originalText = btn.innerHTML;

            // Loading State
            btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Zipping ${filesArray.length} images...`;
            btn.style.pointerEvents = 'none';

            let successCount = 0;

            try {
                const promises = filesArray.map(async (filePath) => {
                    const filename = filePath.split('/').pop();
                    const encodedUrl = encodeURI(filePath);

                    try {
                        const resp = await fetch(encodedUrl);
                        if (!resp.ok) throw new Error(`Failed to load ${filename}`);
                        const blob = await resp.blob();
                        folder.file(filename, blob);
                        successCount++;
                    } catch (err) {
                        console.warn(`Error fetching ${filename}:`, err);
                    }
                });

                await Promise.all(promises);

                if (successCount === 0) {
                    throw new Error("No images could be loaded. Likely a CORS/File protocol issue (Browser security restrictions). Try running a local server.");
                }

                const content = await zip.generateAsync({ type: "blob" });
                saveAs(content, `${zipFilename}.zip`);

                // Success State
                btn.innerHTML = `<i class="fas fa-check"></i> Done!`;
                setTimeout(() => btn.innerHTML = originalText, 2000);
            } catch (err) {
                console.error(err);
                btn.innerHTML = `<i class="fas fa-times"></i> Error`;
                alert(`Download failed: ${err.message}`);
            } finally {
                btn.style.pointerEvents = 'auto';
            }
        }

        // Lightbox Functions
        function openLightbox(src) {
            const lightbox = document.getElementById('lightbox');
            const lightboxImg = document.getElementById('lightbox-img');
            lightbox.style.display = "flex";
            // Proper encoding for src in the lightbox
            lightboxImg.src = encodeURI(src);
        }

        function closeLightbox() {
            document.getElementById('lightbox').style.display = "none";
        }
    </script>
"""

content = content[:script_start] + new_script + content[script_end:]

with codecs.open(r"c:\Users\victor\3D Objects\APSOMU\gallery.html", "w", "utf-8") as f:
    f.write(content)
