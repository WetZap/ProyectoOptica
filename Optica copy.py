import numpy as np
import pandas as pd
import sys
import os

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

longitud_onda = 500  # Longitud de onda en nm



opcion = '' # Variable para la opción del menú
opcion1 = ''  # Variable para la opción del submenú 1

# Datos de los metales leídos desde el archivo externo
Au = {'n': [1.699838715, 1.746948702, 1.782941044, 1.804652963, 1.804621334, 1.763712432, 1.713434851, 1.689202065, 1.678059067, 1.672504217, 1.665616091, 1.653911114, 1.63743714, 1.612343317, 1.581523054, 1.538326354, 1.475285274, 1.386263242, 1.252905499, 1.064360219, 0.848474841, 0.661635502, 0.52912664, 0.438041087, 0.372502061, 0.323930966, 0.284960267, 0.254069233, 0.228936734, 0.207122197, 0.188789629, 0.172726107, 0.160071695, 0.14636792, 0.135417727, 0.125499436, 0.117832095, 0.111117685, 0.105744888, 0.101509306, 0.098607898, 0.097790271, 0.098623269, 0.096903666, 0.099463321, 0.098537395, 0.099206649, 0.101706737, 0.101315225, 0.103067755, 0.10422723, 0.105937788, 0.104338656, 0.104534544, 0.107001078, 0.111012574, 0.11076329, 0.112038779, 0.114173034, 0.116004573, 0.116828465, 0.116997234, 0.11945701, 0.120635837, 0.122558964, 0.124002721, 0.123935366, 0.126244253, 0.127974627, 0.129942772, 0.132311724, 0.133907614, 0.135401137, 0.138148809, 0.137937636, 0.139246667, 0.134049061, 0.135717763, 0.140363062, 0.138686104, 0.138418628, 0.139442944, 0.141677831, 0.141308241, 0.140235564, 0.142817756, 0.146729336, 0.152747848, 0.149693183, 0.147906483, 0.149395088, 0.151984867, 0.153423422, 0.153670698, 0.157748208, 0.159662147, 0.165494236, 0.159382324, 0.163849184, 0.166211578, 0.166156462, 0.170115488, 0.169795214, 0.174809869, 0.176209118, 0.179585571, 0.177483381, 0.184295562, 0.186297714, 0.190837556, 0.191102283, 0.194361931, 0.205426553, 0.208361137, 0.206557078, 0.208044, 0.205758558, 0.212405614, 0.216697642, 0.219902453, 0.215398722, 0.21956893, 0.222004156, 0.230589098, 0.235210701, 0.238229889, 0.236761828, 0.235275342, 0.240819258, 0.246290147, 0.243652913, 0.25211538, 0.248830057, 0.264448459, 0.258451056, 0.265882655, 0.278561249, 0.278188678, 0.28090035, 0.290244511, 0.316481841], 'k': [1.973157788, 1.974499878, 1.959795593, 1.931950392, 1.896796816, 1.870684779, 1.887670254, 1.922090949, 1.948381952, 1.966512231, 1.973924254, 1.975227068, 1.970304643, 1.959477219, 1.940313163, 1.910745397, 1.872315849, 1.827683172, 1.782097694, 1.76786953, 1.828280492, 1.964525779, 2.129735899, 2.294990195, 2.451664289, 2.597158307, 2.738978341, 2.871855006, 2.999518633, 3.1213458, 3.241703491, 3.356759495, 3.465634566, 3.577628204, 3.685964997, 3.792327795, 3.896137113, 3.999543366, 4.102704228, 4.205033191, 4.305081128, 4.403812319, 4.499191766, 4.59580138, 4.687205239, 4.78107829, 4.872354868, 4.958865219, 5.051560628, 5.148069829, 5.223682926, 5.313023886, 5.407391844, 5.49244276, 5.577046641, 5.659268839, 5.749197205, 5.830570529, 5.912954886, 5.992867182, 6.081993825, 6.163820922, 6.241575921, 6.328550624, 6.410383818, 6.491793025, 6.573991175, 6.662877577, 6.73805443, 6.819155749, 6.904527963, 6.978318655, 7.061609835, 7.141574413, 7.222466808, 7.302149658, 7.406616579, 7.48280825, 7.556831465, 7.637030433, 7.719336741, 7.79996438, 7.874202982, 7.960965269, 8.050382973, 8.114887363, 8.201495565, 8.26754691, 8.350413645, 8.443510901, 8.515005513, 8.589999965, 8.666864413, 8.744347585, 8.81753279, 8.900982642, 8.987624177, 9.068759713, 9.146521008, 9.226192405, 9.303580384, 9.372456417, 9.445201449, 9.530926424, 9.61244244, 9.687582308, 9.769365402, 9.839357949, 9.916385775, 9.992267959, 10.07156989, 10.14138928, 10.22263176, 10.32150252, 10.37509835, 10.46581494, 10.54050931, 10.6421387, 10.70593097, 10.78046182, 10.85893165, 10.91137986, 11.00587506, 11.08617027, 11.16849695, 11.26307034, 11.31706924, 11.38092063, 11.44281407, 11.53172402, 11.64299647, 11.70912303, 11.78354431, 11.86507198, 11.92798378, 12.01168987, 12.06969744, 12.1875916, 12.2404618, 12.34683125, 12.37053599]}


