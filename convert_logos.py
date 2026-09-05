import fitz
import os
import glob

pdf_files = glob.glob('logos/*.pdf')
os.makedirs('assets', exist_ok=True)

for pdf_path in pdf_files:
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    pix = page.get_pixmap(alpha=True, dpi=300)
    
    basename = os.path.basename(pdf_path).replace('.pdf', '.png')
    out_path = os.path.join('assets', basename)
    pix.save(out_path)
    print(f"Saved {out_path}")
