
# -*- coding: UTF-8 -*-

import d3profile as d3p
import d3hero as d3h
import d3item as d3item







test_bnet_ids = ['a3366128-3406', 'Abort-3943', 'Abstractor-1397', 'adol-3295',
            'Aegis-1143', 'ahiru-1133', 'Alavar-1624', 'Albert-3932',
            'Alekhine-1542', 'AlexGG-3214', 'Alexkhan-1443', 'ALEXLIN-1387',
            'AlexTheGreat-1216', 'Alff-6211', 'Alfo-6984', 'alfredo-1203',
            'aliafo-6319', 'Allisdust-1895', 'AlmostherE-1148', 'AmauriLP-1441',
            'AML-1386', 'Amswede-1354', 'andrew-1428', 'AndrewFuNg-3177']

bnet_ids = ['a3366128-3406', 'Abort-3943', 'Abstractor-1397', 'adol-3295',
            'Aegis-1143', 'ahiru-1133', 'Alavar-1624', 'Albert-3932',
            'Alekhine-1542', 'AlexGG-3214', 'Alexkhan-1443', 'ALEXLIN-1387',
            'AlexTheGreat-1216', 'Alff-6211', 'Alfo-6984', 'alfredo-1203',
            'aliafo-6319', 'Allisdust-1895', 'AlmostherE-1148', 'AmauriLP-1441',
            'AML-1386', 'Amswede-1354', 'andrew-1428', 'AndrewFuNg-3177',
            'Andy-1668', 'Andy-2854', 'Anek-1797', 'AngelofLight-1383',
            'angry-1225', 'AnkleBiter-1483', 'Antoine-1405', 'ANTON-1687',
            'Anubis-11918', 'Anyntycoiko-1428', 'aperfecte-1441',
            'Archael-1701', 'Archaster-1809', 'aresling-1927', 'Ariel-2620',
            'aroc-1156', 'Arscot-1757', 'Artan-1653', 'arthur-11490',
            'Ashura-6906', 'Asukasan-1349', 'Atlas-1744', 'atomisk-1349',
            'attitude-1961', 'AWD-1159', 'Axis-1247', 'AyeReezy-1113',
            'Azarrel-1750', 'Aznable-3894', 'azreus888-6477', 'Azurean-1727',
            'Backinator-1225', 'Baconinja-1209', 'badA55mF-1662', 'Bagman-6132',
            'BainWulfgar-1961', 'Banemule-1411', 'Barbabrian-6219',
            'Barbarian-1236', 'BARBERJUN88-6722', 'baromir-2282',
            'BaronofTang-6820', 'BATMAN007-1757', 'BattleCactus-1414',
            'Baulz-1327', 'Bawzdeep-1468', 'bear0127-3926', 'Beeotch-1631',
            'Ben-12390', 'Benno-1336', 'BEOWULF-1309', 'bhzBloody-1355',
            'bigarn77-1246', 'BigKriz-1187', 'bigsizzler-1505', 'bigtod-1720',
            'BillAposenta-1224', 'Billbo-1561', 'Bin-3685', 'Binoy-1842',
            'Birdman-1714', 'BiuMV167-1922', 'blackfencer-1248',
            'BladeRnR-1485', 'Bladeweaver-1948', 'blinddot-1294', 'Blink-6811',
            'bloodfucker-1647', 'BloodyHobo-1396', 'Bloodyzbub-1683',
            'bluemagi-1827', 'BLURAY-1226', 'BmanCV60-1706', 'Bobojoe-1158',
            'Bocicsoki-2898', 'Boi-1666', 'bokujuu-1905', 'Bonbon-3112',
            'bonewall-1922', 'Bort-1724', 'Boston-1212', 'branden-1612',
            'Braver-1113', 'Bromby-1673', 'BRozzi-1712', 'bryan828-1126',
            'Btown32-1376', 'BuffGuy-1410', 'BulKathos-2412', 'Bulvai-1755',
            'bum8384-1684', 'Burgina-1874', 'bVlgari-1264', 'BVsHeart-6883',
            'C3aow-1896', 'Cake-1285', 'calling-1884', 'cann-1398',
            'Caraman-1972', 'castle-1164', 'Catdaddy-1929', 'cathy-1137',
            'Cazano-1725', 'cÇharleSs-1435', 'ccmming-1141', 'cedamorim-1886',
            'Cédérick-2695', 'Cha0styLe-1673', 'ChadDaddy-1507',
            'Chaggyman-1891', 'chaming-1341', 'chaos-3612', 'chefdaddy1-1330',
            'ChenChen-1511', 'Cheng-1431', 'ChenYanHui-3419', 'chillchong-1499',
            'chiou-1768', 'chisquarelin-3392', 'Cholesterol-6489',
            'chrisca07-1416', 'Chrisj-6354', 'ChumKiu-1627', 'chungNoka-3685',
            'clayton-1746', 'clement812-1568', 'Cloud-3275', 'Cloud9-1256',
            'cmorrow25-1424', 'CobraChood-1341', 'coiote-1778', 'Colossus-1652',
            'comawhite-1655', 'Combo-1789', 'Conan-1354', 'Condorhero-1232',
            'Conquistador-6134', 'Conrado-1676', 'Convoy-1879',
            'cookiefart-1829', 'Coot-1478', 'Copper-1334', 'Crassus-3396',
            'CrazyEyes-1336', 'CRAZYMAD-1446', 'CrazySushi-1584',
            'crepyjoker-1546', 'Cricys-1408', 'CRISE622-1573',
            'crispnd007-1513', 'CROW-1625', 'Cruxiaer-6604', 'Cyndir-1585',
            'DaFanSu-3848', 'DAKKON-6113', 'DakkonBlack-1895',
            'dangerZONE-1913', 'daNky-1509', 'danny-1632', 'Dano-1686',
            'Dareiznogod-1427', 'Darhk-1910', 'DarkFury-1276', 'DarkSol-1334',
            'DarthVader-3109', 'DatTofu-1562', 'DavidLee-1576', 'DAY-3791',
            'DcTucsonan-1519', 'Deadline-1519', 'Deag-1610', 'Deanman-1573',
            'Death-12917', 'DeathAdvocat-6433', 'DEATHHEAD-1380',
            'DeathLight-1975', 'DebrisBall-1767', 'decorebelo-1958',
            'degamer106-1817', 'Dekaese-1645', 'Denilson-1329', 'dennisc-3274',
            'Derelict-1177', 'DestinyG-1718', 'Deveats-1414', 'DevilDog-1464',
            'DevilX-3437', 'Dexter-3312', 'dharkharma-1300', 'Diabolicman-1965',
            'dicky1020-3824', 'Diego-1316', 'dieselpower-1893', 'digclear-1631',
            'Digglet-1275', 'Dingo-1175', 'Dinte-1301', 'Diogo-1668',
            'diogopm-1397', 'Diore-1452', 'Dipsyman-1525', 'DiscoBot-1548',
            'Djfawa-1977', 'dkimbo-1127', 'DLForce19-1666', 'DMH19-1613',
            'dnordh-2962', 'Dodjy-1634', 'Domo-6908', 'donnybrascox-1812',
            'Doom-1332', 'DoomLenzer-6406', 'Doomlord-1332', 'dproG-1579',
            'Dragonborn-1847', 'DragonRush-3398', 'Drailgonis-1723',
            'DrakWrath-1732', 'DreamKiller-1773', 'Drewcati-1570',
            'drhouse4ever-1922', 'DrMachado-1434', 'Drogba011-3480', 'dsx-1834',
            'Duanger-1994', 'DudeBro-1164', 'Dutra-1471', 'Eak-6603',
            'EatLEAD-1694', 'Edo-1395', 'edsilva-1824', 'eepz-1739',
            'ehong-1314', 'Elitist-1818', 'ElliotM-1581', 'Elune-1289',
            'Emoru-1138', 'EmperorWurm-6530', 'Endo-3313', 'enduro-1604',
            'EnTaroZeus-1835', 'ENZO-1176', 'eRiCcMh-6470', 'Erplayer-1641',
            'Eryn-1660', 'Esquire-1584', 'Eternity-1377', 'Eutanasya-1856',
            'Evgenyka-1494', 'EvilDee-1209', 'evo0901-3799', 'Excallius-1470',
            'eyesea-1683', 'Ezequiel-1490', 'F1MBULW1NT3R-6669', 'Fa11en-1909',
            'Fabio1971-1538', 'Fade9O7-1136', 'Failure-1590',
            'FalconPawnch-1217', 'Fallundead-1819', 'fatpanda-1843',
            'felix-6109', 'Ferociti-1176', 'Feroxius-1444', 'FILHOSANTO-1724',
            'fire0488-3866', 'FireLord-2464', 'FirstToDie-1288', 'fisher-3161',
            'Fivehole57-1623', 'Flintheart-1953', 'Fooba-1908', 'Frank-31699',
            'FrankDux-1788', 'Fre3doM-6235', 'FredK-6562', 'Free-1746',
            'FreeRider-6187', 'Freestyle-1806', 'Friskar-1961', 'Frizank-1729',
            'Frustrashun-1202', 'FSUskygod-1514', 'fukuoverlord-1248',
            'Fury-1888', 'Fusionary-6928', 'g3ntooman-1708', 'Gabriel-6681',
            'Galinhomt-1365', 'GameOverMan-1272', 'Gandalv-1978', 'Gang-1979',
            'Gantz-1194', 'gasherbaum-1627', 'gby-6331', 'GEDROKS-2924',
            'Geeon-6665', 'GeneticLife-1284', 'Genevan-6749',
            'GenghisKhan-1476', 'GEORW-6388', 'Giff-1640', 'Gino-3626',
            'GiuRusso-1115', 'Glumurphonel-1469', 'Godamnyou-6227',
            'Golazo-6132', 'goldenone23-1519', 'Goodlife-1247', 'GoPies-6811',
            'Gosling-1993', 'Granger-1895', 'Grego-1515', 'Gregory-1477',
            'GuiltyAllen-1350', 'hackerwacker-1534', 'Hacor-3128', 'Hadd-1524',
            'Hades-11762', 'HADES-1884', 'HADOUKEN-6193', 'HALIS-1582',
            'Hamboigahs-1176', 'HAMMER-1713', 'haozhou-2617', 'Hardcore-1739',
            'Harlequinn-1861', 'Harrier-6751', 'HawkEye-11718', 'Haybaler-1911',
            'hecco-1320', 'Helen-3729', 'Hellscargo-1644', 'Hellven-1238',
            'henry-1793', 'herbert-1633', 'hermitlord-1103', 'HeyGorgeous-1322',
            'hgchae-1707', 'hhishane-1915', 'Hidemine-1155', 'HielUFF-1251',
            'hiroko-1349', 'hmj-1613', 'hmvh1-1774', 'HodBanYok-1607',
            'honesty-1874', 'hoppel-1712', 'Horax-1774', 'horror-6953',
            'hpcson-1270', 'Hulk-1364', 'HunterKiller-1780', 'Hurin-1173',
            'Hurrdurrdurr-1212', 'Hypnos-3820', 'hzybest-1140', 'ICYEYES-1257',
            'ilhsy-3784', 'Imanoob-1504', 'Immortal88-1515', 'insist4575-3647',
            'IntoTheRain-3172', 'Invidious-1266', 'iPudge-1110', 'isnis-1793',
            'IStrikeDeep-1463', 'iTzClutch-1579', 'Iva-1862', 'Ivern-1298',
            'IWinToLose-1350', 'Jababa-1610', 'Jablo-1713', 'Jackal-1688',
            'JACKAL-6246', 'jackbauer2-1775', 'Jacob-1833', 'jaffizzle-1998',
            'Jakelinus-1877', 'jaowins-1655', 'JaqenHghar-1365', 'jay-1401',
            'JBT-1750', 'Jecklehead-1938', 'Jedak-1271', 'Jefe78-1744',
            'jeji-1957', 'Jerangkung-1266', 'Jerryz-1963', 'Jet-3446',
            'JetChiu-3433', 'JimMoriarty-1641', 'JIRX-1844', 'JJay-1270',
            'Jocose-1332', 'JoeyFerg3-1944', 'JoeZhoutaiba-3164', 'john-1752',
            'Johnny-11609', 'JOHNNY-2362', 'Joho-1180', 'jon-3926',
            'JooLs-1167', 'josephfrye-1206', 'JP20471120JP-1905',
            'jrelthewise-1102', 'JRNA-1626', 'Juggernaut-1164', 'juiceme-1768',
            'JUNZETO-2903', 'K489441139-3925', 'Kagato-1608', 'Kagnarium2-1724',
            'KaioNS-1873', 'kalel-1729', 'Kami-1850', 'Kandaya-1860',
            'KaneHBK-3433', 'Karoline-3247', 'karts-6100', 'kasra123-1993',
            'kaven-1497', 'kenina-1347', 'KentLau-1492', 'KEVIN-32987',
            'kevin-6808', 'kevinhsa-3978', 'Keyo-1431', 'Kheribus-1217',
            'kidd-3744', 'Killer-13668', 'killerclowns-1503', 'Killzone-1580',
            'Kimpoy-6718', 'KingBenjamin-1485', 'kingdo-1687',
            'kingofdiablo-1129', 'KittenQiao-1186', 'KITTO-3121',
            'knivess1983-6961', 'KobayMVP-1146', 'koeda-1526', 'Koguchi-6246',
            'KONA-3892', 'Kongol-1397', 'korgull-1817', 'KORVO11-1303',
            'Kratos-1977', 'krispy-1159', 'Krystal-1953', 'KungFu321-1564',
            'kurenai-3895', 'Kuzoh-1750', 'Kvo-1990', 'LaoNa-3974', 'lbmn-1241',
            'LeandroKP-1856', 'Legion-1524', 'Lekas-3658', 'Leonids-3776',
            'Leozinho187-1587', 'lexus-3432', 'Liakos-1816', 'licorice-1976',
            'Liev-1647', 'lifeisgood-1610', 'lights168-1468', 'LikeABoss-1843',
            'limbs-6512', 'Link-3961', 'Lip-1316', 'Llama-1217', 'loafer-6972',
            'LordDarkness-1446', 'Lordmace-1892', 'lordofhatred-1729',
            'Lotus-6267', 'Louis-1781', 'louisly-3762', 'lovage-1735',
            'lsf-6754', 'lucanlacy-1333', 'Lucas-1962', 'Luciocandido-1285',
            'luciole-1645', 'Lucky-3372', 'luckyhand-1334', 'luffy-3533',
            'Lulão-1792', 'machinegun-1433', 'MaCJohnN-1147', 'macka-1308',
            'Magnus-1322', 'maiconsono-1625', 'Mango-1846', 'Manzatto-1736',
            'mapple-1111', 'Martian-1868', 'Massacre-1374', 'MataraelV-1342',
            'MATENIA-1314', 'Matrix-1283', 'MauroArm-1501', 'MaximusG-1463',
            'May-3108', 'May-6309', 'MeatCrave-1159', 'Menelaus-1207',
            'MerlynYvue-1807', 'mezner-1216', 'microcon-1511', 'Midas0626-3635',
            'Midgul-1856', 'MidNight-6157', 'MightyJack-1975', 'MightyJoe-3911',
            'Mike-6915', 'Mimi-3485', 'mine2355-1161', 'mist-6617',
            'Mister2-1870', 'MisterPibb-1226', 'mixao-6977', 'MJ23-1527',
            'MobiniusIII-1226', 'molandan-3495', 'Momotsai-3872',
            'MonkeyKing-1765', 'Møønstrinho-1989', 'morita-1563',
            'Mortalz-1156', 'Mortay-1363', 'Morthrus-1777', 'Mosh22-1104',
            'mosi-3560', 'Mroil-3535', 'MRQuickiE-1603', 'MrsBBQ-1332',
            'Muffin-1109', 'MUNDZ-1975', 'mungil-2804', 'Murpheus-1542',
            'Murphsbaby-1494', 'Murry-1189', 'Mustafa-1768', 'mvhrad-1345',
            'MyCC-1934', 'n0ne-1788', 'Naffy-1951', 'nainiu-1495', 'Nalor-1466',
            'Nana-1500', 'Nano-1441', 'nbjj-3210', 'Necroanax-1606',
            'Necromorph-1411', 'Nephrost-1428', 'Nerbutitat-6609',
            'Nevermore-1556', 'NeverMoreWc-6842', 'nick323-1628',
            'nightmarex17-1972', 'Nightside-1342', 'Nikkodu-1985', 'ninZU-1391',
            'Nitestorm-1169', 'Nocio-1646', 'noidea-3174', 'NOIL0299-3973',
            'NorthEurope-3716', 'Nostra-1695', 'novacola-1521', 'null-1344',
            'Nuyir-1798', 'o0ojacko0o-3257', 'Oakover-6193', 'OBAMF-1502',
            'Odin-1119', 'Odin-6859', 'OEC-3719', 'ogstaxx-1629',
            'Okakkox-1745', 'OmegaNova-1682', 'OmegaXtc-1930', 'OmiG-1703',
            'Oninowareme-1123', 'onohui-3842', 'Orana-1946', 'OrkEn-1942',
            'OrmusTR-1525', 'Oroan-6285', 'Osíris-1911', 'Otávio-1904',
            'OzADL-1666', 'Pain-1411', 'Pan-1756', 'pan-3357',
            'Pandemic060-1225', 'pantha-1729', 'Paraiba-1348', 'Parallax-1494',
            'Parker-3834', 'parnassus-6316', 'pat-6787', 'PatrickBear-1314',
            'PauliN-1639', 'Pegasus-6139', 'pensfan080-1647', 'Petchowell-1738',
            'PeterPao-1617', 'Phatty-1821', 'PHIL0857-3234', 'phong3795-1556',
            'Pianoguy-6437', 'Pintionelao-1711', 'pionas-1188', 'PIrKo-1271',
            'PisDragon-2212', 'Player3Ready-1903', 'pnissenvy-1388',
            'Polemos-1578', 'PONG-1224', 'pooh30688-3382', 'pookie-1928',
            'PoorYorick-1223', 'Popebenadict-1560', 'popinno2-3331',
            'PPSK-3727', 'Preston-1522', 'Primal-1696', 'primate-1883',
            'ProAnubis-3766', 'ProAznPain-1428', 'Procox-1629',
            'PUREdisdain-1880', 'Purely-1223', 'Pwn-6966', 'qiangge-1724',
            'QtriNitY-1647', 'Quidam1991-2224', 'r3s-6198', 'racerandom-1489',
            'Rafa-1668', 'Rafael-11475', 'RAFSIMONS-1765', 'Ragonar-1177',
            'Rai-1703', 'raichu-1793', 'Rainsnow-6685', 'Rakescar-1447',
            'Rakuria-1793', 'Rampage-1666', 'Rara-3233', 'Raxephon-1171',
            'RaZieL-1296', 'rcezarino102-1126', 'ReallyAsian-6943',
            'rebort-3353', 'redmond-1275', 'RedRamses-1396', 'Rehook-1457',
            'Relentless-2991', 'Relith-1672', 'repezza-1651', 'revhellyoN-1779',
            'rexleon2002-3866', 'Ricky-1784', 'Rigboy-1469', 'Rikku-1529',
            'rilla-1651', 'Riming-3723', 'Risk-1184', 'RJG393-1598', 'RMB-1635',
            'Rocketraid-1209', 'RockHuang-3297', 'rockrobster-1715',
            'Roffloss-1578', 'ROG3RIOL3MAO-1604', 'Rognar-1625', 'Roland-1780',
            'ROMA-1333', 'ronald527-1724', 'RonenRW-1179', 'Ronzoni-1552',
            'rophocale-3964', 'Routliti-1839', 'ryokkk-1605', 'Sabeatiany-1995',
            'sail-3669', 'Samir-1547', 'samszeto2012-3371', 'Santq-1161',
            'saranglinux-1232', 'Saryn-1281', 'Sasquatch-1309',
            'ScarletRider-1486', 'Schocks-1664', 'schumi0227-3366',
            'schwegs-1823', 'Scot-1766', 'ScreaminEgl-1846', 'Scylla-1525',
            'sebendebi23-6641', 'Sectorn9ne-1123', 'seifador-1270',
            'Seige9-1162', 'seiger-1577', 'Sentri-1346', 'Seph-1733',
            'Sergio-1288', 'SHADOW-11333', 'Shadow-11506', 'ShadowDragon-6736',
            'shaliu2589-1650', 'Shanopla-1298', 'Sharphit-6382',
            'Shatterbrain-1969', 'Shawn-1974', 'Sheogorath-1184',
            'shhhpark-1750', 'ShiHong-2368', 'SHIN-3844', 'Shiro-1757',
            'Siang-3116', 'SideShowBob-1594', 'Sieg-1680', 'Siglud-1213',
            'SilverArrow-6931', 'Silverback-1975', 'Silvernext-1171',
            'sin722-6558', 'sinnyd-1497', 'sirius-6820', 'sirmatthew-1591',
            'Sirness-1469', 'Sistemabruto-1322', 'siubo-3405', 'sk7-1866',
            'SkyHai-3883', 'Skylin-1876', 'Skywhoppers-1212', 'Sl0wne-6218',
            'Slayer-1182', 'SlayerJ873-1750', 'Slot-1652', 'SlowDeath-1874',
            'Smeegle925-1580', 'Smoknum-1927', 'smugma-1257',
            'SnuntCiffer-1891', 'SOJxxDooM-6172', 'Som-1272', 'Sombrio-1866',
            'Sopelsa-1572', 'SOURHAZ3-1595', 'Spaceship-6925', 'SpinDrJr-1265',
            'SpunkBC-1822', 'SSF-3765', 'SsTiNgEr77-1704', 'Staeks-1838',
            'Stakahou-1132', 'Stanley-3231', 'stat-6706', 'STEAMER-1397',
            'Stefan-1219', 'Sterling326-1568', 'Stormchylde-6518',
            'Stormrider-1418', 'Strike-1642', 'striker-6426','strummer-1576',
            'suicideking-1500', 'Sukhoi27-1445', 'SuMi-1208', 'Sunflarez-1879',
            'Sunflower-3560', 'Sunny-3269', 'SunShine-6947', 'Sunyixiong-3756',
            'superstorm-3403', 'surly-1640', 'Surmight-1552', 'sven-1745',
            'swapto-1469', 'syck-1731', 'tab-1280', 'Tachi-6907',
            'taconinja-1736', 'TAG-1261', 'Takkonen-1756', 'Tao-1163',
            'Tatiana-1326', 'TBK-1280', 'tdwangwy-3195', 'TedBroiler-1404',
            'TeeBag-1222', 'terryhe-1641', 'Thanthea-1459', 'theOmega-1647',
            'TheOne-6746', 'Theos-1235', 'ThomasDLS-1901', 'Thorgrimn-1903',
            'THRAEX-1767', 'TIAN-3543', 'tien-1151', 'TigerWooody-1755',
            'Timngxd0001-6629', 'Tinman-1822', 'titanlace-1489',
            'TitanNova-1333', 'Tomasi-1288', 'TON-1788', 'tonipoulos-1244',
            'tonysera-1772', 'TOP-3805', 'Torad-1110', 'Totalo-1419',
            'Toxon-1282', 'Traino-1665', 'Trevor-1833', 'Trex-1136',
            'treZealot-1610', 'Trogdor-1595', 'Tukangrusuh-6984',
            'Twister-6844', 'twitcher-1533', 'Twoding-1606', 'Tzeentch-1557',
            'Ubiquity-6737', 'UcoMixx-1601', 'UDIN-3863', 'UltraJerky-1110',
            'Unforgiven-1154', 'Unrest-1617', 'Vaatu-1358', 'VALVE-3945',
            'Vastrolord-1229', 'Vazhr-1362', 'Vdizzle-1122', 'Vegaskid-1261',
            'Vegettoex-1793', 'VENOM7-2430', 'Verdant-1998', 'VERSACE-3694',
            'Vicious-3614', 'Vieruodis-1735', 'Viking-6400', 'Viper-1676',
            'Visions-1612', 'Vivivanus-1426', 'Volgon-1198', 'wangzai-6907',
            'WAR-1318', 'WAR-1658', 'Warge-1321', 'WarTraveller-3258',
            'Wasp-1408', 'WATT60-6297', 'wayne-1472', 'wbb-3837', 'wchens-6331',
            'wedo-1957', 'wewaghost-1890', 'WHAT-3281', 'Wheelson-6151',
            'whitechapel-1493', 'WildFox-3259', 'WildSloth-1443',
            'WILLIAMWU-3409', 'windollars-3565', 'WolfieQiao-1606',
            'Wolfskill-1645', 'wolfwar-1525', 'Wolverine-1998', 'WorkeD-2619',
            'Wrath-1156', 'WRATHFORCE-1200', 'WRECKER-1335', 'WRT23-1610',
            'wuwuto-1501', 'WYY-1476', 'XCLOUD-1544', 'xDoomSayerx-1177',
            'xELDIABLOx-1851', 'Xenoblade-6770', 'xGeN-1463', 'XIAMI-3353',
            'Xiao-1755', 'xiaomaifen-1712', 'xlandk1200s-1602', 'xufuk-3959',
            'xVitOx-1802', 'Xzeeviera-1917', 'Yan-1866', 'yescbok-1336',
            'Yokies-6303', 'Yorieus-6161', 'Yougood-1251', 'YUKI-1860',
            'Yundesa-1582', 'yuzhijun000-1628', 'Zabrax-6478',
            'Zaccaro1211-1572', 'Zammor-1239', 'ZCX-1332', 'Zergz-1774',
            'Zero187-1783', 'ZeroLittle-3776', 'zerz-1756', 'zMaximum-6658',
            'zul-1251', 'Zyhm-1987']

