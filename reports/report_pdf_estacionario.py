import json
import base64
import openpyxl
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
from openpyxl.drawing.image import Image
import pyexcel as pe
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from fpdf import FPDF
import xlsxwriter
from django.http import FileResponse, HttpResponse
import requests
#instalar el libreoffice por comando en la maquina
import platform
import os
import subprocess

def GeneratePDFintoSVG(questions_mtto, question_views, questions_deterioration, tank_identification,
                       observations_and_results, signatures, photos, fecha_convertida,  companie,  id, aprobado):
    
    JSONquestions_mtto = json.loads(questions_mtto)
    JSONquestion_views = json.loads(question_views)
    JSONquestions_deterioration = json.loads(questions_deterioration)
    JSONtank_identification = json.loads(tank_identification)
    JSONobservations_and_results =    json.loads(observations_and_results)
    JSONsignatures = json.loads(signatures)
    JSONphotos = json.loads(photos)
   

    def downloadImage(url):
        response = requests.get(url)
        if response.status_code == 200:
            # Obtener el contenido de la imagen
            image_data = response.content
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            return image_base64
        else:
            print("Error al descargar la imagen:", response.status_code)
            return ("")

    workbook = openpyxl.load_workbook('reports/tpFijo.xlsx')

    # Obtener la hoja de trabajo (puedes ajustar esto según tu necesidad)
    hoja = workbook['INF.0000']
    hoja2= workbook['REGISTRO FOTOGRAFICO']

    #datos usuario
    hoja['D9'] = fecha_convertida
    hoja['O6'] = id
    hoja2['O6'] = id
    hoja['C10'] = companie[1]
    hoja['C11'] = companie[2]
    hoja['C12'] = companie[5]
    hoja['K77'] = companie[5]  
    hoja['C14'] = companie[3]
    hoja['C15'] = companie[6]
    hoja['C13'] = companie[4]
    
    #cumple final 
    if aprobado == True:
     hoja['F69'] = 'X'
    else:
      hoja['M69'] = 'X'

    #galaga
    if JSONquestions_mtto['ensayoNoDestructivo'] == True:
     hoja['G70'] = 'X'
     hoja['I70'] = JSONquestions_mtto['cuales']
    if JSONquestions_mtto['fotografia'] == True:
     hoja['K71'] = 'X'
    if JSONquestions_mtto['video'] == True:
     hoja['M71'] = 'X'
    if JSONquestions_mtto['otros1'] == True:
     hoja['O71'] = 'X'
    #equipos utilizados 
    hoja['B73'] = JSONquestions_mtto['cantidadEquiposUtilizados1']
    hoja['B74'] = JSONquestions_mtto['cantidadEquiposUtilizados2']
    hoja['B75'] = JSONquestions_mtto['cantidadEquiposUtilizados3']
    hoja['B76'] = JSONquestions_mtto['cantidadEquiposUtilizados4']
    hoja['B77'] = JSONquestions_mtto['cantidadEquiposUtilizados5']
    if JSONquestions_mtto['equipos1'] == True:
     hoja['D73'] = 'X'
    if JSONquestions_mtto['equipos2'] == True:
     hoja['D74'] = 'X'
    if JSONquestions_mtto['equipos3'] == True:
     hoja['D75'] = 'X'
    if JSONquestions_mtto['equipos4'] == True:
     hoja['D76'] = 'X'
    if JSONquestions_mtto['equipos5'] == True:
     hoja['D77'] = 'X'
    


    # Realizar las ediciones necesarias en el archivo Excel en memoria
    # capacidad nominal
    hoja['M13'] = JSONtank_identification['capacidadNominal']
    hoja['M14'] = JSONtank_identification['fabricante']
    hoja['M15']=JSONtank_identification['numeroSerie']

    #campos de seleccion doble
    #revision
    if JSONtank_identification['revision'] == '1 Vez':
      hoja['K17'] = 'X'
    if JSONtank_identification['revision'] == '2 Vez':
      hoja['M17'] = 'X'
    #tipo tanque
    if JSONtank_identification['tipoTanque'] == 'Vertical':
     hoja['D18'] = 'X'
    if JSONtank_identification['tipoTanque'] == 'horizontal':
     hoja['G18'] = 'X'

    #campos selecion triple
    #clase de usuario
    if JSONtank_identification['claseUsuario'] == 'Residencial':
     hoja['F19'] = 'X'
    if JSONtank_identification['claseUsuario'] == 'Comercial':
     hoja['J19'] = 'X'
    if JSONtank_identification['claseUsuario'] == 'Industrial':
     hoja['M19'] = 'X'

    #hermeticidad
    if JSONtank_identification['hermeticidad']['presenta']== 'SÍ':
     hoja['F22'] = 'X'
    if JSONtank_identification['hermeticidad']['presenta']== 'NO':
     hoja['G22'] = 'X'
    if JSONtank_identification['hermeticidad']['presenta'] == 'N/A':
     hoja['H22'] = 'X'
    if JSONtank_identification['hermeticidad']['cumple'] == True:
     hoja['O22'] = 'X'
    else:
      hoja['P22'] = 'X'
    # agrietamiento
    if JSONtank_identification['agrietamiento']['presenta']== 'SÍ':
     hoja['F23'] = 'X'
    if JSONtank_identification['agrietamiento']['presenta']== 'NO':
     hoja['G23'] = 'X'
    if JSONtank_identification['agrietamiento']['presenta'] == 'N/A':
     hoja['H23'] = 'X'
    if JSONtank_identification['agrietamiento']['cumple'] == True:
     hoja['O23'] = 'X'
    else:
      hoja['P23'] = 'X'
    # porosidad
    if JSONtank_identification['porosidad']['presenta']== 'SÍ':
     hoja['F24'] = 'X'
    if JSONtank_identification['porosidad']['presenta']== 'NO':
     hoja['G24'] = 'X'
    if JSONtank_identification['porosidad']['presenta'] == 'N/A':
     hoja['H24'] = 'X'
    if JSONtank_identification['porosidad']['cumple'] == True:
     hoja['O24'] = 'X'
    else:
      hoja['P24'] = 'X'
    # salpicadura
    if JSONtank_identification['salpicadura']['presenta']== 'SÍ':
     hoja['F25'] = 'X'
    if JSONtank_identification['salpicadura']['presenta']== 'NO':
     hoja['G25'] = 'X'
    if JSONtank_identification['salpicadura']['presenta'] == 'N/A':
     hoja['H25'] = 'X'
    if JSONtank_identification['salpicadura']['cumple'] == True:
     hoja['O25'] = 'X'
    else:
      hoja['P25'] = 'X'
    # socavado
    if JSONtank_identification['socavado']['presenta']== 'SÍ':
     hoja['F26'] = 'X'
    if JSONtank_identification['socavado']['presenta']== 'NO':
     hoja['G26'] = 'X'
    if JSONtank_identification['socavado']['presenta'] == 'N/A':
     hoja['H26'] = 'X'
    if JSONtank_identification['socavado']['cumple'] == True:
     hoja['O26'] = 'X'
    else:
      hoja['P26'] = 'X'
    # abolladura
    if JSONtank_identification['abolladura']['1']['presenta']== 'SÍ':
     hoja['F27'] = 'X'
     hoja['N27'] = 'X'
    if JSONtank_identification['abolladura']['1']['presenta']== 'NO':
     hoja['G27'] = 'X'
     hoja['N27'] = 'X'
    if JSONtank_identification['abolladura']['1']['presenta'] == 'N/A':
     hoja['H27'] = 'X'
     hoja['N27'] = 'X'
    if JSONtank_identification['abolladura']['1']['cumple'] == True:
     hoja['O27'] = 'X'
    else:
      hoja['P27'] = 'X'
    if JSONtank_identification['abolladura']['2']['presenta']== 'SÍ':
     hoja['F28'] = 'X'
     hoja['N28'] = 'X'
    if JSONtank_identification['abolladura']['2']['presenta']== 'NO':
     hoja['G28'] = 'X'
     hoja['N28'] = 'X'
    if JSONtank_identification['abolladura']['2']['presenta'] == 'N/A':
     hoja['H28'] = 'X'
     hoja['N28'] = 'X'
    if JSONtank_identification['abolladura']['2']['cumple'] == True:
     hoja['O28'] = 'X'
    else:
      hoja['P28'] = 'X'
    if JSONtank_identification['abolladura']['3']['presenta']== 'SÍ':
     hoja['F29'] = 'X'
     hoja['N29'] = 'X'
    if JSONtank_identification['abolladura']['3']['presenta']== 'NO':
     hoja['G29'] = 'X'
     hoja['N29'] = 'X'
    if JSONtank_identification['abolladura']['3']['presenta'] == 'N/A':
     hoja['H29'] = 'X'
     hoja['N29'] = 'X'
    if JSONtank_identification['abolladura']['3']['cumple'] == True:
     hoja['O29'] = 'X'
    else:
      hoja['P29'] = 'X'
    #abombamiento
    if JSONtank_identification['abombamiento']['presenta']== 'SÍ':
     hoja['F30'] = 'X'
    if JSONtank_identification['abombamiento']['presenta']== 'NO':
     hoja['G30'] = 'X'
    if JSONtank_identification['abombamiento']['presenta'] == 'N/A':
     hoja['H30'] = 'X'
    if JSONtank_identification['abombamiento']['defectologia'] == True:
     hoja['N30'] = 'X'
    else:
      hoja['N30'] = ''
    if JSONtank_identification['abombamiento']['cumple'] == True:
     hoja['O30'] = 'X'
    else:
      hoja['P30'] = 'X'
    #corrosionAislada
    if JSONtank_identification['corrosionAislada']['presenta']== 'SÍ':
     hoja['F31'] = 'X'
     hoja['P31'] = 'X'
    if JSONtank_identification['corrosionAislada']['presenta']== 'NO':
     hoja['G31'] = 'X'
     hoja['O31'] = 'X'
    if JSONtank_identification['corrosionAislada']['presenta'] == 'N/A':
     hoja['H31'] = 'X'
     hoja['O31'] = 'X'
    if JSONtank_identification['corrosionAislada']['1']['defectologia']== True:
     hoja['N31'] = 'X'
    if JSONtank_identification['corrosionAislada']['2']['defectologia']== True:
     hoja['N32'] = 'X'
     #corrosion en linea
    if JSONtank_identification['corrosionEnLinea']['presenta']== 'SÍ':
     hoja['F33'] = 'X'
     hoja['P33'] = 'X'
    if JSONtank_identification['corrosionEnLinea']['presenta']== 'NO':
     hoja['G33'] = 'X'
     hoja['O33'] = 'X'
    if JSONtank_identification['corrosionEnLinea']['presenta'] == 'N/A':
     hoja['H33'] = 'X'
     hoja['O33'] = 'X'
    if JSONtank_identification['corrosionEnLinea']['1']['defectologia']== True:
     hoja['N33'] = 'X'
    if JSONtank_identification['corrosionEnLinea']['2']['defectologia']== True:
     hoja['N34'] = 'X'
    if JSONtank_identification['corrosionEnLinea']['3']['defectologia']== True:
     hoja['N35'] = 'X'
    #corrosion general
    if JSONtank_identification['corrosionGeneral']['presenta']== 'SÍ':
     hoja['F36'] = 'X'
     hoja['P36'] = 'X'
    if JSONtank_identification['corrosionGeneral']['presenta']== 'NO':
     hoja['G36'] = 'X'
     hoja['O36'] = 'X'
    if JSONtank_identification['corrosionGeneral']['presenta'] == 'N/A':
     hoja['H36'] = 'X'
     hoja['O36'] = 'X'
    if JSONtank_identification['corrosionGeneral']['1']['defectologia']== True:
     hoja['N36'] = 'X'
    if JSONtank_identification['corrosionGeneral']['2']['defectologia']== True:
     hoja['N37'] = 'X'
    #Accion por fuego
    if JSONtank_identification['AccionPorFuego']['presenta']== 'SÍ':
     hoja['F38'] = 'X'
     hoja['P38'] = 'X'
    if JSONtank_identification['AccionPorFuego']['presenta']== 'NO':
     hoja['G38'] = 'X'
     hoja['O38'] = 'X'
    if JSONtank_identification['AccionPorFuego']['presenta'] == 'N/A':
     hoja['H38'] = 'X'
     hoja['O38'] = 'X'
    if JSONtank_identification['AccionPorFuego']['1']['defectologia']== True:
     hoja['N38'] = 'X'
    if JSONtank_identification['AccionPorFuego']['2']['defectologia']== True:
     hoja['N39'] = 'X' 
    #EstadoConexionCorrosion
    if JSONtank_identification['EstadoConexionCorrosion']['presenta']== 'SÍ':
     hoja['F40'] = 'X'
    if JSONtank_identification['EstadoConexionCorrosion']['presenta']== 'NO':
     hoja['G40'] = 'X'
    if JSONtank_identification['EstadoConexionCorrosion']['presenta'] == 'N/A':
     hoja['H40'] = 'X'
    if JSONtank_identification['EstadoConexionCorrosion']['cumple'] == True:
     hoja['O40'] = 'X'
    else:
      hoja['P40'] = 'X'
    #EstadoConexionEvidenciaGolpes
    if JSONtank_identification['EstadoConexionEvidenciaGolpes']['presenta']== 'SÍ':
     hoja['F41'] = 'X'
    if JSONtank_identification['EstadoConexionEvidenciaGolpes']['presenta']== 'NO':
     hoja['G41'] = 'X'
    if JSONtank_identification['EstadoConexionEvidenciaGolpes']['presenta'] == 'N/A':
     hoja['H41'] = 'X'
    if JSONtank_identification['EstadoConexionEvidenciaGolpes']['cumple'] == True:
     hoja['O41'] = 'X'
    else:
      hoja['P41'] = 'X'
    #EstadoConexionDesgaste
    if JSONtank_identification['EstadoConexionDesgaste']['presenta']== 'SÍ':
     hoja['F42'] = 'X'
    if JSONtank_identification['EstadoConexionDesgaste']['presenta']== 'NO':
     hoja['G42'] = 'X'
    if JSONtank_identification['EstadoConexionDesgaste']['presenta'] == 'N/A':
     hoja['H42'] = 'X'
    if JSONtank_identification['EstadoConexionDesgaste']['cumple'] == True:
     hoja['O42'] = 'X'
    else:
      hoja['P42'] = 'X'
    #EstadoConexionOtros
    if JSONtank_identification['EstadoConexionOtros']['presenta']== 'SÍ':
     hoja['F43'] = 'X'
    if JSONtank_identification['EstadoConexionOtros']['presenta']== 'NO':
     hoja['G43'] = 'X'
    if JSONtank_identification['EstadoConexionOtros']['presenta'] == 'N/A':
     hoja['H43'] = 'X'
    if JSONtank_identification['EstadoConexionOtros']['cumple'] == True:
     hoja['O43'] = 'X'
    else:
      hoja['P43'] = 'X'
    #soporte
    if JSONquestion_views['soportetanque']['presenta']== 'Bueno':
     hoja['F45'] = 'X'
    if JSONquestion_views['soportetanque']['presenta']== 'Malo':
     hoja['G45'] = 'X'
    if JSONquestion_views['soportetanque']['presenta'] == 'N/A':
     hoja['H45'] = 'X'
    if JSONquestion_views['soportetanque']['cumple'] == True:
     hoja['O45'] = 'X'
    else:
      hoja['P45'] = 'X'
    #domoprotector
    if JSONquestion_views['domoprotector']['presenta']== 'Bueno':
     hoja['F46'] = 'X'
    if JSONquestion_views['domoprotector']['presenta']== 'Malo':
     hoja['G46'] = 'X'
    if JSONquestion_views['domoprotector']['presenta'] == 'N/A':
     hoja['H46'] = 'X'
    if JSONquestion_views['domoprotector']['cumple'] == True:
     hoja['O46'] = 'X'
    else:
      hoja['P46'] = 'X'
    #orejasizaminto
    if JSONquestion_views['orejasizaminto']['presenta']== 'Bueno':
     hoja['F47'] = 'X'
    if JSONquestion_views['orejasizaminto']['presenta']== 'Malo':
     hoja['G47'] = 'X'
    if JSONquestion_views['orejasizaminto']['presenta'] == 'N/A':
     hoja['H47'] = 'X'
    if JSONquestion_views['orejasizaminto']['cumple'] == True:
     hoja['O47'] = 'X'
    else:
      hoja['P47'] = 'X'
    #pintura
    if JSONquestion_views['pintura']['presenta']== 'Bueno':
     hoja['F48'] = 'X'
    if JSONquestion_views['pintura']['presenta']== 'Malo':
     hoja['G48'] = 'X'
    if JSONquestion_views['pintura']['presenta'] == 'N/A':
     hoja['H48'] = 'X'
    if JSONquestion_views['pintura']['cumple'] == True:
     hoja['O48'] = 'X'
    else:
      hoja['P48'] = 'X'
    #proteccioncatodica
    if JSONquestion_views['proteccioncatodica']['presenta']== 'Bueno':
     hoja['F49'] = 'X'
    if JSONquestion_views['proteccioncatodica']['presenta']== 'Malo':
     hoja['G49'] = 'X'
    if JSONquestion_views['proteccioncatodica']['presenta'] == 'N/A':
     hoja['H49'] = 'X'
    if JSONquestion_views['proteccioncatodica']['cumple'] == True:
     hoja['O49'] = 'X'
    else:
      hoja['P49'] = 'X'
    #continuidad
    if JSONquestion_views['continuidad']['presenta']== 'Bueno':
     hoja['F50'] = 'X'
    if JSONquestion_views['continuidad']['presenta']== 'Malo':
     hoja['G50'] = 'X'
    if JSONquestion_views['continuidad']['presenta'] == 'N/A':
     hoja['H50'] = 'X'
    if JSONquestion_views['continuidad']['cumple'] == True:
     hoja['O50'] = 'X'
    else:
      hoja['P50'] = 'X'
    #tuberiadefectuosa
    if JSONquestions_deterioration['tuberiadefectosoldadura']['presenta']== 'SÍ':
     hoja['F52'] = 'X'
    if JSONquestions_deterioration['tuberiadefectosoldadura']['presenta']== 'NO':
     hoja['G52'] = 'X'
    if JSONquestions_deterioration['tuberiadefectosoldadura']['presenta'] == 'N/A':
     hoja['H52'] = 'X'
    if JSONquestions_deterioration['tuberiadefectosoldadura']['cumple'] == True:
     hoja['O52'] = 'X'
    else:
      hoja['P52'] = 'X'
    #tuberiapresentacorrosion
    if JSONquestions_deterioration['tuberiapresentacorrosion']['presenta']== 'SÍ':
     hoja['F53'] = 'X'
    if JSONquestions_deterioration['tuberiapresentacorrosion']['presenta']== 'NO':
     hoja['G53'] = 'X'
    if JSONquestions_deterioration['tuberiapresentacorrosion']['presenta'] == 'N/A':
     hoja['H53'] = 'X'
    if JSONquestions_deterioration['tuberiapresentacorrosion']['cumple'] == True:
     hoja['O53'] = 'X'
    else:
      hoja['P53'] = 'X'
    #tuberiapresentafisura
    if JSONquestions_deterioration['tuberiapresentafisura']['presenta']== 'SÍ':
     hoja['F54'] = 'X'
    if JSONquestions_deterioration['tuberiapresentafisura']['presenta']== 'NO':
     hoja['G54'] = 'X'
    if JSONquestions_deterioration['tuberiapresentafisura']['presenta'] == 'N/A':
     hoja['H54'] = 'X'
    if JSONquestions_deterioration['tuberiapresentafisura']['cumple'] == True:
     hoja['O54'] = 'X'
    else:
      hoja['P54'] = 'X'
    #tuberiaaplastamiento
    if JSONquestions_deterioration['tuberiaaplastamiento']['presenta']== 'SÍ':
     hoja['F55'] = 'X'
    if JSONquestions_deterioration['tuberiaaplastamiento']['presenta']== 'NO':
     hoja['G55'] = 'X'
    if JSONquestions_deterioration['tuberiaaplastamiento']['presenta'] == 'N/A':
     hoja['H55'] = 'X'
    if JSONquestions_deterioration['tuberiaaplastamiento']['cumple'] == True:
     hoja['O55'] = 'X'
    else:
      hoja['P55'] = 'X'
    #roscaencuentrabuenestado
    if JSONquestions_deterioration['roscaencuentrabuenestado']['presenta']== 'SÍ':
     hoja['F56'] = 'X'
    if JSONquestions_deterioration['roscaencuentrabuenestado']['presenta']== 'NO':
     hoja['G56'] = 'X'
    if JSONquestions_deterioration['roscaencuentrabuenestado']['presenta'] == 'N/A':
     hoja['H56'] = 'X'
    if JSONquestions_deterioration['roscaencuentrabuenestado']['cumple'] == True:
     hoja['O56'] = 'X'
    else:
      hoja['P56'] = 'X'
    #accesoriosencuentrabuenestado
    if JSONquestions_deterioration['accesoriosencuentrabuenestado']['presenta']== 'SÍ':
     hoja['F57'] = 'X'
    if JSONquestions_deterioration['accesoriosencuentrabuenestado']['presenta']== 'NO':
     hoja['G57'] = 'X'
    if JSONquestions_deterioration['accesoriosencuentrabuenestado']['presenta'] == 'N/A':
     hoja['H57'] = 'X'
    if JSONquestions_deterioration['accesoriosencuentrabuenestado']['cumple'] == True:
     hoja['O57'] = 'X'
    else:
      hoja['P57'] = 'X'
    #visual estadovalvulas
    if JSONobservations_and_results['estadovalvulas']['presenta']== 'Bueno':
     hoja['F59'] = 'X'
    if JSONobservations_and_results['estadovalvulas']['presenta']== 'Malo':
     hoja['G59'] = 'X'
    if JSONobservations_and_results['estadovalvulas']['presenta'] == 'N/A':
     hoja['H59'] = 'X'
    if JSONobservations_and_results['estadovalvulas']['cumple'] == True:
     hoja['O59'] = 'X'
    else:
      hoja['P59'] = 'X'
    #estadovalvulasalivio
    if JSONobservations_and_results['estadovalvulasalivio']['presenta']== 'Bueno':
     hoja['F60'] = 'X'
    if JSONobservations_and_results['estadovalvulasalivio']['presenta']== 'Malo':
     hoja['G60'] = 'X'
    if JSONobservations_and_results['estadovalvulasalivio']['presenta'] == 'N/A':
     hoja['H60'] = 'X'
    if JSONobservations_and_results['estadovalvulasalivio']['cumple'] == True:
     hoja['O60'] = 'X'
    else:
      hoja['P60'] = 'X'
    #estadoindicadornivel
    if JSONobservations_and_results['estadoindicadornivel']['presenta']== 'Bueno':
     hoja['F61'] = 'X'
    if JSONobservations_and_results['estadoindicadornivel']['presenta']== 'Malo':
     hoja['G61'] = 'X'
    if JSONobservations_and_results['estadoindicadornivel']['presenta'] == 'N/A':
     hoja['H61'] = 'X'
    if JSONobservations_and_results['estadoindicadornivel']['cumple'] == True:
     hoja['O61'] = 'X'
    else:
      hoja['P61'] = 'X'
    #conclusiones
    hoja['A64'] = JSONobservations_and_results['observacionesConclusiones']
    #Revision Stiker
    hoja['J69'] = JSONquestions_mtto['numeroSticker']
    if JSONquestions_mtto['ensayoNoDestructivo'] == True:
     hoja['G70'] = 'X'
    else:
      hoja['I70'] = JSONquestions_mtto['cuales']
    #evidencia foto video otro
    if JSONquestions_mtto['fotografia'] == True:
     hoja['K71'] = 'X'
    if JSONquestions_mtto['video'] == True:
     hoja['M71'] = 'X'
    if JSONquestions_mtto['otros1'] == True:
     hoja['O71'] = 'X'
   

    #registro fotografico
    #placa
    routeFotoPlaca =JSONphotos['placadeidentificacion']    
    response = requests.get(routeFotoPlaca)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = 550 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = 275  # Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
   
    print(img.width)
    print(img.height)
    hoja2.add_image(img, 'B11')  # Agregar la imagen en la celda A1 o en la celda que desees 

    #tanque 
    routeFotoTanque =JSONphotos['tanqueentero']    
    response = requests.get(routeFotoTanque)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = 550 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = 275  # Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
    
    hoja2.add_image(img, 'J11')  # Agregar la imagen en la celda A1 o en la celda que desees 

    #stiker 
    #hoja2['A26'] = JSONphotos['stickerinstalado']

    routeFotoStiker =JSONphotos['stickerinstalado']    
    response = requests.get(routeFotoStiker)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = 550 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = 275  # Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
    
    hoja2.add_image(img, 'B27')


  
    #acsesorios 
    routeFotoAcsesorio =JSONphotos['accesoriosenpruebadehermeticidad']    
    response = requests.get(routeFotoAcsesorio)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = 550 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = 275  # Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
    
    hoja2.add_image(img, 'J27')  # Agregar la imagen en la celda A1 o en la celda que desees 

    routeFotoDefectorechazo =JSONphotos['defectologiaderechazo']    
    response = requests.get(routeFotoDefectorechazo)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = 550 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = 275  # Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
    
    hoja2.add_image(img, 'F43')  # Agregar la imagen en la celda A1 o en la celda que desees 

    #defectologia y defectos encointrados 
    #hoja2['A43'] = JSONphotos['defectologiaderechazo']

    routeFotoDefecto =JSONphotos['defectosencontradosenlainspeccion']    
    response = requests.get(routeFotoDefecto)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = 400 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = 200  # Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
    
    hoja2.add_image(img, 'G60')  # Agregar la imagen en la celda A1 o en la celda que desees 

    #hoja2['A60'] = JSONphotos['defectosencontradosenlainspeccion']

    #firma
    routeFirmaUsuario =JSONsignatures['firmaUsuario']
    response = requests.get(routeFirmaUsuario)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = img.width / 0.5 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = img.height * 0.3  # Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
    
    hoja.add_image(img, 'J73')  # Agregar la imagen en la celda A1 o en la celda que desees
    
    #firma instructor
    routeFirmaInstructor =JSONsignatures['firmaInspector']
    response = requests.get(routeFirmaInstructor)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = img.width / 2 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = img.height * 0.3  # Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
    
    hoja.add_image(img, 'E73')  # Agregar la imagen en la celda A1 o en la celda que desees
    
   
    # Convertir la hoja de cálculo a un DataFrame de pandas
    df = pd.DataFrame(hoja.values, columns=[col[0].value for col in hoja.iter_cols()])

    # Crear un objeto BytesIO para almacenar la salida del archivo PDF
    pdf_output = BytesIO()

    # Crear un objeto PdfPages de matplotlib
    pdf_pages = matplotlib.backends.backend_pdf.PdfPages(pdf_output)

    # Tabular el DataFrame y agregarlo al PDF
    fig, ax = plt.subplots()
    ax.axis('off')  # Desactivar los ejes
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

    pdf_pages.savefig(fig, bbox_inches='tight', pad_inches=0.1)
    pdf_pages.close()

    # Hacer que BytesIO esté listo para ser leído
    pdf_output.seek(0)

    # Hacer algo con el PDF, por ejemplo, ofrecerlo para su descarga
    # En este ejemplo, simplemente imprimiré el contenido del PDF
    
    pdf_output.read()

    # Guardar el archivo Excel editado en un nuevo archivo
    workbook.save(f'reports/nuevo_archivo_editado{id}.xlsx')
    # Offer the PDF file for download    
    input_excel =  f'reports/nuevo_archivo_editado{id}.xlsx' 
    output_pdf = f'reports/nuevo_archivo_editado{id}.pdf'
    
    # Comando para convertir Excel a PDF en Windows
    if platform.system() == 'Windows':
      cmd = f"start /wait soffice --headless --convert-to pdf {input_excel} --outdir {output_pdf}"
      subprocess.run(cmd, shell=True)
    else:
     os.system(f"libreoffice --headless --convert-to pdf {input_excel} --outdir {output_pdf}")  
    # Obtener el nombre del archivo PDF creado
    pdf_filename = os.path.splitext(os.path.basename(input_excel))[0] + ".pdf"
    # Construir la ruta completa al archivo PDF
    pdf_path = os.path.join(output_pdf, pdf_filename)
    return pdf_path
    
