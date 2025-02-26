import fpdf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def fill_pdf(pdf_file, data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)

    pdf.image("static/rmklogo.png", x=10, y=10, w=25, h=25)
    pdf.image("static/rmkyears.png", x=172, y=10, w=25, h=25)

    pdf.set_font("Times", size=16, style="B")
    title_y = 15
    pdf.set_y(title_y)
    pdf.cell(190, 10, txt="R.M.K College Of Engineering And Technology", ln=1, align="C")
    pdf.set_font("Times", size=14, style="B")
    pdf.cell(190, 10, txt="Outing Form", ln=1, align="C")
    pdf.ln(5)

    pdf.set_font("Times", size=14, style="B")
    room_no_y = pdf.get_y() + 8  
    pdf.set_y(room_no_y)
    pdf.cell(0, 10, txt="Room No: " + data["Room No"], align="R", ln=1)
    del data["Room No"]
    pdf.ln(2)

    pdf.set_font("Times", size=12, style="B")
    cell_width = 85
    for key, value in data.items():
        pdf.cell(cell_width, 10, txt=key + ":", border=0, align="L")
        pdf.set_font("Times", size=13) 
        pdf.cell(cell_width, 10, txt=value, border=0, ln=1, align="L")
        pdf.ln(1)

    pdf.ln(28)

    pdf.set_font("Times", size=14, style="B") 
    pdf.cell(60, 10, txt="Class Counselor", align="C")
    pdf.cell(60, 10, txt="H.O.D", align="C")
    pdf.cell(60, 10, txt="Principal", ln=1, align="C")

    pdf.output(pdf_file, "F")

def send_email(pdf_file, recipient, sender, password):
    msg = MIMEMultipart()
    with open(pdf_file, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={pdf_file}")
    msg.attach(part)
    msg["To"] = recipient
    msg["From"] = sender
    msg["Subject"] = "Outing Form"
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(msg)

def email_data(id, datas):
    if 'd' in datas:
        value = datas['d']
    else:
        value = None
    # rest of the code

    data = {}
    num = 0
    keys = ["Id", "Name", "Registeration Number", "Room No", "Department", "Email", "Phone Number", "Address", "Leaving Date", "Arriving Date",]
    for key,num in keys:
        value =  datas[num]
        data[key] = value
    pdf_file = "Outing Form.pdf"
    fill_pdf(pdf_file, data)
    recipient = data['Email']
    sender = "Enter your email"
    password = "Enter your passkey"
    send_email(pdf_file, recipient, sender, password)
    print("\"Successfully Sent the E-mail\"")
