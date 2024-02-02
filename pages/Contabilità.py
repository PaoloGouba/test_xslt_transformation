import streamlit as st
import pandas as pd
from lxml import etree
import os

st.title("Convertitore Fatture Excel - XML")

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

def sanitize(tag_name):
    """Sostituisce spazi con underscore e aggiunge un prefisso se il nome inizia con un numero o caratteri non validi."""
    tag_name = ''.join(e for e in tag_name if e.isalnum() or e in ['_'])
    tag_name = tag_name.replace(' ', '_')
    if not tag_name[0].isalpha():
        tag_name = 'tag_' + tag_name
    return tag_name

def dataframe_to_xml(df, root_tag="root", row_tag="row"):
    root = Element(root_tag)
    for _, row in df.iterrows():
        row_element = SubElement(root, row_tag)
        for field, value in row.items():
            field = sanitize(field)  # Sanitize field name to make it a valid XML tag
            field_element = SubElement(row_element, field)
            field_element.text = str(value)
    return tostring(root, 'utf-8')

# Funzione per applicare la trasformazione XSLT
def apply_xslt(xml_bytes, xslt_path="PA.xslt"):
    xml_tree = etree.fromstring(xml_bytes)
    xslt_tree = etree.parse(xslt_path)
    transform = etree.XSLT(xslt_tree)
    transformed_tree = transform(xml_tree)
    return etree.tostring(transformed_tree, pretty_print=True)

# Caricamento file Excel e XSLT
uploaded_files = st.file_uploader("Scegli il tuo file Excel", accept_multiple_files=True, type=['xlsx'])

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Legge il file Excel in un DataFrame
        df = pd.read_excel(uploaded_file, engine='openpyxl')
        # Converti il DataFrame in XML
        xml_bytes = dataframe_to_xml(df)
        print(xml_bytes)
        
        # Applica la trasformazione XSLT
        transformed_xml_bytes = apply_xslt(xml_bytes)
        
        # Mostra il nome del file e permette il download del file XML trasformato
        st.write("Filename:", uploaded_file.name)
        st.download_button(label="Download XML",
                           data=transformed_xml_bytes,
                           file_name=uploaded_file.name.replace('.xlsx', '.xml'),
                           mime='text/xml')

