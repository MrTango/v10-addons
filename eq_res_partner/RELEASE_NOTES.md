## Modul eq_res_partner

#### 20.02.2019
#### Version 1.0.50
##### FIX
- Fixed name (full name) on many2one field  in res.users

#### 20.02.2019
#### Version 1.0.49
##### ADD
- added 3 new custom fiels (eq_custom1, eq_custom2, eq_custom3) defined here https://gitlab.ownerp.io/v10-myodoo-public/v10-addons/issues/22

#### 20.02.2019
#### Version 1.0.48
##### CHG
- Changed name of the function for compute display name in res.users

#### 22.01.2019
#### Version 1.0.47
##### CHG
- restored old logic for generating of display_name

#### 21.01.2019
#### Version 1.0.46
##### CHG
- changed logic for generating of display_name

#### 07.01.2019
#### Version 1.0.45
##### ADD
- add placeholder to zip on res.partner form view.

#### 17.12.2018
#### Version 1.0.44
##### FIX
- Commented the part for udpate the customer_number in write method

#### 05.12.2018
#### Version 1.0.43
##### ADD
- Overrided base java script function from UserMenu, for showing the full name in topbar_name
- Overrided _compute_display_name function in res.partner
- Full name is shown in Preferences too

#### 04.12.2018
#### Version 1.0.42
##### ADD
- New computed field display_name in res.users

#### 04.12.2018
#### Version 1.0.41
##### ADD
- New field eq_firstname in res.users model, related to eq_firstname field in res.partner
- Added to Tree and Form view

#### 17.10.2018
#### Version 1.0.40
##### CHG
- Contact: The Title now will only be shown when the contact is a person, not a company
- Fixed Break above the name-field when its a company

#### 13.08.2018
#### Version 1.0.39
##### FIX
- Zendesk-6084, fixed an error in call of search. We'll use sudo

#### 05.07.2018
#### Version 1.0.38
##### FIX
- Ticket 5923: singleton fix.

#### 21.06.2018
#### Version 1.0.37
##### CHG
- Changing customer_number if parent_id is set, and write the customer_number to this parent_id

#### 19.06.2018
#### Version 1.0.36
##### FIX
- Switching the meaning of received/send-emails

#### 18.06.2018
#### Version 1.0.35
##### CHG
- Changed logic of write() and create() method, Zendesk-5835

#### 14.06.2018
#### Version 1.0.34
##### CHG
- old state before changes restored

#### 14.06.2018
#### Version 1.0.33
##### CHG
- Our new extension of create handler to be able to set the same customer number by company and contact person

#### 08.06.2018
#### Version 1.0.32
##### CHG
- Ticket #5777: when type of adress now not set => 'contact'

#### 22.05.2018
#### Version 1.0.31
##### CHG
- Remove readonly from plz for contact type 'contact'.

#### 26.04.2018
#### Version 1.0.30
##### CHG
- All received/send mails of the subcontacts are shown under the smart buttons Received/Send Mails

#### 24.04.2018
#### Version 1.0.29
##### ADD
- add eq_house_no to res.company

#### 20.04.2018
#### Version 1.0.28
##### CHG
- Add contact type to sub contact tree view of a res.partner

#### 17.04.2018
#### Version 1.0.27
##### ADD
- now it's possible to search for customer number and supplier number.

#### 10.04.2018
#### Version 1.0.26
##### FIX
- wrong smart button and action send/received mails

#### 04.04.2018
#### Version 1.0.25
##### CHG
- first view of contacts now tree view (old kanban)

#### 04.04.2018
#### Version 1.0.24
##### CHG/FIX
- another performance issue: change kanban view in res.partner form view (contacts) to list view.

#### 03.04.2018
#### Version 1.0.23
##### FIX
- performance issue in res.partner is now resolved

#### 03.04.2018
#### Version 1.0.22
##### CHG
- update of po-file with new German translations

