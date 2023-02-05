import pdfkit
import streamlit as st
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime



st.title('Invoice Generator')

st.write('Generate your Invoice')

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())
template = env.get_template("invoice.html")


with st.form("template_form"):
    logo = st.text_input('Logo', value='templates/mashable.png')
    left, right = st.columns((2, 2))
    company_name = left.text_input("Company Name", value="MASHABLE VENTURES LTD")
    company_address = right.text_input('Company Address', value='12 London Way')
    company_city = left.text_input('Company City', value='Houston, Texas')
    customer_name = right.text_input('Customer name', value='Mr. Johnson Halls')
    customer_address = left.text_input("Customer Address", value='15B Shuttle Service Way')
    invoice_number = right.text_input('Invoice Number', value='6579')
    date = datetime.now().strftime('%B %-d, %Y')
    due_date = left.text_input('Due Date', value='March 10, 2023')
    customer_email = right.text_input('Customer Email Address', value='johnsonhalls@gmail.com')
    payment_method = left.text_input('Payment Method', value='Bank Transfer')
    payment_number = right.text_input('Payment Method Number', value='1289')
    prod_1 = left.text_input('Enter Produt Name', value='Website design')
    amt_1 = right.number_input('Enter Amount ($)', value='Hosting (3 months)')
    prod_2 = left.text_input('Enter Product Name', value='Domain name (1 year)')
    amt_2 = right.number_input('Enter Amount ($)', value=300)
    prod_3 = left.text_input('Enter Product Name', value=75)
    amt_3 = right.number_input('Enter Amount ($)', value=10)
    submit = st.form_submit_button('Submit')

    total = amt_1 + amt_2 + amt_3

if submit:
    html = template.render(
        company_name=company_name,
        company_address=company_address,
        company_city=company_city,
        customer_name=customer_name,
        customer_address=customer_address,
        invoic_number=invoice_number,
        date=date,
        due_date=due_date,
        customer_email=customer_email,
        payment_method=payment_method,
        payment_number=payment_number,
        prod_1=prod_1,
        prod_2=prod_2,
        prod_3=prod_3,
        amt_1=amt_1,
        amt_2=amt_2,
        amt_3=amt_3,
        total=total
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    st.success('Invoice generated successfully!')

    st.download_button(
        'Download PDF',
        data=pdf,
        file_name='invoice.pdf',
        mime='application/octet-stream',
    )