# Menu de opciones para el usuario
def menu():
    print("Seleccione una opción:")
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
    opcion1 = input("Opción: ")
    return opcion1


# Petición de datos al usuario para Opción 1 MENU y opción 1 SUBMENU
def pedir_datosLINEAL():
    print("Ingrese los datos en el siguiente formato: angulo de incidencia (grados)/n - ki/acimut")
    print("Este sería un ejemplo de entrada: 45/1.33 - 2.5i/30")
    entrada = input("")

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
    print("Ingrese los datos en el siguiente formato: angulo de incidencia (grados)/n - ki/desfase (grados)")
    print("Este sería un ejemplo de entrada: 45/1.33 - 2.5i/30")
    entrada = input("")

    # Procesar la entrada
    entrada = entrada.split("/")

    if len(entrada) != 3:
        print("Formato incorrecto. Por favor, ingrese los datos en el formato correcto.")
        return pedir_datosLINEAL()
    
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
    print("Ingrese los datos en el siguiente formato: angulo de incidencia (grados)/n - ki")
    print("Este sería un ejemplo de entrada: 45/1.33 - 2.5i")
    entrada = input("")

    # Procesar la entrada
    entrada = entrada.split("/")

    if len(entrada) != 2:
        print("Formato incorrecto. Por favor, ingrese los datos en el formato correcto.")
        return pedir_datos_Natural()
    
    try:
        float(entrada[0])
    except ValueError:
        print("Ángulo de incidencia o acimut no válidos. Por favor, ingrese valores numéricos.")
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
    print("Datos disponibles para los siguientes elementos metálicos: Ag, Au, Cu, Al, Pt, Zn, Fe.\n Longitudes de onda disponibles entre 300 nm y 1700 nm.")
    print("Ingrese los datos en el siguiente formato: elemento metalico/longitud de onda (nm)/angulo de incidencia (grados)")
    print("Este sería un ejemplo de entrada: Ag/500/45")
    entrada = input("")

    # Procesar la entrada
    entrada = entrada.split("/")

    elemento = entrada[0].strip().lower()
    if elemento not in ['ag', 'au', 'cu', 'al', 'pt', 'zn', 'fe']:
        print("Elemento no válido. Por favor, ingrese un elemento válido (Ag, Au, Cu, Al, Pt, Zn, Fe).")
        return pedir_datos_Elemento()
    try:
        float(entrada[1])
        float(entrada[2])
    except ValueError:
        print("Longitud de onda o ángulo de incidencia no válidos. Por favor, ingrese valores numéricos.")
        return pedir_datos_Elemento()
    
    if len(entrada) != 3:
        print("Formato incorrecto. Por favor, ingrese los datos en el formato correcto.")
        return pedir_datos_Elemento()

    longitud_onda = float(entrada[1])
    angulo_incidencia = float(entrada[2]) * np.pi / 180  # Convertir a radianes

    return elemento, longitud_onda, angulo_incidencia