slots = ['head', 'torso', 'feet', 'hands', 'shoulders', 'legs', 'bracers',
          'mainHand', 'offHand', 'waist', 'rightFinger', 'leftFinger', 'neck']

level2_parents = ["armor", "attacksPerSecond", "attributes", "attributesRaw",
                  "dps", "dyeColor", "maxDamage", "minDamage", "recipe",
                  "set", "transmogItem", "type"]

test_item_ids = [
            "CuoBCOqz6KMCEgcIBBWJeX1OHXMjBlAd3DtTaB2EA6HWHX52VaEdZz7s5B0EBj61MIsaONYCQABIAVASWARg1gJqKwoMCAAQ0eCfgIGAgKArEhsIlYSaqQoSBwgEFdddtnowixI4AEABWASQAQBqKwoMCAAQ0uCfgIGAgKArEhsIyeri3AISBwgEFdddtnowixI4AEABWASQAQBqKwoMCAAQqrSoi4GAgOA2EhsI5avipQoSBwgEFdddtnowixI4AEABWASQAQCAAUaNAewdGWClAWc-7OStAfOVZfq1ATEiGWC4Ab-H5Z4BwAFJGJLm6-cJUARYAKABwa2bsAGgAZLm6-cJ",
            "CuoBCP7p07EMEgcIBBWZuGwPHbRPiW4dt1tUTR2PKT1QHd6C_OUdcyMGUB3q1ZI_MIsaOIoDQABIAVASWARgigNqKwoMCAAQzZau1oSAgKAIEhsInoDUrgQSBwgEFWv1i18wixI4AEABWASQAQBqKwoMCAAQ0pau1oSAgKAIEhsI_5WOmAcSBwgEFWv1i18wixI4AEABWASQAQBqKwoMCAAQ3Jau1oSAgKAIEhsIgevG1ggSBwgEFWv1i18wixI4AEABWASQAQCAAUaNAagZGWClAY8pPVCtAYQDoda1ATEiGWC4AczsrckLwAFoGLLi5fYBUAJYAKAB78j87A6gAa_KjOIOoAGy4uX2AaAB0NbNkwagAaSU86oP",
            "CuoBCPKXisMEEgcIBBXARX4PHdk_1J8drNOZOR1DTkRRHWaxmXAdcyMGUB2pIDa6MIsCOIYDQABIEFASWARghgNqKwoMCAAQ7O6VqoKAgIAnEhsI2teS6AMSBwgEFWv1i18wixI4AEABWASQAQBqKwoMCAAQ8O6VqoKAgIAnEhsI49KTuAoSBwgEFWv1i18wixI4AEABWASQAQBqKwoMCAAQmKuajYKAgMAfEhsIq9OarAQSBwgEFWv1i18wixI4AEABWASQAQCAAUaNAe0dGWClAWaxmXCtATAIA7q1ATEiGWC4AamiruQLwAEHGICX8vcBUApYAKAB4ZWA4Q6gAd-11PsFoAGAl_L3AaABnovalAagAfLI_6sP",
            "CuoBCPP1j_wNEgcIBBUdjDgNHT_yCdgdrdOZOR2EA6HWHcsN6RMdcyMGUB0yicdaMIsaOJkCQABIAVASWARgkwNqKwoMCAAQ14XLuIOAgOAjEhsI-_fhuQwSBwgEFSOWrpgwixI4AEABWASQAQBqKwoMCAAQ2IXLuIOAgOAjEhsIq-3rugkSBwgEFSOWrpgwixI4AEABWASQAQBqKwoMCAAQ2YXLuIOAgOAjEhsIwabVsAgSBwgEFSOWrpgwixI4AEABWASQAQCAAUaNAXpnbwKlAYQDodatAR5SM2G1AQFwbwK4AZmCnd8BwAEEGLqwxNMBUABYAKABqdKLzAigAbHSzcQBoAHFrZuwAaABurDE0wGgAfip-r4CoAHszK27Dg",
            "CuoBCP_N2bYOEgcIBBWZuGwPHbRPiW4dZTrU4B2PKT1QHYQDodYdcyMGUB3q1ZI_MIsaOKcCQABIA1ASWARgpwJqKwoMCAAQxM3c0oWAgOAyEhsI_4vc_wISBwgEFWv1i18wixI4AEABWASQAQBqKwoMCAAQyM3c0oWAgOAyEhsI75fioA8SBwgEFWv1i18wixI4AEABWASQAQBqKwoMCAAQ2c3c0oWAgOAyEhsIuv3O0A8SBwgEFWv1i18wixI4AEABWASQAQCAAUaNASoiGWClAY8pPVCtAd6C_OW1ATEiGWC4AYeXnq0EwAEKGLLi5fYBUAJYAKABr8qM4g6gAa3q4PwFoAGy4uX2AaAB0NbNkwagAaSU86oP",
            "CuoBCPz63egCEgcIBBWZuGwPHSlMJiMdX9EZGB31PkQUHYQDodYdcyMGUB3q1ZI_MIsaOJ0CQABIAlASWARgoAJqKwoMCAAQ-OKvsYeAgMAZEhsIsqe13goSBwgEFWv1i18wixI4AEABWASQAQBqKwoMCAAQ-eKvsYeAgMAZEhsIsfvpjgwSBwgEFWv1i18wixI4AEABWASQAQBqKwoMCAAQ-uKvsYeAgMAZEhsIv9_AnQ4SBwgEFWv1i18wixI4AEABWASQAQCAAUaNAagZGWClAfU-RBStATAIA7q1ATEiGWC4Abve0YcBwAEpGLLi5fYBUAJYAKAB78j87A6gAa_KjOIOoAGy4uX2AaAB0NbNkwagAaSU86oP",
            "CusBCKjXu80OEgcIBBUo7XxOHbRPiW4dBAY-tR2EA6HWHY8pPVAdcyMGUB3q1ZI_MIsaOO8BQABIAlASWARglAJqKwoMCAAQwJWYh4SAgIA4EhsIxcHJlwUSBwgEFWv1i18wixI4AEABWASQAQBqKwoMCAAQw5WYh4SAgIA4EhsIr97TtwUSBwgEFWv1i18wixI4AEABWASQAQBqKwoMCAAQyJWYh4SAgIA4EhsIj4bB-ggSBwgEFWv1i18wixI4AEABWASQAQCAAUaNAagZGWClAY8pPVCtAbNR5RK1ATEiGWC4AauAl9MOwAGSARjQtOfnCVACWACgAcOtm7ABoAG2-PW-AqABsrmypgOgAajyv_EGoAHQtOfnCaABrv6xuw4",
            "CusBCMiB1qkEEgcIBBUk624PHakgNrodcyMGUB0VCILVHUNORFEdxK05XB2s05k5MIsCOJADQABIAVASWARglANqKwoMCAAQq4mj6ICAgMA2EhsI5NrvzwsSBwgEFWv1i18wiwI4AEABWASQAQBqKwoMCAAQromj6ICAgMA2EhsIieSyqgwSBwgEFWv1i18wiwI4AEABWASQAQBqKwoMCAAQtYmj6ICAgMA2EhsIgNXD_w0SBwgEFWv1i18wiwI4AEABWASQAQCAAUaNAeP9ozSlARUIgtWtAaM-oLe1ATEiGWC4AYW9yJcEwAGGARjIrPf2AVACWAKgAdn-6uwOoAGXoM_8BaAByKz39gGgAeag35MGoAG63oSrDw"
]

