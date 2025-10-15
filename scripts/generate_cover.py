from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
TITLE = "IA e RPA: O Futuro da Automação Inteligente e seus Impactos na Carreira"
SUBTITLE = "Como Inteligência Artificial e RPA estão transformando o trabalho e criando novas oportunidades"
AUTHOR = "por Pedro Cunha"
LOGO = "IA & RPA Segura"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "capa.png"
def main():
    W, H = 1200, 1200
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    top = (6, 72, 188); bottom = (24, 153, 86)
    for y in range(H):
        t = y/(H-1)
        r = int(top[0]*(1-t)+bottom[0]*t)
        g = int(top[1]*(1-t)+bottom[1]*t)
        b = int(top[2]*(1-t)+bottom[2]*t)
        draw.line([(0,y),(W,y)], fill=(r,g,b))
    try:
        bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 66)
        semi = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
        small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    except:
        bold = semi = small = ImageFont.load_default()
    def center(text, y, font):
        w, h = draw.textbbox((0,0), text, font=font)[2:]
        draw.text(((W-w)//2, y), text, fill="white", font=font)
    center(TITLE, 160, bold)
    center(SUBTITLE, 260, semi)
    center(AUTHOR, 330, small)
    cx, cy = W//2, 520
    draw.ellipse((cx-40, cy-40, cx+40, cy+40), outline=(255,255,255), width=6)
    draw.rectangle((cx-8, cy+40, cx+8, cy+110), fill=(255,255,255))
    draw.rectangle((cx-28, cy+110, cx+28, cy+126), fill=(255,255,255))
    center(LOGO, 640, semi)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG")
if __name__ == "__main__":
    main()
