from lxml import etree

def trasforma_xml_con_xslt(xml, xslt):
    try:
        # Carica il file XML e il foglio di stile XSLT
        xml_tree = etree.parse(xml)
        xslt_tree = etree.parse(xslt)
        
        # Crea il trasformatore XSLT
        transform = etree.XSLT(xslt_tree)
        
        # Applica la trasformazione
        nuovo_xml = transform(xml_tree)
        
        # Restituisci il risultato come stringa
        return str(nuovo_xml)
    except Exception as e:
        return str(e)

# Percorsi dei file XML e XSLT
file_xml = 'input.xml'
file_xslt = 'trasformazione.xsl'

# Esegui la trasformazione
risultato = trasforma_xml_con_xslt(file_xml, file_xslt)
print(risultato)
