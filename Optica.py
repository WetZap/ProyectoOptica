import numpy as np

# Declaracion de las variables

# Variables inicializadas
r_perpe = 0  # Coeficiente de reflexión perpendicular (Complejo)
r_paral = 0 # Coeficiente de reflexión paralelo (Complejo)

r_perpend = {'radio':0,'Angulo':0} # Diccionario para almacenar el valor polar de r_perpe
r_paralle = {'radio':0,'Angulo':0} # Diccionario para almacenar el valor polar de r_paral

n = 1  # Índice de refracción del aire
n_comp = 1.33  # Índice de refracción del metal
coef_transmision = 0  # Coeficiente de transmisión
coef_reflexion = 0  # Coeficiente de reflexión

# Variables de entrada
theta = 0  # Ángulo de incidencia en rad
acimut = 0  # Ángulo de acimut
desfase = 0  # Desfase entre componentes
desfase_inicial = 0  # Desfase inicial


elemento = ''  # Elemento metálico

longitud_onda = 0  # Longitud de onda en nm



opcion = '' # Variable para la opción del menú
opcion1 = ''  # Variable para la opción del submenú 1

lambda_Datos = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700]
# Datos de los metales leídos desde el archivo externo
Au = {'n': [1.699838715, 1.746948702, 1.782941044, 1.804652963, 1.804621334, 1.763712432, 1.713434851, 1.689202065, 1.678059067, 1.672504217, 1.665616091, 1.653911114, 1.63743714, 1.612343317, 1.581523054, 1.538326354, 1.475285274, 1.386263242, 1.252905499, 1.064360219, 0.848474841, 0.661635502, 0.52912664, 0.438041087, 0.372502061, 0.323930966, 0.284960267, 0.254069233, 0.228936734, 0.207122197, 0.188789629, 0.172726107, 0.160071695, 0.14636792, 0.135417727, 0.125499436, 0.117832095, 0.111117685, 0.105744888, 0.101509306, 0.098607898, 0.097790271, 0.098623269, 0.096903666, 0.099463321, 0.098537395, 0.099206649, 0.101706737, 0.101315225, 0.103067755, 0.10422723, 0.105937788, 0.104338656, 0.104534544, 0.107001078, 0.111012574, 0.11076329, 0.112038779, 0.114173034, 0.116004573, 0.116828465, 0.116997234, 0.11945701, 0.120635837, 0.122558964, 0.124002721, 0.123935366, 0.126244253, 0.127974627, 0.129942772, 0.132311724, 0.133907614, 0.135401137, 0.138148809, 0.137937636, 0.139246667, 0.134049061, 0.135717763, 0.140363062, 0.138686104, 0.138418628, 0.139442944, 0.141677831, 0.141308241, 0.140235564, 0.142817756, 0.146729336, 0.152747848, 0.149693183, 0.147906483, 0.149395088, 0.151984867, 0.153423422, 0.153670698, 0.157748208, 0.159662147, 0.165494236, 0.159382324, 0.163849184, 0.166211578, 0.166156462, 0.170115488, 0.169795214, 0.174809869, 0.176209118, 0.179585571, 0.177483381, 0.184295562, 0.186297714, 0.190837556, 0.191102283, 0.194361931, 0.205426553, 0.208361137, 0.206557078, 0.208044, 0.205758558, 0.212405614, 0.216697642, 0.219902453, 0.215398722, 0.21956893, 0.222004156, 0.230589098, 0.235210701, 0.238229889, 0.236761828, 0.235275342, 0.240819258, 0.246290147, 0.243652913, 0.25211538, 0.248830057, 0.264448459, 0.258451056, 0.265882655, 0.278561249, 0.278188678, 0.28090035, 0.290244511, 0.316481841], 'k': [1.973157788, 1.974499878, 1.959795593, 1.931950392, 1.896796816, 1.870684779, 1.887670254, 1.922090949, 1.948381952, 1.966512231, 1.973924254, 1.975227068, 1.970304643, 1.959477219, 1.940313163, 1.910745397, 1.872315849, 1.827683172, 1.782097694, 1.76786953, 1.828280492, 1.964525779, 2.129735899, 2.294990195, 2.451664289, 2.597158307, 2.738978341, 2.871855006, 2.999518633, 3.1213458, 3.241703491, 3.356759495, 3.465634566, 3.577628204, 3.685964997, 3.792327795, 3.896137113, 3.999543366, 4.102704228, 4.205033191, 4.305081128, 4.403812319, 4.499191766, 4.59580138, 4.687205239, 4.78107829, 4.872354868, 4.958865219, 5.051560628, 5.148069829, 5.223682926, 5.313023886, 5.407391844, 5.49244276, 5.577046641, 5.659268839, 5.749197205, 5.830570529, 5.912954886, 5.992867182, 6.081993825, 6.163820922, 6.241575921, 6.328550624, 6.410383818, 6.491793025, 6.573991175, 6.662877577, 6.73805443, 6.819155749, 6.904527963, 6.978318655, 7.061609835, 7.141574413, 7.222466808, 7.302149658, 7.406616579, 7.48280825, 7.556831465, 7.637030433, 7.719336741, 7.79996438, 7.874202982, 7.960965269, 8.050382973, 8.114887363, 8.201495565, 8.26754691, 8.350413645, 8.443510901, 8.515005513, 8.589999965, 8.666864413, 8.744347585, 8.81753279, 8.900982642, 8.987624177, 9.068759713, 9.146521008, 9.226192405, 9.303580384, 9.372456417, 9.445201449, 9.530926424, 9.61244244, 9.687582308, 9.769365402, 9.839357949, 9.916385775, 9.992267959, 10.07156989, 10.14138928, 10.22263176, 10.32150252, 10.37509835, 10.46581494, 10.54050931, 10.6421387, 10.70593097, 10.78046182, 10.85893165, 10.91137986, 11.00587506, 11.08617027, 11.16849695, 11.26307034, 11.31706924, 11.38092063, 11.44281407, 11.53172402, 11.64299647, 11.70912303, 11.78354431, 11.86507198, 11.92798378, 12.01168987, 12.06969744, 12.1875916, 12.2404618, 12.34683125, 12.37053599]}

