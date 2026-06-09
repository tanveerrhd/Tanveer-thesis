import sys
from pathlib import Path
from markdown import markdown
from xhtml2pdf import pisa

def md_to_pdf(md_file, pdf_file=None):
    md_path = Path(md_file)
    html = markdown(md_path.read_text(encoding='utf-8'), extensions=['extra','tables'])
    html = "<meta charset='utf-8'>\n" + html
    if pdf_file is None:
        pdf_file = md_path.with_suffix('.pdf')
    with open(pdf_file, 'wb') as f:
        status = pisa.CreatePDF(html, dest=f)
    return status.err == 0, str(pdf_file)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        md = sys.argv[1]
    else:
        md = r"g:\My Drive\Hiroshima University\MS Thesis related\Presentations\Tanveer_meeting_template_en.md"
    ok, pdf = md_to_pdf(md)
    if ok:
        print('PDF_CREATED:' + pdf)
        sys.exit(0)
    else:
        print('PDF_ERROR:' + pdf)
        sys.exit(2)
