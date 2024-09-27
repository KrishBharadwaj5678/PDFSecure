import streamlit as st
from PyPDF2 import PdfWriter,PdfReader

st.set_page_config(
    page_title="Encrypt & Decrypt PDF document",
    page_icon="icon.png",
    menu_items={
        "About":"PDF Secure is your go-to solution for encrypting and decrypting PDF passwords. Encrypt your PDFs to protect confidential information or decrypt them for easy access. Download your files securely and enjoy peace of mind knowing your documents are safe with PDF Secure."
    }
)

st.write("<h2 style='color:#F74648;'>Protect and Manage Your PDFs Effortlessly</h2>",unsafe_allow_html=True)
tab1,tab2=st.tabs(["Encrypt PDF","Decrypt PDF"])

out=PdfWriter()

def rd_pdf(val):
    file=st.file_uploader("Upload PDF",type="pdf",accept_multiple_files=False,key=val)
    return file

def addPages():
    for i in range(0,len(fil.pages)):
        page=fil.pages[i]
        out.add_page(page)

def createFile(filename):
     with open(filename,"wb") as wpdf:
         out.write(wpdf)

def download(filename):
    with open(filename,"rb") as rdpdf:
        st.download_button("Download",rdpdf.read(),filename) 

with tab1:

    file=rd_pdf(1)
    if file:
        pasword=st.text_input("Set a password to protect your PDF file",placeholder="Type password",type="password")
        if pasword:

            btn=st.button("Encrypt")
            if btn:
                fil=PdfReader(file)

                addPages()
                out.encrypt(pasword)
                createFile("encrypted.pdf")
                st.toast("PDF Encrypted Successfully!",icon="🔒")
                download("encrypted.pdf")

with tab2:
    file=rd_pdf(2)
    if file:
        fil=PdfReader(file)
        if fil.is_encrypted:
            
            decry_pass=st.text_input("Type this file’s password to unlock it",placeholder="Password",type="password")

            if decry_pass:
                btn=st.button("Decrypt")
                if btn:
                    
                    try:
                        fil.decrypt(decry_pass)
                        
                        addPages()
                        createFile("decrypted.pdf")
                        st.toast("PDF Decrypted Successfully!",icon="🔑")
                        download("decrypted.pdf")
                    except:
                        st.error("Invalid Password!")

        else:
            st.success("PDF is already unlocked.")