Ag = {'n': [1.646857286, 1.455629699, 0.920058628, 0.233797996, 0.103893124, 0.07599858, 0.063180003, 0.056279242, 0.050752406, 0.048660415, 0.04572895, 0.04451952, 0.043287376, 0.041992656, 0.041101491, 0.040932342, 0.040956736, 0.040727224, 0.040781493, 0.041249589, 0.041373355, 0.041602686, 0.04237275, 0.042204211, 0.043403286, 0.043817181, 0.044507429, 0.045973387, 0.046819894, 0.046840293, 0.047410447, 0.048985705, 0.049617793, 0.051101901, 0.051646932, 0.05091337, 0.053388535, 0.052475104, 0.054218627, 0.054429231, 0.054860386, 0.056538596, 0.057401233, 0.057733458, 0.059629401, 0.060113603, 0.059047193, 0.063824207, 0.063464686, 0.062217489, 0.063950702, 0.067473356, 0.067636134, 0.068189561, 0.067475107, 0.070135706, 0.070503234, 0.072455233, 0.073943622, 0.074927946, 0.074793597, 0.077646805, 0.07877958, 0.080106493, 0.080039752, 0.081098618, 0.083963945, 0.082327665, 0.08532286, 0.087779237, 0.088025428, 0.090501937, 0.091223005, 0.093163641, 0.090978009, 0.093069308, 0.087488108, 0.090085692, 0.091414911, 0.08952186, 0.087625115, 0.090461037, 0.094528298, 0.092749501, 0.095451077, 0.084359933, 0.095878288, 0.097053265, 0.09493293, 0.098324452, 0.094881447, 0.098216298, 0.098772673, 0.095285601, 0.10376706, 0.100172489, 0.105090726, 0.103513926, 0.106644981, 0.107642765, 0.112669175, 0.115274563, 0.110070769, 0.113725572, 0.110796441, 0.115127087, 0.121692797, 0.120000737, 0.127761842, 0.127391401, 0.129567338, 0.129532614, 0.139425972, 0.136689082, 0.1337676, 0.13753433, 0.136002449, 0.140018996, 0.145683795, 0.143029825, 0.140671824, 0.146851335, 0.145574468, 0.151117653, 0.159989508, 0.156488871, 0.163061728, 0.146280234, 0.160846655, 0.160289135, 0.179696729, 0.177528577, 0.17444857, 0.180256871, 0.185834026, 0.18452807, 0.196882981, 0.175222972, 0.194315172, 0.20553684, 0.198531592], 'k': [0.972336834, 0.572501372, 0.331538655, 0.585441289, 1.052042671, 1.326866905, 1.533000885, 1.708000982, 1.858729622, 1.99546181, 2.122943979, 2.241825593, 2.357153749, 2.465312026, 2.573264334, 2.675756988, 2.776954709, 2.873753418, 2.972181544, 3.066333564, 3.159400537, 3.251112238, 3.342124392, 3.433188197, 3.522198723, 3.610113564, 3.69702325, 3.783928323, 3.870683674, 3.95716995, 4.041936139, 4.126305805, 4.208973975, 4.293088795, 4.376833034, 4.460223332, 4.543110205, 4.623716431, 4.705947265, 4.788419629, 4.869087149, 4.950777375, 5.034212441, 5.113152956, 5.195339803, 5.274430173, 5.356816832, 5.436181889, 5.512987191, 5.598827647, 5.678123783, 5.753307975, 5.836229489, 5.911315405, 5.99554442, 6.076505494, 6.15532052, 6.235643492, 6.313593878, 6.38980549, 6.469203512, 6.547597195, 6.627986589, 6.706073147, 6.784129005, 6.865098469, 6.942265476, 7.024370281, 7.10009014, 7.177095875, 7.254153877, 7.335202151, 7.410959562, 7.488436383, 7.571609934, 7.647526521, 7.738194503, 7.812561387, 7.896414166, 7.969003336, 8.055909518, 8.13167776, 8.207066199, 8.287376091, 8.352970185, 8.445952676, 8.521220138, 8.593219381, 8.675598669, 8.74909525, 8.829439534, 8.901272181, 8.982747689, 9.065378059, 9.1406656, 9.224588583, 9.306720371, 9.373618039, 9.450046198, 9.532921219, 9.60555539, 9.681233817, 9.760538693, 9.83991532, 9.919993743, 9.983749508, 10.07495951, 10.1436877, 10.21157789, 10.30564062, 10.37144097, 10.45450997, 10.54179489, 10.61313733, 10.69616257, 10.76749347, 10.84612819, 10.9453006, 10.99641868, 11.08649889, 11.16108366, 11.21746697, 11.30314965, 11.41064575, 11.45450115, 11.56695676, 11.59683531, 11.70390524, 11.76120196, 11.85857043, 11.89337172, 12.00172973, 12.10786655, 12.14794191, 12.23538043, 12.29243876, 12.38502172, 12.45755606, 12.56772686, 12.63496123, 12.70351978]}

Al = {'n': [0.095390828, 0.095510386, 0.09903925, 0.098692838, 0.100850207, 0.1069563, 0.099715746, 0.108316112, 0.106567769, 0.111513266, 0.110803374, 0.111587326, 0.11365555, 0.115928445, 0.116173424, 0.119771906, 0.124315543, 0.129276519, 0.133002743, 0.139688588, 0.141162655, 0.148765766, 0.150722638, 0.161465056, 0.164610587, 0.172365826, 0.178635303, 0.18587018, 0.188953314, 0.197315218, 0.204991638, 0.210097266, 0.218816718, 0.224454799, 0.237666454, 0.24464928, 0.251892832, 0.259391824, 0.267481852, 0.275201252, 0.28349792, 0.291774119, 0.300125667, 0.308578012, 0.317597538, 0.32692637, 0.335956002, 0.345714203, 0.354901676, 0.364968364, 0.375150842, 0.385211589, 0.396086448, 0.40706511, 0.417647849, 0.429543735, 0.440996226, 0.452837879, 0.464232752, 0.477070026, 0.489220122, 0.501228231, 0.514817248, 0.528042125, 0.53987657, 0.554932886, 0.568005038, 0.582771419, 0.596705366, 0.610784373, 0.625686295, 0.640306464, 0.655709839, 0.672565753, 0.688336416, 0.704045108, 0.720793584, 0.737603948, 0.75446839, 0.772330366, 0.789405353, 0.808351698, 0.829205097, 0.848630853, 0.867376853, 0.887661988, 0.908569739, 0.928308533, 0.948955518, 0.9714896, 0.992465612, 1.016073317, 1.038145667, 1.062059906, 1.088160063, 1.112663572, 1.136328574, 1.165731637, 1.190265203, 1.218505245, 1.246364405, 1.275302761, 1.304382818, 1.333854457, 1.365410391, 1.395892303, 1.426024482, 1.457391234, 1.493230683, 1.5274935, 1.559751729, 1.596346402, 1.631621525, 1.669698976, 1.706780893, 1.745260386, 1.786398844, 1.827772224, 1.872189153, 1.916802427, 1.958355454, 2.005349601, 2.054224115, 2.09984451, 2.144528834, 2.189915668, 2.231500036, 2.275479945, 2.314643646, 2.350258044, 2.373653298, 2.399438967, 2.409296598, 2.414395973, 2.410049326, 2.399462094, 2.375277499, 2.342102357, 2.301774531, 2.257656113, 2.204898553], 'k': [1.283666394, 1.337393822, 1.402928641, 1.46616516, 1.532569987, 1.596539899, 1.657661977, 1.734368006, 1.79116071, 1.853411775, 1.908606137, 1.969936987, 2.028057589, 2.091850713, 2.151998203, 2.213039835, 2.274896559, 2.336773934, 2.395514502, 2.457358928, 2.515219055, 2.573777623, 2.633214255, 2.693431077, 2.750035753, 2.81099804, 2.868973784, 2.923276881, 2.98248275, 3.042340102, 3.100858199, 3.157347124, 3.214790935, 3.267473023, 3.323775766, 3.37932734, 3.436779015, 3.493749292, 3.550147397, 3.607178361, 3.663518946, 3.719829584, 3.776251503, 3.831608068, 3.889198914, 3.945995546, 4.002607455, 4.058265431, 4.114238107, 4.169676475, 4.226433266, 4.281283449, 4.336805792, 4.391435073, 4.447407079, 4.503499508, 4.559109307, 4.613682059, 4.669101846, 4.724044433, 4.778319404, 4.832828338, 4.887948117, 4.943260916, 4.997345967, 5.051331558, 5.105940631, 5.159226931, 5.212874187, 5.265933683, 5.320477736, 5.374848125, 5.428163169, 5.481545831, 5.535955836, 5.58799423, 5.641767754, 5.693773756, 5.746496546, 5.799008035, 5.851936501, 5.905288517, 5.958236408, 6.009090973, 6.060226283, 6.112687118, 6.165184423, 6.215605902, 6.267417058, 6.317103137, 6.368986418, 6.417351867, 6.46681888, 6.517052343, 6.566589093, 6.61475776, 6.66312559, 6.710806975, 6.759417967, 6.807110623, 6.852329839, 6.898361917, 6.942363757, 6.987643931, 7.031951759, 7.071104251, 7.116287362, 7.157652493, 7.197481356, 7.23603734, 7.27391404, 7.311383032, 7.34575992, 7.380372258, 7.414249862, 7.446739811, 7.475374294, 7.502849546, 7.528352557, 7.55216072, 7.571403838, 7.585211073, 7.599462923, 7.605086914, 7.61216158, 7.610567038, 7.603853787, 7.589387919, 7.572223927, 7.547894599, 7.522581337, 7.486541749, 7.449477169, 7.410756231, 7.369351244, 7.325600203, 7.288411569, 7.253098886, 7.225729444, 7.204374444, 7.188085811]}