item_ids = [

]

name_list = []
attribs = {}
item_ids = []

def test_slot_items():
  count = { 'head':{}, 'torso':{}, 'feet':{}, 'hands':{}, 'shoulders':{},
            'legs':{}, 'bracers':{},'mainHand':{}, 'offHand':{}, 'waist':{},
            'rightFinger':{}, 'leftFinger':{}, 'neck':{}
          }
  total_items = 0
  total_barbs = 0

  for bnet_id in bnet_ids:
    profile = d3p.Profile(bnet_id)
    for hero in profile.heroes:
      if hero.pc_class == 'barbarian' and hero.level == 70:
        '''
        try:
          print "%s %s %s" % (bnet_id, hero.name, hero.id)
        except(UnicodeDecodeError):
          print "%s BADNAME %s" % (bnet_id, hero.id)
        '''

        # Now we have a level 70 barb...
        total_barbs = total_barbs + 1
        print "----- %s --------" % hero.name
        hero_data = d3h.get_hero_info(bnet_id, hero.id)
        items = hero_data['items']
        for item in items:
          for slot in slots:
            if items.has_key(slot):
              item_name = hero_data['items'][slot]['name']
              total_items = total_items + 1
              if count[slot].has_key(item_name):
                count[slot][item_name] = count[slot][item_name] + 1
                #print "%s is now: %s" % (item_name, count[slot][item_name])
              else:
                count[slot].update({item_name: 1})
                #print "Added new key: %s" % item_name
            else:
              item_name = "NONE"
              total_items = total_items + 1
              if count[slot].has_key('NONE'):
                count[slot]['NONE'] = count[slot]['NONE'] +1
              else:
                count[slot].update({'NONE':1})

  for slot in slots:
    #print "%s" % slot
    for item in count[slot]:
      print "%s\t%s\t%s" % (slot, item, count[slot][item])
  print "%s total items" % total_items


