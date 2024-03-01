import json
from django.conf import settings
from django.http import HttpResponse
import requests
import base64
from io import BytesIO
import qrcode
from qrcode.image import svg

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


import platform
import os
import subprocess


#instalar el

def GenerateCertificatePDFintoSVG(questions_mtto, JSONquestion_views, questions_deterioration, tank_identification,
                       observations_and_results,  fecha_convertida,  companie,  id, aprobado):
   # Crear un objeto BytesIO para guardar la imagen en memoria
   print(companie)
   
   qr = qrcode.QRCode(
      version=1,  # Tamaño del código QR (1-40)
      error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores (L, M, Q, H)
      box_size=2,  # Tamaño de los cuadros en el código QR
      border=2,  # Ancho del borde blanco alrededor del código QR
   )
   data = f"https://api-qc-drf.onrender.com/api/pdfcreatecertificate/{id}/"  # Puedes cambiar esto por tu propio enlace o datos
   qr.add_data(data)   
   img = qr.make_image(fill_color="black", back_color="white")
   img.resize((20, 20))   
   # Guardar la imagen en un búfer de bytes
   buffer = BytesIO()
   img.save(buffer)

   # Obtener los datos binarios del código QR en formato SVG
   codigo_qr_svg = buffer.getvalue()
   #guarda la imagen
   
   
   JSONquestions_mtto = json.loads(questions_mtto)
   JSONquestion_views = json.loads(JSONquestion_views)
   JSONquestions_deterioration = json.loads(questions_deterioration)
   JSONtank_identification = json.loads(tank_identification)
   JSONobservations_and_results =    json.loads(observations_and_results)

   def recorridoCumple(data,nombre):
      all_valid = all(value['cumple'] == True for key, value in data.items() if nombre in key)
      return all_valid

   workbook = openpyxl.load_workbook('reports/certificadoTemplate.xlsx')   
    # Obtener la hoja de trabajo (puedes ajustar esto según tu necesidad)
   hoja = workbook['Hoja1']

    #datos iniciales
   hoja['D37'] = id
   hoja['F9'] = id
   hoja['G10'] = fecha_convertida
   hoja['C11'] = companie[1] #nombre
   
   hoja['C12'] = companie[2] #nit
   hoja['C13'] = companie[3] #ciudad
   hoja['C17'] = companie[7]
   hoja['F12'] = companie[4]
   hoja['E17'] = companie[6]
   
   
	#hoja['B38'] // codigo QR

    #datos vahiculo
   hoja['E16']=JSONtank_identification['capacidadNominal']
   hoja['G16']='X'
   hoja['H15']=JSONtank_identification['fabricante']
   hoja['F15']=JSONtank_identification['numeroSerie']
   hoja['C15']=JSONtank_identification['tipoTanque']
   

    #hermeticidad
   if JSONtank_identification['hermeticidad']['cumple']== True:
     hoja['G24'] = 'CUMPLE'
    #abolladura
   if JSONtank_identification['abolladura']['1']['cumple']== True & JSONtank_identification['abolladura']['2']['cumple']== True & JSONtank_identification['abolladura']['3']['cumple']== True:
     hoja['G25'] = 'CUMPLE'
    #abombamiento
   if JSONtank_identification['abombamiento']['cumple']== True:
     hoja['G26'] = 'CUMPLE'
    #aislada
   if JSONtank_identification['corrosionAislada']['1']['cumple']== True & JSONtank_identification['corrosionAislada']['2']['cumple']== True :
     hoja['G27'] = 'CUMPLE'
     #en linea
   if JSONtank_identification['corrosionEnLinea']['1']['cumple']== True & JSONtank_identification['corrosionEnLinea']['2']['cumple']== True & JSONtank_identification['corrosionEnLinea']['3']['cumple']== True:
    hoja['G28'] = 'CUMPLE'
    #general
   if JSONtank_identification['corrosionGeneral']['1']['cumple']== True & JSONtank_identification['corrosionGeneral']['2']['cumple']== True :
     hoja['G29'] = 'CUMPLE'
    #aacion por fuego
   if JSONtank_identification['AccionPorFuego']['1']['cumple']== True & JSONtank_identification['AccionPorFuego']['2']['cumple']== True :
     hoja['G30'] = 'CUMPLE'
    #sobresano y soporte
   if JSONquestion_views['soportetanque']['cumple']== True:
     hoja['G31'] = 'CUMPLE'
    #roscas
   if JSONquestions_deterioration['roscaencuentrabuenestado']['cumple']== True & JSONquestions_deterioration['accesoriosencuentrabuenestado']['cumple']== True:
     hoja['G32'] = 'CUMPLE'
    #JSONquestions_deterioration
   if JSONquestions_deterioration['tuberiadefectosoldadura']['cumple']== True & JSONquestions_deterioration['tuberiapresentacorrosion']['cumple']== True &  JSONquestions_deterioration['tuberiapresentafisura']['cumple']== True &  JSONquestions_deterioration['tuberiaaplastamiento']['cumple']== True:
     hoja['G33'] = 'CUMPLE'
    #nivel
   if JSONobservations_and_results['estadoindicadornivel']['cumple']== True:
     hoja['G34'] = 'CUMPLE'
    #catodica
   if JSONquestion_views['proteccioncatodica']['cumple']== True:
     hoja['G35'] = 'CUMPLE'

    # Crear un objeto BytesIO para almacenar la salida del archivo PDF
   workbook.save(f'reports/xlxs/certificado_QC_{id}.xlsx')
    # Offer the PDF file for download    
   input_excel =  f'reports/xlxs/certificado_QC_{id}.xlsx' 
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