Cu = {'n': [1.347459987, 1.321473211, 1.301896917, 1.278815346, 1.257856058, 1.229714372, 1.205793784, 1.183134074, 1.16577487, 1.139929606, 1.119339006, 1.097661459, 1.082884327, 1.067185209, 1.056310845, 1.048210496, 1.044058354, 1.040826414, 1.040383818, 1.035622719, 1.0292166, 1.01596237, 0.995463808, 0.957525814, 0.896412084, 0.79745994, 0.649913539, 0.467667795, 0.308052581, 0.206477543, 0.15342929, 0.129738592, 0.116677068, 0.110069919, 0.107194012, 0.104232496, 0.102539467, 0.102449402, 0.101216009, 0.101603953, 0.101236908, 0.101557633, 0.101132194, 0.100848965, 0.100919789, 0.101173963, 0.101837799, 0.101672055, 0.104166566, 0.10154611, 0.105089997, 0.105640925, 0.1047717, 0.108065424, 0.106329275, 0.106803015, 0.10806138, 0.109423947, 0.109226995, 0.110739052, 0.111474071, 0.110565481, 0.114354773, 0.115741932, 0.116243076, 0.11651561, 0.117227546, 0.117612103, 0.1200286, 0.120693135, 0.123314675, 0.123500553, 0.12589253, 0.126656415, 0.125456304, 0.127879983, 0.123044899, 0.124058562, 0.12724857, 0.126108804, 0.127049082, 0.127924195, 0.12687364, 0.129233188, 0.126930498, 0.128135739, 0.131236652, 0.130534766, 0.132958217, 0.134086968, 0.132204904, 0.131954806, 0.134536782, 0.132059034, 0.135380438, 0.140947312, 0.145305612, 0.142654978, 0.145808605, 0.143636497, 0.14357746, 0.14815507, 0.146774504, 0.153662011, 0.14795299, 0.156618782, 0.153286699, 0.158020584, 0.159435601, 0.164929309, 0.160903598, 0.165878545, 0.170083525, 0.170430805, 0.177719488, 0.176808354, 0.174975159, 0.184898936, 0.189874398, 0.180372997, 0.182478591, 0.18486728, 0.190872505, 0.190985335, 0.1989454, 0.194332409, 0.198165888, 0.192594699, 0.207420155, 0.204793341, 0.209186703, 0.213365941, 0.217596043, 0.226803672, 0.225634749, 0.219982349, 0.238848652, 0.243445023, 0.226005004, 0.26002749, 0.255894846], 'k': [1.679419071, 1.740141215, 1.781554261, 1.816251273, 1.857525737, 1.895968733, 1.941169403, 1.99326522, 2.046321345, 2.090129064, 2.14224644, 2.193481406, 2.251163803, 2.306769228, 2.361946782, 2.413637347, 2.464134299, 2.50896784, 2.549587906, 2.577676166, 2.600958825, 2.610628188, 2.613856957, 2.60358516, 2.584135179, 2.56420404, 2.566649101, 2.633707115, 2.774526337, 2.953105649, 3.124794481, 3.28082796, 3.422223479, 3.546563885, 3.666809315, 3.775693898, 3.879628119, 3.981770445, 4.082308744, 4.175083635, 4.27062629, 4.365353818, 4.453675754, 4.541494304, 4.632837662, 4.718605321, 4.806908667, 4.890330992, 4.985764803, 5.058785587, 5.141307607, 5.225721003, 5.314412207, 5.399044187, 5.471682183, 5.558363688, 5.64355183, 5.718126756, 5.799390531, 5.87326682, 5.957887752, 6.04212088, 6.114742596, 6.194384247, 6.272201563, 6.352367739, 6.433641449, 6.506983372, 6.588429772, 6.665250695, 6.744939326, 6.819402641, 6.894769679, 6.97753838, 7.048669327, 7.128558991, 7.21443969, 7.290911502, 7.368255709, 7.447140621, 7.525831613, 7.605285307, 7.67574732, 7.744914539, 7.827905937, 7.904898403, 7.984812024, 8.061453921, 8.142031558, 8.211088802, 8.276924437, 8.369911115, 8.444530783, 8.511723656, 8.594668572, 8.661747292, 8.740887468, 8.812170586, 8.885620977, 8.96290307, 9.049122305, 9.118823933, 9.199486005, 9.262861977, 9.342156608, 9.420006871, 9.497236272, 9.563627476, 9.624262035, 9.719012382, 9.787537482, 9.863240628, 9.953638953, 10.01843534, 10.07430316, 10.15732549, 10.25088368, 10.3234775, 10.3863397, 10.47246554, 10.53438648, 10.60679857, 10.67597454, 10.74925464, 10.8263373, 10.92097821, 10.97767142, 11.04885029, 11.16839394, 11.20544244, 11.29087061, 11.36334128, 11.4432228, 11.53045706, 11.58753257, 11.65025288, 11.72164872, 11.80081631, 11.89332074, 11.92047039, 12.02603352]}

