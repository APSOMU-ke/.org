import codecs

# 1. Update CSS
css_path = r"c:\Users\victor\3D Objects\APSOMU\css\gallery.css"
with codecs.open(css_path, "r", "utf-8") as f:
    css_content = f.read()

# Replace .style1-slide definition
old_slide = """
.style1-slide {
    width: 500px;
    height: 350px;
    border-radius: 20px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 15px 50px rgba(0, 0, 0, 0.5);
    background: #000;
}
"""

new_slide = """
.style1-slide {
    width: 60vw;
    max-width: 800px;
    aspect-ratio: 16/9;
    height: auto;
    border-radius: 10px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 15px 50px rgba(0, 0, 0, 0.5);
    background: #000;
}
"""

if old_slide.strip() in css_content:
    css_content = css_content.replace(old_slide.strip(), new_slide.strip())

# Strip out style2 and style3
style2_idx = css_content.find("/* --- STYLE 2: EXPANDING CARDS --- */")
if style2_idx != -1:
    dl_btn_idx = css_content.find("/* Download Button Style */")
    if dl_btn_idx != -1:
        css_content = css_content[:style2_idx] + css_content[dl_btn_idx:]

with codecs.open(css_path, "w", "utf-8") as f:
    f.write(css_content)

# 2. Update HTML
html_path = r"c:\Users\victor\3D Objects\APSOMU\gallery.html"
with codecs.open(html_path, "r", "utf-8") as f:
    html_content = f.read()

new_main = """
    <main>
        <!-- Section 1: Members -->
        <section id="members" class="gallery-section style1-section" style="background: #050505; color: #fff;">
            <div class="category-header">
                <h2>Our Members</h2>
                <p>The Heart of APSOMU</p>
                <button class="download-btn" onclick="downloadCollection(galleryData['Members'], 'APSOMU_Members')">
                    <i class="fas fa-download"></i> Download Selection
                </button>
            </div>
            <div class="swiper members-swiper" style="width: 100%; padding-bottom: 50px;">
                <div class="swiper-wrapper" id="members-wrapper"></div>
                <div class="swiper-pagination" style="bottom: 0;"></div>
            </div>
        </section>

        <!-- Section 2: Launching -->
        <section id="launching" class="gallery-section style1-section" style="background: #111; color: #fff;">
            <div class="category-header">
                <h2>Association Launch</h2>
                <p>Witness the beginning of a structured platform for students.</p>
                <button class="download-btn" onclick="downloadCollection(galleryData['Launching'], 'APSOMU_Launch')">
                    <i class="fas fa-download"></i> Download Selection
                </button>
            </div>
            <div class="swiper launching-swiper" style="width: 100%; padding-bottom: 50px;">
                <div class="swiper-wrapper" id="launching-wrapper"></div>
                <div class="swiper-pagination" style="bottom: 0;"></div>
            </div>
        </section>

        <!-- Section 3: Public Lecture -->
        <section id="lecture" class="gallery-section style1-section" style="background: #050505; color: #fff;">
            <div class="category-header">
                <h2>Prof. PLO Lumumba Public Lecture</h2>
                <p>Ethical Leadership & Governance Insights</p>
                <button class="download-btn" onclick="downloadCollection(galleryData['Public Lecture'], 'Public_Lecture')">
                    <i class="fas fa-download"></i> Download Selection
                </button>
            </div>
            <div class="swiper lecture-swiper" style="width: 100%; padding-bottom: 50px;">
                <div class="swiper-wrapper" id="lecture-wrapper"></div>
                <div class="swiper-pagination" style="bottom: 0;"></div>
            </div>
        </section>

        <!-- Section 4: County Assembly -->
        <section id="county-visit" class="gallery-section style1-section" style="background: #111; color: #fff;">
            <div class="category-header">
                <h2>County Assembly Visit</h2>
                <p>Bridging Theory and Practice</p>
                <button class="download-btn" onclick="downloadCollection(galleryData['County Assembly'], 'County_Assembly')">
                    <i class="fas fa-download"></i> Download Selection
                </button>
            </div>
            <div class="swiper county-swiper" style="width: 100%; padding-bottom: 50px;">
                <div class="swiper-wrapper" id="county-wrapper"></div>
                <div class="swiper-pagination" style="bottom: 0;"></div>
            </div>
        </section>

        <!-- Section 5: AGM -->
        <section id="agm" class="gallery-section style1-section" style="background: #050505; color: #fff;">
            <div class="category-header">
                <h2>Annual General Meeting</h2>
                <p>Evaluating progress and transitioning leadership.</p>
                <button class="download-btn" onclick="downloadCollection(galleryData['AGM'], 'APSOMU_AGM')">
                    <i class="fas fa-download"></i> Download Selection
                </button>
            </div>
            <div class="swiper agm-swiper" style="width: 100%; padding-bottom: 50px;">
                <div class="swiper-wrapper" id="agm-wrapper"></div>
                <div class="swiper-pagination" style="bottom: 0;"></div>
            </div>
        </section>
    </main>
"""