def test_instance_items():
  attribs = {}

  for bnet_id in test_bnet_ids:
    profile = d3p.Profile(bnet_id)
    for hero in profile.heroes:
      hero_data = d3h.get_hero_info(bnet_id, hero.id)
      items = hero_data["items"]
      for item in items:
        for slot in slots:
          if items.has_key(slot):
            tooltip_params = items[item]["tooltipParams"]
            item_id = tooltip_params.split('/')[1]
            info = d3item.get_item_instance_info(item_id)
            # now get a list of all the keys, add them to list if absent
            for key1 in info:
              typestr = "%s" % type(info[key1])
              typestr = typestr.split('\'')[1]
              keystr = "%s" % ("balhahaksbjaksbasdxb")
              if level_1.has_key(key1):
                # increment the count for that key
                level_1[key1] = level_1[key1] + 1
              else:
                # add the key to the list
                print "Adding level 1 key: <<%s>>" % key1
                print "ItemID: %s" % item_id
                level_1.update({key1: 1})
              # Check to see if this key is itself a dict
              if type(info[key1]) is dict:
                for key2 in info[key1]:
                  if level_2.has_key(key2):
                    level_2[key2] = level_2[key2] + 1
                  else:
                    print "Adding level 2 key: [%s]<<%s>>" % (key1, key2)
                    print "ItemID: %s" % item_id
                    level_2.update({key2:1})
                  if type(info[key1][key2]) is dict:
                    for key3 in info[key1][key2]:
                      if level_3.has_key(key3):
                        level_3[key3] = level_3[key3] + 1
                      else:
                        print "Adding level 3 key: [%s][%s]<<%s>>" % (key1, key2, key3)
                        print "ItemID: %s" % item_id
                        level_3.update({key3:1})
                    print "*****"
                    print "Keys: [%s][%s][%s]" % (key1, key2, key3)
                    print "type(info[key1][key2][key3]): %s" % type(info[key1][key2][key3])

                    print "*****"
                    if type(info[key1][key2][key3]) is dict:
                      for key4 in info[key1][key2][key3]:
                        if level_4.has_key(key4):
                          level_4[key4] = level_4[key4] + 1
                        else:
                          print "Adding level 4 key: [%s][%s][%s]<<%s>>" % (key1, key2, key3, key4)
                          print "ItemID: %s" % item_id
                          level_4.update({key4:1})
                        if type(info[key1][key2][key3][key4]) is dict:
                          for key5 in info[key1][key2][key3][key4]:
                            if level_5.has_key(key5):
                              level_5[key5] = level_5[key5] + 1
                            else:
                              print "Adding level 5 key: [%s][%s][%s][%s]<<%s>>" % (key1, key2, key3, key4, key5)
                              print "ItemID: %s" % item_id
                              level_5.update({key5:1})
                            if type(info[key1][key2][key3][key4][key5]) is dict:
                              print "******** IT GOES DEEPER **************"
          else:
            #print "Key missing: bnet_id:%s, name:%s, item:%s, slot:%s " % (bnet_id, hero.name, item, slot)
            # They are not wearing any gear in that slot
            pass
  print " ______ RESULTS ________"
  print "Level 1:"
  for key1 in level_1:
    print "  %s" % key1
  print "Level 2:"
  for key2 in level_2:
    print "    %s" % key2
  print "Level 3:"
  for key3 in level_3:
    print "      %s" % key3
  print "Level 4:"
  for key4 in level_4:
    print "        %s" % key4
  print "Level 5:"
  for key5 in level_5:
    print "        %s" % key5