Pt = {'n': [0.8718, 0.8709, 0.8699, 0.8695, 0.8685, 0.8675, 0.8661, 0.8651, 0.8636, 0.8621, 0.8606, 0.8591, 0.857, 0.855, 0.8523, 0.8503, 0.8473, 0.8441, 0.8411, 0.8376, 0.8341, 0.8302, 0.8258, 0.8215, 0.8171, 0.8128, 0.8091, 0.8061, 0.8049, 0.8071, 0.813, 0.8241, 0.8408, 0.8623, 0.8844, 0.9034, 0.915, 0.9182, 0.9124, 0.8974, 0.8681, 0.8233, 1.0933, 1.0283, 0.9782, 0.9517, 0.9333, 0.9187, 0.9068, 0.896, 0.8858, 0.8762, 0.8677, 0.8588, 0.8504, 0.8427, 0.8346, 0.8272, 0.82, 0.8136, 0.8086, 0.8044, 0.8006, 0.7979, 0.7954, 0.7913, 0.7858, 0.7787, 0.7698, 0.7603, 0.7504, 0.7393, 0.7283, 0.7174, 0.7068, 0.6958, 0.6853, 0.6766, 0.6689, 0.6642, 0.664, 0.6706, 0.6866, 0.7135, 0.7468, 0.777, 0.7921, 0.7903, 0.7764, 0.7571, 0.738, 0.7206, 0.7069, 0.6965, 0.6903, 0.6889, 0.6925, 0.7025, 0.7197, 0.7457, 0.7829, 0.8332, 0.8981, 0.9756, 1.0582, 1.132, 1.1831, 1.2052, 1.2027, 1.1851, 1.1619, 1.1398, 1.1224, 1.1124, 1.11, 1.1157, 1.1288, 1.149, 1.1754, 1.2072, 1.2427, 1.2857, 1.371, 1.4624, 1.4746, 1.4658, 1.459, 1.433, 1.3774, 1.2876, 1.1748, 1.1058, 1.1449, 1.2192, 1.1883, 1.1505, 1.304, 1.5367, 1.2882, 0.8675, 0.6273], 'k': [0.1182, 0.12, 0.1213, 0.1225, 0.1238, 0.1251, 0.127, 0.1283, 0.1297, 0.1311, 0.1325, 0.1344, 0.1359, 0.138, 0.1396, 0.1417, 0.1446, 0.1469, 0.1498, 0.1534, 0.1571, 0.162, 0.1671, 0.1729, 0.1805, 0.1889, 0.199, 0.2115, 0.2255, 0.2416, 0.2589, 0.276, 0.2896, 0.2975, 0.2968, 0.2884, 0.2743, 0.2592, 0.246, 0.2396, 0.2482, 0.3298, 0.3787, 0.2057, 0.184, 0.1781, 0.1763, 0.1763, 0.177, 0.1786, 0.1806, 0.1837, 0.1867, 0.191, 0.1952, 0.2005, 0.2061, 0.2128, 0.2201, 0.228, 0.2362, 0.2449, 0.2529, 0.2601, 0.2659, 0.2704, 0.2749, 0.28, 0.2858, 0.2933, 0.3018, 0.3124, 0.3247, 0.3387, 0.3544, 0.373, 0.3933, 0.4168, 0.4432, 0.4735, 0.5068, 0.5428, 0.5782, 0.6075, 0.6227, 0.621, 0.6078, 0.5947, 0.5906, 0.5977, 0.6145, 0.639, 0.6698, 0.7057, 0.746, 0.7903, 0.8382, 0.8897, 0.9434, 0.999, 1.055, 1.1078, 1.1518, 1.1793, 1.1827, 1.1586, 1.1153, 1.0675, 1.0293, 1.0087, 1.0065, 1.0208, 1.0478, 1.0842, 1.1275, 1.1751, 1.2252, 1.2764, 1.328, 1.3792, 1.4315, 1.4953, 1.5237, 1.5785, 1.5004, 1.522, 1.5459, 1.5768, 1.6288, 1.7257, 1.9066, 2.2174, 2.3998, 2.5123, 2.6012, 2.8379, 3.1046, 3.0624, 2.908, 3.2129, 3.7605]}

Zn = {'n': [0.9522, 0.9523, 0.9518, 0.9519, 0.9514, 0.9515, 0.951, 0.951, 0.9506, 0.9507, 0.9502, 0.9498, 0.9499, 0.9494, 0.9495, 0.949, 0.9491, 0.9487, 0.9488, 0.9484, 0.9479, 0.948, 0.9476, 0.9477, 0.9473, 0.9469, 0.947, 0.9466, 0.9467, 0.9463, 0.9459, 0.946, 0.9457, 0.9453, 0.9454, 0.945, 0.9452, 0.9448, 0.9445, 0.9441, 0.9442, 0.9439, 0.9436, 0.9438, 0.9434, 0.9431, 0.9428, 0.943, 0.9427, 0.9424, 0.9421, 0.9418, 0.9421, 0.9418, 0.9416, 0.9413, 0.9411, 0.9409, 0.9406, 0.9404, 0.9402, 0.94, 0.9399, 0.9398, 0.9396, 0.9395, 0.9393, 0.9388, 0.9386, 0.9386, 0.9385, 0.938, 0.9379, 0.9374, 0.9375, 0.937, 0.9365, 0.9367, 0.9362, 0.9358, 0.9354, 0.9352, 0.9349, 0.934, 0.9338, 0.9331, 0.9328, 0.9322, 0.9315, 0.9305, 0.9294, 0.9288, 0.9274, 0.9263, 0.9244, 0.923, 0.9212, 0.9189, 0.9161, 0.9128, 0.9097, 0.9055, 0.901, 0.896, 0.8901, 0.8834, 0.8751, 0.8662, 0.856, 0.844, 0.8304, 0.815, 0.7981, 0.7791, 0.7589, 0.7388, 0.7209, 0.7093, 0.708, 0.7192, 0.7342, 0.7318, 0.6955, 0.6304, 0.5561, 0.4922, 0.4516, 0.4444, 0.4937, 0.6184, 0.6196, 0.4994, 0.4873, 0.5524, 0.7446, 0.6411, 0.5362, 0.524, 0.5508, 0.6029, 0.6794], 'k': [0.0688, 0.0693, 0.0704, 0.0709, 0.072, 0.0725, 0.0736, 0.0741, 0.0752, 0.0763, 0.0768, 0.0779, 0.079, 0.08, 0.0811, 0.0817, 0.0827, 0.0838, 0.0848, 0.0859, 0.087, 0.0881, 0.0892, 0.0902, 0.0913, 0.0924, 0.094, 0.0951, 0.0961, 0.0972, 0.0988, 0.0999, 0.1015, 0.1026, 0.1037, 0.1053, 0.1069, 0.108, 0.1096, 0.1112, 0.1123, 0.1139, 0.1155, 0.1171, 0.1187, 0.1203, 0.122, 0.1235, 0.1252, 0.1268, 0.129, 0.1306, 0.1322, 0.1343, 0.1365, 0.1381, 0.1403, 0.1424, 0.1441, 0.1462, 0.1484, 0.1505, 0.1532, 0.1554, 0.1575, 0.1602, 0.1623, 0.1651, 0.1673, 0.1699, 0.1726, 0.1754, 0.1781, 0.1808, 0.184, 0.1868, 0.1901, 0.1932, 0.196, 0.1993, 0.2026, 0.2064, 0.2097, 0.2131, 0.2169, 0.2208, 0.224, 0.228, 0.2319, 0.2364, 0.2405, 0.2444, 0.2491, 0.2531, 0.258, 0.2627, 0.2676, 0.2726, 0.2778, 0.2832, 0.2891, 0.2949, 0.3013, 0.308, 0.3151, 0.3232, 0.3314, 0.3411, 0.3517, 0.3637, 0.3775, 0.3939, 0.4135, 0.437, 0.4658, 0.5008, 0.5438, 0.5942, 0.6483, 0.6966, 0.7273, 0.74, 0.7541, 0.7971, 0.8811, 1.0066, 1.167, 1.357, 1.5648, 1.7124, 1.7464, 1.9795, 2.172, 2.394, 2.4832, 2.4613, 2.7034, 2.9907, 3.2986, 3.6376, 4.0209]}

