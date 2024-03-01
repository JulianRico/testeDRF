import json
from django.conf import settings
from django.http import HttpResponse
import requests
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
import requests
#instalar el libreoffice por comando en la maquina
import platform
import os
import subprocess


def GeneratePDFintoSVGMovil(questions_mtto, question_views, questions_deterioration, tank_identification,
                       observations_and_results, signatures, photos, fecha_convertida,  companie,  id, aprobado):

    JSONquestions_mtto = json.loads(questions_mtto)
    JSONquestion_views = json.loads(question_views)
    JSONquestions_deterioration = json.loads(questions_deterioration)
    JSONtank_identification = json.loads(tank_identification)
    JSONobservations_and_results =    json.loads(observations_and_results)
    JSONsignatures = json.loads(signatures)
    JSONphotos = json.loads(photos)  
                    
    print(companie)
    workbook = openpyxl.load_workbook('reports/tpMovil.xlsx')    

    # Obtener la hoja de trabajo (puedes ajustar esto según tu necesidad)
    hoja = workbook['SGQC-PGT-FT-06']
    hoja2= workbook['REGISTRO FOTOGRAFICO']
    #datos usuario
    hoja['D9'] = fecha_convertida
    hoja['O5'] = id
    hoja2['O5']= id
    hoja['C10'] = companie[1]
    hoja['C11'] = companie[2]
    hoja['C12'] = companie[5]
    hoja['K71'] = companie[5]    
    hoja['C14'] = companie[3]
    hoja['C15'] = companie[6]
    hoja['C13'] = companie[4]
    hoja['F71'] = companie[0]
    
    #revision 
    if aprobado == True:
      hoja['F63'] = 'X'
    else:
      hoja['M63'] = 'X'    
    hoja['I63']=JSONquestions_mtto['numeroSticker']
    hoja['I64']=JSONquestions_mtto['cuales']
    if JSONquestions_mtto['ensayoNoDestructivo'] == True:
     hoja['G64'] = 'X'    
    if JSONquestions_mtto['fotografia'] == True:
     hoja['J65'] = 'X'
    if JSONquestions_mtto['fotografia'] == None:
     hoja['N65'] = 'X'
    hoja['C67']=JSONquestions_mtto['serieEquiposUtilizados1']
    hoja['C68'] =JSONquestions_mtto['serieEquiposUtilizados2'] 
      
    if JSONquestions_mtto['serieEquiposUtilizados3'] != None:
     hoja['C69'] = 'X'
    if JSONquestions_mtto['serieEquiposUtilizados4'] != None:
     hoja['C70'] = 'X'
    if JSONquestions_mtto['serieEquiposUtilizados5'] != None:
     hoja['C71'] = 'X'
   #fajas
    if JSONquestion_views['fajasapoyo']['presenta']== 'Bueno':
     hoja['F36'] = 'X'
    if JSONquestion_views['fajasapoyo']['presenta']== 'Malo':
     hoja['G36'] = 'X'
    if JSONquestion_views['fajasapoyo']['presenta'] == 'N/A':
     hoja['H36'] = 'X'
    if JSONquestion_views['fajasapoyo']['cumple'] == True:
     hoja['O36'] = 'X'
    else:
      hoja['P36'] = 'X'
   #sobresanos
    if JSONquestion_views['sobresanos']['presenta']== 'Bueno':
     hoja['F37'] = 'X'
    if JSONquestion_views['sobresanos']['presenta']== 'Malo':
     hoja['G37'] = 'X'
    if JSONquestion_views['sobresanos']['presenta'] == 'N/A':
     hoja['H37'] = 'X'
    if JSONquestion_views['sobresanos']['cumple'] == True:
     hoja['O37'] = 'X'
    else:
      hoja['P37'] = 'X'
   #soporte
    if JSONquestion_views['soportes']['presenta']== 'Bueno':
     hoja['F38'] = 'X'
    if JSONquestion_views['soportes']['presenta']== 'Malo':
     hoja['G38'] = 'X'
    if JSONquestion_views['soportes']['presenta'] == 'N/A':
     hoja['H38'] = 'X'
    if JSONquestion_views['soportes']['cumple'] == True:
     hoja['O38'] = 'X'
    else:
      hoja['P38'] = 'X'

   #revision de accesorios
   #valbulas globo 
    if JSONquestions_deterioration['valvulasglobo']['presenta']=='Bueno':
     hoja['F40'] ='X' 
    if JSONquestions_deterioration['valvulasglobo']['presenta']=='Regular':
     hoja['G40'] ='X' 
    if JSONquestions_deterioration['valvulasglobo']['presenta']=='Malo':
     hoja['H40'] ='X' 
    if JSONquestions_deterioration['valvulasglobo']['cumple']==True:
      hoja['O40']='X'
    else:
      hoja['P40']='X'
    #valbulas interna
    if JSONquestions_deterioration['valvulasinternas']['presenta']=='Bueno':
     hoja['F41'] ='X' 
    if JSONquestions_deterioration['valvulasinternas']['presenta']=='Regular':
     hoja['G41'] ='X' 
    if JSONquestions_deterioration['valvulasinternas']['presenta']=='Malo':
     hoja['H41'] ='X' 
    if JSONquestions_deterioration['valvulasinternas']['cumple']==True:
      hoja['O41']='X'
    else:
      hoja['P41']='X'
    #manometro
    if JSONquestions_deterioration['manometro']['presenta']=='Bueno':
     hoja['F42'] ='X' 
    if JSONquestions_deterioration['manometro']['presenta']=='Regular':
     hoja['G42'] ='X' 
    if JSONquestions_deterioration['manometro']['presenta']=='Malo':
     hoja['H42'] ='X' 
    if JSONquestions_deterioration['manometro']['cumple']==True:
      hoja['O42']='X'
    else:
      hoja['P42']='X'
    #termometro
    if JSONquestions_deterioration['termometro']['presenta']=='Bueno':
     hoja['F43'] ='X' 
    if JSONquestions_deterioration['termometro']['presenta']=='Malo':
     hoja['G43'] ='X' 
    if JSONquestions_deterioration['termometro']['presenta']=='Regular':
     hoja['H43'] ='X' 
    if JSONquestions_deterioration['termometro']['cumple']==True:
      hoja['O43']='X'
    else:
      hoja['P43']='X'
    #nivel
    if JSONquestions_deterioration['indicadornivel']['presenta']=='Bueno':
     hoja['F44'] ='X' 
    if JSONquestions_deterioration['indicadornivel']['presenta']=='Malo':
     hoja['G44'] ='X' 
    if JSONquestions_deterioration['indicadornivel']['presenta']=='Regular':
     hoja['H44'] ='X' 
    if JSONquestions_deterioration['indicadornivel']['cumple']==True:
      hoja['O44']='X'
    else:
      hoja['P44']='X'
    #magage
    if JSONquestions_deterioration['manholle']['presenta']=='Bueno':
     hoja['F45'] ='X' 
    if JSONquestions_deterioration['manholle']['presenta']=='Malo':
     hoja['G45'] ='X' 
    if JSONquestions_deterioration['manholle']['presenta']=='Regular':
     hoja['H45'] ='X' 
    if JSONquestions_deterioration['manholle']['cumple']==True:
      hoja['O45']='X'
    else:
      hoja['P45']='X'
    #requisitos
    #inicio
    hoja['M13']=JSONtank_identification['placa']
    hoja['M14']=JSONtank_identification['capacidadNominal']
    hoja['M15']=JSONtank_identification['fabricante']
    hoja['M16']=JSONtank_identification['numeroSerie']
    if JSONtank_identification['tipoTanque']=='Carrotanque':
      hoja['P10']='X'
    else:
      hoja['P11']='X'
    #valbula alivio
    if JSONtank_identification['valvulaAlivio']['presenta']=='SÍ':
     hoja['F19'] ='X' 
    if JSONtank_identification['valvulaAlivio']['presenta']=='NO':
     hoja['G19'] ='X' 
    if JSONtank_identification['valvulaAlivio']['presenta']=='N/A':
     hoja['H19'] ='X' 
     hoja['K19'] =JSONtank_identification['valvulaAlivio']['cantidad']
     hoja['N19'] =JSONtank_identification['valvulaAlivio']['fechaFabricacion']
    if JSONtank_identification['valvulaAlivio']['cumple']==True:
      hoja['O19']='X'
    else:
      hoja['P19']='X'
   #hermeticidad
    if JSONtank_identification['hermeticidad']['presenta']=='SÍ':
     hoja['F20'] ='X' 
    if JSONtank_identification['hermeticidad']['presenta']=='NO':
     hoja['G20'] ='X' 
    if JSONtank_identification['hermeticidad']['presenta']=='N/A':
     hoja['H20'] ='X' 
    if JSONtank_identification['hermeticidad']['defectologia']==True:
      hoja['K20']='X'
      hoja['N20']='X'
    if JSONtank_identification['hermeticidad']['cumple']==True:
      hoja['O20']='X'
    else:
      hoja['P20']='X'
    #agrietamiento 
    if JSONtank_identification['agrietamiento']['presenta']=='SÍ':
     hoja['F21'] ='X' 
    if JSONtank_identification['agrietamiento']['presenta']=='NO':
     hoja['G21'] ='X' 
    if JSONtank_identification['agrietamiento']['presenta']=='N/A':
     hoja['H21'] ='X' 
    if JSONtank_identification['agrietamiento']['cumple']==True:
      hoja['O21']='X'
    else:
      hoja['P21']='X'
    #porosidad
    if JSONtank_identification['porosidad']['presenta']=='SÍ':
     hoja['F22'] ='X' 
    if JSONtank_identification['porosidad']['presenta']=='NO':
     hoja['G22'] ='X' 
    if JSONtank_identification['porosidad']['presenta']=='N/A':
     hoja['H22'] ='X' 
    if JSONtank_identification['porosidad']['cumple']==True:
      hoja['O22']='X'
    else:
      hoja['P22']='X'
    #salpicadura
    if JSONtank_identification['salpicadura']['presenta']=='SÍ':
     hoja['F23'] ='X'
     hoja['P23'] ='X'
    if JSONtank_identification['salpicadura']['presenta']=='NO':
     hoja['G23'] ='X'
     hoja['O23'] ='X'
    if JSONtank_identification['salpicadura']['presenta']=='NA':
     hoja['H23'] ='X'
   
    #socavado
    if JSONtank_identification['socavado']['presenta']=='SÍ':
     hoja['F24'] ='X'
     hoja['P24'] ='X'
    if JSONtank_identification['socavado']['presenta']=='NO':
     hoja['G24'] ='X'
     hoja['O24'] ='X'
    if JSONtank_identification['socavado']['presenta']=='N/A':
     hoja['H24'] ='X'

    #abolladura
    if JSONtank_identification['abolladura']['presenta']=='SÍ':
     hoja['F25'] ='X'
     hoja['P25'] ='X'
    if JSONtank_identification['abolladura']['presenta']=='NO':
     hoja['G25'] ='X'
     hoja['O25'] ='X'
    if JSONtank_identification['abolladura']['presenta']=='N/A':
     hoja['H25'] ='X'

    #hinchamiento
    if JSONtank_identification['hinchamiento']['presenta']=='SÍ':
     hoja['F26'] ='X'
     hoja['P26'] ='X'
    if JSONtank_identification['hinchamiento']['presenta']=='NO':
     hoja['G26'] ='X'
     hoja['O26'] ='X'
    if JSONtank_identification['hinchamiento']['presenta']=='N/A':
     hoja['H26'] ='X'

    #hendidura
    if JSONtank_identification['hendiduras']['presenta']=='SÍ':
     hoja['F27'] ='X'
     hoja['P27'] ='X'
    if JSONtank_identification['hendiduras']['presenta']=='NO':
     hoja['G27'] ='X'
     hoja['O27'] ='X'
    if JSONtank_identification['hendiduras']['presenta']=='N/A':
     hoja['H27'] ='X'

    #corrosion
    if JSONtank_identification['corrosion']['presenta']=='SÍ':
     hoja['F28'] ='X'
     hoja['P28'] ='X'
    if JSONtank_identification['corrosion']['presenta']=='NO':
     hoja['G28'] ='X'
     hoja['O28'] ='X'
    if JSONtank_identification['corrosion']['presenta']=='N/A':
     hoja['H28'] ='X'

    #resane
    if JSONtank_identification['resane']['presenta']=='SÍ':
     hoja['F29'] ='X'
     hoja['P29'] ='X'
    if JSONtank_identification['resane']['presenta']=='NO':
     hoja['G29'] ='X'
     hoja['O29'] ='X'
    if JSONtank_identification['resane']['presenta']=='N/A':
     hoja['H29'] ='X'

    #polimeres
    if JSONtank_identification['polimeros']['presenta']=='SÍ':
     hoja['F30'] ='X'
     hoja['P30'] ='X'
    if JSONtank_identification['polimeros']['presenta']=='NO':
     hoja['G30'] ='X'
     hoja['O30'] ='X'
    if JSONtank_identification['polimeros']['presenta']=='N/A':
     hoja['H30'] ='X'

    #estado corrosion
    if JSONtank_identification['EstadoConexionCorrosion']['presenta']=='SÍ':
     hoja['F31'] ='X'
     hoja['P31'] ='X'
    if JSONtank_identification['EstadoConexionCorrosion']['presenta']=='NO':
     hoja['G31'] ='X'
     hoja['O31'] ='X'
    if JSONtank_identification['EstadoConexionCorrosion']['presenta']=='N/A':
     hoja['H31'] ='X'

    #estado evidencia
    if JSONtank_identification['EstadoConexionEvidenciaGolpes']['presenta']=='SÍ':
     hoja['F32'] ='X'
     hoja['P32'] ='X'
    if JSONtank_identification['EstadoConexionEvidenciaGolpes']['presenta']=='NO':
     hoja['G32'] ='X'
     hoja['O32'] ='X'
    if JSONtank_identification['EstadoConexionEvidenciaGolpes']['presenta']=='N/A':
     hoja['H32'] ='X'
    #estado desgaste
    if JSONtank_identification['EstadoConexionDesgaste']['presenta']=='SÍ':
     hoja['F33'] ='X' 
    if JSONtank_identification['EstadoConexionDesgaste']['presenta']=='NO':
     hoja['G33'] ='X' 
    if JSONtank_identification['EstadoConexionDesgaste']['presenta']=='N/A':
     hoja['H33'] ='X' 
    if JSONtank_identification['EstadoConexionDesgaste']['cumple']==True:
      hoja['O33']='X'
    else:
      hoja['P33']='X'
    #otros
    if JSONtank_identification['EstadoConexionOtros']['presenta']=='SÍ':
     hoja['F34'] ='X' 
    if JSONtank_identification['EstadoConexionOtros']['presenta']=='NO':
     hoja['G34'] ='X' 
    if JSONtank_identification['EstadoConexionOtros']['presenta']=='N/A':
     hoja['H34'] ='X' 
    if JSONtank_identification['EstadoConexionOtros']['cumple']==True:
      hoja['O34']='X'
    else:
      hoja['P34']='X'
    #revision visual 
    #soldadura
    if JSONobservations_and_results['soldadura']['presenta']=='SÍ':
     hoja['F47'] ='X' 
    if JSONobservations_and_results['soldadura']['presenta']=='No':
     hoja['G47'] ='X' 
    if JSONobservations_and_results['soldadura']['presenta']=='N/A':
     hoja['H47'] ='X' 
    if JSONobservations_and_results['soldadura']['cumple']==True:
      hoja['O47']='X'
    else:
      hoja['P47']='X'
    #corrocion
    if JSONobservations_and_results['corrosion']['presenta']=='SÍ':
     hoja['F4'] ='X' 
    if JSONobservations_and_results['corrosion']['presenta']=='No':
     hoja['G48'] ='X' 
    if JSONobservations_and_results['corrosion']['presenta']=='N/A':
     hoja['H48'] ='X' 
    if JSONobservations_and_results['corrosion']['cumple']==True:
      hoja['O48']='X'
    else:
      hoja['P48']='X'  
    #escape 
    if JSONobservations_and_results['fisurasoescape']['presenta']=='SÍ':
     hoja['F49'] ='X' 
    if JSONobservations_and_results['fisurasoescape']['presenta']=='No':
     hoja['G49'] ='X' 
    if JSONobservations_and_results['fisurasoescape']['presenta']=='N/A':
     hoja['H49'] ='X' 
    if JSONobservations_and_results['fisurasoescape']['cumple']==True:
      hoja['O49']='X'
    else:
      hoja['P49']='X'
    #estado roscas
    if JSONobservations_and_results['roscas']['presenta']=='SÍ':
     hoja['F50'] ='X' 
    if JSONobservations_and_results['roscas']['presenta']=='No':
     hoja['G50'] ='X' 
    if JSONobservations_and_results['roscas']['presenta']=='N/A':
     hoja['H50'] ='X' 
    if JSONobservations_and_results['roscas']['cumple']==True:
      hoja['O50']='X'
    else:
      hoja['P50']='X'
    #dobleces
    if JSONobservations_and_results['aplastamiento']['presenta']=='SÍ':
     hoja['F51'] ='X' 
    if JSONobservations_and_results['aplastamiento']['presenta']=='No':
     hoja['G51'] ='X' 
    if JSONobservations_and_results['aplastamiento']['presenta']=='N/A':
     hoja['H51'] ='X' 
    if JSONobservations_and_results['aplastamiento']['cumple']==True:
      hoja['O51']='X'
    else:
      hoja['P51']='X'
    #observaciopnes 
    hoja['A53']=JSONobservations_and_results['observacionesConclusiones']
    #firmas
    #firmaUsuario
    routeFirmaUsuario =JSONsignatures['firmaUsuario']
    response = requests.get(routeFirmaUsuario)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = img.width / 3.5 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = img.height * 0.3  # Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
    
    hoja.add_image(img, 'K67')  # Agregar la imagen en la celda A1 o en la celda que desees

    #firma inspector
    routeFirmaInspector =JSONsignatures['firmaInspector']
    response = requests.get(routeFirmaInspector)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = img.width / 3.5 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = img.height * 0.3  # Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
    
    hoja.add_image(img, 'F67')  # Agregar la imagen en la celda A1 o en la celda que desees
    
    #registro fotografico 
    #placa
    routePlaca =JSONphotos['placadeidentificacion']
    response = requests.get(routePlaca)

    image_bytes = BytesIO(response.content)
    # Cargar la imagen en la hoja de trabajo
    img = Image(image_bytes)

    img.width = 500 # Puedes ajustar el ancho de la imagen según tus necesidades
    img.height = 275 #Puedes ajustar la altura de la imagen según tus necesidades
    # firma de inspector - tamaño
    
    hoja2.add_image(img, 'B11')  # Agregar la imagen en la celda A1 o en la celda que desees

    #tanque
    routeTanque =JSONphotos['tanqueentero']
    if routeTanque:    
      response = requests.get(routeTanque)

      image_bytes = BytesIO(response.content)
      # Cargar la imagen en la hoja de trabajo
      img = Image(image_bytes)

      img.width = 500 # Puedes ajustar el ancho de la imagen según tus necesidades
      img.height = 275 #Puedes ajustar la altura de la imagen según tus necesidades
      # firma de inspector - tamaño
      
      hoja2.add_image(img, 'J11')  # Agregar la imagen en la celda A1 o en la celda que desees
    #tanque placa
    routeTanquePlaca =JSONphotos['placaCarrotanque']
    if routeTanquePlaca:
      response = requests.get(routeTanquePlaca)

      image_bytes = BytesIO(response.content)
      # Cargar la imagen en la hoja de trabajo
      img = Image(image_bytes)

      img.width = 500 # Puedes ajustar el ancho de la imagen según tus necesidades
      img.height = 275 #Puedes ajustar la altura de la imagen según tus necesidades
      # firma de inspector - tamaño
      
      hoja2.add_image(img, 'B28')  # Agregar la imagen en la celda A1 o en la celda que desees

    #accesorios
    routeAcce =JSONphotos['accesoriosenpruebadehermeticidad']
    if routeAcce:
      response = requests.get(routeAcce)

      image_bytes = BytesIO(response.content)
      # Cargar la imagen en la hoja de trabajo
      img = Image(image_bytes)

      img.width = 500 # Puedes ajustar el ancho de la imagen según tus necesidades
      img.height = 275 #Puedes ajustar la altura de la imagen según tus necesidades
      # firma de inspector - tamaño
      
      hoja2.add_image(img, 'J28')  # Agregar la imagen en la celda A1 o en la celda que desees

    #stiker
    routeStiker =JSONphotos['stickerinstalado']
    if routeStiker:
      response = requests.get(routeStiker)

      image_bytes = BytesIO(response.content)
      # Cargar la imagen en la hoja de trabajo
      img = Image(image_bytes)

      img.width = 500 # Puedes ajustar el ancho de la imagen según tus necesidades
      img.height = 275 #Puedes ajustar la altura de la imagen según tus necesidades
      # firma de inspector - tamaño
      
      hoja2.add_image(img, 'B45')  # Agregar la imagen en la celda A1 o en la celda que desees
    
    #foto defectoslogia 
    routeFdefecto =JSONphotos['defectosencontradosenlainspeccion']
    if routeFdefecto:
      response = requests.get(routeFdefecto)

      image_bytes = BytesIO(response.content)
      # Cargar la imagen en la hoja de trabajo
      img = Image(image_bytes)

      img.width = 500 # Puedes ajustar el ancho de la imagen según tus necesidades
      img.height = 275 #Puedes ajustar la altura de la imagen según tus necesidades
      # firma de inspector - tamaño
      
      hoja2.add_image(img, 'J45')  # Agregar la imagen en la celda A1 o en la celda que desees

      #defectologia
    routeFdefectore =JSONphotos['defectologiaderechazo']
    if routeFdefectore:
      response = requests.get(routeFdefectore)

      image_bytes = BytesIO(response.content)
      # Cargar la imagen en la hoja de trabajo
      img = Image(image_bytes)

      img.width = 400 # Puedes ajustar el ancho de la imagen según tus necesidades
      img.height = 200  # Puedes ajustar la altura de la imagen según tus necesidades
      hoja2.add_image(img, 'F62')


      # Guardar el archivo Excel editado en un nuevo archivo
      workbook.save(f'reports/xlxs/reporte_tanque_movil_QC_{id}.xlsx')
      # Offer the PDF file for download    
      input_excel =  f'reports/xlxs/reporte_tanque_movil_QC_{id}.xlsx' 
      output_pdf = f'reports/pdfs'
      
      # Comando para convertir Excel a PDF en Windows
      if platform.system() == 'Windows':
        cmd = f"start /wait soffice --headless --convert-to pdf {input_excel} --outdir {output_pdf}"
        subprocess.run(cmd, shell=True)          
      else:
        os.system(f"libreoffice --headless --convert-to pdf {input_excel} --outdir {output_pdf}")  
      # Obtener el nombre del archivo PDF creado
      pdf_filename = os.path.splitext(os.path.basename(input_excel))[0] + ".pdf"
      # Construir la ruta completa al archivo PDF  
      

      pdf_path = os.path.join(settings.BASE_DIR, f'reports\pdfs', pdf_filename)
      
      if os.path.exists(pdf_path):
          with open(pdf_path, 'rb') as pdf_file:
              response = HttpResponse(pdf_file.read(), content_type='application/pdf')
              response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'
              # Borrar el archivo PDF después de enviarlo como respuesta
              os.remove(input_excel)
              return {'response':response, 'path': pdf_path}
      else:
          return {'response': HttpResponse("El archivo PDF no existe", status=404)}

     
     
     
     