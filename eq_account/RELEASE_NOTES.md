## Modul eq_account

#### 25.10.2018
#### Version 1.0.68
##### FIX
- Ticket 6288: Invoice Report: for move_line quantity, changing the product_qty to product_uom_qty

#### 16.10.2018
#### Version 1.0.67
##### IMP
- Ticket 6268: Setting Title and Firstname only when the contact is NOT a company

#### 02.10.2018
#### Version 1.0.66
##### FIX
- Ticket 6238: fix expected singleton issue with loop.

#### 23.07.2018
#### Version 1.0.65
##### CHG
- payment term: changing CSS Construction from pre-line to pre-wrap without a DIV container

#### 20.07.2018
#### Version 1.0.64
##### ADD
- Adding css inside xml tags for making new lines in payment term note

#### 17.07.2018
#### Version 1.0.63
##### ADD
- change decorator account.invoice.line from api.multi to api.model

#### 27.06.2018
#### Version 1.0.62
##### ADD
- (Ticket 5943) Changing Invoice Report Address-IF-statements for, if parent address is a company, then show parent company name (instead of "if parent-contact has a name")

#### 27.06.2018
#### Version 1.0.61
##### ADD
- Creating new function for payment placeholders
- Showing payment note in report invoice

#### 25.06.2018
#### Version 1.0.60
##### FIX
- Ticket 5891: fix invoice report with retoure

#### 18.06.2018
#### Version 1.0.59
##### IMP
- Improve IF Statements for Correct customer No

#### 16.06.2018
#### Version 1.0.58
##### FIX
- Correct customer no functionality on INVOICE Report

#### 12.06.2018
#### Version 1.0.57
##### FIX
- Ticket 5800: addition bugfix.

#### 11.06.2018
#### Version 1.0.56
##### FIX
- Ticket 5800: fix in invoice report when there is a backorder_id.
- Ticket 5802: fix change to product_uom_qty (check also with wdm)

#### 06.06.2018
#### Version 1.0.55
##### FIX
- add account_account Security for sales_team view all documents.

#### 09.05.2018
#### Version 1.0.54
##### FIX
- fix if you use a product_uom like 8x1 pieces.

#### 27.04.2018
#### Version 1.0.53
##### CHG
- t t-if clause change with another t t-if clause from default_code (first with eq_move_ids, secound without eq_move_ids)

#### 23.04.2018
#### Version 1.0.52
##### FIX
- fix in account invoice report when only a service product is in the lines, it will be shown now.

#### 19.04.2018
#### Version 1.0.51
##### FIX
- bugfix in discount computation.

#### 10.04.2018
#### Version 1.0.50
##### CHG
- delete action for sending invoice (now in eq_mail_templates)

#### 09.04.2018
#### Version 1.0.49
##### FIX
- correct translation for account_payment_term_immediate in account module (odoo core bug)

#### 06.04.2018
#### Version 1.0.48
##### CHG
- move templates into new module eq_mail_templates

#### 05.04.2018
#### Version 1.0.47
##### FIX
- include discount into the computation of a invoice line.

#### 04.04.2018
#### Version 1.0.46
##### ADD
- add delivered at place in invoice report, if 'DAP' is set as incoterm.

#### 08.03.2018
#### Version 1.0.45
##### ADD
- Jira-Issue VAAB-1 und Jira-Issue VEP-176: Rechnungen beinhalten nun auch Teillieferungen.
- Kundenreferenz auf Positionsebene entfernt.

#### 26.02.2018
#### Version 1.0.44
##### FIX
- Übersetzung Rechnungsreport: Proforma Invoice zu Proforma Rechnung

#### 09.02.2018
#### Version 1.0.43
##### IMP
- Rechnungsreport: Kontakt E-Mailadresse hat nun mehr Platz und bricht bei zu langen Adressen nun um, statt den Block zu verziehen.

