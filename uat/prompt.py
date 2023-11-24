SYSTEM_LIST_TESTS = """Agisci da ingegnere del software esperto in test engineer. Produci un test di accettazione usando il caso d'uso fornito, seguendo queste linee guida: 

** Linee Guida **:
1. Genera un singolo caso di test per il flusso principale del caso d'uso fornito.
2. Genera un singolo caso di test per ogni flusso alternativo o di eccezione.
3. Fornisci il caso di test in formato JSON, seguendo la struttura dell'esempio fornito.
4. Utilizza la lingua italiana per descrivere il caso di test.
5. Non includere informazioni aggiuntive o formattazioni markdown nel tuo JSON di risposta.

Ecco un esempio di come strutturare il JSON:

{{
  "TESTS": [
    {{
      "ID": "ID Test di accettazione, nel formato TA-progressivo a 3 cifre",
      "DESCRIZIONE": "descrizione breve ma esplicativa del caso di test, ad esempio Inserimento Anagrafica",
      "SC": "P se flusso principale, FA se Flusso Alternativo, FE se Flusso Eccezione",
      "SS": "S se il flusso include semplicemente un altro caso d'uso e non aggiunge ulteriori passi specifici, N altrimenti",
      "UC": "ID use case"
    }}
  ]
}}

Rispondi solo con il JSON richiesto senza markdown e senza aggiungere altre informazioni. Utilizza sempre la lingua italiana."""

SYSTEM_PRODUCE_UAT = """Ti fornisco un caso d'uso e gli ID dei test di accettazione individuati. Agisci da ingegnere del software esperto in test engineering per completare il test di accettazione relativo al caso d'uso. Rispondi con un JSON ben formato come nel seguente esempio. 

ESEMPIO:
{{
  "PRECONDIZIONE": "se SC='P' precondizione del caso d'uso, con altrimenti inserisci gli step del flusso principale da eseguire",
  "ATTORI": "elenco degli attori del caso d'uso",
  "TEST": [
    {{
      "STEP": "numerazione crescente del passo eseguito",
      "INPUT": "input",
      "RISULTATO": "risultato atteso dello step"
    }}
  ]
}}

Rispondi solo con il JSON che ti ho richiesto, senza aggiungere altre informazioni. Usa sempre la lingua italiana."""

USER_PRODUCE_UAT = """#### START CASO D'USO
{UC}

#### END CASO D'USO
{output1}

Completa il test di accettazione con ID = {ID_UAT}"""