# Función para ajustar el ángulo dentro de 0-360 grados
def VueltaAngular(angulo):
    while angulo > 360:
        angulo = angulo - 360
    while angulo < 0:
        angulo = angulo + 360
    return angulo


# Calculo de r perpendicular
def calcular_r_perpe(n, n_comp, theta):
    # Definimos x como el seno de theta primado
    x = (n/ n_comp) * np.sin(theta)

    # Devolvemos el valor tras operar sobre la definicion de r perpendicular como la suma y resta de los valores de los angulos.
    return (x* np.cos(theta) - np.sqrt(1 - x**2)*np.sin(theta))/(x* np.cos(theta) + np.sqrt(1 - x**2)*np.sin(theta))

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
    if getattr(sys, 'frozen', False):
        # Cuando está empaquetado en exe
        base_path = sys._MEIPASS
    else:
        # Modo script normal
        base_path = os.path.abspath(".")

    ruta_archivo = os.path.join(base_path, "Metales_IndRef.xlsx")
    nombre_hoja = 'USO'
    df = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja)

    n = df["n" + elemento.capitalize()]
    k = df["k" + elemento.capitalize()]

    if longitud_onda % 10 == 0:
        indice = df.index[df['lambda'] == longitud_onda].tolist()
        if indice:
            idx = indice[0]
            n_comp = n[idx] - 1j * k[idx]
            return n_comp
        else:
            # Si no existe el valor exacto, se puede continuar con la interpolación
            pass

    # Interpolación lineal si no es múltiplo de 10 o valor exacto no encontrado
    lambdas = df['lambda'].values

    # Buscar índice inferior y superior para interpolar
    idx_posterior = next((i for i, val in enumerate(lambdas) if val > longitud_onda), None)
    if idx_posterior is None or idx_posterior == 0:
        raise ValueError("Longitud de onda fuera de rango para interpolación")

    idx_anterior = idx_posterior - 1

    # Pendientes para n y k
    pendiente_n = (n[idx_posterior] - n[idx_anterior]) / (lambdas[idx_posterior] - lambdas[idx_anterior])
    pendiente_k = (k[idx_posterior] - k[idx_anterior]) / (lambdas[idx_posterior] - lambdas[idx_anterior])

    # Interpolación
    n_pre = pendiente_n * (longitud_onda - lambdas[idx_anterior]) + n[idx_anterior]
    k_pre = pendiente_k * (longitud_onda - lambdas[idx_anterior]) + k[idx_anterior]

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
    """Cálculos y salida formateada para polarización no lineal (con desfase inicial)."""



    theta, n_comp, desfase_inicial = pedir_datosNOLINEAL()

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
    desfase = desfase_inicial * 180 / np.pi + r_perpend['Angulo'] - r_paralle['Angulo']
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
                    print("----------------------------------------------------------------------------")
                    CalculosSubmenu1()
                    print("----------------------------------------------------------------------------")

                    input("Pulsa Enter para continuar…")
                # 2º Opcion: Polarización no lineal
                elif opcion1 == '2':
                    print("Ha seleccionado polarización no lineal.")
                    print("----------------------------------------------------------------------------")
                    CalculosSubmenu2()
                    print("----------------------------------------------------------------------------")

                    input("Pulsa Enter para continuar…")
                # 3º Opcion: Luz natural
                elif opcion1 == '3':
                    print("Ha seleccionado luz natural.")
                    print("----------------------------------------------------------------------------")
                    CalculosSubmenu3()
                    print("----------------------------------------------------------------------------")

                    input("Pulsa Enter para continuar…")
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")
                    continue


            input("Pulsa Enter para continuar…")
        elif opcion == '2':
            print("Ha seleccionado cálculo por elementos metálicos.")
            print("----------------------------------------------------------------------------")
            CalculosMenu2()
            print("----------------------------------------------------------------------------")

            input("Pulsa Enter para continuar…")
        elif opcion == '3':
            print("Saliendo del programa.")
            break



        elif opcion == '0':
            print("Cambiar valor de n.")
            n = float(input("Ingrese el nuevo valor de n: "))
            print(f"El nuevo valor de n es: {n}")

            input("Pulsa Enter para continuar…")
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            continue
    else:
        print("Gracias por usar el programa.")

if __name__ == "__main__":
    main()