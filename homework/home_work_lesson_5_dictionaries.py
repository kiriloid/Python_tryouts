text1 = """Abkhazia
Afghanistan
Åland Islands
Albania
Algeria
American Samoa
Andorra
Angola
Anguilla
Antigua and Barbuda
Argentina
Armenia
Aruba
Ascension
Australia
Australian Antarctic Territory
Australian External Territories
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Barbuda
Belarus
Belgium
Belize
Benin
Bermuda
Bhutan
Bolivia
Bonaire
Bosnia and Herzegovina
Botswana
Brazil
British Indian Ocean Territory
British Virgin Islands
Brunei Darussalam
Bulgaria
Burkina Faso
Burundi
Cambodia
Cameroon
Canada
Cape Verde
Caribbean Netherlands
Cayman Islands
Central African Republic
Chad
Chatham Island, New Zealand
Chile
China
Christmas Island
Cocos (Keeling) Islands
Colombia
Comoros
Congo
Congo, Democratic Republic of the (Zaire)
Cook Islands
Costa Rica
Ivory Coast
Croatia
Cuba
Guantanamo Bay, Cuba
Curaçao
Cyprus
Czech Republic
Denmark
Diego Garcia
Djibouti
Dominica
Dominican Republic
East Timor
Easter Island
Ecuador
Egypt
El Salvador
Ellipso (Mobile Satellite service)
EMSAT (Mobile Satellite service)
Equatorial Guinea
Eritrea
Estonia
Ethiopia
Falkland Islands
Faroe Islands
Fiji
Finland
France
French Antilles
French Guiana
French Polynesia
Gabon
Gambia
Georgia
Germany
Ghana
Gibraltar
Global Mobile Satellite System (GMSS)
Globalstar (Mobile Satellite Service)
Greece
Greenland
Grenada
Guadeloupe
Guam
Guatemala
Guernsey
Guinea
Guinea-Bissau
Guyana
Haiti
Honduras
Hong Kong
Hungary
Iceland
ICO Global (Mobile Satellite Service)
India
Indonesia
Inmarsat SNAC
International Freephone Service (UIFN)
International Networks
International Premium Rate Service'
International Shared Cost Service (ISCS)
Iran
Iraq
Ireland
Iridium (Mobile Satellite service)
Isle of Man
Israel
Italy
Jamaica
Jan Mayen
Japan
Jersey
Jordan
Kazakhstan
Kenya
Kiribati
Korea, North
Korea, South
Kosovo
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Macau
Macedonia
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Martinique
Mauritania
Mauritius
Mayotte
Mexico
Micronesia, Federated States of
Midway Island, USA
Moldova
Monaco
Mongolia
Montenegro
Montserrat
Morocco
Mozambique
Myanmar
Nagorno-Karabakh
Namibia
Nauru
Nepal
Netherlands
Nevis
New Caledonia
New Zealand
Nicaragua
Niger
Nigeria
Niue
Norfolk Island
Northern Cyprus
Northern Ireland
Northern Mariana Islands
Norway
Oman
Pakistan
Palau
Palestine, State of
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Pitcairn Islands
Poland
Portugal
Puerto Rico
Qatar
Réunion
Romania
Russia
Rwanda
Saba
Saint Barthélemy
Saint Helena
Saint Kitts and Nevis
Saint Lucia
Saint Martin (France)
Saint Pierre and Miquelon
Saint Vincent and the Grenadines
Samoa
San Marino
São Tomé and Príncipe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Sint Eustatius
Sint Maarten (Netherlands)
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
South Georgia and the South Sandwich Islands
South Ossetia
South Sudan
Spain
Sri Lanka
Sudan
Suriname
Svalbard
Swaziland
Sweden
Switzerland
Syria
Taiwan
Tajikistan
Tanzania
Telecommunications for Disaster Relief by OCHA
Thailand
Thuraya (Mobile Satellite service)
Togo
Tokelau
Tonga
Transnistria
Trinidad and Tobago
Tristan da Cunha
Tunisia
Turkey
Turkmenistan
Turks and Caicos Islands
Tuvalu
Uganda
Ukraine
United Arab Emirates
United Kingdom
United States
Universal Personal Telecommunications (UPT)
Uruguay
US Virgin Islands
Uzbekistan
Vanuatu
Venezuela
Vatican City State (Holy See)
Vietnam
Wake Island, USA
Wallis and Futuna
Yemen
Zambia
Zanzibar
Zimbabwe"""

text2 = """7840
93
35818
355
213
1684
376
244
1264
1268
54
374
297
247
61
6721
672
43
994
1242
973
880
1246
1268
375
32
501
229
1441
975
591
5997
387
267
55
246
1284
673
359
226
257
855
237
1
238
5993
1345
236
235
64
56
86
6189164
6189162
57
269
242
243
682
506
225
385
53
5399
5999
357
420
45
246
253
1767
1809
670
56
593
20
503
8812
88213
240
291
372
251
500
298
679
358
33
596
594
689
241
220
995
49
233
350
881
8818
30
299
1473
590
1671
502
441481
224
245
592
509
504
852
36
354
8810
91
62
870
800
882
979
808
98
964
353
8816
441624
972
39
1876
4779
81
441534
962
76
254
686
850
82
38139
965
996
856
371
961
266
231
218
423
370
352
853
389
261
265
60
960
223
356
692
596
222
230
262269
52
691
1808
373
377
976
382
1664
212
258
95
37447
264
674
977
31
1869
687
64
505
227
234
683
6723
90392
4428
1670
47
968
92
680
970
507
675
595
51
63
64
48
351
1787
974
262
40
7
250
5994
590
290
1869
1758
590
508
1784
685
378
239
966
221
381
248
232
65
5993
1721
421
386
677
252
27
500
99534
211
34
94
249
597
4779
268
46
41
963
886
992
255
888
66
88216
228
690
676
3732
1868
2908
216
90
993
1649
688
256
380
971
44
1
878
598
1340
998
678
58
3906698
84
1808
681
967
260
25524
263"""

import pprint

dict_countries = {}
dict_phones = {}

for key1 in text1.split('\n'):
    dict_countries[key1] = None

for key2, value in zip(text1.split('\n'), text2.split('\n')):
    dict_phones[key2] = {'dict_phones'}#value #, int(value)

# print(dict_phones)
# pprint.pprint(dict_phones)
# print(dict_countries)

keys = text1.split('\n')
merged_dict = {}

for key3 in keys:
    merged_dict[key3] = dict_countries[key1]
    merged_dict[key3] = dict_phones.setdefault(key3, dict_phones[key2])

pprint.pprint(merged_dict)



# nested = dict(merged_dict={'merged_dict': (int(value), str(value))})
#for i in merged_dict:
#    merged_dict[i] = {'merged_dict[i]': {'merged_dict': (int(value), str(value))}


#print(merged_dict)
#print(nested)"""