#### 29.03.2018
#### Version 1.0.21
##### FIX
- update apps caused a odoo error, when you want to open a res.partner

#### 28.03.2018
#### Version 1.0.20
##### FIX
- Ticket 5479: contact of company creation caused a odoo error.

#### 26.03.2018
#### Version 1.0.19
##### CHG
- Two new buttons on the form view of the customer
- Send mails are for seeing the mails that are sent to the current customer
- Received mails are for see the mails that are received from the current customer

#### 09.03.2018
#### Version 1.0.18
##### ADD
- add field supplier_number and customer_number

#### 06.03.2018
#### Version 1.0.17
##### ADD
- Ticket 5402: Anpassung: Sofern bei dem Unterkontakt eine Straße gepflegt ist, wird diese bei der Änderung der Straße der Mutter nicht mehr überschrieben.
- Ist bei dem Kindkontakt keine Straße hinterlegt, so wird die Straße der Mutter übernommen.

#### 06.03.2018
#### Version 1.0.16
##### ADD
- Kundennummer/Lieferantennumer Anzeige entfernt.

#### 31.01.2018
#### Version 1.0.15
##### ADD
- Ticket 5215: Anpassung bei der Erstellung eines Unterkontakts.
- Adresse der Mutter wird nur dann gezogen und bei dem Unterkontakt gespeichert ('Kontakt'), wenn keine Straße bei dem Unterkontakt gespeichert ist.

#### 16.11.2017
#### Version 1.0.14
##### CHG
- Umbenennen des Moduls zu Kontakt Optimierungen

#### 18.09.2017
#### Version 1.0.13
##### CHG
- Kanbanerweiterung wieder hinzugefügt.

#### 15.09.2017
#### Version 1.0.12
##### CHG
- Kanbanerweiterung entfernt.

#### 31.07.2017
#### Version 1.0.11
##### CHG
- Modulbeschreibung erweitert 

#### 17.07.2017
#### Version 1.0.10
##### CHG
- Titel eines Kontaktes nun normal-groß
- PLZ nun direkt unterhalb der Stadt im EDIT-Modus


#### 03.07.2017
#### Version 1.0.9
##### CHG
(VEP-90) Kontaktmaske der Kundenansicht bearbeitet:
- Vorname hinzugefügt wenn der Kontakt keine Firma ist
- eq_name2 & eq_name3 hinzugefügt wenn der Kontakt eine Firma ist
- Label von Ansprechpartner auf "Name" gewechselt, damit es auch für Firmen sinnvoll benannt ist
- Übersetzung von "Address" gefixt

#### 03.07.2017
#### Version 1.0.8
##### CHG
- Übersetzungsfehler korrigiert "E-Mail (zusätzlich", fehlte eine Klammer

#### 21.06.2017
#### Version 1.0.7
##### CHG
- Anpassungen für Anzeige der Kunden- und Lieferantennr in Kanbanview


#### 20.06.2017
#### Version 1.0.6
##### CHG
- VEP-87: Anzeige von Kunden- und Lieferantennr in Kanbanview


#### 20.06.2017
#### Version 1.0.5
##### CHG
- Anpassungen für Ordnerstruktur


#### 08.06.2017
#### Version 1.0.4
##### CHG
- Modul-Beschreibungsseite angepasst und doppelte Einträge in der Manifestdatei entfernt.

#### 29.05.2017
#### Version 1.0.3
##### CHG
- Anpassungen für Partnerformular: Kunden-/Lieferantennr; neue Felder E-Mail 2 und Telefon 2


#### 24.05.2017
#### Version 1.0.2
##### CHG
- Weitere Anpassungen für Partnerformular


#### 24.05.2017
#### Version 1.0.1
##### CHG
- Ansicht der Partner bearbeitet


#### 23.05.2017
#### Version 1.0.0
##### ADD
- Neues Modul für die Erweiterung der Partner

