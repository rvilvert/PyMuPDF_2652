import fitz

doc = fitz.open("PDF_Example.pdf")
pdf_page = doc[0]

p1 = fitz.Point(0,0)
p2 = fitz.Point(50,50)

pdf_page.clean_contents()
#pdf_page.wrap_contents()

pdf_page.draw_rect([0,0,50,50], color=(1, 0, 0), fill=(0, 1, 0), width=3)

doc.save("PDF_Example_WithRect3.pdf")
doc.close()