main_start = html_content.find("<main>")
main_end = html_content.find("</main>") + 7
html_content = html_content[:main_start] + new_main + html_content[main_end:]

new_script = """<script src="js/gallery-data.js"></script>
    <script>
        function buildSwiper(folderKey, containerId, swiperClass) {
            const data = galleryData[folderKey] || [];
            if (data.length === 0) return;
            const wrapper = document.getElementById(containerId);
            
            data.forEach((imgSrc) => {
                const safeImgSrc = encodeURI(imgSrc);
                const slide = document.createElement('div');
                slide.className = 'swiper-slide style1-slide';
                slide.onclick = () => openLightbox(imgSrc);
                // Set as background image for perfect 16:9 aspect ratio coverage mapping Guardian of Galaxy style
                slide.style.backgroundImage = `url('${safeImgSrc}')`;
                slide.style.backgroundSize = "cover";
                slide.style.backgroundPosition = "center";
                wrapper.appendChild(slide);
            });

            new Swiper("." + swiperClass, {
                effect: "coverflow",
                grabCursor: true,
                centeredSlides: true,
                slidesPerView: "auto",
                loop: data.length > 2,
                coverflowEffect: {
                    rotate: 0,
                    stretch: 150, // Pushes slides horizontally under
                    depth: 200,   // Scales background image depth
                    modifier: 1, 
                    slideShadows: true,
                },
                pagination: { 
                    el: "." + swiperClass + " .swiper-pagination", 
                    clickable: true 
                },
                initialSlide: Math.floor(data.length / 2) // start centered
            });
        }

        buildSwiper('Members', 'members-wrapper', 'members-swiper');
        buildSwiper('Launching', 'launching-wrapper', 'launching-swiper');
        buildSwiper('Public Lecture', 'lecture-wrapper', 'lecture-swiper');
        buildSwiper('County Assembly', 'county-wrapper', 'county-swiper');
        buildSwiper('AGM', 'agm-wrapper', 'agm-swiper');

        // Batch Download Function
        async function downloadCollection(filesArray, zipFilename) {
            if (!filesArray || filesArray.length === 0) {
                alert("No files to download in this category.");
                return;
            }

            const zip = new JSZip();
            const folder = zip.folder(zipFilename);
            const btn = event.currentTarget;
            const originalText = btn.innerHTML;

            btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Zipping ${filesArray.length} images...`;
            btn.style.pointerEvents = 'none';

            let successCount = 0;
            try {
                const promises = filesArray.map(async (filePath) => {
                    const filename = filePath.split('/').pop();
                    const encodedUrl = encodeURI(filePath);
                    try {
                        const resp = await fetch(encodedUrl);
                        if (!resp.ok) throw new Error(`Failed to load`);
                        const blob = await resp.blob();
                        folder.file(filename, blob);
                        successCount++;
                    } catch (err) {}
                });

                await Promise.all(promises);

                const content = await zip.generateAsync({ type: "blob" });
                saveAs(content, `${zipFilename}.zip`);
                btn.innerHTML = `<i class="fas fa-check"></i> Done!`;
                setTimeout(() => btn.innerHTML = originalText, 2000);
            } catch (err) {
                btn.innerHTML = `<i class="fas fa-times"></i> Error`;
                alert(`Download failed.`);
            } finally {
                btn.style.pointerEvents = 'auto';
            }
        }

        function openLightbox(src) {
            document.getElementById('lightbox').style.display = "flex";
            document.getElementById('lightbox-img').src = encodeURI(src);
        }
        function closeLightbox() {
            document.getElementById('lightbox').style.display = "none";
        }
    </script>
"""

script_start = html_content.find("<script src=\"js/gallery-data.js\">")
script_end = html_content.find("</body>")
html_content = html_content[:script_start] + new_script + html_content[script_end:]

with codecs.open(html_path, "w", "utf-8") as f:
    f.write(html_content)

print("Standardized Gallery successfully applied.")
