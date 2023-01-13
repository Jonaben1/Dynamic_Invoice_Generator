from base64 import b64encode
import streamlit as st
from datetime import datetime
from reportlab.pdfgen.canvas import Canvas

st.title('DYNAMIC INVOICE GENERATOR')

st.write('Enter your company and product details, then, your invoice will be generated')

with st.form('Template Form'):
    left, right = st.columns((2,2))
    logo = left.text_input('Company Logo', value='tnw.png')
    company_name = right.text_input('Company Name', value='JONABEN ENTERPRISES LIMITED')
    address = left.text_input('Company Address', value='12 London Way')
    location = right.text_input('Company Location', value='Istanbul, Turkey')
    reg_num = left.text_input('Registration Number', value='234558B6VX')
    invoice_num = right.text_input('Invoice Number', value='6579')
    date = datetime.today().strftime('%B %-d, %Y')
    customer_name = left.text_input('Customer Name', value='Mr. Bill Gates')
    company_number = right.text_input('Company Phone Number', value='012394736')

    st.header('Product 1')
    # Goods description_1s
    left, right = st.columns((2,2))
    item_1 = left.text_input('Name of product', value='Laptop')
    price_per_unit_1 = right.number_input("Price per unit ($)", 1, 100, 60)
    quantity_1 = st.slider('Quantity', 1, 500, 80)
    amount_1 = price_per_unit_1 * quantity_1

    # Goods description_2
    st.header('Product 2')
    left, right = st.columns((2,2))
    item_2 = left.text_input('Name of product', value='Decoder')
    price_per_unit_2 = right.number_input("Price per unit ($)", 1, 100, 24)
    quantity_2 = st.slider("Quantity", 1, 500, 10)
    amount_2 = price_per_unit_2 * quantity_2
    # Goods description_3
    st.header('Product 3')
    left, right = st.columns((2,2))
    item_3 = left.text_input('Name of product', value='Toys')
    price_per_unit_3 = right.number_input("Price per unit ($)", 1, 100, 25)
    quantity_3 = st.slider("Quantity", 1, 500, 35)
    amount_3 = price_per_unit_3 * quantity_3

    # Goods description_4
    st.header('Product 4')
    left, right = st.columns((2,2))
    item_4 = left.text_input('Name of product', value='Books')
    price_per_unit_4 = right.number_input("Price per unit ($)", 1, 100, 35)
    quantity_4 = st.slider("Quantity", 1, 500, 15)
    amount_4 = price_per_unit_4 * quantity_4

    # Goods description_5
    st.header('Product 5')
    left, right = st.columns((2,2))
    item_5 = left.text_input('Name of product', value='Vanilla')
    price_per_unit_5 = right.number_input("Price per unit ($)", 1, 100, 95)
    quantity_5 = st.slider("Quantity", 1, 500, 65)
    amount_5 = price_per_unit_5 * quantity_5
    #total
    total = amount_1 + amount_2 + amount_3 + amount_4 + amount_5
    submit = st.form_submit_button()



