# Packs the 3D models and voices into the page so it works as a single file.
# Run it from anywhere: it reads index.src.html and the assets folder beside it, and writes index.html there.
import base64, os, re
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'index.src.html')).read()
def inline(m):
    return base64.b64encode(open(os.path.join(here, 'assets', m.group(1)), 'rb').read()).decode()
out = re.sub(r'@@ASSET:([\w.-]+)@@', inline, src)
open(os.path.join(here, 'index.html'), 'w').write(out)
print('built', len(out) // 1024, 'KB')
