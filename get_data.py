import pandas as pd
from datetime import datetime

#leemos los datos desde csv y lo convertimos a un formato legible por el html
def data_to_html():
    data = pd.read_csv('templates/graficos/SmartHouse.csv')
    data = data.tail(1) #cogemos la ultima fila 
    datos = []
    fechaNow = datetime.now()
    currentDate = fechaNow.strftime("%d-%b-%Y")

    for index, row in data.iterrows():
        datos.append({
            'Fecha': row['Fecha'], 'Humedad': float(row['Humedad']), 'EnergiaSolar': float(row['EnergiaSolar']), 
            'EnergiaEolica': float(row['EnergiaEolica']), 'LuzHabitacion1': float(row['LuzHabitacion1']), 
            'LuzHabitacion2': float(row['LuzHabitacion2']), 'LuzSalon': float(row['LuzSalon']), 
            'LuzCocina': float(row['LuzCocina']), 'LuzBano1': float(row['LuzBano1']), 'LuzBano2': float(row['LuzBano2']), 
            'LuzDespacho': float(row['LuzDespacho']), 'LuzExterior': float(row['LuzExterior']), 
            'ConsumoAguaDucha1': float(row['ConsumoAguaDucha1']), 'ConsumoAguaDucha2': float(row['ConsumoAguaDucha2']), 
            'ConsumoAguaWC1': float(row['ConsumoAguaWC1']), 'ConsumoAguaWC2': float(row['ConsumoAguaWC2']), 
            'ConsumoAguaLavabo1': float(row['ConsumoAguaLavabo1']), 'ConsumoAguaLavabo2': float(row['ConsumoAguaLavabo2']), 
            'ConsumoAguaLavadora': float(row['ConsumoAguaLavadora']), 'ConsumoAguaLavavajillas': float(row['ConsumoAguaLavavajillas']), 
            'ConsumoAguaFregadero': float(row['ConsumoAguaFregadero']), 'ConsumoAguaExterior': float(row['ConsumoAguaExterior']), 
            'ConsumoAguaBano1': float(row['ConsumoAguaBano1']), 'ConsumoAguaBano2': float(row['ConsumoAguaBano2']), 
            'ConsumoAguaCocina': float(row['ConsumoAguaCocina']), 'GastoAguaTotal': float(row['GastoAguaTotal']), 
            'ConsumoVitroceramica': float(row['ConsumoVitroceramica']), 'ConsumoFrigorifico': float(row['ConsumoFrigorifico']), 
            'ConsumoLavadora': float(row['ConsumoLavadora']), 'ConsumoHorno': float(row['ConsumoHorno']), 
            'ConsumoTelevision': float(row['ConsumoTelevision']), 'ConsumoMicroondas': float(row['ConsumoMicroondas']),
            'ConsumoLavavajillas': float(row['ConsumoLavavajillas']), 'GastoLuzTotal': float(row['GastoLuzTotal']), 
            'Amanecer': row['Amanecer'], 'Atardecer': row['Atardecer'], 'DuracionDia': row['DuracionDia'],
            'Precipitaciones': float(row['Precipitaciones']), 'TemperaturaMax': float(row['TemperaturaMax']), 
            'TemperaturaMin': float(row['TemperaturaMin']), 'Viento': float(row['Viento']), 'PresionMax': float(row['PresionMax']), 
            'PresionMin': float(row['PresionMin']), 'TemperaturaHora': float(row['TemperaturaHora']), 
            'VentanaHabitacion1': float(row['VentanaHabitacion1']), 'VentanaHabitacion2': float(row['VentanaHabitacion2']), 
            'VentanaSalon': float(row['VentanaSalon']), 'VentanaCocina': float(row['VentanaCocina']), 'VentanaBano1': float(row['VentanaBano1']), 
            'VentanaBano2': float(row['VentanaBano2']), 'VentanaDespacho': float(row['VentanaDespacho']), 
            'PersianaHabitacion1': float(row['PersianaHabitacion1']), 'PersianaHabitacion2': float(row['PersianaHabitacion2']), 
            'PersianaSalon': float(row['PersianaSalon']), 'PersianaCocina': float(row['PersianaCocina']), 
            'PersianaBano1': float(row['PersianaBano1']), 'PersianaBano2': float(row['PersianaBano2']), 
            'PersianaDespacho': float(row['PersianaDespacho']), 'PuertaHabitacion1': float(row['PuertaHabitacion1']), 
            'PuertaHabitacion2': float(row['PuertaHabitacion2']), 'PuertaSalon': float(row['PuertaSalon']), 
            'PuertaCocina': float(row['PuertaCocina']), 'PuertaBano1': float(row['PuertaBano1']), 'PuertaBano2': float(row['PuertaBano2']), 
            'PuertaDespacho': float(row['PuertaDespacho']), 'PuertaEntrada': float(row['PuertaEntrada']), 
            'CalefaccionHabitacion1': float(row['CalefaccionHabitacion1']), 'CalefaccionHabitacion2': float(row['CalefaccionHabitacion2']), 
            'CalefaccionSalon': float(row['CalefaccionSalon']), 'CalefaccionCocina': float(row['CalefaccionCocina']), 
            'CalefaccionBano1': float(row['CalefaccionBano1']), 'CalefaccionBano2': float(row['CalefaccionBano2']), 
            'CalefaccionDespacho': float(row['CalefaccionDespacho']), 'ACHabitacion1': float(row['ACHabitacion1']), 
            'ACHabitacion2': float(row['ACHabitacion2']), 'ACSalon': float(row['ACSalon']), 'ACCocina': float(row['ACCocina']), 
            'ACBano1': float(row['ACBano1']), 'ACBano2': float(row['ACBano2']), 'ACDespacho': float(row['ACDespacho']), 
            'TempHabitacion1': float(row['TempHabitacion1']), 'TempHabitacion2': float(row['TempHabitacion2']), 
            'TempSalon': float(row['TempSalon']), 'TempCocina': float(row['TempCocina']), 'TempBano1': float(row['TempBano1']), 
            'TempBano2': float(row['TempBano2']), 'TempDespacho': float(row['TempDespacho']), 'Anomalias': int(row['Anomalias']), 
            'LugarAnomalia': row['LugarAnomalia'], 'TemperaturaMediaCasa': float(row['TemperaturaMediaCasa']), 
            'GastoElecHab1': float(row['GastoElecHab1']), 'GastoElecHab2': float(row['GastoElecHab2']), 
            'GastoElecSalon': float(row['GastoElecSalon']), 'GastoElecCocina': float(row['GastoElecCocina']), 
            'GastoElecBano1': float(row['GastoElecBano1']), 'GastoElecBano2': float(row['GastoElecBano2']), 
            'GastoElecDespacho': float(row['GastoElecDespacho']), 'GastoElecExterior': float(row['GastoElecExterior']), 
            'GastoElecTotal': float(row['GastoElecTotal']), 'LuzPasillo': float(row['LuzPasillo']), 
            'CalefaccionPasillo': float(row['CalefaccionPasillo']), 'ACPasillo': float(row['ACPasillo']), 
            'EstadoVentanaHab1': row['EstadoVentanaHab1'], 'EstadoVentanaHab2': row['EstadoVentanaHab2'], 
            'EstadoVentanaSalon': row['EstadoVentanaSalon'], 'EstadoVentanaCocina': row['EstadoVentanaCocina'],
            'EstadoVentanaBano1': row['EstadoVentanaBano1'], 'EstadoVentanaBano2': row['EstadoVentanaBano2'],
            'EstadoVentanaDespacho': row['EstadoVentanaDespacho'], 'EstadoPersianaHabitacion1': row['EstadoPersianaHabitacion1'], 
            'EstadoPersianaHabitacion2': row['EstadoPersianaHabitacion2'], 'EstadoPersianaSalon': row['EstadoPersianaSalon'], 
            'EstadoPersianaCocina': row['EstadoPersianaCocina'], 'EstadoPersianaBano1': row['EstadoPersianaBano1'], 
            'EstadoPersianaBano2': row['EstadoPersianaBano2'], 'EstadoPersianaDespacho': row['EstadoPersianaDespacho'], 
            'EstadoPuertaHabitacion1': row['EstadoPuertaHabitacion1'], 'EstadoPuertaHabitacion2': row['EstadoPuertaHabitacion2'], 
            'EstadoPuertaSalon': row['EstadoPuertaSalon'], 'EstadoPuertaCocina': row['EstadoPuertaCocina'], 
            'EstadoPuertaBano1': row['EstadoPuertaBano1'], 'EstadoPuertaBano2': row['EstadoPuertaBano2'], 
            'EstadoPuertaDespacho': row['EstadoPuertaDespacho'], 'EstadoPuertaEntrada': row['EstadoPuertaEntrada'], 
            'EstadoCalefaccionHab1': row['EstadoCalefaccionHab1'], 'EstadoCalefaccionHab2': row['EstadoCalefaccionHab2'], 
            'EstadoCalefaccionSalon': row['EstadoCalefaccionSalon'], 'EstadoCalefaccionCocina': row['EstadoCalefaccionCocina'], 
            'EstadoCalefaccionBano1': row['EstadoCalefaccionBano1'], 'EstadoCalefaccionBano2': row['EstadoCalefaccionBano2'], 
            'EstadoCalefaccionDespacho': row['EstadoCalefaccionDespacho'], 'EstadoCalefaccionPasillo': row['EstadoCalefaccionPasillo'],
            'EstadoACHab1': row['EstadoACHab1'], 'EstadoACHab2': row['EstadoACHab2'], 'EstadoACSalon': row['EstadoACSalon'], 
            'EstadoACCocina': row['EstadoACCocina'], 'EstadoACBano1': row['EstadoACBano1'], 'EstadoACBano2': row['EstadoACBano2'], 
            'EstadoACDespacho': row['EstadoACDespacho'], 'EstadoACPasillo': row['EstadoACPasillo'],
            'EstadoPuerta2Bano': row['EstadoPuerta2Bano'], 'EstadoPuerta2Salon': row['EstadoPuerta2Salon'],
            'EstadoPuertaPatio': row['EstadoPuertaPatio'], 'EstadoPuerta2Cocina': row['EstadoPuerta2Cocina'],
            'TempPasillo': float(row['TempPasillo']), 'HabitacionAnomalia': row['HabitacionAnomalia'], 'currentDate': currentDate
        })
        print(datos)
    return datos