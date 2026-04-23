import re, codecs

html_path = 'about.html'
text = codecs.open(html_path, 'r', 'utf-8').read()

# Replace the entire <style> block with the link to the external stylesheet
text = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="css/about.css">', text, flags=re.DOTALL)

# Remove all inline style="..." attributes to fully migrate to the CSS file control
text = re.sub(r'\sstyle="[^"]+"', '', text)

codecs.open(html_path, 'w', 'utf-8').write(text)
print("Migration completed.")