#### 29.01.2018
#### Version 1.0.42
##### FIX
- stock.picking @api.model Decorator hinzugefügt, um Fehlermeldung bei der Erstellung eines Lagervorgangs zu vermeiden.

#### 24.01.2018
#### Version 1.0.40
##### ADD
- Spalte 'Netto' in Eingangs-und Ausgangsrechnungen hinzugefügt.

#### 20.12.2017
#### Version 1.0.40
##### IMP
- Übersetzung angepasst (Auftragsnr.)

#### 19.12.2017
#### Version 1.0.39
##### IMP
- Beschreibungstexte bei Rechnungen nutzen nun eine größere Breite; Übersetzungen angepasst

#### 19.12.2017
#### Version 1.0.38
##### FIX
- Rabatte haben die Spalten im RechnungsReport falsch verschoben

#### 19.12.2017
#### Version 1.0.37
##### FIX
- Mini Fix: RechnungsReport: Wenn mehrere Steuersätze verwendet werden.

#### 19.12.2017
#### Version 1.0.36
##### CHG
- Rechnungs-Report: Übersetzungen angepasst; Artikelnr. Zeile (Spalte) Hinzugefügt; Währungszeichen für "Einzelpreis" hinzugefügt

#### 15.12.2017
#### Version 1.0.35
##### ADD
- Rechnungszeilen um das Liefer + Leistungsdatum ergänzt, für Artikel die versendet werden können

#### 24.11.2017
#### Version 1.0.34
##### CHG
Anpassung IDs + Layout.

#### 23.11.2017
#### Version 1.0.33
##### CHG
Vorlage Rechnung - Footer angepasst (grauer HG - neu)

#### 22.11.2017
#### Version 1.0.32
##### CHG
- RechnungsReport: Zahlungskonditionen werden nun aus dem Text der Zahlungskondition gezogen, statt vorher aus dem Namen

#### 22.11.2017
#### Version 1.0.31
##### CHG
- Invoice Vorlage Default Template wird jetzt gezogen

#### 22.11.2017
#### Version 1.0.30
##### CHG
- Invoice Vorlage mit Footer versehen (einkommentiert)

#### 22.11.2017
#### Version 1.0.29
##### CHG
- Custom Layout entfernt.

#### 22.11.2017
#### Version 1.0.28
##### CHG
- Anpassung Mail ID

#### 22.11.2017
#### Version 1.0.27
##### CHG
- Wichtig: Rechnungsvorlage vor dem Update löschen. Dadurch wird das alte Template gelöscht und die Übersetzungen neu erstellt.
- 'Übersetzung laden' überspielt nicht mehr die vorhandene Übersetzung.

#### 21.11.2017
#### Version 1.0.26
##### CHG
- invoice_send_by_email.xml bearbeitet (nbsp entfernt)

#### 21.11.2017
#### Version 1.0.25
##### CHG
- Löschfunktion mail.templates zu 'account' hinzugefügt.

#### 16.11.2017
#### Version 1.0.24
##### CHG
- Modul umbenannt in Finanzen (vorher: Account)

#### 07.11.2017
#### Version 1.0.23
##### CHG
- Description angepasst

#### 06.11.2017
#### Version 1.0.22
##### CHG
- Es wird nur das eingefügte Template zuvor entfernt.

#### 06.11.2017
#### Version 1.0.21
##### ADD
- Mail Template hinzugefügt 'Rechnung'.


#### 11.10.2017
#### Version 1.0.20
##### ADD
- Jira-Issue OE10-10: In den Rechnungsreport ein p-Element mit einer Abfrage auf die payment_term_id hinzugefügt, welcher für die fehlerfreie Installation von dem OCA-Modul
account_payment_partner notwendig ist.

#### 05.09.2017
#### Version 1.0.19
##### FIX
- Feld 'eq_move_ids' hinzugefügt, welche bei Teillieferungen benötigt werden.

