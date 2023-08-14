import streamlit as st
from lxml import etree

def trasforma_xml_con_xslt(xml_content, xslt_content):
    try:
        xml_tree = etree.XML(xml_content)
        xslt_tree = etree.XML(xslt_content)
        
        transform = etree.XSLT(xslt_tree)
        
        nuovo_xml = transform(xml_tree)
        
        return str(nuovo_xml)
    except Exception as e:
        return str(e)

default_xml = '''<root>
    <element>Exemple</element>
</root>'''
default_xslt = '''<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="yes"/>
    
    <xsl:template match="/">
        <output>Exemple</output>
    </xsl:template>
</xsl:stylesheet>'''

st.title("XSLT Tranformer")

st.header("Insert your XML and XSLT contents")

xml_input = st.text_area("Past your XML content here", value=default_xml, height=300, key="xml")


xslt_input = st.text_area("Paste your XSLT content here", value=default_xslt, height=300, key="xslt")


if st.button("Run Transformation"):
    if xml_input and xslt_input:
        risultato = trasforma_xml_con_xslt(xml_input, xslt_input)
        st.header("Transformation Result")
        st.code(risultato, language="xml")

st.sidebar.header("Informations")
st.sidebar.markdown("This is a simple tool for performing XSLT transformations on XML using Streamlit.")
