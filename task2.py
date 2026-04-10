from fpdf import FPDF

# 1. Sample Data (Analyze this)
data = {
    "Project Name": "Noida Expo 2026",
    "Developer": "Aditya Tripathi",
    "Total Tasks": 32,
    "Status": "Completed",
    "Completion Rate": "100%"
}

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Automated Project Status Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# 2. PDF Generation Logic
pdf = PDFReport()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Adding Content to PDF
pdf.set_text_color(0, 51, 102) # Dark Blue Header
pdf.cell(200, 10, txt="Analysis Summary:", ln=True, align='L')
pdf.ln(5)

pdf.set_text_color(0, 0, 0) # Black Text
for key, value in data.items():
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(50, 10, txt=f"{key}:", border=0)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, txt=f"{value}", border=0, ln=True)

pdf.ln(20)
pdf.set_fill_color(200, 220, 255)
pdf.cell(0, 10, txt="Report generated automatically via Python Script.", ln=True, align='C', fill=True)

# 3. Save the PDF
pdf.output("Project_Report.pdf")
print("✅ PDF Report Generated Successfully: Project_Report.pdf")
