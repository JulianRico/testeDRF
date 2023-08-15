import io
from django.http import FileResponse
from django.views import View
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


class SVGtoPDFView(View):
    def get(self, request):
        svg_code = """
            <svg width="100" height="100">
                <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
            </svg>
        """

        response = FileResponse(self.convert_svg_to_pdf(
            svg_code), as_attachment=True, filename='svg_to_pdf.pdf')
        return response

    def convert_svg_to_pdf(self, svg_code):
        buffer = io.BytesIO()

        drawing = svg2rlg(io.StringIO(svg_code))
        renderPDF.drawToFile(drawing, buffer)

        buffer.seek(0)
        return buffer