Fe = {'n': [0.8555, 0.8552, 0.8543, 0.8546, 0.8545, 0.8555, 0.8566, 0.8582, 0.8605, 0.8633, 0.8666, 0.8704, 0.8741, 0.8775, 0.8815, 0.8847, 0.8877, 0.89, 0.8916, 0.8916, 0.8908, 0.8885, 0.8846, 0.8784, 0.8704, 0.8596, 0.8466, 0.8303, 0.81, 0.7867, 0.7617, 0.7433, 0.7524, 0.8287, 1.0068, 1.222, 1.3227, 1.3147, 1.2744, 1.2334, 1.1982, 1.1692, 1.1452, 1.1253, 1.1081, 1.0936, 1.0804, 1.0685, 1.058, 1.0484, 1.0397, 1.0315, 1.0237, 1.0158, 1.009, 1.0021, 0.9957, 0.9887, 0.9828, 0.9764, 0.9703, 0.9644, 0.9578, 0.9518, 0.9458, 0.9398, 0.9337, 0.9271, 0.9211, 0.9145, 0.9079, 0.9008, 0.8937, 0.8866, 0.8795, 0.8718, 0.8643, 0.8562, 0.8476, 0.8391, 0.8301, 0.8212, 0.8119, 0.8023, 0.7923, 0.782, 0.7715, 0.7608, 0.7502, 0.7399, 0.7301, 0.7206, 0.7121, 0.7046, 0.699, 0.6959, 0.6947, 0.6968, 0.7022, 0.7109, 0.7227, 0.7369, 0.7517, 0.7669, 0.7793, 0.7889, 0.7941, 0.796, 0.7944, 0.7912, 0.7883, 0.7862, 0.7869, 0.7911, 0.7994, 0.8123, 0.8299, 0.8523, 0.8791, 0.9105, 0.9448, 0.9811, 1.0174, 1.0508, 1.078, 1.0952, 1.0979, 1.0834, 1.0524, 1.0114, 0.9786, 0.9848, 1.0157, 1.0709, 1.1477, 1.2262, 1.2657, 1.2321, 1.1422, 1.0547, 1.0197], 'k': [0.1262, 0.1316, 0.137, 0.1428, 0.1486, 0.1543, 0.1605, 0.166, 0.1714, 0.1767, 0.1817, 0.1861, 0.1899, 0.1926, 0.1951, 0.1967, 0.1977, 0.1978, 0.1974, 0.1974, 0.1964, 0.1958, 0.1961, 0.1964, 0.1988, 0.2024, 0.2091, 0.2198, 0.237, 0.2644, 0.3085, 0.3787, 0.4838, 0.6106, 0.6948, 0.6326, 0.4642, 0.3263, 0.2432, 0.1954, 0.1665, 0.1484, 0.1362, 0.128, 0.1218, 0.118, 0.1148, 0.1128, 0.1111, 0.1102, 0.1092, 0.1091, 0.1089, 0.1093, 0.1095, 0.1103, 0.1115, 0.1123, 0.1135, 0.1152, 0.1165, 0.1182, 0.1201, 0.1224, 0.1248, 0.1272, 0.1296, 0.1327, 0.1357, 0.1389, 0.1426, 0.1465, 0.1505, 0.1551, 0.1597, 0.1646, 0.1701, 0.1764, 0.1829, 0.1901, 0.1976, 0.2058, 0.2149, 0.225, 0.236, 0.2481, 0.2612, 0.2754, 0.2912, 0.3088, 0.3287, 0.3497, 0.3729, 0.3981, 0.4249, 0.4541, 0.4844, 0.5152, 0.5469, 0.5774, 0.6061, 0.6324, 0.6558, 0.6754, 0.6923, 0.7073, 0.7222, 0.7393, 0.7603, 0.7855, 0.8163, 0.8522, 0.8934, 0.938, 0.9864, 1.0372, 1.0899, 1.1434, 1.1966, 1.2494, 1.3003, 1.3485, 1.3943, 1.4374, 1.4792, 1.523, 1.5749, 1.644, 1.7437, 1.8905, 2.1009, 2.3822, 2.5445, 2.7112, 2.8678, 2.9991, 3.1106, 3.2521, 3.4954, 3.8792, 4.4072]}

# Menu de opciones para el usuario
def menu():
    print("Seleccione una opción:")
    print('0. Cambiar n de referencia (actual: n_air = 1.0).')
    print("1. Introducir n arbitrario.")
    print("2. Calculo por elementos metalicos.")
    print("3. Salir")
    opcion = input("Opción: ")
    return opcion

# Submenú para determinar si es linealmente polarizado o no
def sub_menu():
    print("Seleccione una opción:")
    print("1. Polarización lineal.")
    print("2. Polarización no lineal.")
    print("3. Luz natural ")
    print("4. Volver al menú principal.")
    opcion1 = input("Opción: ")
    return opcion1


# Petición de datos al usuario para Opción 1 MENU y opción 1 SUBMENU
def pedir_datosLINEAL():

    entrada = input("Entada: ")

    # Procesar la entrada
    entrada = entrada.split("/")

    if len(entrada) != 3:
        print("Formato incorrecto. Por favor, ingrese los datos en el formato correcto.")
        return pedir_datosLINEAL()
    
    try:
        float(entrada[0])
        float(entrada[2])
    except ValueError:
        print("Ángulo de incidencia o acimut no válidos. Por favor, ingrese valores numéricos.")
        return pedir_datosLINEAL()


    # Convertir ángulo de grados a radianes
    theta = (float(entrada[0]) * np.pi / 180)

    # Convertir ángulo de acimut de grados a radianes
    acimut = (float(entrada[2]) * np.pi / 180)

    # Procesar el número complejo


    while ' ' in entrada[1]: # Eliminar espacios en blanco
        entrada[1] = entrada[1].replace(" ", "")
    try:

        complex(entrada[1].replace("i","j"))
    except ValueError:
        print("Número complejo no válido. Por favor, ingrese un número complejo en el formato o a-bi.")
        return pedir_datosLINEAL()
    

    if '+' not in entrada[1]: # Distinción entre valores positivos y negativos
        numeroComple = entrada[1].split("-")
        numeroComple[1] = numeroComple[1].replace("i", "")
        n_comp = np.complex64(float(numeroComple[0]) - 1j*float(numeroComple[1]))
    else:
        numeroComple = entrada[1].split("+")
        numeroComple[1] = numeroComple[1].replace("i", "")
        n_comp = np.complex64(float(numeroComple[0]) - 1j*float(numeroComple[1]))



    # Devolver los valores procesados
    return theta, n_comp, acimut

