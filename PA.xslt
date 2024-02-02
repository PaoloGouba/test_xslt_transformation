<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="yes" encoding="UTF-8" standalone="no"/>
    
    
    <xsl:template match="/root">
        <FatturaElettronica xmlns="http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2"
                            xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
                            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" versione="FPR12"
                            xsi:schemaLocation="http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2 C:/Users/Administrator/Documents/MapForce/NuovaMappatura/fatturaPA1.2.xsd">
            
            <xsl:apply-templates select="row"/>
        </FatturaElettronica>            
    </xsl:template>
    
    <xsl:template match="row">
        <FatturaElettronicaBody xmlns="">
            <DatiGenerali xmlns:p="http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2">
                <DatiGeneraliDocumento>
                    <!-- <TipoDocumento>TD01</TipoDocumento> -->
                    <Divisa>EUR</Divisa>
                    <Data><xsl:value-of select="substring(Dataemissione, 1, 10)"/></Data>
                    <Numero><xsl:value-of select="Numerofatt"/></Numero>
                    <ImportoTotaleDocumento><xsl:value-of select="Unnamed7"/></ImportoTotaleDocumento>
                </DatiGeneraliDocumento>
                <!-- <DatiDDT>
                    <NumeroDDT>DEL12160912</NumeroDDT>
                    <DataDDT><xsl:value-of select="Dataemissione"/></DataDDT>
                    <RiferimentoNumeroLinea>1</RiferimentoNumeroLinea>
                    <RiferimentoNumeroLinea>2</RiferimentoNumeroLinea> 
                </DatiDDT>-->
            </DatiGenerali>
            <DatiBeniServizi xmlns:p="http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2">
                <DettaglioLinee>
                    <!-- <NumeroLinea>1</NumeroLinea> 
                    <CodiceArticolo>
                        <CodiceTipo>Codice Art. fornitore</CodiceTipo>
                        <CodiceValore>0019</CodiceValore>
                    </CodiceArticolo>
                    <Descrizione>Commissione di Just-Eat</Descrizione>
                    <Quantita>1.00</Quantita>
                    <UnitaMisura>EA</UnitaMisura>
                    <PrezzoUnitario>70.15</PrezzoUnitario>
                    <PrezzoTotale>70.15</PrezzoTotale>
                    <AliquotaIVA>22.00</AliquotaIVA>-->
                    <!-- <RiferimentoAmministrazione>IVA Ordinaria 22%</RiferimentoAmministrazione>
                    <AltriDatiGestionali>
                        <TipoDato>INFO</TipoDato>
                        <RiferimentoTesto>Corrisp. comprensivo del C. A. Conai già assolto ove dovuto</RiferimentoTesto>
                    </AltriDatiGestionali>
                     -->
                </DettaglioLinee> 

                <DatiRiepilogo>
                    <!-- <AliquotaIVA>22.00</AliquotaIVA> -->
                    <ImponibileImporto> ImponibileImportototaleineuro </ImponibileImporto>
                    <Imposta> Impostatotaleineuro </Imposta>
                    <!-- <EsigibilitaIVA>I</EsigibilitaIVA> -->
                </DatiRiepilogo>
            </DatiBeniServizi>
            <!--
            <DatiPagamento xmlns:p="http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2">
                <CondizioniPagamento>TP02</CondizioniPagamento>
                <DettaglioPagamento>
                    <ModalitaPagamento>MP05</ModalitaPagamento>
                    <DataScadenzaPagamento>2024-02-07</DataScadenzaPagamento>
                    <ImportoPagamento>91.73</ImportoPagamento>
                    <IBAN>IT44O0305101699000000000060</IBAN>
                </DettaglioPagamento>
            </DatiPagamento>
            -->
        </FatturaElettronicaBody>
    </xsl:template>
    
</xsl:stylesheet>