def test_get_attribs():
  print "%s\t%s" % ("Key", "Type")
  for bnet_id in test_bnet_ids:
    profile = d3p.Profile(bnet_id)
    for hero in profile.heroes:
      hero_data = d3h.get_hero_info(bnet_id, hero.id)
      items = hero_data["items"]
      for item in items:
        for slot in slots:
          if items.has_key(slot):
            tooltip_params = items[item]["tooltipParams"]
            item_id = tooltip_params.split('/')[1]
            info = d3item.get_item_instance_info(item_id)
            # now get a list of all the keys, add them to list if absent
            #get_level_one_attribs(info)
            for parent in level2_parents:
              if info.has_key(parent):
                get_attribs(info[parent])
  print_results()


def test_get_item_id_list():
  for bnet_id in bnet_ids:
    profile = d3p.Profile(bnet_id)
    for hero in profile.heroes:
      hero_data = d3h.get_hero_info(bnet_id, hero.id)
      items = hero_data["items"]
      for item in items:
        for slot in slots:
          if items.has_key(slot):
            tooltip_params = items[item]["tooltipParams"]
            item_id = tooltip_params.split('/')[1]
            #info = d3item.get_item_instance_info(item_id)
            if item_id in item_ids:
              # We've already added this item
              pass
            else:
              print "Adding %s..." % items[item]["name"]
              item_ids.append(item_id)
  print "Finished."
  print
  print
  print
  print
  print
  item_ids.sort()
  for item in item_ids:
    print "\"%s\", " % item





def get_attribs(info):
  for key in info:
    typestr = "%s" % type(info[key])
    xkey = "%s__%s" % (key, typestr.split('\'')[1])
    if attribs.has_key(xkey):
      attribs[xkey] = attribs[xkey] + 1
    else:
      print "Adding new key: %s" % xkey
      attribs.update({xkey:1})








def print_results():
  print "--------------------------------------------------------------------"
  print  "%s\t%s\t%s" % ("Attribute", "Type", "Occurances")
  for attrib in attribs:
    part = attrib.split('__')
    print "%s\t%s\t%s" % (part[0], part[1], attribs[attrib])








#transmogItem attributesRaw Weapon_On_Hit_Knockback_Proc_Chance

#test_instance_items()
#test_get_attribs()
test_get_item_id_list()
#http://us.battle.net/api/d3/profile/Alff-6211/hero/57311980

#bnet_id = 'gray808-1128'
#char_id = '6470632'
#x = d3p.Profile(bnet_id)
#x.display()
#x = d3h.Hero(bnet_id, char_id)
#x.display()
#test_slot_items()