# Petición de datos al usuario para Opción 1 MENU y opción 2 SUBMENU
def pedir_datosNOLINEAL():
    
    entrada = input("Entada: ")

    # Procesar la entrada
    entrada = entrada.split("/")

    if len(entrada) != 3:
        print("Formato incorrecto. Por favor, ingrese los datos en el formato correcto.")
        return pedir_datosNOLINEAL()
    
    try:
        float(entrada[0])
        float(entrada[2])
    except ValueError:
        print("Ángulo de incidencia o desfase no válidos. Por favor, ingrese valores numéricos.")
        return pedir_datosNOLINEAL()


    # Convertir ángulo de grados a radianes
    theta = (float(entrada[0]) * np.pi / 180)

    # Convertir ángulo de desfase de grados a radianes
    desfase = (float(entrada[2]) * np.pi / 180)

    # Procesar el número complejo

    while ' ' in entrada[1]: # Eliminar espacios en blanco
        entrada[1] = entrada[1].replace(" ", "")
    
    if '+' not in entrada[1]: # Distinción entre valores positivos y negativos
        numeroComple = entrada[1].split("-")
        numeroComple[1] = numeroComple[1].replace("i", "")
        n_comp = np.complex64(float(numeroComple[0]) - 1j*float(numeroComple[1]))
    else:
        numeroComple = entrada[1].split("+")
        numeroComple[1] = numeroComple[1].replace("i", "")
        n_comp = np.complex64(float(numeroComple[0]) - 1j*float(numeroComple[1]))



    # Devolver los valores procesados
    return theta, n_comp, desfase

# Petición de datos al usuario para Opción 1 MENU y opción 3 SUBMENU
def pedir_datos_Natural():
    
    entrada = input("Entada: ")

    # Procesar la entrada
    entrada = entrada.split("/")

    if len(entrada) != 2:
        print("Formato incorrecto. Por favor, ingrese los datos en el formato correcto.")
        return pedir_datos_Natural()
    
    try:
        float(entrada[0])
    except ValueError:
        print("Ángulo de incidencia  no válido. Por favor, ingrese valores numéricos.")
        return pedir_datos_Natural()


    # Convertir ángulo de grados a radianes
    theta = (float(entrada[0]) * np.pi / 180)



    # Procesar el número complejo

    while ' ' in entrada[1]: # Eliminar espacios en blanco
        entrada[1] = entrada[1].replace(" ", "")
    
    if '+' not in entrada[1]: # Distinción entre valores positivos y negativos
        numeroComple = entrada[1].split("-")
        numeroComple[1] = numeroComple[1].replace("i", "")
        n_comp = np.complex64(float(numeroComple[0]) - 1j*float(numeroComple[1]))
    else:
        numeroComple = entrada[1].split("+")
        numeroComple[1] = numeroComple[1].replace("i", "")
        n_comp = np.complex64(float(numeroComple[0]) - 1j*float(numeroComple[1]))



    # Devolver los valores procesados
    return theta, n_comp

# Petición de datos al usuario para Opción 2 MENU
def pedir_datos_Elemento():
    entrada = input("")

    # Procesar la entrada
    entrada = entrada.split("/")
    
    if len(entrada) != 3:
        print("Formato incorrecto. Por favor, ingrese los datos en el formato correcto.")
        return pedir_datos_Elemento()
    

    elemento = entrada[0].strip().lower()
    if elemento not in ['ag', 'au', 'cu', 'al', 'pt', 'zn', 'fe']:
        print("Elemento no válido. Por favor, ingrese un elemento válido (Ag, Au, Cu, Al, Pt, Zn, Fe).")
        return pedir_datos_Elemento()
    try:
        float(entrada[2])
    except ValueError:
        print("Ángulo de incidencia no válidos. Por favor, ingrese valores numéricos.")
        return pedir_datos_Elemento()
    try:
        longitud_onda = float(entrada[1])
        if longitud_onda < 300 or longitud_onda > 1700:
            print("Longitud de onda fuera de rango. Por favor, ingrese un valor entre 300 nm y 1700 nm.")
            return pedir_datos_Elemento()
    except ValueError:
        print("Longitud de onda no válida. Por favor, ingrese un valor numérico.")
        return pedir_datos_Elemento()
        



    longitud_onda = float(entrada[1])
    angulo_incidencia = float(entrada[2]) * np.pi / 180  # Convertir a radianes

    return elemento, longitud_onda, angulo_incidencia

# Función para ajustar el ángulo dentro de 0-360 grados
def VueltaAngular(angulo):
    # Normaliza el ángulo al intervalo [0, 360)
    angulo = angulo % 360
    return angulo



# Calculo de r perpendicular
def calcular_r_perpe(n, n_comp, theta):
    # Definimos x como el seno de theta primado
    x = (n/ n_comp) * np.sin(theta)

    # Devolvemos el valor tras operar sobre la definicion de r perpendicular como la suma y resta de los valores de los angulos.
    return (x* np.cos(theta) - np.sqrt(1 - x**2)*np.sin(theta))/(x * np.cos(theta) + np.sqrt(1 - x**2)*np.sin(theta))

# Calculo de r paralelo
def calcular_r_paral(n, n_comp, theta):
    # Definimos x como el seno de theta primado
    x = (n/ n_comp) * np.sin(theta)
    # Definimos t como la tangente de theta y t prima como la tangente de theta primado
    t = np.tan(theta)
    t_prima = x/ np.sqrt(1 - x**2)
    # Devolvemos el valor tras operar sobre la definicion de r paralelo como la suma y resta de los valores de los angulos.
    return ((t - t_prima)*(1 - t*t_prima))/((t + t_prima)*(1 + t*t_prima))

# Calculo de la 2º forma del desfase y de la razón entre los coeficientes de reflexión
def Calcular_2ºForma(n, n_comp, theta):
    cos_theta_prima = np.sqrt(1 - ((n* np.sin(theta))/n_comp)**2)
    ncompcos = n_comp * cos_theta_prima
    return ((np.cos(theta)*ncompcos + n*np.sin(theta)**2)/(np.cos(theta)*ncompcos - n*np.sin(theta)**2))

# Determinación del índice de refracción complejo a partir del elemento y la longitud de onda
def determinar_ncomp(elemento, longitud_onda):
    # Selección del diccionario correspondiente al elemento
    elementos = [ {'name': 'ag', 'data': Ag},
                  {'name': 'au', 'data': Au},
                  {'name': 'cu', 'data': Cu},
                  {'name': 'al', 'data': Al},
                  {'name': 'pt', 'data': Pt},
                  {'name': 'zn', 'data': Zn},
                  {'name': 'fe', 'data': Fe} ]

    
    elemento = next((item['data'] for item in elementos if item['name'] == elemento), None)
    if elemento is None:
        raise ValueError("Elemento no válido")
    if longitud_onda < 300 or longitud_onda > 1700:
        raise ValueError("Longitud de onda fuera de rango")


    if longitud_onda % 10 == 0:
        indice = lambda_Datos.index(longitud_onda)
        n_comp = elemento['n'][indice] - 1j * elemento['k'][indice]
        return n_comp

    # Interpolación lineal si no es múltiplo de 10 o valor exacto no encontrado

    # Buscar índice inferior y superior para interpolar
    idx_posterior = next((i for i, val in enumerate(lambda_Datos) if val > longitud_onda), None)
    if idx_posterior is None or idx_posterior == 0:
        raise ValueError("Longitud de onda fuera de rango para interpolación")

    idx_anterior = idx_posterior - 1

    # Pendientes para n y k
    pendiente_n = (elemento['n'][idx_posterior] - elemento['n'][idx_anterior]) / (lambda_Datos[idx_posterior] - lambda_Datos[idx_anterior])
    pendiente_k = (elemento['k'][idx_posterior] - elemento['k'][idx_anterior]) / (lambda_Datos[idx_posterior] - lambda_Datos[idx_anterior])

    # Interpolación
    n_pre = pendiente_n * (longitud_onda - lambda_Datos[idx_anterior]) + elemento['n'][idx_anterior]
    k_pre = pendiente_k * (longitud_onda - lambda_Datos[idx_anterior]) + elemento['k'][idx_anterior]
    n_comp = n_pre - 1j * k_pre
    return n_comp

