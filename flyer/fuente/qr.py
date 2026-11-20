# Genera el QR como SVG (módulos cuadrados para que se lea siempre, en los colores de la marca) y lo verifica leyéndolo con OpenCV.
import sys
from reportlab.graphics.barcode import qrencoder
URL=sys.argv[1]; OUT=sys.argv[2]; BN=len(sys.argv)>3 and sys.argv[3]=='bn'
q=qrencoder.QRCode(None, qrencoder.QRErrorCorrectLevel.H)
q.addData(URL); q.make()
n=q.getModuleCount(); M=4  # margen (zona silenciosa) de 4 módulos
ink='#000' if BN else '#2B1A15'; eye='#000' if BN else '#9E241C'
def finder(r,c): return (r<7 and c<7) or (r<7 and c>=n-7) or (r>=n-7 and c<7)
parts=[]
for r in range(n):
    for c in range(n):
        if q.isDark(r,c) and not finder(r,c):
            parts.append(f'<rect x="{c+M}" y="{r+M}" width="1" height="1"/>')
eyes=''
for (r,c) in ((0,0),(0,n-7),(n-7,0)):
    x,y=c+M,r+M
    eyes+=(f'<path fill="{eye}" fill-rule="evenodd" d="M{x} {y}h7v7h-7zM{x+1} {y+1}v5h5v-5z"/>'
           f'<rect x="{x+2}" y="{y+2}" width="3" height="3" fill="{eye}"/>')
S=n+2*M
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}" shape-rendering="crispEdges"><rect width="{S}" height="{S}" fill="#fff"/><g fill="{ink}">{"".join(parts)}</g>{eyes}</svg>'
open(OUT,'w').write(svg); print('módulos',n)
