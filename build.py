# Packs the 3D models into the page so it works as a single file
import base64, re, sys
src = open('/home/user/snooker/index.src.html').read()
def inline(m):
    return base64.b64encode(open('/home/user/snooker/assets/' + m.group(1), 'rb').read()).decode()
out = re.sub(r'@@ASSET:([\w.-]+)@@', inline, src)
open('/home/user/snooker/index.html', 'w').write(out)
print('built', len(out) // 1024, 'KB')
