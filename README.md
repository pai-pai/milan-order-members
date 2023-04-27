# milan-order-members

Scrape all people data on this page https://consulentidellavoro.mi.it/ordine/gli-iscritti-allordine/ and the following ones (84 pages total, pagination is at bottom).

Result csv file should contain:
- Nome
- Numero
- Codice fiscale
- PEC
- Status
- Indirizzo
- Città
- Provincia

Example:
- Abagnale Amalia
- 1810
- BGNMLA60H47A294O
- a.abagnale@consulentidellavoropec.it
- Attivo
- Via C. Poma 7
- Milano
- Mi

### List page

<img src="https://pai-pai-github-images.s3.amazonaws.com/milan-order-members-page.png" height="75%" width="75%" alt="List page" />

### Result

<img src="https://pai-pai-github-images.s3.amazonaws.com/milan-order-members-result.png" height="75%" width="75%" alt="Result" />

## Technology stack
- Scrapy