#### 05.09.2017
#### Version 1.0.18
##### FIX
- Im Bezug auf Jira Issue VEP-139 gab es den gleichen Fehler, allerdings bei einer Teillieferung. Dieser wurde durch eine angepasste Abfrage behoben.

#### 31.08.2017
#### Version 1.0.17
##### ADD
- Referenzbeleg und Referenznr. werden nun auf den Rechnungen angedruckt

#### 28.08.2017
#### Version 1.0.16
##### FIX
- Auftragszeilen werden nun auch gedruckt wenn die Option für die Kategorien(Sektionen) nicht aktiviert wurde

#### 17.08.2017
#### Version 1.0.15
##### ADD
- Sektionen für die Rechnungen sind nun eingebunden und funktionieren
- Visuelle Anpassungen an dem Summenblock

#### 09.08.2017
#### Version 1.0.14
##### ADD
Rechnungsreport: Lieferdatum / Leistungstag auf Auftragszeilenposition nun im Rechnungsreport enthalten


#### 09.08.2017
#### Version 1.0.13
##### FIX
- BugFix Jira-Issue [VEP-139]: eq_move_id wird nicht mehr bei einer Rückerstattung gesetzt, dies hat den Odoo Error verursacht.

#### 04.08.2017
#### Version 1.0.12
##### ADD/CHG
- Dependency zu eq_sale_stock hinzugefügt (anhand der eq_sale_order_id wird die eq_ref_number (client_order_ref) bis in die stock.picking durchgezogen.
- eq_move_id hinzugefügt: Verbindung zwischen account.invoice.line und dem dazugehörigen stock.move

#### 03.08.2017
#### Version 1.0.11
##### ADD
- Report: USt.ID-Nr. wird nun auf der Rechnung angezeigt, wenn die Rechnung die Steuerzuordnung für EU Kunde mit eingetragener USt.ID-Nr. hat 

#### 01.08.2017
#### Version 1.0.10
##### IMP
- Report erweitert:
- Kopf und Fußtext hinzugefügt. 
- Lieferanschrift umgebaut mit eq_house_no, Citypart usw

#### 01.08.2017
#### Version 1.0.9
##### FIX
- Report: Es wurde noch ein Templating (in rot) angezeigt welche die Kategorien der Auftragszeilen enthalten sollte, dies funktioniert aber noch nicht und wurde nun erstmal wiedr ausgeblendet, damit der Rechnungs-Report wieder fehlerfrei aussieht.

#### 28.07.2017
#### Version 1.0.8
##### CHG
- Modulbeschreibung erweitert

#### 28.07.2017
#### Version 1.0.7
##### CHG
- Konfigurierbarer Seitenumbruch für Kopf- und Fußtexte im Report


#### 28.07.2017
#### Version 1.0.6
##### CHG
- Hilfsfunktionen für Report


#### 03.07.2017
#### Version 1.0.5
##### IMP
Summentabelle der Reports angepasst
- Übersetzung gepflegt
- Position und Ausrichtung korrigiert
- Zusätzliche Steuerzeilen-Tabelle ausgeblendet

#### 30.06.2017
#### Version 1.0.4
##### IMP
- Rechnugnsreport: Übersetzungen angepasst & korrigiert, Pos-Nr. hinzugefügt. Zeilenvariante überarbeitet & andere ausgeblendet

#### 29.06.2017
#### Version 1.0.3
##### CHG
- Rechnungsreport: Neuer Report überschreibt den Standard-Report

#### 22.06.2017
#### Version 1.0.2
##### CHG
- Anzeige von Kopf- und Fußtext bearbeitet


#### 22.06.2017
#### Version 1.0.1
##### CHG
- Neues Feld für Kopftext


#### 19.06.2017
#### Version 1.0.0
##### ADD
- Neues Modul für die Erweiterung des Moduls account
- Erweiterungen für Adressfelder einer Rechnung