# Cálculos para cada opción del submenú 1
def CalculosSubmenu1():
    """Cálculos y salida formateada para polarización lineal.

    Mejora de ortografía y presentación:
    - Encabezados claros (Primera/Segunda forma)
    - Magnitudes con símbolos (ρ, Δφ, °)
    - Valores alineados/limitados en decimales
    - Clasificación final de la polarización
    """


    # Pedir datos al usuario
    theta, n_comp, acimut = pedir_datosLINEAL()

    # Cálculo de coeficientes de reflexión
    r_perpe = calcular_r_perpe(n, n_comp, theta)
    r_paral = calcular_r_paral(n, n_comp, theta)

    # Forma polar (módulo y ángulo en grados)
    r_perpend = {"radio": float(np.abs(r_perpe)), "Angulo": float(np.angle(r_perpe) * 180 / np.pi)}
    r_paralle = {"radio": float(np.abs(r_paral)), "Angulo": float(np.angle(r_paral) * 180 / np.pi)}

    # Salida formateada
    print("\n" + "═" * 70)
    print("Polarización lineal – Resultados")
    print("═" * 70)



    print("Primera forma")
    print("─" * 70)
    print(f"r⟂: |r⟂| = {r_perpend['radio']:.4f}, ∠r⟂ = {r_perpend['Angulo']:.2f}°")
    print(f"r∥: |r∥| = {r_paralle['radio']:.4f}, ∠r∥ = {r_paralle['Angulo']:.2f}°")

    rho = r_perpend['radio'] / r_paralle['radio'] if r_paralle['radio'] != 0 else np.inf
    desfase = r_perpend['Angulo'] - r_paralle['Angulo']
    desfase_corr = desfase + 180
    desfase_corr = VueltaAngular(desfase_corr)
    print(f"ρ = |r⟂|/|r∥| = {rho:.8f}")
    print(f"Δφ (sin corrección) = {desfase:.2f}°")
    print(f"Δφ (corregido) = {desfase_corr:.2f}°")

    print("\nSegunda forma")
    print("─" * 70)
    desfase_2forma = Calcular_2ºForma(n, n_comp, theta)
    print(f"|ρ| (2ª forma) = {np.abs(desfase_2forma):.8f}")
    print(f"Δφ (2ª forma) = {np.angle(desfase_2forma) * 180 / np.pi:.2f}°")

    # Coeficientes de reflexión y transmisión para acimut dado
    coef_reflexion = (np.sin(acimut) ** 2) * np.abs(r_perpe) ** 2 + (np.cos(acimut) ** 2) * np.abs(r_paral) ** 2
    coef_reflexion = float(coef_reflexion)
    coef_transmision = float(max(0.0, 1.0 - coef_reflexion))  # recorte numérico
    print("\nCoeficientes energéticos")
    print("─" * 70)
    print(f"R (reflexión) = {coef_reflexion:.4f}")
    print(f"T (transmisión) = {coef_transmision:.4f}")

    # Clasificación de la polarización
    print("\nClasificación de la polarización")
    print("─" * 70)
    if 0 < desfase_corr < 90 or -180 < desfase_corr < -90:
        print("Elíptica dextrógira (Δφ en (0°, 90°) o (−180°, −90°)).")
    elif 90 < desfase_corr < 180 or -90 < desfase_corr < 0:
        print("Elíptica levógira (Δφ en (90°, 180°) o (−90°, 0°)).")
    else:
        # Cercanía a 0° o 180° se toma como lineal
        if abs(desfase_corr) < 1e-6 or abs(abs(desfase_corr) - 180) < 1e-6:
            print("Lineal (Δφ ≈ 0° o 180°).")
        else:
            print("Lineal (aprox.)")
    print("═" * 70 + "\n")

# Cálculos para cada opción del submenú 2
def CalculosSubmenu2():
    """Cálculos y salida formateada para polarización no lineal."""


    # Pedir datos al usuario
    theta, n_comp, razon_semiejes = pedir_datosNOLINEAL()

    r_perpe = calcular_r_perpe(n, n_comp, theta)
    r_paral = calcular_r_paral(n, n_comp, theta)

    r_perpend = {"radio": float(np.abs(r_perpe)), "Angulo": float(np.angle(r_perpe) * 180 / np.pi)}
    r_paralle = {"radio": float(np.abs(r_paral)), "Angulo": float(np.angle(r_paral) * 180 / np.pi)}

    print("\n" + "═" * 70)
    print("Polarización no lineal – Resultados")
    print("═" * 70)

    print("Primera forma")
    print("─" * 70)
    print(f"r⟂: |r⟂| = {r_perpend['radio']:.4f}, ∠r⟂ = {r_perpend['Angulo']:.2f}°")
    print(f"r∥: |r∥| = {r_paralle['radio']:.4f}, ∠r∥ = {r_paralle['Angulo']:.2f}°")
    rho = r_perpend['radio'] / r_paralle['radio'] if r_paralle['radio'] != 0 else np.inf
    desfase = r_perpend['Angulo'] - r_paralle['Angulo']
    desfase_corr = desfase + 180
    desfase_corr = VueltaAngular(desfase_corr)
    print(f"ρ = |r⟂|/|r∥| = {rho:.8f}")
    print(f"Δφ_total  = {desfase:.2f}°")
    print(f"Δφ_total (corregido) = {desfase_corr:.2f}°")

    print("\nSegunda forma")
    print("─" * 70)
    desfase_2forma = Calcular_2ºForma(n, n_comp, theta)
    print(f"|ρ| (2ª forma) = {np.abs(desfase_2forma):.8f}")
    print(f"Δφ (2ª forma) = {np.angle(desfase_2forma) * 180 / np.pi:.2f}°")

    print("\nClasificación de la polarización")
    print("─" * 70)
    if 0 < desfase_corr < 90 or -180 < desfase_corr < -90:
        print("Elíptica dextrógira (Δφ en (0°, 90°) o (−180°, −90°)).")
    elif 90 < desfase_corr < 180 or -90 < desfase_corr < 0:
        print("Elíptica levógira (Δφ en (90°, 180°) o (−90°, 0°)).")
    else:
        if abs(desfase_corr) < 1e-6 or abs(abs(desfase_corr) - 180) < 1e-6:
            print("Lineal (Δφ ≈ 0° o 180°).")
        else:
            print("Lineal (aprox.)")
    print("═" * 70 + "\n")