def template():
    c = Canvas("invoice.pdf", pagesize=(230, 250), bottomup=0)
    # Logo Section
    # Setting th origin to (10,40)
    c.translate(10, 40)
    # Inverting the scale for getting mirror Image of logo
    c.scale(1, -1)
    # Inserting Logo into the Canvas at required position
    # c.drawImage(data, 0, 0, width=50, height=30)
    c.drawInlineImage(logo, 0, -25, width=50, height=30)
    # Title Section
    # Again Inverting Scale For strings insertion
    c.scale(1, -1)
    # Again Setting the origin back to (0,0) of top-left
    c.translate(-10, -40)
    # Setting the font for Name title of company
    c.setFont("Helvetica-Bold", 10)
    # Inserting the name of the company
    c.drawCentredString(145, 20, company_name)
    # For under lining the title
    #c.line(70,52, 180, 22)
    # Changing the font size for Specifying Address
    c.setFont("Helvetica-Bold", 5)
    c.drawCentredString(125,30, address)
    c.drawCentredString(125,35, location)
    # Changing the font size for Specifying REG Number of firm
    c.setFont("Helvetica-Bold",6)
    c.drawCentredString(125,42, reg_num)

    # Line Seprating the page header from the body
    c.line(5, 45, 225, 45)

    # Document Information
    # Changing the font for Document title
    c.setFont("Courier-Bold", 8)
    c.drawCentredString(120,55, "INVOICE")

    # This Block Consists of Costumer Details
    c.roundRect(15, 63, 200, 40, 10, stroke=1, fill=0)
    c.setFont("Times-Bold", 5)
    c.drawRightString(70, 70, "INVOICE No.:  " + invoice_num)
    c.drawRightString(81, 80,"DATE :  "+ date)
    c.drawRightString(105, 90,"CUSTOMER NAME:  " + customer_name)
    c.drawRightString(79, 100,"PHONE No.:  " + company_number)

    # This Block Consists of Item Description
    c.roundRect(15, 108, 200, 130, 10, stroke=1, fill=0)
    c.line(15, 120, 215, 120)
    c.drawCentredString(25, 115,"S/N")
    c.drawCentredString(75, 115,"GOODS DESCRIPTION")
    c.drawCentredString(127,115,"RATE ($)")
    c.drawCentredString(148,115,"QTY")
    c.drawCentredString(183,115,"TOTAL ($)")
    # Drawing table for Item Description
    c.line(15,210,215,210)
    c.line(30,108,30,220)

    c.line(115,108,115,220)
    c.line(140,108,140,220)
    c.line(160,108,160,220)
    # Inputing Sales details for product 1
    c.line(15, 135, 215, 135)
    c.drawCentredString(23, 130, '1')
    c.drawCentredString(75, 130, item_1)
    c.drawCentredString(125, 130, str(price_per_unit_1))
    c.drawCentredString(148, 130, str(quantity_1))
    c.drawCentredString(183, 130, str(amount_1))
    #inputing sales details for product 2
    c.line(15, 155, 215, 155)
    c.drawCentredString(23, 150, '2')
    c.drawCentredString(75, 150, item_2)
    c.drawCentredString(125, 150, str(price_per_unit_2))
    c.drawCentredString(148, 150, str(quantity_2))
    c.drawCentredString(183, 150, str(amount_2))
    # inputing sales details for product 3
    c.line(15, 175, 215, 175)
    c.drawCentredString(23, 170, '3')
    c.drawCentredString(75, 170, item_3)
    c.drawCentredString(125, 170, str(price_per_unit_3))
    c.drawCentredString(148, 170, str(quantity_3))
    c.drawCentredString(183, 170, str(amount_3))

    # inputing sales details for product 4
    c.line(15, 195, 215, 195)
    c.drawCentredString(23, 190, '4')
    c.drawCentredString(75, 190, item_4)
    c.drawCentredString(125, 190, str(price_per_unit_4))
    c.drawCentredString(148, 190, str(quantity_4))
    c.drawCentredString(183, 190, str(amount_4))
     # inputing sales details for product 5
    c.drawCentredString(23, 205, '5')
    c.drawCentredString(75, 205, item_5)
    c.drawCentredString(125, 205, str(price_per_unit_5))
    c.drawCentredString(148, 205, str(quantity_5))
    c.drawCentredString(183, 205, str(amount_5))
     # Grand Total

    c.drawCentredString(75, 217, 'GRAND TOTAL')
    c.drawCentredString(183, 217, str(total))
    # Declaration and Signature

    c.line(15,220,215,220)
    c.line(100,220,100,238)
    c.drawString(20,225,"We declare that the above")
    c.drawString(20,230,"information is true.")
    c.drawString(20,235,"(This is system generated invoice)")
    c.drawRightString(200,235,"____________________Authorised Signatory")

    # End the Page and Start with new
    c.showPage()
    # Saving the PDF
    c.save()




# embed and display PDF


with open('invoice.pdf', 'rb') as pdf_file:
    pdf_byte = pdf_file.read()

st.download_button(label="Download Invoice",
    data=pdf_byte,
    file_name="rceipt.pdf",
    mime = 'application/octet-stream')


def show_pdf():
    with open('invoice.pdf', 'rb') as f:
        base64_pdf = b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

if submit:
    template()
    show_pdf()