# Cálculos para cada opción del submenú 3
def CalculosSubmenu3():
    print("\n" + "═" * 70)
    # Pedir datos al usuario
    theta, n_comp = pedir_datos_Natural()

    # Cálculo de coeficientes de reflexión
    r_perpe = calcular_r_perpe(n, n_comp, theta)
    r_paral = calcular_r_paral(n, n_comp, theta)

    # Forma polar (módulo y ángulo en grados)
    r_perpend = {"radio": float(np.abs(r_perpe)), "Angulo": float(np.angle(r_perpe) * 180 / np.pi)}
    r_paralle = {"radio": float(np.abs(r_paral)), "Angulo": float(np.angle(r_paral) * 180 / np.pi)}

    # Salida formateada
    print("\n" + "═" * 70)
    print("Luz Natural – Resultados")
    print("═" * 70)

    print("Primera forma")
    print("─" * 70)
    print(f"r⟂: |r⟂| = {r_perpend['radio']:.4f}, ∠r⟂ = {r_perpend['Angulo']:.2f}°")
    print(f"r∥: |r∥| = {r_paralle['radio']:.4f}, ∠r∥ = {r_paralle['Angulo']:.2f}°")

    rho = r_perpend['radio'] / r_paralle['radio'] if r_paralle['radio'] != 0 else np.inf
    desfase = r_perpend['Angulo'] - r_paralle['Angulo']
    desfase_corr = desfase + 180
    desfase_corr = VueltaAngular(desfase_corr)
    print(f"ρ = |r⟂|/|r∥| = {rho:.8f}")
    print(f"Δφ (sin corrección) = {desfase:.2f}°")
    print(f"Δφ (corregido) = {desfase_corr:.2f}°")

    print("\nSegunda forma")
    print("─" * 70)
    desfase_2forma = Calcular_2ºForma(n, n_comp, theta)
    print(f"|ρ| (2ª forma) = {np.abs(desfase_2forma):.8f}")
    print(f"Δφ (2ª forma) = {np.angle(desfase_2forma) * 180 / np.pi:.2f}°")

    # Coeficientes de reflexión y transmisión para acimut dado
    coef_reflexion = (1/2)*(np.abs(r_perpe) ** 2 + np.abs(r_paral) ** 2)
    coef_transmision = float(max(0.0, 1.0 - coef_reflexion))  # recorte numérico
    print("\nCoeficientes energéticos")
    print("─" * 70)
    print(f"R (reflexión) = {coef_reflexion:.4f}")
    print(f"T (transmisión) = {coef_transmision:.4f}")
    print("═" * 70 + "\n")


# Cálculos para la opción 2 del menú principal
def CalculosMenu2():
    """Cálculo usando datos de elementos metálicos y salida embellecida."""

    elemento, longitud_onda, theta = pedir_datos_Elemento()
    n_comp = determinar_ncomp(elemento, longitud_onda)

    print("\n" + "═" * 70)
    print("Cálculo por elementos metálicos – Resultados")
    print("═" * 70)
    print(f"Elemento: {elemento.upper()} | λ = {longitud_onda:.1f} nm | θ = {theta * 180 / np.pi:.2f}°")
    print(f"n* (complejo) = {n_comp}")

    r_perpe = calcular_r_perpe(n, n_comp, theta)
    r_paral = calcular_r_paral(n, n_comp, theta)

    r_perpend = {"radio": float(np.abs(r_perpe)), "Angulo": float(np.angle(r_perpe) * 180 / np.pi)}
    r_paralle = {"radio": float(np.abs(r_paral)), "Angulo": float(np.angle(r_paral) * 180 / np.pi)}

    print("\nPrimera forma")
    print("─" * 70)
    print(f"r⟂: |r⟂| = {r_perpend['radio']:.4f}, ∠r⟂ = {r_perpend['Angulo']:.2f}°")
    print(f"r∥: |r∥| = {r_paralle['radio']:.4f}, ∠r∥ = {r_paralle['Angulo']:.2f}°")
    rho = r_perpend['radio'] / r_paralle['radio'] if r_paralle['radio'] != 0 else np.inf
    desfase = r_perpend['Angulo'] - r_paralle['Angulo']
    desfase_corr = desfase + 180
    desfase_corr = VueltaAngular(desfase_corr)
    print(f"ρ = |r⟂|/|r∥| = {rho:.8f}")
    print(f"Δφ_total  = {desfase:.2f}°")
    print(f"Δφ_total (corregido) = {desfase_corr:.2f}°")

    print("\nSegunda forma")
    print("─" * 70)
    desfase_2forma = Calcular_2ºForma(n, n_comp, theta)
    print(f"|ρ| (2ª forma) = {np.abs(desfase_2forma):.8f}")
    print(f"Δφ (2ª forma) = {np.angle(desfase_2forma) * 180 / np.pi:.2f}°")
    print("═" * 70 + "\n")
    return

# Función principal
def main():
        
    while opcion := menu():
        if opcion == '1':

            while opcion1 := sub_menu():

                # 1º Opcion: Polarización lineal
                if opcion1 == '1':
                    print("Ha seleccionado polarización lineal.")
                    print("-"* 100)
                    print("Ingrese los datos en el siguiente formato: angulo de incidencia (grados)/n - ki/acimut")
                    print("Este sería un ejemplo de entrada: 45/1.33 - 2.5i/30")
                    print("-"* 100)
                    CalculosSubmenu1()
                    print("-"* 100)

                    input("Pulsa Enter para continuar…")
                # 2º Opcion: Polarización no lineal
                elif opcion1 == '2':
                    print("Ha seleccionado polarización no lineal.")
                    print("-"* 100)
                    print("Ingrese los datos en el siguiente formato: angulo de incidencia (grados)/n - ki/razon de ejes (grados)")
                    print("Este sería un ejemplo de entrada: 45/1.33 - 2.5i/30")
                    print("-"* 100) 
                    CalculosSubmenu2()
                    print("-"* 100)

                    input("Pulsa Enter para continuar…")
                # 3º Opcion: Luz natural
                elif opcion1 == '3':
                    print("Ha seleccionado luz natural.")
                    print("-"* 100)
                    print("Ingrese los datos en el siguiente formato: angulo de incidencia (grados)/n - ki")
                    print("Este sería un ejemplo de entrada: 45/1.33 - 2.5i")
                    print("-"* 100)
                    CalculosSubmenu3()
                    print("-"* 100)


                    input("Pulsa Enter para continuar…")
                elif opcion1 == '4':
                    break
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")
                    continue


            input("Pulsa Enter para continuar…")
        elif opcion == '2':
            print("Ha seleccionado cálculo por elementos metálicos.")
            print("-"* 100)
            print("Datos disponibles para los siguientes elementos metálicos: Ag, Au, Cu, Al, Pt, Zn, Fe.\nLongitudes de onda disponibles entre 300 nm y 1700 nm.")
            print("Ingrese los datos en el siguiente formato: elemento metalico/longitud de onda (nm)/angulo de incidencia (grados)")
            print("Este sería un ejemplo de entrada: Ag/500/45")
            CalculosMenu2()
            print("-"* 100)

            input("Pulsa Enter para continuar…")
       
        elif opcion == '0':
            print("-"* 100)
            global n
            print("Cambiar valor de n.")
            n = float(input("Ingrese el nuevo valor de n: "))
            print(f"El nuevo valor de n es: {n}")
            print("-"* 100)

        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            continue
    else:
        print("Gracias por usar el programa.")

if __name__ == "__main__":
    main()