import json
import requests
import base64



def GeneratePDFintoSVG(questions_mtto, question_views, questions_deterioration, tank_identification,
                       observations_and_results, signatures, photos, fecha_convertida, companieuser, companie, user, id, aprobado, nombreusuario= "otro user"):
    """ print(questions_mtto)
    print(question_views)
    print(questions_deterioration)
    print(tank_identification)
    print(observations_and_results)
    print(signatures)
    print(photos)
    print(fecha_convertida) """

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

    svg_code = f"""  
<svg
   width="8.5in"
   height="14in"
   viewBox="0 0 215.9 355.6"
   version="1.1"
   id="svg5"
   xml:space="preserve"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:dc="http://purl.org/dc/elements/1.1/"><defs
     id="defs2"><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath1"><path
         d="M 0,0 H 1656.7181 V 2862.3496 H 0 Z"
         id="path10272" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath2"><path
         d="M 1.1716535,1.1716535 H 1656.7181 V 2862.3496 H 1.1716535 Z"
         id="path10275" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath3"><path
         d="m 421.79528,1448.1638 h 65.61259 v 42.1795 h -65.61259 z"
         id="path10278" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath4"><path
         d="m 421.79528,1702.4126 h 65.61259 v 42.1795 h -65.61259 z"
         id="path10281" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath6"><path
         d="M 1.1716535,2135.9244 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10287" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath9"><path
         d="M 1.1716535,2549.5181 H 274.16693 v 24.6047 H 1.1716535 Z"
         id="path10296" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath10"><path
         d="M 1.1716535,2575.2945 H 274.16693 v 24.6047 H 1.1716535 Z"
         id="path10299" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath11"><path
         d="M 1.1716535,2601.0709 H 274.16693 v 24.6047 H 1.1716535 Z"
         id="path10302" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath12"><path
         d="M 1.1716535,2360.8819 H 224.95748 v 24.6047 H 1.1716535 Z"
         id="path10305" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath13"><path
         d="M 1.1716535,2626.8472 H 274.16693 v 24.6048 H 1.1716535 Z"
         id="path10308" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath14"><path
         d="M 1.1716535,2386.6583 H 420.62362 v 37.4929 H 1.1716535 Z"
         id="path10311" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath15"><path
         d="M 1.1716535,2652.6236 H 1655.5465 V 2861.178 H 1.1716535 Z"
         id="path10314" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath16"><path
         d="M 1.1716535,2497.9654 H 274.16693 v 24.6047 H 1.1716535 Z"
         id="path10317" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath19"><path
         d="M 1.1716535,2523.7417 H 274.16693 v 24.6048 H 1.1716535 Z"
         id="path10326" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath20"><path
         d="M 1.1716535,2005.8709 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10329" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath22"><path
         d="M 1.1716535,2049.222 H 353.83937 v 42.1796 H 1.1716535 Z"
         id="path10335" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath24"><path
         d="M 1.1716535,2092.5732 H 353.83937 v 42.1796 H 1.1716535 Z"
         id="path10341" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath26"><path
         d="M 1.1716535,2425.3228 H 1655.5465 v 37.4929 H 1.1716535 Z"
         id="path10347" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath27"><path
         d="M 1.1716535,2463.9874 H 274.16693 v 32.8063 H 1.1716535 Z"
         id="path10350" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath28"><path
         d="m 275.33858,2463.9874 h 422.96693 v 32.8063 H 275.33858 Z"
         id="path10353" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath29"><path
         d="m 699.47717,2463.9874 h 956.06933 v 32.8063 H 699.47717 Z"
         id="path10356" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath30"><path
         d="M 1.1716535,2179.2756 H 1655.5465 v 39.8362 H 1.1716535 Z"
         id="path10359" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath31"><path
         d="M 1.1716535,2220.2835 H 1655.5465 v 22.2614 H 1.1716535 Z"
         id="path10362" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath33"><path
         d="M 1.1716535,2337.4488 H 1655.5465 v 22.2614 H 1.1716535 Z"
         id="path10368" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath34"><path
         d="m 226.12913,2360.8819 h 127.71024 v 24.6047 H 226.12913 Z"
         id="path10371" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath35"><path
         d="m 421.79528,2360.8819 h 276.51023 v 24.6047 H 421.79528 Z"
         id="path10374" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath36"><path
         d="m 843.59055,2360.8819 h 287.05515 v 24.6047 H 843.59055 Z"
         id="path10377" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath38"><path
         d="M 1.1716535,1832.4661 H 353.83937 v 42.1796 H 1.1716535 Z"
         id="path10383" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath40"><path
         d="M 1.1716535,1962.5197 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10389" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath42"><path
         d="M 1.1716535,1919.1685 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10395" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath44"><path
         d="M 1.1716535,1875.8173 H 353.83937 v 42.1796 H 1.1716535 Z"
         id="path10401" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath46"><path
         d="M 1.1716535,1702.4126 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10407" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath48"><path
         d="M 1.1716535,1745.7638 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10413" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath50"><path
         d="M 1.1716535,1789.115 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10419" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath53"><path
         d="M 1.1716535,1596.9638 H 133.5685 v 104.2771 H 1.1716535 Z"
         id="path10428" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath54"><path
         d="m 134.74016,1596.9638 h 219.09921 v 33.9779 H 134.74016 Z"
         id="path10431" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath56"><path
         d="m 134.74016,1632.1134 h 219.09921 v 33.9779 H 134.74016 Z"
         id="path10437" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath58"><path
         d="m 134.74016,1667.263 h 219.09921 v 33.9779 H 134.74016 Z"
         id="path10443" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath60"><path
         d="m 134.74016,1404.8126 h 219.09921 v 42.1795 H 134.74016 Z"
         id="path10449" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath62"><path
         d="M 1.1716535,1448.1638 H 353.83937 v 42.1795 H 1.1716535 Z"
         id="path10455" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath63"><path
         d="M 555.36378,1448.1638 H 1655.5465 v 42.1795 H 555.36378 Z"
         id="path10458" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath64"><path
         d="M 1.1716535,1491.515 H 133.5685 v 104.2771 H 1.1716535 Z"
         id="path10461" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath65"><path
         d="m 134.74016,1491.515 h 219.09921 v 33.9779 H 134.74016 Z"
         id="path10464" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath67"><path
         d="m 134.74016,1526.6646 h 219.09921 v 33.9779 H 134.74016 Z"
         id="path10470" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath69"><path
         d="m 134.74016,1561.8142 h 219.09921 v 33.9779 H 134.74016 Z"
         id="path10476" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath70"><path
         d="M 1.1716535,1231.4079 H 133.5685 v 42.1795 H 1.1716535 Z"
         id="path10479" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath71"><path
         d="m 134.74016,1231.4079 h 219.09921 v 42.1795 H 134.74016 Z"
         id="path10482" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath72"><path
         d="m 555.36378,1231.4079 h 863.50862 v 42.1795 H 555.36378 Z"
         id="path10485" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath73"><path
         d="M 1.1716535,1274.7591 H 133.5685 v 172.233 H 1.1716535 Z"
         id="path10488" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath74"><path
         d="m 134.74016,1274.7591 h 219.09921 v 42.1795 H 134.74016 Z"
         id="path10491" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath76"><path
         d="m 134.74016,1318.1102 h 219.09921 v 42.1796 H 134.74016 Z"
         id="path10497" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath78"><path
         d="m 134.74016,1361.4614 h 219.09921 v 42.1795 H 134.74016 Z"
         id="path10503" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath80"><path
         d="M 1.1716535,1033.3984 H 353.83937 v 42.1796 H 1.1716535 Z"
         id="path10509" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath81"><path
         d="m 555.36378,1033.3984 h 863.50862 v 42.1796 H 555.36378 Z"
         id="path10512" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath82"><path
         d="M 1.1716535,1076.7496 H 133.5685 v 153.4866 H 1.1716535 Z"
         id="path10515" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath83"><path
         d="m 134.74016,1076.7496 h 219.09921 v 42.1795 H 134.74016 Z"
         id="path10518" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath84"><path
         d="m 555.36378,1076.7496 h 863.50862 v 42.1795 H 555.36378 Z"
         id="path10521" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath85"><path
         d="m 134.74016,1120.1008 h 219.09921 v 66.7842 H 134.74016 Z"
         id="path10524" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath86"><path
         d="m 555.36378,1120.1008 h 863.50862 v 66.7842 H 555.36378 Z"
         id="path10527" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath87"><path
         d="m 134.74016,1188.0567 h 219.09921 v 42.1795 H 134.74016 Z"
         id="path10530" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath88"><path
         d="m 555.36378,1188.0567 h 863.50862 v 42.1795 H 555.36378 Z"
         id="path10533" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath89"><path
         d="m 134.74016,859.9937 h 219.09921 v 42.17953 H 134.74016 Z"
         id="path10536" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath91"><path
         d="M 1.1716535,903.34488 H 353.83937 V 1032.2268 H 1.1716535 Z"
         id="path10542" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath92"><path
         d="m 555.36378,903.34488 h 863.50862 v 42.17953 H 555.36378 Z"
         id="path10545" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath93"><path
         d="m 555.36378,946.69606 h 863.50862 v 42.17953 H 555.36378 Z"
         id="path10548" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath94"><path
         d="m 555.36378,990.04724 h 863.50862 v 42.17956 H 555.36378 Z"
         id="path10551" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath95"><path
         d="M 1.1716535,686.58898 H 133.5685 V 728.7685 H 1.1716535 Z"
         id="path10554" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath96"><path
         d="M 134.74016,686.58898 H 353.83937 V 728.7685 H 134.74016 Z"
         id="path10557" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath97"><path
         d="M 555.36378,686.58898 H 1418.8724 V 728.7685 H 555.36378 Z"
         id="path10560" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath98"><path
         d="M 1.1716535,729.94016 H 133.5685 V 902.17323 H 1.1716535 Z"
         id="path10563" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath99"><path
         d="m 134.74016,729.94016 h 219.09921 v 42.17953 H 134.74016 Z"
         id="path10566" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath101"><path
         d="m 134.74016,773.29134 h 219.09921 v 42.17953 H 134.74016 Z"
         id="path10572" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath103"><path
         d="m 134.74016,816.64252 h 219.09921 v 42.17953 H 134.74016 Z"
         id="path10578" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath104"><path
         d="m 555.36378,816.64252 h 863.50862 v 42.17953 H 555.36378 Z"
         id="path10581" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath105"><path
         d="M 1.1716535,619.80472 H 224.95748 V 645.5811 H 1.1716535 Z"
         id="path10584" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath106"><path
         d="M 226.12913,619.80472 H 1655.5465 V 645.5811 H 226.12913 Z"
         id="path10587" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath107"><path
         d="M 1.1716535,646.75276 H 353.83937 v 38.66456 H 1.1716535 Z"
         id="path10590" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath108"><path
         d="m 355.01102,646.75276 h 199.18111 v 18.74645 H 355.01102 Z"
         id="path10593" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath109"><path
         d="m 555.36378,646.75276 h 863.50862 v 38.66456 H 555.36378 Z"
         id="path10596" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath110"><path
         d="m 1420.0441,646.75276 h 117.1653 v 38.66456 h -117.1653 z"
         id="path10599" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath111"><path
         d="m 1538.3811,646.75276 h 117.1654 v 38.66456 h -117.1654 z"
         id="path10602" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath114"><path
         d="m 843.59055,351.49606 h 811.95595 v 43.35118 H 843.59055 Z"
         id="path10611" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath115"><path
         d="M 1.1716535,440.54173 H 133.5685 v 43.35118 H 1.1716535 Z"
         id="path10614" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath116"><path
         d="M 1.1716535,485.06457 H 133.5685 v 43.35118 H 1.1716535 Z"
         id="path10617" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath117"><path
         d="M 1.1716535,592.85669 H 133.5685 v 25.77638 H 1.1716535 Z"
         id="path10620" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath118"><path
         d="m 275.33858,592.85669 h 145.28504 v 25.77638 H 275.33858 Z"
         id="path10623" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath119"><path
         d="m 488.57953,592.85669 h 209.72598 v 25.77638 H 488.57953 Z"
         id="path10626" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath120"><path
         d="m 843.59055,592.85669 h 287.05515 v 25.77638 H 843.59055 Z"
         id="path10629" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath123"><path
         d="M 488.57953,1.1716535 H 1274.7591 V 30.462992 H 488.57953 Z"
         id="path10638" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath124"><path
         d="M 488.57953,31.634646 H 1274.7591 V 50.381102 H 488.57953 Z"
         id="path10641" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath125"><path
         d="M 488.57953,51.552756 H 1274.7591 V 73.814173 H 488.57953 Z"
         id="path10644" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath126"><path
         d="M 488.57953,74.985827 H 1274.7591 V 97.247244 H 488.57953 Z"
         id="path10647" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath127"><path
         d="m 1275.9307,1.1716535 h 379.6158 V 30.462992 h -379.6158 z"
         id="path10650" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath128"><path
         d="m 1275.9307,31.634646 h 379.6158 v 18.746456 h -379.6158 z"
         id="path10653" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath129"><path
         d="m 1275.9307,51.552756 h 379.6158 v 22.261417 h -379.6158 z"
         id="path10656" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath130"><path
         d="m 1275.9307,74.985827 h 379.6158 v 45.694483 h -379.6158 z"
         id="path10659" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath131"><path
         d="M 488.57953,98.418898 H 1274.7591 V 120.68031 H 488.57953 Z"
         id="path10662" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath132"><path
         d="M 1.1716535,529.5874 H 1655.5465 v 30.46299 H 1.1716535 Z"
         id="path10665" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath133"><path
         d="M 1.1716535,561.22205 H 133.5685 v 30.46299 H 1.1716535 Z"
         id="path10668" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath134"><path
         d="m 421.79528,561.22205 h 276.51023 v 30.46299 H 421.79528 Z"
         id="path10671" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath136"><path
         d="m 1420.0441,396.0189 h 235.5024 v 43.35118 h -235.5024 z"
         id="path10677" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath137"><path
         d="m 843.59055,396.0189 h 287.05515 v 43.35118 H 843.59055 Z"
         id="path10680" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath138"><path
         d="m 843.59055,485.06457 h 287.05515 v 43.35118 H 843.59055 Z"
         id="path10683" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath139"><path
         d="M 1.1716535,306.97323 H 133.5685 v 43.35118 H 1.1716535 Z"
         id="path10686" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath140"><path
         d="M 1.1716535,351.49606 H 133.5685 v 43.35118 H 1.1716535 Z"
         id="path10689" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath141"><path
         d="M 1.1716535,396.0189 H 133.5685 v 43.35118 H 1.1716535 Z"
         id="path10692" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath143"><path
         d="m 843.59055,440.54173 h 287.05515 v 43.35118 H 843.59055 Z"
         id="path10698" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath145"><path
         d="M 1.1716535,212.06929 H 554.19213 V 249.5622 H 1.1716535 Z"
         id="path10704" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath146"><path
         d="M 1.1716535,145.28504 H 1655.5465 v 28.11968 H 1.1716535 Z"
         id="path10707" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath147"><path
         d="M 1.1716535,174.57638 H 1655.5465 v 36.32126 H 1.1716535 Z"
         id="path10710" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath148"><path
         d="M 555.36378,212.06929 H 1655.5465 V 249.5622 H 555.36378 Z"
         id="path10713" /></clipPath><clipPath
       clipPathUnits="userSpaceOnUse"
       id="clipEmfPath149"><path
         d="M 1.1716535,250.73386 H 133.5685 v 55.06771 H 1.1716535 Z"
         id="path10716" /></clipPath></defs><g
     id="layer1"
     style="display:inline"><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 224.95748,560.05039 h 50.3811 v 32.8063 h -50.3811 z"
       id="path10739"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 353.83937,560.05039 h 67.95591 v 32.8063 h -67.95591 z"
       id="path10741"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="72.520256"
       id="text30644-9"><tspan
         id="tspan30642-9"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="72.520256">{ 'X' if JSONtank_identification['ubicacion'] == "In-situ" else "" }</tspan></text><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 842.4189,560.05039 h 145.28504 v 32.8063 H 842.4189 Z"
       id="path10743"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="118.51374"
       y="72.430695"
       id="text30644-5"><tspan
         id="tspan30642-90"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="118.51374"
         y="72.430695">{ 'X' if JSONtank_identification['revision'] == "1 Vez" else "" }</tspan></text><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 1130.6457,560.05039 h 145.285 v 32.8063 h -145.285 z"
       id="path10745"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="156.31049"
       y="72.341133"
       id="text30644-2"><tspan
         id="tspan30642-79"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="156.31049"
         y="72.341133">{ 'X' if JSONtank_identification['revision'] == "2 Vez" else "" }</tspan></text><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 224.95748,591.68504 h 50.3811 v 28.11968 h -50.3811 z"
       id="path10747"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="31.464067"
       y="76.304413"
       id="text30644-1"><tspan
         id="tspan30642-0"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="31.464067"
         y="76.304413"> { 'X' if JSONtank_identification['tipoTanque'] == "Vertical" else "" } </tspan></text><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 420.62362,591.68504 h 67.95591 v 28.11968 h -67.95591 z"
       id="path10749"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.415131"
       y="76.37159"
       id="text30644-7"><tspan
         id="tspan30642-3"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.415131"
         y="76.37159">{ 'X' if JSONtank_identification['tipoTanque'] == "Horizontal" else "" }</tspan></text><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 698.30551,591.68504 h 145.28504 v 28.11968 H 698.30551 Z"
       id="path10751"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="99.615372"
       y="76.282021"
       id="text30644-8"><tspan
         id="tspan30642-7"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="99.615372"
         y="76.282021">{ 'X' if JSONtank_identification['tipoTanque'] == "Superficial" else "" }</tspan></text><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 1130.6457,591.68504 h 145.285 v 28.11968 h -145.285 z"
       id="path10753"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="156.57918"
       y="76.461151"
       id="text30644-57"><tspan
         id="tspan30642-8"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="156.57918"
         y="76.461151">{ 'X' if JSONtank_identification['tipoTanque'] == "Carcamo" else "" }</tspan></text><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 1418.8724,591.68504 h 119.5087 v 28.11968 h -119.5087 z"
       id="path10755"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="191.95766"
       y="76.37159"
       id="text30644-19"><tspan
         id="tspan30642-4"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.95766"
         y="76.37159">{ 'X' if JSONtank_identification['tipoTanque'] == "Enterrado" else "" }</tspan></text><path
       style="fill:#eefc98;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 0,2336.2772 h 1656.7181 v 24.6047 H 0 Z"
       id="path10757"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 353.83937,2359.7102 h 67.95591 v 26.9481 h -67.95591 z"
       id="path10759"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 1130.6457,2359.7102 h 145.285 v 26.9481 h -145.285 z"
       id="path10761"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 420.62362,2385.4866 h 67.95591 v 39.8362 h -67.95591 z"
       id="path10763"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="m 0,2462.8157 h 1656.7181 v 35.1497 H 0 Z"
       id="path10765"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.68895"
       y="167.45995"
       id="text30644-85-89-235-6"><tspan
         id="tspan30642-905-67-42-8"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.68895"
         y="167.45995">{'X' if JSONtank_identification["EstadoConexionEvidenciaGolpes"]["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.77852"
       y="162.17557"
       id="text30644-85-89-235-64"><tspan
         id="tspan30642-905-67-42-0"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.77852"
         y="162.17557">{'X' if JSONtank_identification["EstadoConexionCorrosion"]["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.68895"
       y="156.6225"
       id="text30644-85-89-235-0"><tspan
         id="tspan30642-905-67-42-1"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.68895"
         y="156.6225">{'X' if JSONtank_identification["AccionPorFuego"]["1"]["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.68895"
       y="178.20784"
       id="text30644-85-89-235-4"><tspan
         id="tspan30642-905-67-42-9"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.68895"
         y="178.20784">{'X' if JSONtank_identification["EstadoConexionOtros"]["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.77852"
       y="172.92346"
       id="text30644-85-89-235-9"><tspan
         id="tspan30642-905-67-42-2"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.77852"
         y="172.92346">{'X' if JSONtank_identification["EstadoConexionDesgaste"]["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.565613"
       y="178.29739"
       id="text30644-55"><tspan
         id="tspan30642-54"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.565613"
         y="178.29739">{ 'X' if JSONtank_identification["EstadoConexionOtros"]["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.9673"
       y="178.29739"
       id="text30644-34"><tspan
         id="tspan30642-21"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.9673"
         y="178.29739">{ 'X' if JSONtank_identification["EstadoConexionOtros"]["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="178.20784"
       id="text30644-60"><tspan
         id="tspan30642-605"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="178.20784">{ 'X' if JSONtank_identification["EstadoConexionOtros"]["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.655174"
       y="172.83389"
       id="text30644-74"><tspan
         id="tspan30642-08"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.655174"
         y="172.83389">{ 'X' if JSONtank_identification["EstadoConexionDesgaste"]["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.415127"
       y="172.92346"
       id="text30644-71"><tspan
         id="tspan30642-47"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.415127"
         y="172.92346">{ 'X' if JSONtank_identification["EstadoConexionDesgaste"]["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.548119"
       y="172.83389"
       id="text30644-97"><tspan
         id="tspan30642-64"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.548119"
         y="172.83389">{ 'X' if JSONtank_identification["EstadoConexionDesgaste"]["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.565613"
       y="167.45995"
       id="text30644-05"><tspan
         id="tspan30642-26"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.565613"
         y="167.45995">{ 'X' if JSONtank_identification["EstadoConexionEvidenciaGolpes"]["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.504692"
       y="167.54951"
       id="text30644-119"><tspan
         id="tspan30642-500"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.504692"
         y="167.54951">{ 'X' if JSONtank_identification["EstadoConexionEvidenciaGolpes"]["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.637684"
       y="167.37038"
       id="text30644-68"><tspan
         id="tspan30642-94"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.637684"
         y="167.37038">{ 'X' if JSONtank_identification["EstadoConexionEvidenciaGolpes"]["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.565613"
       y="162.26514"
       id="text30644-907"><tspan
         id="tspan30642-63"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.565613"
         y="162.26514">{ 'X' if JSONtank_identification["EstadoConexionCorrosion"]["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.146431"
       y="162.26514"
       id="text30644-83"><tspan
         id="tspan30642-02"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.146431"
         y="162.26514">{ 'X' if JSONtank_identification["EstadoConexionCorrosion"]["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.189857"
       y="162.086"
       id="text30644-260"><tspan
         id="tspan30642-60"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.189857"
         y="162.086">{ 'X' if JSONtank_identification["EstadoConexionCorrosion"]["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="156.80162"
       id="text30644-38"><tspan
         id="tspan30642-781"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="156.80162">{ 'X' if JSONtank_identification["AccionPorFuego"]["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.594261"
       y="156.80162"
       id="text30644-67"><tspan
         id="tspan30642-24"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.594261"
         y="156.80162">{ 'X' if JSONtank_identification["AccionPorFuego"]["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.458553"
       y="156.6225"
       id="text30644-64"><tspan
         id="tspan30642-685"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.458553"
         y="156.6225">{ 'X' if JSONtank_identification["AccionPorFuego"]["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.282135"
       y="151.06941"
       id="text30644-317"><tspan
         id="tspan30642-715"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.282135"
         y="151.06941">{ 'X' if JSONtank_identification["corrosionGeneral"]["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="151.69638"
       id="text30644-79"><tspan
         id="tspan30642-83"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="151.69638">{ 'X' if JSONtank_identification["corrosionGeneral"]["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.368988"
       y="151.42767"
       id="text30644-359"><tspan
         id="tspan30642-226"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.368988"
         y="151.42767">{ 'X' if JSONtank_identification["corrosionGeneral"]["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.504692"
       y="144.71025"
       id="text30644-84"><tspan
         id="tspan30642-66"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.504692"
         y="144.71025">{ 'X' if JSONtank_identification["corrosionEnLinea"]["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="144.79982"
       id="text30644-410"><tspan
         id="tspan30642-58"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="144.79982">{ 'X' if JSONtank_identification["corrosionEnLinea"]["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.371704"
       y="137.54498"
       id="text30644-18"><tspan
         id="tspan30642-62"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.371704"
         y="137.54498">{ 'X' if JSONtank_identification["corrosionAislada"]["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.773392"
       y="137.63455"
       id="text30644-316"><tspan
         id="tspan30642-29"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.773392"
         y="137.63455">{ 'X' if JSONtank_identification["corrosionAislada"]["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.100292"
       y="137.27629"
       id="text30644-69"><tspan
         id="tspan30642-50"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.100292"
         y="137.27629">{ 'X' if JSONtank_identification["corrosionAislada"]["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.103004"
       y="132.17105"
       id="text30644-80"><tspan
         id="tspan30642-36"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.103004"
         y="132.17105">{ 'X' if JSONtank_identification["abombamiento"]["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.146431"
       y="132.17105"
       id="text30644-94"><tspan
         id="tspan30642-51"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.146431"
         y="132.17105">{ 'X' if JSONtank_identification["abombamiento"]["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="132.08148"
       id="text30644-54"><tspan
         id="tspan30642-27"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="132.08148">{ 'X' if JSONtank_identification["abombamiento"]["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="126.7971"
       id="text30644-11"><tspan
         id="tspan30642-03"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="126.7971">{ 'X' if JSONtank_identification["abolladura"]["3"]["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.683826"
       y="126.7971"
       id="text30644-32"><tspan
         id="tspan30642-688"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.683826"
         y="126.7971">{ 'X' if JSONtank_identification["abolladura"]["3"]["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.548119"
       y="126.61797"
       id="text30644-41"><tspan
         id="tspan30642-68"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.548119"
         y="126.61797">{ 'X' if JSONtank_identification["abolladura"]["3"]["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.282135"
       y="121.42316"
       id="text30644-13"><tspan
         id="tspan30642-20"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.282135"
         y="121.42316">{ 'X' if JSONtank_identification["abolladura"]["2"]["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.594261"
       y="121.33359"
       id="text30644-31"><tspan
         id="tspan30642-17"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.594261"
         y="121.33359">{ 'X' if JSONtank_identification["abolladura"]["2"]["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.189857"
       y="121.33359"
       id="text30644-53"><tspan
         id="tspan30642-799"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.189857"
         y="121.33359">{ 'X' if JSONtank_identification["abolladura"]["2"]["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="116.04921"
       id="text30644-231"><tspan
         id="tspan30642-000"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="116.04921">{ 'X' if JSONtank_identification["abolladura"]["1"]["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.415127"
       y="116.31791"
       id="text30644-237"><tspan
         id="tspan30642-57"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.415127"
         y="116.31791">{ 'X' if JSONtank_identification["abolladura"]["1"]["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.727253"
       y="115.95965"
       id="text30644-20"><tspan
         id="tspan30642-84"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.727253"
         y="115.95965">{ 'X' if JSONtank_identification["abolladura"]["1"]["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.103004"
       y="110.67527"
       id="text30644-90"><tspan
         id="tspan30642-6"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.103004"
         y="110.67527">{ 'X' if JSONtank_identification['socavado']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.773392"
       y="110.5857"
       id="text30644-26"><tspan
         id="tspan30642-93"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.773392"
         y="110.5857">{ 'X' if JSONtank_identification['socavado']["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.727253"
       y="110.49613"
       id="text30644-52"><tspan
         id="tspan30642-22"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.727253"
         y="110.49613">{ 'X' if JSONtank_identification['socavado']["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.013443"
       y="105.12219"
       id="text30644-873"><tspan
         id="tspan30642-2"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.013443"
         y="105.12219">{ 'X' if JSONtank_identification['salpicadura']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.056866"
       y="105.39089"
       id="text30644-72"><tspan
         id="tspan30642-5"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.056866"
         y="105.39089">{ 'X' if JSONtank_identification['salpicadura']["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.637684"
       y="105.03262"
       id="text30644-23"><tspan
         id="tspan30642-00"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.637684"
         y="105.03262">{ 'X' if JSONtank_identification['salpicadura']["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.013443"
       y="99.569115"
       id="text30644-87"><tspan
         id="tspan30642-49"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.013443"
         y="99.569115">{ 'X' if JSONtank_identification['porosidad']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.773392"
       y="99.837814"
       id="text30644-77"><tspan
         id="tspan30642-42"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.773392"
         y="99.837814">{ 'X' if JSONtank_identification['porosidad']["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="99.837814"
       id="text30644-0"><tspan
         id="tspan30642-11"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="99.837814">{ 'X' if JSONtank_identification['porosidad']["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="94.642998"
       id="text30644-92"><tspan
         id="tspan30642-714"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="94.642998">{ 'X' if JSONtank_identification['agrietamiento']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.415127"
       y="94.284737"
       id="text30644-4"><tspan
         id="tspan30642-96"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.415127"
         y="94.284737">{ 'X' if JSONtank_identification['agrietamiento']["presenta"] == "NO" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.189857"
       y="94.374306"
       id="text30644-6"><tspan
         id="tspan30642-71"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.189857"
         y="94.374306">{ 'X' if JSONtank_identification['agrietamiento']["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.103004"
       y="89.08992"
       id="text30644-70"><tspan
         id="tspan30642-18"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.103004"
         y="89.08992">{ 'X' if JSONtank_identification['hermeticidad']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="89.179489"
       id="text30644-88"><tspan
         id="tspan30642-77"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="89.179489">{ 'X' if JSONtank_identification['hermeticidad']["presenta"] == "NO" else "" }</tspan></text><g
       clip-path="url(#clipEmfPath3)"
       id="g11353"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:140.098%;font-family:Arial;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(439.37008,1448.1638)"
         x="17.077988"
         y="15.898865"
         id="text11351"><tspan
           x="17.077988"
           y="15.898865"
           id="tspan11345"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan11343">Mal </tspan></tspan><tspan
           x="17.077988"
           y="40.503578"
           id="tspan11349"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan11347">Estado</tspan></tspan></text></g><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="197.1062"
       id="text30644-85"><tspan
         id="tspan30642-905"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="197.1062">{ 'X' if JSONquestion_views['domoprotector']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.923874"
       y="192.89662"
       id="text30644-799"><tspan
         id="tspan30642-56"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.923874"
         y="192.89662">{ 'X' if JSONquestion_views['domoprotector']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.056866"
       y="192.89662"
       id="text30644-2606"><tspan
         id="tspan30642-07"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.056866"
         y="192.89662">{ 'X' if JSONquestion_views['domoprotector']["presenta"] == "Mal Estado" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.100292"
       y="193.34445"
       id="text30644-753"><tspan
         id="tspan30642-213"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.100292"
         y="193.34445">{ 'X' if JSONquestion_views['domoprotector']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.923874"
       y="188.68703"
       id="text30644-28"><tspan
         id="tspan30642-30"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.923874"
         y="188.68703">{ 'X' if JSONquestion_views['soportetanque']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.9673"
       y="189.04529"
       id="text30644-95"><tspan
         id="tspan30642-85"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.9673"
         y="189.04529">{ 'X' if JSONquestion_views['soportetanque']["presenta"] == "Mal Estado" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.010727"
       y="188.95573"
       id="text30644-207"><tspan
         id="tspan30642-67"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.010727"
         y="188.95573">{ 'X' if JSONquestion_views['soportetanque']["presenta"] == "Bueno" else "" }</tspan></text><g
       clip-path="url(#clipEmfPath4)"
       id="g11559"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:140.098%;font-family:Arial;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(439.37008,1702.4126)"
         x="17.077988"
         y="15.898865"
         id="text11557"><tspan
           x="17.077988"
           y="15.898865"
           id="tspan11551"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan11549">Mal </tspan></tspan><tspan
           x="17.077988"
           y="40.503578"
           id="tspan11555"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan11553">Estado</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath2)"
       id="g11867"
       transform="matrix(0.12936474,0,0,0.12441101,0.87341335,0.14005654)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(507.32598,1712.9575)"
         x="0"
         y="15.898865"
         id="text11565"><tspan
           x="0"
           y="15.898865"
           id="tspan11563"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan11561">N/A</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(507.32598,1712.9575)"
         x="1.171654"
         y="147.02742"
         id="text11643"><tspan
           x="0"
           y="0"
           id="tspan11641"><tspan
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:18.75px;font-family:Arial;fill:#f2f2f2"
             id="tspan11639" /></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="353.85992"
         y="2027.1394"
         id="text11753"><tspan
           x="353.85992"
           y="2027.1394"
           id="tspan11751"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan11747">BUENO</tspan><tspan
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:11.6875px;font-family:Arial;fill:#000000"
             id="tspan11749" /></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="511.93515"
         y="2031.9336"
         id="text11759"><tspan
           x="511.93515"
           y="2031.9336"
           id="tspan11757"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan11755">N/A</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(507.32598,1712.9575)"
         x="-14.059843"
         y="696.87946"
         id="text11855"><tspan
           x="-14.059843"
           y="696.87946"
           id="tspan11853"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan11851">cuales?</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:146.568%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(507.32598,1712.9575)"
         x="194.49449"
         y="904.26208"
         id="text11865"><tspan
           x="194.49449"
           y="904.26208"
           id="tspan11859"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan11857">Nombre:</tspan></tspan><tspan
           x="194.49449"
           y="926.79907"
           id="tspan11863"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan11861">CC</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1623.2183"
         y="1906.0547"
         id="text30644-85-89-835"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1623.2183"
           y="1906.0547">{'X' if JSONquestions_deterioration['roscaencuentrabuenestado']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1621.2948"
         y="1950.7648"
         id="text30644-85-89-835-5"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-6"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1621.2948"
           y="1950.7648">{'X' if JSONquestions_deterioration['accesoriosencuentrabuenestado']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1620.9418"
         y="2036.1907"
         id="text30644-85-89-835-8"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-8"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1620.9418"
           y="2036.1907">{'X' if JSONobservations_and_results['estadovalvulas']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1620.9418"
         y="2080.6687"
         id="text30644-85-89-835-4"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-9"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1620.9418"
           y="2080.6687">{'X' if JSONobservations_and_results['estadovalvulasalivio']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1620.5887"
         y="2121.2637"
         id="text30644-85-89-835-7"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-7"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1620.5887"
           y="2121.2637">{'X' if JSONobservations_and_results['estadoindicadornivel']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1498.8038"
         y="2122.6758"
         id="text30644-85-89-835-0"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-77"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1498.8038"
           y="2122.6758">{'X' if JSONobservations_and_results['estadoindicadornivel']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1499.1569"
         y="2076.7856"
         id="text30644-85-89-835-3"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-4"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1499.1569"
           y="2076.7856">{'X' if JSONobservations_and_results['estadovalvulasalivio']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1501.2748"
         y="2031.6017"
         id="text30644-85-89-835-34"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-0"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1501.2748"
           y="2031.6017">{'X' if JSONobservations_and_results['estadovalvulas']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1500.5688"
         y="1948.2937"
         id="text30644-85-89-835-56"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-5"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1500.5688"
           y="1948.2937">{'X' if JSONquestions_deterioration['accesoriosencuentrabuenestado']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1500.5688"
         y="1902.7567"
         id="text30644-85-89-835-82"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-2"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1500.5688"
           y="1902.7567">{'X' if JSONquestions_deterioration['roscaencuentrabuenestado']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1500.9218"
         y="1861.8088"
         id="text30644-85-89-835-824"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-97"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1500.9218"
           y="1861.8088">{'X' if JSONquestions_deterioration['tuberiaaplastamiento']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1500.5688"
         y="1818.7428"
         id="text30644-85-89-835-89"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-85"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1500.5688"
           y="1818.7428">{'X' if JSONquestions_deterioration['tuberiapresentafisura']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1501.9808"
         y="1776.7358"
         id="text30644-85-89-835-02"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-95"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1501.9808"
           y="1776.7358">{'X' if JSONquestions_deterioration['tuberiapresentacorrosion']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1503.3928"
         y="1734.0228"
         id="text30644-85-89-835-825"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-74"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1503.3928"
           y="1734.0228">{'X' if JSONquestions_deterioration['tuberiadefectosoldadura']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1623.7657"
         y="1862.8678"
         id="text30644-85-89-835-6"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-47"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1623.7657"
           y="1862.8678">{'X' if JSONquestions_deterioration['tuberiaaplastamiento']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1625.1777"
         y="1822.9788"
         id="text30644-85-89-835-74"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-54"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1625.1777"
           y="1822.9788">{'X' if JSONquestions_deterioration['tuberiapresentafisura']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1626.2368"
         y="1776.0298"
         id="text30644-85-89-835-62"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-746"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1626.2368"
           y="1776.0298">{'X' if JSONquestions_deterioration['tuberiapresentacorrosion']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1626.2368"
         y="1733.3168"
         id="text30644-85-89-835-899"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-55-24"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1626.2368"
           y="1733.3168">{'X' if JSONquestions_deterioration['tuberiadefectosoldadura']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1501.4092"
         y="1658.2655"
         id="text30644-85-89-653"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-46"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1501.4092"
           y="1658.2655">{'X' if JSONquestion_views['continuidad']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1502.4077"
         y="1623.3203"
         id="text30644-85-89-35"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-71"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1502.4077"
           y="1623.3203">{'X' if JSONquestion_views['proteccioncatodica']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1501.4092"
         y="1587.3767"
         id="text30644-85-89-50"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-60"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1501.4092"
           y="1587.3767">{'X' if JSONquestion_views['pintura']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1500.4108"
         y="1551.433"
         id="text30644-85-89-21"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-65"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1500.4108"
           y="1551.433">{'X' if JSONquestion_views['orejasizaminto']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1501.4092"
         y="1515.4894"
         id="text30644-85-89-24"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-43"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1501.4092"
           y="1515.4894">{'X' if JSONquestion_views['domoprotector']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1499.4124"
         y="1485.5364"
         id="text30644-85-89-235"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-42"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1499.4124"
           y="1485.5364">{'X' if JSONquestion_views['soportetanque']["cumple"] == True else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1623.2183"
         y="1485.5364"
         id="text30644-85-89-68"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-716"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1623.2183"
           y="1485.5364">{'X' if JSONquestion_views['soportetanque']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1626.2136"
         y="1524.4753"
         id="text30644-85-89-67"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-45"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1626.2136"
           y="1524.4753">{'X' if JSONquestion_views['domoprotector']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1626.2136"
         y="1556.4252"
         id="text30644-85-89-97"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-91"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1626.2136"
           y="1556.4252">{'X' if JSONquestion_views['orejasizaminto']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1623.2183"
         y="1589.3735"
         id="text30644-85-89-98"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-3990"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1623.2183"
           y="1589.3735">{'X' if JSONquestion_views['pintura']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1622.2198"
         y="1623.3203"
         id="text30644-85-89-944"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-70"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1622.2198"
           y="1623.3203">{'X' if JSONquestion_views['proteccioncatodica']["cumple"] == False else " "}</tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.41205;stroke-dasharray:none;stroke-opacity:1"
         x="1623.2183"
         y="1657.4445"
         id="text30644-85-89-32"
         transform="scale(0.98066674,1.0197144)"><tspan
           id="tspan30642-905-67-72"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:25.0269px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:2.41204"
           x="1623.2183"
           y="1657.4445">{'X' if JSONquestion_views['continuidad']["cumple"] == False else " "}</tspan></text></g><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="268.93793"
       id="text30644-85-89-03"><tspan
         id="tspan30642-905-67-95"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="268.93793">{ 'X' if JSONobservations_and_results['estadoindicadornivel']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="268.93793"
       id="text30644-85-89-089"><tspan
         id="tspan30642-905-67-733"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="268.93793">{ 'X' if JSONobservations_and_results['estadoindicadornivel']["presenta"] == "Regular" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.010727"
       y="269.0275"
       id="text30644-85-89-949"><tspan
         id="tspan30642-905-67-51"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.010727"
         y="269.0275">{ 'X' if JSONobservations_and_results['estadoindicadornivel']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.371704"
       y="263.74313"
       id="text30644-85-89-33"><tspan
         id="tspan30642-905-67-69"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.371704"
         y="263.74313">{ 'X' if JSONobservations_and_results['estadovalvulasalivio']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.788166"
       y="264.01181"
       id="text30644-85-89-435"><tspan
         id="tspan30642-905-67-877"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.788166"
         y="264.01181">{ 'X' if JSONobservations_and_results['estadovalvulasalivio']["presenta"] == "Regular" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.461266"
       y="258.36917"
       id="text30644-85-89-432"><tspan
         id="tspan30642-905-67-5"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.461266"
         y="258.36917">{ 'X' if JSONobservations_and_results['estadovalvulas']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.9673"
       y="258.63788"
       id="text30644-85-89-7"><tspan
         id="tspan30642-905-67-92"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.9673"
         y="258.63788">{ 'X' if JSONobservations_and_results['estadovalvulas']["presenta"] == "Regular" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.655174"
       y="247.62129"
       id="text30644-85-89-39"><tspan
         id="tspan30642-905-67-85"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.655174"
         y="247.62129">{ 'X' if JSONquestions_deterioration['accesoriosencuentrabuenestado']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.877735"
       y="247.44215"
       id="text30644-85-89-90"><tspan
         id="tspan30642-905-67-35"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.877735"
         y="247.44215">{ 'X' if JSONquestions_deterioration['accesoriosencuentrabuenestado']["presenta"] == "Mal Estado" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.189857"
       y="247.35258"
       id="text30644-85-89-82"><tspan
         id="tspan30642-905-67-09"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.189857"
         y="247.35258">{ 'X' if JSONquestions_deterioration['accesoriosencuentrabuenestado']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="242.06821"
       id="text30644-85-89-3"><tspan
         id="tspan30642-905-67-87"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="242.06821">{ 'X' if JSONquestions_deterioration['roscaencuentrabuenestado']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.788166"
       y="242.42647"
       id="text30644-85-89-94"><tspan
         id="tspan30642-905-67-9"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.788166"
         y="242.42647">{ 'X' if JSONquestions_deterioration['roscaencuentrabuenestado']["presenta"] == "Mal Estado" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="57.877735"
       y="236.8734"
       id="text30644-85-89-87"><tspan
         id="tspan30642-905-67-1"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="57.877735"
         y="236.8734">{ 'X' if JSONquestions_deterioration['tuberiaaplastamiento']["presenta"] == "Mal Estado" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="231.49945"
       id="text30644-85-89-8"><tspan
         id="tspan30642-905-67-4"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="231.49945">{ 'X' if JSONquestions_deterioration['tuberiapresentafisura']["presenta"] == "Mal Estado" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.189857"
       y="231.49945"
       id="text30644-85-89-06"><tspan
         id="tspan30642-905-67-73"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.189857"
         y="231.49945">{ 'X' if JSONquestions_deterioration['tuberiapresentafisura']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.282135"
       y="226.21507"
       id="text30644-85-89-5"><tspan
         id="tspan30642-905-67-7"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.282135"
         y="226.21507">{ 'X' if JSONquestions_deterioration['tuberiapresentafisura']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.111801"
       y="231.51765"
       id="text30644-85-89-5-5"><tspan
         id="tspan30642-905-67-7-8"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.111801"
         y="231.51765">{ 'X' if JSONquestions_deterioration['tuberiapresentafisura']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.238464"
       y="237.13593"
       id="text30644-85-89-5-8"><tspan
         id="tspan30642-905-67-7-0"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.238464"
         y="237.13593">{ 'X' if JSONquestions_deterioration['tuberiaaplastamiento']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="226.21507"
       id="text30644-85-89-0"><tspan
         id="tspan30642-905-67-2"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="226.21507">{ 'X' if JSONquestions_deterioration['tuberiapresentacorrosion']["presenta"] == "Mal Estado" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.325562"
       y="220.57243"
       id="text30644-85-89-4"><tspan
         id="tspan30642-905-67-8"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.325562"
         y="220.57243">{ 'X' if JSONquestions_deterioration['tuberiadefectosoldadura']["presenta"] == "Mal Estado" else "" }</tspan></text><g
       clip-path="url(#clipEmfPath6)"
       id="g11883"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2147.6409)"
         x="0"
         y="12.730408"
         id="text11881"><tspan
           x="0"
           y="12.730408"
           id="tspan11879"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan11877">¿En que estado de Indicador de Nivel?</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath9)"
       id="g11907"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2553.0331)"
         x="0"
         y="11.4375"
         id="text11905"><tspan
           x="0"
           y="11.4375"
           id="tspan11903"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan11901">Galga pico loro                   N°</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath10)"
       id="g11915"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2578.8094)"
         x="0"
         y="11.4375"
         id="text11913"><tspan
           x="0"
           y="11.4375"
           id="tspan11911"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan11909">Cinta Metrica                      N°</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath11)"
       id="g11923"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2604.5858)"
         x="0"
         y="11.4375"
         id="text11921"><tspan
           x="0"
           y="11.4375"
           id="tspan11919"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan11917">Agua Jabonosa                   N°</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath12)"
       id="g11931"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(10.544882,2363.2252)"
         x="0"
         y="12.730408"
         id="text11929"><tspan
           x="0"
           y="12.730408"
           id="tspan11927"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan11925">Tanque Inspeccionado                </tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath13)"
       id="g11939"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2630.3622)"
         x="0"
         y="11.4375"
         id="text11937"><tspan
           x="0"
           y="11.4375"
           id="tspan11935"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan11933">OTRO</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath14)"
       id="g11947"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2394.8598)"
         x="0"
         y="13.80542"
         id="text11945"><tspan
           x="0"
           y="13.80542"
           id="tspan11943"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan11941">Tanque se reporta para ensayo no destructivos</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath15)"
       id="g11991"
       transform="matrix(0.13030134,0,0,0.12421712,1.8810923,-1.5197022)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;line-height:140.098%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2653.7953)"
         x="0"
         y="13.171875"
         id="text11957"><tspan
           x="0"
           y="0"
           id="tspan11951"><tspan
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan11949" /></tspan><tspan
           x="0"
           y="0"
           id="tspan11955"><tspan
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan11953" /></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;line-height:133.427%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2653.7953)"
         x="0"
         y="61.209671"
         id="text11989"><tspan
           x="0"
           y="61.209671"
           id="tspan11961" /><tspan
           x="0"
           y="84.642784"
           id="tspan11967" /><tspan
           x="0"
           y="108.0759"
           id="tspan11975"
           style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Calibri;fill:#000000"> </tspan><tspan
           x="0"
           y="131.50902"
           id="tspan11983" /><tspan
           x="0"
           y="154.94214"
           id="tspan11987" /></text></g><g
       clip-path="url(#clipEmfPath16)"
       id="g11999"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2501.4803)"
         x="0"
         y="11.4375"
         id="text11997"><tspan
           x="0"
           y="11.4375"
           id="tspan11995"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan11993">Detector de Fugas             N° </tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath19)"
       id="g12023"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2527.2567)"
         x="0"
         y="11.4375"
         id="text12021"><tspan
           x="0"
           y="11.4375"
           id="tspan12019"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan12017">Multimetro                         N°</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath20)"
       id="g12031"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2017.5874)"
         x="0"
         y="12.730408"
         id="text12029"><tspan
           x="0"
           y="12.730408"
           id="tspan12027"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12025">REVISION VISUAL DE ACCESORIOS</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath22)"
       id="g12047"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2060.9386)"
         x="0"
         y="12.730408"
         id="text12045"><tspan
           x="0"
           y="12.730408"
           id="tspan12043"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12041">¿En que estado se encuentran las Valvulas?</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath24)"
       id="g12063"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2104.2898)"
         x="0"
         y="12.730408"
         id="text12061"><tspan
           x="0"
           y="12.730408"
           id="tspan12059"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12057">¿En que estado se encuentran las Valvulas alivio?</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath26)"
       id="g12079"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,2433.5244)"
         x="0"
         y="13.80542"
         id="text12077"><tspan
           x="0"
           y="13.80542"
           id="tspan12075"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12073">En el momento de la inspeccion se dejan evidencias      Fotograficas                       Video                           Otra  </tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath27)"
       id="g12087"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(60.925984,2469.8457)"
         x="0"
         y="13.171875"
         id="text12085"><tspan
           x="0"
           y="13.171875"
           id="tspan12083"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12081">EQUIPOS UTILIZADOS</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath28)"
       id="g12095"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(406.56378,2469.8457)"
         x="0"
         y="13.171875"
         id="text12093"><tspan
           x="0"
           y="13.171875"
           id="tspan12091"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12089">FIRMA DEL INSPECTOR</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath29)"
       id="g12103"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1103.6976,2469.8457)"
         x="0"
         y="13.171875"
         id="text12101"><tspan
           x="0"
           y="13.171875"
           id="tspan12099"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12097">FIRMA DEL USUARIO</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath30)"
       id="g12111"
       transform="matrix(0.12840848,0,0,0.12421712,1.7943407,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.5749px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.990664"
         transform="scale(0.99066422,1.0094238)"
         x="953.27893"
         y="2185.0315"
         id="text12109"><tspan
           x="953.27893"
           y="2185.0315"
           id="tspan12107"
           style="stroke-width:0.990664"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.5749px;font-family:Arial;fill:#000000;stroke-width:0.990664"
             id="tspan12105">Numerales exigidos por Resolución 40245 del 2016 De Ministerio De Minas Y Energia</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath31)"
       id="g12119"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(693.6189,2221.4551)"
         x="0"
         y="13.80542"
         id="text12117"><tspan
           x="0"
           y="13.80542"
           id="tspan12115"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12113">OBSERVACIONES Y CONCLUSIONES</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath33)"
       id="g12135"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(738.14173,2337.4488)"
         x="0"
         y="16.973877"
         id="text12133"><tspan
           x="0"
           y="16.973877"
           id="tspan12131"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:18.75px;font-family:Arial;fill:#000000"
             id="tspan12129">Resultado Revisión:</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath34)"
       id="g12143"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(258.93543,2363.2252)"
         x="0"
         y="13.80542"
         id="text12141"><tspan
           x="0"
           y="13.80542"
           id="tspan12139"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12137">CUMPLE</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath35)"
       id="g12151"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(424.13858,2364.3969)"
         x="0"
         y="11.655396"
         id="text12149"><tspan
           x="0"
           y="11.655396"
           id="tspan12147"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Arial;fill:#000000"
             id="tspan12145">Numero de Sticker</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath36)"
       id="g12159"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(942.00945,2363.2252)"
         x="0"
         y="13.80542"
         id="text12157"><tspan
           x="0"
           y="13.80542"
           id="tspan12155"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12153">NO CUMPLE</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath38)"
       id="g12175"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1844.1827)"
         x="0"
         y="12.730408"
         id="text12173"><tspan
           x="0"
           y="12.730408"
           id="tspan12171"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12169">¿La tubería presenta fisuras y/o escape</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath40)"
       id="g12191"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1974.2362)"
         x="0"
         y="12.730408"
         id="text12189"><tspan
           x="0"
           y="12.730408"
           id="tspan12187"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12185">¿Los accesorios se encuentran en buen estado?</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath42)"
       id="g12207"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1930.885)"
         x="0"
         y="12.730408"
         id="text12205"><tspan
           x="0"
           y="12.730408"
           id="tspan12203"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12201">¿Las roscas se encuentran en buen estado?</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath44)"
       id="g12223"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1887.5339)"
         x="0"
         y="12.730408"
         id="text12221"><tspan
           x="0"
           y="12.730408"
           id="tspan12219"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12217">¿La tubería presenta aplastamiento o dobleces?</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath46)"
       id="g12239"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1714.1291)"
         x="0"
         y="12.730408"
         id="text12237"><tspan
           x="0"
           y="12.730408"
           id="tspan12235"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12233">REVISION VISUAL DE tubería</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath48)"
       id="g12255"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1757.4803)"
         x="0"
         y="12.730408"
         id="text12253"><tspan
           x="0"
           y="12.730408"
           id="tspan12251"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12249">¿La tubería presenta defecto de soldadura?</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath50)"
       id="g12271"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1800.8315)"
         x="0"
         y="12.730408"
         id="text12269"><tspan
           x="0"
           y="12.730408"
           id="tspan12267"><tspan
             dx="0 0"
             dy="0 0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12265">¿La tubería presenta corrosion?</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath53)"
       id="g12299"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:141.64%;font-family:Arial;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(37.492913,1629.7701)"
         x="30.73082"
         y="12.730408"
         id="text12297"><tspan
           x="30.73082"
           y="12.730408"
           id="tspan12291"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12289">ESTADO </tspan></tspan><tspan
           x="32.684326"
           y="32.648533"
           id="tspan12295"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12293">GENERAL </tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath54)"
       id="g12307"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1603.9937)"
         x="0"
         y="13.80542"
         id="text12305"><tspan
           x="0"
           y="13.80542"
           id="tspan12303"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12301">Pintura y acabado</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath56)"
       id="g12323"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1639.1433)"
         x="0"
         y="12.730408"
         id="text12321"><tspan
           x="0"
           y="12.730408"
           id="tspan12319"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12317">Protección catódica (enterrados)</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath58)"
       id="g12339"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1674.2929)"
         x="0"
         y="12.730408"
         id="text12337"><tspan
           x="0"
           y="12.730408"
           id="tspan12335"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12333">Continuidad</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath60)"
       id="g12355"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1415.3575)"
         x="0"
         y="13.80542"
         id="text12353"><tspan
           x="0"
           y="13.80542"
           id="tspan12351"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12349">Otros</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath62)"
       id="g12373"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1458.7087)"
         x="0"
         y="15.898865"
         id="text12371"><tspan
           x="0"
           y="15.898865"
           id="tspan12369"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12365">Estado </tspan><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan12367">(B=Bueno - M=Mal Estado)</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath63)"
       id="g12381"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1029.8835,1458.7087)"
         x="0"
         y="15.898865"
         id="text12379"><tspan
           x="0"
           y="15.898865"
           id="tspan12377"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12375">OBSERVACIONES</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath64)"
       id="g12389"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(10.544882,1533.6945)"
         x="0"
         y="12.730408"
         id="text12387"><tspan
           x="0"
           y="12.730408"
           id="tspan12385"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12383">CRITERIO MTTO</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath65)"
       id="g12397"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1498.5449)"
         x="0"
         y="13.80542"
         id="text12395"><tspan
           x="0"
           y="13.80542"
           id="tspan12393"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12391">Soportes Del Tanque</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath67)"
       id="g12413"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1533.6945)"
         x="0"
         y="13.80542"
         id="text12411"><tspan
           x="0"
           y="13.80542"
           id="tspan12409"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12407">Domo protector o Embebidos</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath69)"
       id="g12429"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1568.8441)"
         x="0"
         y="13.80542"
         id="text12427"><tspan
           x="0"
           y="13.80542"
           id="tspan12425"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12423">Orejas de izamiento</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath70)"
       id="g12443"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(25.776378,1234.9228)"
         x="0"
         y="11.655396"
         id="text12435"><tspan
           x="0"
           y="11.655396"
           id="tspan12433"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Arial;fill:#000000"
             id="tspan12431">Numeral 10,3                  </tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(25.776378,1234.9228)"
         x="15.231496"
         y="30.401852"
         id="text12441"><tspan
           x="15.231496"
           y="30.401852"
           id="tspan12439"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Arial;fill:#000000"
             id="tspan12437">Literal g</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath71)"
       id="g12451"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1241.9528)"
         x="0"
         y="13.80542"
         id="text12449"><tspan
           x="0"
           y="13.80542"
           id="tspan12447"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12445">Accion por Fuego</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath72)"
       id="g12463"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:138.294%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1232.5795)"
         x="0"
         y="13.80542"
         id="text12461"><tspan
           x="0"
           y="13.80542"
           id="tspan12455"><tspan
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12453">Ha soportado temperaturas excesivas                                                                                                                              </tspan></tspan><tspan
           x="0"
           y="34.895256"
           id="tspan12459"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12457">Tiene variacion en su geometria original</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath73)"
       id="g12481"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:141.64%;font-family:Arial;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(39.83622,1333.3417)"
         x="30.73082"
         y="12.730408"
         id="text12473"><tspan
           x="30.73082"
           y="12.730408"
           id="tspan12467"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12465">ESTADO </tspan></tspan><tspan
           x="30.73082"
           y="32.648533"
           id="tspan12471"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan12469">CONEXIONES</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(39.83622,1333.3417)"
         x="-31.634645"
         y="49.49247"
         id="text12479"><tspan
           x="-31.634645"
           y="49.49247"
           id="tspan12477"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan12475">numeral 10,3 literal h</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath74)"
       id="g12489"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1285.3039)"
         x="0"
         y="13.80542"
         id="text12487"><tspan
           x="0"
           y="13.80542"
           id="tspan12485"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12483">Corrosión</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath76)"
       id="g12505"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1328.6551)"
         x="0"
         y="13.80542"
         id="text12503"><tspan
           x="0"
           y="13.80542"
           id="tspan12501"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12499">Evidencia de Golpes</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath78)"
       id="g12521"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1372.0063)"
         x="0"
         y="13.80542"
         id="text12519"><tspan
           x="0"
           y="13.80542"
           id="tspan12517"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12515">Desgaste</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath80)"
       id="g12539"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:italic;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,1043.9433)"
         x="0"
         y="13.80542"
         id="text12537"><tspan
           x="0"
           y="13.80542"
           id="tspan12535"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12531">ABOMBAMIENTO </tspan><tspan
             dx="-0.61917198"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan12533">  numeral 10,3 literal c</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath81)"
       id="g12547"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1043.9433)"
         x="0"
         y="13.80542"
         id="text12545"><tspan
           x="0"
           y="13.80542"
           id="tspan12543"><tspan
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12541">Presenta abombamiento visible definido</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath82)"
       id="g12565"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:135.132%;font-family:Calibri;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(31.634646,1121.2724)"
         x="37.271118"
         y="10.546875"
         id="text12557"><tspan
           x="37.271118"
           y="10.546875"
           id="tspan12551"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Calibri;fill:#000000"
             id="tspan12549">CORROSIÓN </tspan></tspan><tspan
           x="39.256332"
           y="30.424812"
           id="tspan12555"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12553">numeral 10,3 </tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(31.634646,1121.2724)"
         x="-4.686614"
         y="56.523056"
         id="text12563"><tspan
           x="-4.686614"
           y="56.523056"
           id="tspan12561"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12559">literal d,e,f</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath83)"
       id="g12573"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1087.2945)"
         x="0"
         y="13.80542"
         id="text12571"><tspan
           x="0"
           y="13.80542"
           id="tspan12569"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12567">Corrosión aislada</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath84)"
       id="g12585"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:138.294%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1077.9213)"
         x="0"
         y="13.80542"
         id="text12583"><tspan
           x="0"
           y="13.80542"
           id="tspan12577"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12575">Presenta picadura aislada de una profundidad &gt; 15% del espesor                                                                      </tspan></tspan><tspan
           x="0"
           y="34.895256"
           id="tspan12581"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12579">El espesor de pared remanente es inferior a 3,18 mm </tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath85)"
       id="g12593"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1143.5339)"
         x="0"
         y="13.80542"
         id="text12591"><tspan
           x="0"
           y="13.80542"
           id="tspan12589"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12587">Corrosión en línea</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath86)"
       id="g12611"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:138.294%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1123.6157)"
         x="0"
         y="13.80542"
         id="text12603"><tspan
           x="0"
           y="13.80542"
           id="tspan12597"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12595">Corrosion en linea con longitud &gt; de 76mm                                                                                                                                                              </tspan></tspan><tspan
           x="0"
           y="34.895256"
           id="tspan12601"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12599">Profundidad de picadura &gt; al 15% de espesor                                                                                                                                                                   </tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1123.6157)"
         x="0"
         y="54.813293"
         id="text12609"><tspan
           x="0"
           y="54.813293"
           id="tspan12607"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12605">El espesor de pared remanente es inferior a 3,18 mm       </tspan></tspan></text></g><g
       id="g15703-5-1-4-76-5"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.543051,79.192371)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-1" /><g
         id="g15698-7-9-3-10-2"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-0" /></g></g><g
       id="g15703-5-1-4-76-54"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.543051,81.599008)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-6" /><g
         id="g15698-7-9-3-10-9"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-1" /></g></g><g
       id="g15703-5-1-4-76-7"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.479718,84.195643)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-7" /><g
         id="g15698-7-9-3-10-5"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-2" /></g></g><g
       clip-path="url(#clipEmfPath87)"
       id="g12619"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,1198.6016)"
         x="0"
         y="13.80542"
         id="text12617"><tspan
           x="0"
           y="13.80542"
           id="tspan12615"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12613">Corrosión general</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath88)"
       id="g12631"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:138.294%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1189.2283)"
         x="0"
         y="13.80542"
         id="text12629"><tspan
           x="0"
           y="13.80542"
           id="tspan12623"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12621">Profundidad de picadura &gt; al 15% de espesor                                                                                                                                            </tspan></tspan><tspan
           x="0"
           y="34.895256"
           id="tspan12627"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12625">El espesor de pared remanente es inferior a 3,18 mm</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath89)"
       id="g12639"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,870.53858)"
         x="0"
         y="13.80542"
         id="text12637"><tspan
           x="0"
           y="13.80542"
           id="tspan12635"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12633">Socavado</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath91)"
       id="g12657"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:italic;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,957.24094)"
         x="0"
         y="13.80542"
         id="text12655"><tspan
           x="0"
           y="13.80542"
           id="tspan12653"><tspan
             dx="0"
             dy="0"
             style="font-style:italic;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12649">ABOLLADURA </tspan><tspan
             dx="0.65633702"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan12651"> numeral 10,3 literal b</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath92)"
       id="g12665"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,913.88976)"
         x="0"
         y="13.80542"
         id="text12663"><tspan
           x="0"
           y="13.80542"
           id="tspan12661"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12659">Compromete un zona de soldadura</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath93)"
       id="g12677"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:138.294%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,947.86772)"
         x="0"
         y="13.80542"
         id="text12675"><tspan
           x="0"
           y="13.80542"
           id="tspan12669"><tspan
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12667">Se encuentra en la zona afectada por el calor de una soldadura                                                                                                                                                                                                                                       </tspan></tspan><tspan
           x="0"
           y="34.895256"
           id="tspan12673"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12671">( dis. A 3 cm a partir de la soldadura)</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath94)"
       id="g12685"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,1000.5921)"
         x="0"
         y="13.80542"
         id="text12683"><tspan
           x="0"
           y="13.80542"
           id="tspan12681"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12679">Su profundidad exceda de 6,35 mm o 1/10 de diametro promedio                                             de la abolladura</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath95)"
       id="g12693"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(14.059843,697.13386)"
         x="0"
         y="15.898865"
         id="text12691"><tspan
           x="0"
           y="15.898865"
           id="tspan12689"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12687">Numeral 10.1</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath96)"
       id="g12701"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,697.13386)"
         x="0"
         y="15.898865"
         id="text12699"><tspan
           x="0"
           y="15.898865"
           id="tspan12697"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12695">Hermeticidad</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath97)"
       id="g12709"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,697.13386)"
         x="0"
         y="13.80542"
         id="text12707"><tspan
           x="0"
           y="13.80542"
           id="tspan12705"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12703">Presenta fisuras/escape </tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath98)"
       id="g12727"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(29.291339,785.00787)"
         x="0"
         y="10.546875"
         id="text12715"><tspan
           x="0"
           y="10.546875"
           id="tspan12713"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:14.0625px;font-family:Calibri;fill:#000000"
             id="tspan12711">SOLDADURA         </tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:133.427%;font-family:Calibri;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(29.291339,785.00787)"
         x="40.814529"
         y="34.261639"
         id="text12725"><tspan
           x="40.814529"
           y="34.261639"
           id="tspan12719"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12717">numeral 10,3 </tspan></tspan><tspan
           x="40.814529"
           y="57.694756"
           id="tspan12723"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan12721">literal a</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath99)"
       id="g12735"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,740.48504)"
         x="0"
         y="13.80542"
         id="text12733"><tspan
           x="0"
           y="13.80542"
           id="tspan12731"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12729">Agrietamiento</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath101)"
       id="g12751"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,783.83622)"
         x="0"
         y="13.80542"
         id="text12749"><tspan
           x="0"
           y="13.80542"
           id="tspan12747"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12745">Porosidad</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath103)"
       id="g12767"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(137.08346,827.1874)"
         x="0"
         y="13.80542"
         id="text12765"><tspan
           x="0"
           y="13.80542"
           id="tspan12763"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12761">Salpicadura</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath104)"
       id="g12775"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(557.70709,827.1874)"
         x="0"
         y="13.80542"
         id="text12773"><tspan
           x="0"
           y="13.80542"
           id="tspan12771"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12769"> </tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath105)"
       id="g12783"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,622.14803)"
         x="0"
         y="13.80542"
         id="text12781"><tspan
           x="0"
           y="13.80542"
           id="tspan12779"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12777">CLASE DE USUARIO</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath106)"
       id="g12791"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(636.20787,622.14803)"
         x="0"
         y="15.898865"
         id="text12789"><tspan
           x="0"
           y="15.898865"
           id="tspan12787"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12785"> {str(JSONtank_identification['claseUsuario']) if JSONtank_identification['claseUsuario'] != None else ""}</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath107)"
       id="g12799"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(78.500787,654.95433)"
         x="0"
         y="15.898865"
         id="text12797"><tspan
           x="0"
           y="15.898865"
           id="tspan12795"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12793">REQUISITO A EVALUAR</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath108)"
       id="g12807"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(405.39213,645.5811)"
         x="0"
         y="13.80542"
         id="text12805"><tspan
           x="0"
           y="13.80542"
           id="tspan12803"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12801">¿PRESENTA?</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath109)"
       id="g12815"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(917.40472,654.95433)"
         x="0"
         y="15.898865"
         id="text12813"><tspan
           x="0"
           y="15.898865"
           id="tspan12811"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12809">DEFECTOLOGIA</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath110)"
       id="g12823"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1441.1339,654.95433)"
         x="0"
         y="15.898865"
         id="text12821"><tspan
           x="0"
           y="15.898865"
           id="tspan12819"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12817">CUMPLE</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath111)"
       id="g12831"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1543.0677,654.95433)"
         x="0"
         y="15.898865"
         id="text12829"><tspan
           x="0"
           y="15.898865"
           id="tspan12827"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12825">NO CUMPLE</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath114)"
       id="g12855"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1120.1008,362.04095)"
         x="0"
         y="15.898865"
         id="text12853"><tspan
           x="0"
           y="15.898865"
           id="tspan12851"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12849">IDENTIFICACIÓN DEL TANQUE</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath115)"
       id="g12863"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,451.08661)"
         x="0"
         y="15.898865"
         id="text12861"><tspan
           x="0"
           y="15.898865"
           id="tspan12859"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12857">Teléfono:</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath116)"
       id="g12871"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,495.60945)"
         x="0"
         y="15.898865"
         id="text12869"><tspan
           x="0"
           y="15.898865"
           id="tspan12867"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12865">Contacto:</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath117)"
       id="g12879"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,595.2)"
         x="0"
         y="13.80542"
         id="text12877"><tspan
           x="0"
           y="13.80542"
           id="tspan12875"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12873">TIPO DE TANQUE</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath118)"
       id="g12887"
       transform="matrix(0.13030134,0,0,0.12421712,-0.52505608,0.52944585)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="320.48694"
         y="609.00543"
         id="text12885"><tspan
           x="320.48694"
           y="609.00543"
           id="tspan12883"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12881">HORIZONTAL</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath119)"
       id="g12895"
       transform="matrix(0.13030134,0,0,0.12421712,-0.52505608,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(597.54331,599.88661)"
         x="0"
         y="13.80542"
         id="text12893"><tspan
           x="0"
           y="13.80542"
           id="tspan12891"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12889">SUPERFICIAL</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath120)"
       id="g12903"
       transform="matrix(0.13030134,0,0,0.12421712,-0.52505608,0.52944585)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1050.9732,595.2)"
         x="0"
         y="13.80542"
         id="text12901"><tspan
           x="0"
           y="13.80542"
           id="tspan12899"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan12897">CARCAMO</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath123)"
       id="g12927"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(796.72441,4.686614)"
         x="0"
         y="16.973877"
         id="text12925"><tspan
           x="0"
           y="16.973877"
           id="tspan12923"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12921">NIT. 901.356.384 – 1</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath124)"
       id="g12935"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(686.58898,30.462992)"
         x="0"
         y="16.973877"
         id="text12933"><tspan
           x="0"
           y="16.973877"
           id="tspan12931"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12929">Carrera 13ª N° 28 – 38 oficina 241 C.E Bavaria </tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath125)"
       id="g12943"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(785.00787,51.552756)"
         x="0"
         y="16.973877"
         id="text12941"><tspan
           x="0"
           y="16.973877"
           id="tspan12939"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12937">Teléfonos 3133184230 </tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath126)"
       id="g12951"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(640.89449,74.985827)"
         x="0"
         y="16.973877"
         id="text12949"><tspan
           x="0"
           y="16.973877"
           id="tspan12947"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12945">Email:  gerencia@qcsas.com; director.tecnico@qcsas.com</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath127)"
       id="g12959"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1347.4016,4.686614)"
         x="0"
         y="16.973877"
         id="text12957"><tspan
           x="0"
           y="16.973877"
           id="tspan12955"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12953">CODIGO: SGQC-PGT-FT-03</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath128)"
       id="g12967"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1413.0142,30.462992)"
         x="0"
         y="16.973877"
         id="text12965"><tspan
           x="0"
           y="16.973877"
           id="tspan12963"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12961">EDICION: 01</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath129)"
       id="g12975"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1381.3795,51.552756)"
         x="0"
         y="16.973877"
         id="text12973"><tspan
           x="0"
           y="16.973877"
           id="tspan12971"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#404040"
             id="tspan12969">FECHA: 2022-02-01</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath130)"
       id="g12983"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1329.8268,86.702362)"
         x="0"
         y="16.973877"
         id="text12981"><tspan
           x="0"
           y="16.973877"
           id="tspan12979"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:18.75px;font-family:Arial;fill:#0070c0"
             id="tspan12977">REVISION PARCIAL N° 000{id}</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath131)"
       id="g12991"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(813.12756,98.418898)"
         x="0"
         y="13.171875"
         id="text12989"><tspan
           x="0"
           y="13.171875"
           id="tspan12987"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Calibri;fill:#0563c1"
             id="tspan12985">WWW.QCSAS.COM</tspan></tspan></text></g><path
       style="fill:#0563c1;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath131)"
       d="m 813.12756,117.16535 h 138.25512 v 1.17166 H 813.12756 Z"
       id="path12993"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><g
       clip-path="url(#clipEmfPath132)"
       id="g13001"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,534.27402)"
         x="0"
         y="15.898865"
         id="text12999"><tspan
           x="0"
           y="15.898865"
           id="tspan12997"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan12995">CRITERIOS DE INSPECCION: Resolucion 40245 del 16 de marzo del 2016 Numeral 10.1 y 10.3 de Ministerio de Minas y Energia</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath133)"
       id="g13009"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(24.604724,565.90866)"
         x="0"
         y="15.898865"
         id="text13007"><tspan
           x="0"
           y="15.898865"
           id="tspan13005"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13003">Ubicación </tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath134)"
       id="g13017"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(523.72913,565.90866)"
         x="0"
         y="15.898865"
         id="text13015"><tspan
           x="0"
           y="15.898865"
           id="tspan13013"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13011">Revisión</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath136)"
       id="g13033"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(1470.4252,406.56378)"
         x="0"
         y="15.898865"
         id="text13031"><tspan
           x="0"
           y="15.898865"
           id="tspan13029"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13027">galones de agua</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath137)"
       id="g13041"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(913.88976,407.73543)"
         x="0"
         y="13.80542"
         id="text13039"><tspan
           x="0"
           y="13.80542"
           id="tspan13037"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan13035">Capacidad Nominal</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath138)"
       id="g13049"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(922.09134,496.7811)"
         x="0"
         y="13.80542"
         id="text13047"><tspan
           x="0"
           y="13.80542"
           id="tspan13045"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan13043">Número de Serie:</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath139)"
       id="g13057"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,317.51811)"
         x="0"
         y="15.898865"
         id="text13055"><tspan
           x="0"
           y="15.898865"
           id="tspan13053"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13051">NIT o C.C:</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath140)"
       id="g13065"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,362.04095)"
         x="0"
         y="15.898865"
         id="text13063"><tspan
           x="0"
           y="15.898865"
           id="tspan13061"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13059">Usuario:</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath141)"
       id="g13073"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,406.56378)"
         x="0"
         y="15.898865"
         id="text13071"><tspan
           x="0"
           y="15.898865"
           id="tspan13069"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13067">Dirección:</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath143)"
       id="g13089"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(945.52441,452.25827)"
         x="0"
         y="13.80542"
         id="text13087"><tspan
           x="0"
           y="13.80542"
           id="tspan13085"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan13083">Fabricante:</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath145)"
       id="g13105"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,220.27087)"
         x="0"
         y="13.171875"
         id="text13103"><tspan
           x="0"
           y="13.171875"
           id="tspan13101"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan13099">FECHA DE INSPECCION: </tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath146)"
       id="g13113"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:24.625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(697.13386,144.11339)"
         x="0"
         y="18.46875"
         id="text13111"><tspan
           x="0"
           y="18.46875"
           id="tspan13109"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:24.625px;font-family:Calibri;fill:#000000"
             id="tspan13107">INFORME DE INSPECCION</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath147)"
       id="g13121"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:24.625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(522.55748,176.91968)"
         x="0"
         y="18.46875"
         id="text13119"><tspan
           x="0"
           y="18.46875"
           id="tspan13117"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:24.625px;font-family:Calibri;fill:#000000"
             id="tspan13115">REVISION PARCIAL DE TANQUES ESTACIONARIOS PARA GLP</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath148)"
       id="g13129"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:22.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(988.87559,217.92756)"
         x="0"
         y="20.142334"
         id="text13127"><tspan
           x="0"
           y="20.142334"
           id="tspan13125"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:22.25px;font-family:Arial;fill:#000000"
             id="tspan13123">DATOS DEL CLIENTE</tspan></tspan></text></g><g
       clip-path="url(#clipEmfPath149)"
       id="g13137"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(3.514961,267.13701)"
         x="0"
         y="15.898865"
         id="text13135"><tspan
           x="0"
           y="15.898865"
           id="tspan13133"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Arial;fill:#000000"
             id="tspan13131">Propietario:</tspan></tspan></text></g><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 0,0 V 209.72598"
       id="path13155"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 0,0 H 1.1716535 V 209.72598 H 0 Z"
       id="path13157"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1655.5465,1.1716535 V 209.72598"
       id="path13159"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,1.1716535 h 1.1716 V 209.72598 h -1.1716 z"
       id="path13161"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,249.5622 H 553.02047"
       id="path13163"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,249.5622 H 553.02047 v 1.17166 H 1.1716535 Z"
       id="path13165"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 133.5685,250.73386 V 529.5874"
       id="path13167"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,250.73386 h 1.17166 V 529.5874 h -1.17166 z"
       id="path13169"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 842.4189,351.49606 V 529.5874"
       id="path13171"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 842.4189,351.49606 h 1.17165 V 529.5874 h -1.17165 z"
       id="path13173"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1130.6457,396.0189 V 529.5874"
       id="path13175"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1130.6457,396.0189 h 1.1716 v 133.5685 h -1.1716 z"
       id="path13177"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,396.0189 v 44.52283"
       id="path13179"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,396.0189 h 1.1717 v 44.52283 h -1.1717 z"
       id="path13181"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 353.83937,561.22205 v 31.63464"
       id="path13183"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 353.83937,561.22205 h 1.17165 v 31.63464 h -1.17165 z"
       id="path13185"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 553.02047,212.06929 h 2.34331 v 38.66457 h -2.34331 z"
       id="path13187"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,561.22205 v 58.58267"
       id="path13189"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,561.22205 h 1.1717 v 58.58267 h -1.1717 z"
       id="path13191"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,561.22205 v 58.58267"
       id="path13193"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,561.22205 h 1.1717 v 58.58267 h -1.1717 z"
       id="path13195"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 420.62362,561.22205 v 58.58267"
       id="path13197"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 420.62362,561.22205 h 1.17166 v 58.58267 h -1.17166 z"
       id="path13199"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 487.40787,592.85669 v 26.94803"
       id="path13201"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 487.40787,592.85669 h 1.17166 v 26.94803 h -1.17166 z"
       id="path13203"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,561.22205 v 58.58267"
       id="path13205"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,561.22205 h 1.17166 v 58.58267 h -1.17166 z"
       id="path13207"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,686.58898 v 216.7559"
       id="path13209"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,686.58898 h 1.17166 v 216.7559 h -1.17166 z"
       id="path13211"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,1076.7496 v 371.4142"
       id="path13213"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,1076.7496 h 1.17166 v 371.4142 h -1.17166 z"
       id="path13215"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1418.8724,646.75276 V 1448.1638"
       id="path13217"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,646.75276 h 1.1717 v 801.41104 h -1.1717 z"
       id="path13219"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1537.2094,646.75276 V 1448.1638"
       id="path13221"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,646.75276 h 1.1717 v 801.41104 h -1.1717 z"
       id="path13223"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,1491.515 v 210.8976"
       id="path13225"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,1491.515 h 1.1717 v 210.8976 h -1.1717 z"
       id="path13227"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,1491.515 v 210.8976"
       id="path13229"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,1491.515 h 1.1717 v 210.8976 h -1.1717 z"
       id="path13231"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,1745.7638 v 260.1071"
       id="path13233"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,1745.7638 h 1.1717 v 260.1071 h -1.1717 z"
       id="path13235"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,1745.7638 v 260.1071"
       id="path13237"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,1745.7638 h 1.1717 v 260.1071 h -1.1717 z"
       id="path13239"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 0,212.06929 V 2217.9402"
       id="path13241"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 0,212.06929 H 1.1716535 V 2217.9402 H 0 Z"
       id="path13243"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1655.5465,212.06929 V 2217.9402"
       id="path13245"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,212.06929 h 1.1716 V 2217.9402 h -1.1716 z"
       id="path13247"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2220.2835 v 21.0897"
       id="path13249"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2220.2835 h 1.1716535 v 21.0897 H 0 Z"
       id="path13251"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2220.2835 v 21.0897"
       id="path13253"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2220.2835 h 1.1716 v 21.0897 h -1.1716 z"
       id="path13255"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2243.7165 v 91.389"
       id="path13257"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2243.7165 h 1.1716535 v 91.389 H 0 Z"
       id="path13259"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2243.7165 v 91.389"
       id="path13261"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2243.7165 h 1.1716 v 91.389 h -1.1716 z"
       id="path13263"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2337.4488 v 21.0898"
       id="path13265"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2337.4488 h 1.1716535 v 21.0898 H 0 Z"
       id="path13267"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 353.83937,646.75276 V 2179.2756"
       id="path13269"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 353.83937,646.75276 h 1.17165 V 2179.2756 h -1.17165 z"
       id="path13271"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 420.62362,666.67087 V 2179.2756"
       id="path13273"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 420.62362,666.67087 h 1.17166 V 2179.2756 h -1.17166 z"
       id="path13275"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 842.4189,561.22205 v 58.58267"
       id="path13277"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 842.4189,561.22205 h 1.17165 v 58.58267 h -1.17165 z"
       id="path13279"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1130.6457,561.22205 v 58.58267"
       id="path13281"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1130.6457,561.22205 h 1.1716 v 58.58267 h -1.1716 z"
       id="path13283"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1274.7591,561.22205 v 58.58267"
       id="path13285"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1274.7591,561.22205 h 1.1716 v 58.58267 h -1.1716 z"
       id="path13287"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2337.4488 v 21.0898"
       id="path13289"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2337.4488 h 1.1716 v 21.0898 h -1.1716 z"
       id="path13291"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2360.8819 v 23.4331"
       id="path13293"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2360.8819 h 1.1716535 v 23.4331 H 0 Z"
       id="path13295"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 487.40787,666.67087 V 2179.2756"
       id="path13297"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 487.40787,666.67087 h 1.17166 V 2179.2756 h -1.17166 z"
       id="path13299"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2360.8819 v 23.4331"
       id="path13301"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2360.8819 h 1.1716 v 23.4331 h -1.1716 z"
       id="path13303"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2386.6583 v 36.3212"
       id="path13305"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2386.6583 h 1.1716535 v 36.3212 H 0 Z"
       id="path13307"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2386.6583 v 36.3212"
       id="path13309"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2386.6583 h 1.1716 v 36.3212 h -1.1716 z"
       id="path13311"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2425.3228 v 36.3213"
       id="path13313"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2425.3228 h 1.1716535 v 36.3213 H 0 Z"
       id="path13315"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 274.16693,561.22205 v 58.58267"
       id="path13317"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 274.16693,561.22205 h 1.17165 v 58.58267 h -1.17165 z"
       id="path13319"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 698.30551,561.22205 v 58.58267"
       id="path13321"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 698.30551,561.22205 h 1.17166 v 58.58267 h -1.17166 z"
       id="path13323"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2425.3228 v 36.3213"
       id="path13325"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2425.3228 h 1.1716 v 36.3213 h -1.1716 z"
       id="path13327"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2463.9874 v 31.6346"
       id="path13329"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2463.9874 h 1.1716535 v 31.6346 H 0 Z"
       id="path13331"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2463.9874 v 31.6346"
       id="path13333"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2463.9874 h 1.1716 v 31.6346 h -1.1716 z"
       id="path13335"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2497.9654 v 23.433"
       id="path13337"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2497.9654 h 1.1716535 v 23.433 H 0 Z"
       id="path13339"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2523.7417 v 23.4331"
       id="path13341"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2523.7417 h 1.1716535 v 23.4331 H 0 Z"
       id="path13343"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2549.5181 v 23.4331"
       id="path13345"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2549.5181 h 1.1716535 v 23.4331 H 0 Z"
       id="path13347"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2575.2945 v 23.4331"
       id="path13349"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2575.2945 h 1.1716535 v 23.4331 H 0 Z"
       id="path13351"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2598.7276 h 275.33858 v 2.3433 H 0 Z"
       id="path13353"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 841.24724,2360.8819 h 2.34331 v 25.7764 h -2.34331 z"
       id="path13355"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2497.9654 v 100.7622"
       id="path13357"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2497.9654 h 1.1716 v 100.7622 h -1.1716 z"
       id="path13359"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2601.0709 v 23.433"
       id="path13361"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2601.0709 h 1.1716535 v 23.433 H 0 Z"
       id="path13363"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2624.5039 h 275.33858 v 2.3433 H 0 Z"
       id="path13365"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2626.8472 v 23.4331"
       id="path13367"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2626.8472 h 1.1716535 v 23.4331 H 0 Z"
       id="path13369"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2601.0709 v 49.2094"
       id="path13371"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2601.0709 h 1.1716 v 49.2094 h -1.1716 z"
       id="path13373"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2652.6236 v 209.726"
       id="path13375"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2652.6236 h 1.1716535 v 209.726 H 0 Z"
       id="path13377"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2652.6236 v 209.726"
       id="path13379"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1655.5465,2652.6236 h 1.1716 v 209.726 h -1.1716 z"
       id="path13381"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 554.19213,646.75276 V 2179.2756"
       id="path13383"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 554.19213,646.75276 h 1.17165 V 2179.2756 h -1.17165 z"
       id="path13385"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.534149"
       y="93.567505"
       id="text2073-3"><tspan
         id="tspan2071-6"
         style="stroke-width:0.557"
         x="75.534149"
         y="93.567505">{str(JSONtank_identification['agrietamiento']["comentario"]) if JSONtank_identification['agrietamiento']["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="99.105446"
       id="text2073-34"><tspan
         id="tspan2071-67"
         style="stroke-width:0.557"
         x="75.416817"
         y="99.105446">{str(JSONtank_identification['porosidad']["comentario"]) if JSONtank_identification['porosidad']["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="104.36465"
       id="text2073-8"><tspan
         id="tspan2071-3"
         style="stroke-width:0.557"
         x="75.416817"
         y="104.36465">{str(JSONtank_identification['salpicadura']["comentario"]) if JSONtank_identification['salpicadura']["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="109.87431"
       id="text2073-4"><tspan
         id="tspan2071-9"
         style="stroke-width:0.557"
         x="75.416817"
         y="109.87431">{str(JSONtank_identification['socavado']["comentario"]) if JSONtank_identification['socavado']["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="106.93966"
       y="115.38396"
       id="text2073-31"><tspan
         id="tspan2071-0"
         style="stroke-width:0.557"
         x="106.93966"
         y="115.38396">{str(JSONtank_identification["abolladura"]["1"]["comentario"]) if JSONtank_identification["abolladura"]["1"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="131.95941"
       y="120.36444"
       id="text2073-5"><tspan
         id="tspan2071-1"
         style="stroke-width:0.557"
         x="131.95941"
         y="120.36444">{str(JSONtank_identification["abolladura"]["2"]["comentario"]) if JSONtank_identification["abolladura"]["2"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="132.18156"
       y="125.87409"
       id="text2073-46"><tspan
         id="tspan2071-7"
         style="stroke-width:0.557"
         x="132.18156"
         y="127.47409">{str(JSONtank_identification["abolladura"]["3"]["comentario"]) if JSONtank_identification["abolladura"]["3"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="112.78462"
       y="131.16159"
       id="text2073-1"><tspan
         id="tspan2071-37"
         style="stroke-width:0.557"
         x="112.78462"
         y="131.16159">{str(JSONtank_identification["abombamiento"]["comentario"]) if JSONtank_identification["abombamiento"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="133.54279"
       y="135.39078"
       id="text2073-47"><tspan
         id="tspan2071-03"
         style="stroke-width:0.557"
         x="133.54279"
         y="135.39078">{str(JSONtank_identification["corrosionAislada"]["1"]["comentario"]) if JSONtank_identification["corrosionAislada"]["1"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="124.93887"
       y="138.42432"
       id="text2073-51"><tspan
         id="tspan2071-4"
         style="stroke-width:0.557"
         x="124.93887"
         y="138.42432">{str(JSONtank_identification["corrosionAislada"]["2"]["comentario"]) if JSONtank_identification["corrosionAislada"]["2"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="116.12518"
       y="141.17914"
       id="text2073-2"><tspan
         id="tspan2071-35"
         style="stroke-width:0.557"
         x="116.12518"
         y="141.17914">{str(JSONtank_identification["corrosionEnLinea"]["1"]["comentario"]) if JSONtank_identification["corrosionEnLinea"]["1"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="116.64228"
       y="144.05919"
       id="text2073-58"><tspan
         id="tspan2071-671"
         style="stroke-width:0.557"
         x="116.64228"
         y="144.05919">{str(JSONtank_identification["corrosionEnLinea"]["2"]["comentario"]) if JSONtank_identification["corrosionEnLinea"]["2"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="122.02671"
       y="146.43837"
       id="text2073-89"><tspan
         id="tspan2071-42"
         style="stroke-width:0.557"
         x="122.02671"
         y="146.43837">{str(JSONtank_identification["corrosionEnLinea"]["3"]["comentario"]) if JSONtank_identification["corrosionEnLinea"]["3"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="119.27189"
       y="149.31841"
       id="text2073-13"><tspan
         id="tspan2071-31"
         style="stroke-width:0.557"
         x="119.27189"
         y="149.31841">{str(JSONtank_identification["corrosionGeneral"]["1"]["comentario"]) if JSONtank_identification["corrosionGeneral"]["1"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="122.02671"
       y="152.07323"
       id="text2073-6"><tspan
         id="tspan2071-60"
         style="stroke-width:0.557"
         x="122.02671"
         y="152.07323">{str(JSONtank_identification["corrosionGeneral"]["2"]["comentario"]) if JSONtank_identification["corrosionGeneral"]["2"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="110.13087"
       y="154.70284"
       id="text2073-85"><tspan
         id="tspan2071-04"
         style="stroke-width:0.557"
         x="110.13087"
         y="154.70284">{str(JSONtank_identification["AccionPorFuego"]["1"]["comentario"]) if JSONtank_identification["AccionPorFuego"]["1"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="110.50652"
       y="157.45766"
       id="text2073-83"><tspan
         id="tspan2071-2"
         style="stroke-width:0.557"
         x="110.50652"
         y="157.45766">{str(JSONtank_identification["AccionPorFuego"]["2"]["comentario"]) if JSONtank_identification["AccionPorFuego"]["2"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.138092"
       y="161.71512"
       id="text2073-517"><tspan
         id="tspan2071-5"
         style="stroke-width:0.557"
         x="75.138092"
         y="161.71512">{str(JSONtank_identification["EstadoConexionCorrosion"]["comentario"]) if JSONtank_identification["EstadoConexionCorrosion"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.138092"
       y="167.22478"
       id="text2073-80"><tspan
         id="tspan2071-78"
         style="stroke-width:0.557"
         x="75.138092"
         y="167.22478">{str(JSONtank_identification["EstadoConexionEvidenciaGolpes"]["comentario"]) if JSONtank_identification["EstadoConexionEvidenciaGolpes"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.166382"
       y="172.23355"
       id="text2073-50"><tspan
         id="tspan2071-38"
         style="stroke-width:0.557"
         x="75.166382"
         y="172.23355">{str(JSONtank_identification["EstadoConexionDesgaste"]["comentario"]) if JSONtank_identification["EstadoConexionDesgaste"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="177.46448"
       id="text2073-0"><tspan
         id="tspan2071-08"
         style="stroke-width:0.557"
         x="75.416817"
         y="177.46448">{str(JSONtank_identification["EstadoConexionOtros"]["comentario"]) if JSONtank_identification["EstadoConexionOtros"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.388527"
       y="187.76074"
       id="text2073-9"><tspan
         id="tspan2071-29"
         style="stroke-width:0.557"
         x="75.388527"
         y="187.76074">{str(JSONquestion_views["soportetanque"]["comentario"]) if JSONquestion_views["soportetanque"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="192.54736"
       id="text2073-95"><tspan
         id="tspan2071-99"
         style="stroke-width:0.557"
         x="75.416817"
         y="192.54736">{str(JSONquestion_views["domoprotector"]["comentario"]) if JSONquestion_views["domoprotector"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="196.52609"
       id="text2073-86"><tspan
         id="tspan2071-8"
         style="stroke-width:0.557"
         x="75.416817"
         y="196.52609">{str(JSONquestion_views["orejasizaminto"]["comentario"]) if JSONquestion_views["orejasizaminto"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.416817"
       y="200.78355"
       id="text2073-589"><tspan
         id="tspan2071-316"
         style="stroke-width:0.557"
         x="75.416817"
         y="200.78355">{str(JSONquestion_views["pintura"]["comentario"]) if JSONquestion_views["pintura"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.667259"
       y="205.79233"
       id="text2073-49"><tspan
         id="tspan2071-01"
         style="stroke-width:0.557"
         x="75.667259"
         y="205.79233">{str(JSONquestion_views["proteccioncatodica"]["comentario"]) if JSONquestion_views["proteccioncatodica"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.667259"
       y="209.77107"
       id="text2073-7"><tspan
         id="tspan2071-44"
         style="stroke-width:0.557"
         x="75.667259"
         y="209.77107">{str(JSONquestion_views["continuidad"]["comentario"]) if JSONquestion_views["continuidad"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.138092"
       y="219.81689"
       id="text2073-18"><tspan
         id="tspan2071-449"
         style="stroke-width:0.557"
         x="75.138092"
         y="219.81689">{str(JSONquestions_deterioration["tuberiadefectosoldadura"]["comentario"]) if JSONquestions_deterioration["tuberiadefectosoldadura"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.138092"
       y="225.32655"
       id="text2073-10"><tspan
         id="tspan2071-27"
         style="stroke-width:0.557"
         x="75.138092"
         y="225.32655">{str(JSONquestions_deterioration["tuberiapresentacorrosion"]["comentario"]) if JSONquestions_deterioration["tuberiapresentacorrosion"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.138092"
       y="230.08488"
       id="text2073-79"><tspan
         id="tspan2071-25"
         style="stroke-width:0.557"
         x="75.138092"
         y="230.08488">{str(JSONquestions_deterioration["tuberiapresentafisura"]["comentario"]) if JSONquestions_deterioration["tuberiapresentafisura"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.166382"
       y="235.3441"
       id="text2073-43"><tspan
         id="tspan2071-97"
         style="stroke-width:0.557"
         x="75.166382"
         y="235.3441">{str(JSONquestions_deterioration["tuberiaaplastamiento"]["comentario"]) if JSONquestions_deterioration["tuberiaaplastamiento"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.166382"
       y="240.85374"
       id="text2073-70"><tspan
         id="tspan2071-447"
         style="stroke-width:0.557"
         x="75.166382"
         y="240.85374">{str(JSONquestions_deterioration["roscaencuentrabuenestado"]["comentario"]) if JSONquestions_deterioration["roscaencuentrabuenestado"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.445107"
       y="246.61383"
       id="text2073-854"><tspan
         id="tspan2071-84"
         style="stroke-width:0.557"
         x="75.445107"
         y="246.61383">{str(JSONquestions_deterioration["accesoriosencuentrabuenestado"]["comentario"]) if JSONquestions_deterioration["accesoriosencuentrabuenestado"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.194672"
       y="257.38272"
       id="text2073-33"><tspan
         id="tspan2071-66"
         style="stroke-width:0.557"
         x="75.194672"
         y="257.38272">{str(JSONobservations_and_results["estadovalvulas"]["comentario"]) if JSONobservations_and_results["estadovalvulas"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.445107"
       y="263.17108"
       id="text2073-315"><tspan
         id="tspan2071-26"
         style="stroke-width:0.557"
         x="75.445107"
         y="263.17108">{str(JSONobservations_and_results["estadovalvulasalivio"]["comentario"]) if JSONobservations_and_results["estadovalvulasalivio"]["comentario"] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="75.194672"
       y="268.37372"
       id="text2073-61"><tspan
         id="tspan2071-56"
         style="stroke-width:0.557"
         x="75.194672"
         y="268.37372">{str(JSONobservations_and_results["estadoindicadornivel"]["comentario"]) if JSONobservations_and_results["estadoindicadornivel"]["comentario"] != None else ""}</tspan></text><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,1491.515 v 210.8976"
       id="path13387"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 133.5685,1491.515 h 1.17166 v 210.8976 h -1.17166 z"
       id="path13389"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 841.24724,2601.0709 h 2.34331 v 51.5527 h -2.34331 z"
       id="path13391"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1129.474,2360.8819 h 2.3433 v 25.7764 h -2.3433 z"
       id="path13393"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,2049.222 v 130.0536"
       id="path13395"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1418.8724,2049.222 h 1.1717 v 130.0536 h -1.1717 z"
       id="path13397"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 224.95748,561.22205 v 85.53071"
       id="path13399"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 224.95748,561.22205 h 1.17165 v 85.53071 h -1.17165 z"
       id="path13401"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 272.99528,2463.9874 h 2.3433 v 188.6362 h -2.3433 z"
       id="path13403"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 352.66772,2360.8819 h 2.3433 v 25.7764 h -2.3433 z"
       id="path13405"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 419.45197,2360.8819 h 2.34331 v 64.4409 h -2.34331 z"
       id="path13407"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 697.13386,2463.9874 h 2.34331 v 188.6362 h -2.34331 z"
       id="path13409"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 986.53228,561.22205 v 31.63464"
       id="path13411"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 986.53228,561.22205 h 1.17166 v 31.63464 h -1.17166 z"
       id="path13413"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1273.5874,2360.8819 h 2.3433 v 25.7764 h -2.3433 z"
       id="path13415"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,2049.222 v 130.0536"
       id="path13417"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 1537.2094,2049.222 h 1.1717 v 130.0536 h -1.1717 z"
       id="path13419"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 486.23622,2386.6583 h 2.34331 v 38.6645 h -2.34331 z"
       id="path13421"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,0 H 1656.7181"
       id="path13423"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,0 H 1656.7181 V 1.1716535 H 1.1716535 Z"
       id="path13425"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,209.72598 h 1656.7181 v 2.34331 H 0 Z"
       id="path13427"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 555.36378,249.5622 H 1656.7181"
       id="path13429"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 555.36378,249.5622 H 1656.7181 v 1.17166 H 555.36378 Z"
       id="path13431"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,305.80157 H 1656.7181"
       id="path13433"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,305.80157 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13435"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,350.32441 H 1656.7181"
       id="path13437"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,350.32441 H 1656.7181 v 1.17165 H 1.1716535 Z"
       id="path13439"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,394.84724 H 1656.7181"
       id="path13441"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,394.84724 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13443"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,439.37008 H 1656.7181"
       id="path13445"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,439.37008 H 1656.7181 v 1.17165 H 1.1716535 Z"
       id="path13447"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,483.89291 H 1656.7181"
       id="path13449"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,483.89291 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13451"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,528.41575 H 1656.7181"
       id="path13453"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,528.41575 H 1656.7181 v 1.17165 H 1.1716535 Z"
       id="path13455"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,560.05039 H 1656.7181"
       id="path13457"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,560.05039 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13459"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,591.68504 H 1656.7181"
       id="path13461"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,591.68504 H 1656.7181 v 1.17165 H 1.1716535 Z"
       id="path13463"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,618.63307 H 1656.7181"
       id="path13465"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,618.63307 H 1656.7181 v 1.17165 H 1.1716535 Z"
       id="path13467"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,645.5811 H 1656.7181"
       id="path13469"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,645.5811 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13471"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 355.01102,665.49921 H 555.36378"
       id="path13473"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 355.01102,665.49921 h 200.35276 v 1.17166 H 355.01102 Z"
       id="path13475"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,685.41732 H 1656.7181"
       id="path13477"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,685.41732 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13479"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,728.7685 H 1656.7181"
       id="path13481"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,728.7685 H 1656.7181 v 1.17166 H 1.1716535 Z"
       id="path13483"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,772.11969 H 1656.7181"
       id="path13485"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,772.11969 H 1656.7181 v 1.17165 H 134.74016 Z"
       id="path13487"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,815.47087 H 1656.7181"
       id="path13489"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,815.47087 H 1656.7181 v 1.17165 H 134.74016 Z"
       id="path13491"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,858.82205 H 1656.7181"
       id="path13493"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,858.82205 H 1656.7181 v 1.17165 H 134.74016 Z"
       id="path13495"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,902.17323 H 1656.7181"
       id="path13497"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,902.17323 H 1656.7181 v 1.17165 H 1.1716535 Z"
       id="path13499"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 355.01102,945.52441 H 1656.7181"
       id="path13501"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 355.01102,945.52441 H 1656.7181 v 1.17165 H 355.01102 Z"
       id="path13503"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 355.01102,988.87559 H 1656.7181"
       id="path13505"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 355.01102,988.87559 H 1656.7181 v 1.17165 H 355.01102 Z"
       id="path13507"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1032.2268 H 1656.7181"
       id="path13509"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1032.2268 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13511"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1075.578 H 1656.7181"
       id="path13513"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1075.578 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13515"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1118.9291 H 1656.7181"
       id="path13517"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1118.9291 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13519"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1186.885 H 1656.7181"
       id="path13521"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1186.885 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13523"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1230.2362 H 1656.7181"
       id="path13525"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1230.2362 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13527"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1273.5874 H 1656.7181"
       id="path13529"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1273.5874 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13531"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1316.9386 H 1656.7181"
       id="path13533"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1316.9386 H 1656.7181 v 1.1716 H 134.74016 Z"
       id="path13535"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1360.2898 H 1656.7181"
       id="path13537"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1360.2898 H 1656.7181 v 1.1716 H 134.74016 Z"
       id="path13539"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1403.6409 H 1656.7181"
       id="path13541"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1403.6409 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13543"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1446.9921 H 1656.7181"
       id="path13545"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1446.9921 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13547"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1490.3433 H 1656.7181"
       id="path13549"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1490.3433 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13551"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1525.4929 H 1656.7181"
       id="path13553"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1525.4929 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13555"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1560.6425 H 1656.7181"
       id="path13557"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1560.6425 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13559"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1595.7921 H 1656.7181"
       id="path13561"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1595.7921 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13563"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1630.9417 H 1656.7181"
       id="path13565"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1630.9417 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13567"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1666.0913 H 1656.7181"
       id="path13569"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 134.74016,1666.0913 H 1656.7181 v 1.1717 H 134.74016 Z"
       id="path13571"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1701.2409 H 1656.7181"
       id="path13573"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1701.2409 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13575"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1744.5921 H 1656.7181"
       id="path13577"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1744.5921 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13579"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1787.9433 H 1656.7181"
       id="path13581"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1787.9433 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13583"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1831.2945 H 1656.7181"
       id="path13585"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1831.2945 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13587"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1874.6457 H 1656.7181"
       id="path13589"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1874.6457 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13591"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1917.9969 H 1656.7181"
       id="path13593"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1917.9969 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13595"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1961.348 H 1656.7181"
       id="path13597"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,1961.348 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13599"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2004.6992 H 1656.7181"
       id="path13601"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2004.6992 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13603"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2048.0504 H 1656.7181"
       id="path13605"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2048.0504 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13607"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2091.4016 H 1656.7181"
       id="path13609"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2091.4016 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13611"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2134.7528 H 1656.7181"
       id="path13613"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2134.7528 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13615"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2178.1039 H 1656.7181"
       id="path13617"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2178.1039 H 1656.7181 v 1.1717 H 1.1716535 Z"
       id="path13619"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2217.9402 h 1656.7181 v 2.3433 H 0 Z"
       id="path13621"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2241.3732 h 1656.7181 v 2.3433 H 0 Z"
       id="path13623"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2335.1055 h 1656.7181 v 2.3433 H 0 Z"
       id="path13625"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2358.5386 h 1656.7181 v 2.3433 H 0 Z"
       id="path13627"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2384.315 h 1656.7181 v 2.3433 H 0 Z"
       id="path13629"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2422.9795 h 1656.7181 v 2.3433 H 0 Z"
       id="path13631"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2461.6441 h 1656.7181 v 2.3433 H 0 Z"
       id="path13633"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2495.622 h 1656.7181 v 2.3434 H 0 Z"
       id="path13635"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2521.3984 h 275.33858 v 2.3433 H 0 Z"
       id="path13637"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2547.1748 h 275.33858 v 2.3433 H 0 Z"
       id="path13639"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2572.9512 h 275.33858 v 2.3433 H 0 Z"
       id="path13641"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 699.47717,2598.7276 h 957.24093 v 2.3433 H 699.47717 Z"
       id="path13643"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 699.47717,2624.5039 h 144.11338 v 2.3433 H 699.47717 Z"
       id="path13645"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="m 0,2650.2803 h 1656.7181 v 2.3433 H 0 Z"
       id="path13647"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:none;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2861.178 H 1656.7181"
       id="path13649"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1.17165px;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       clip-path="url(#clipEmfPath1)"
       d="M 1.1716535,2861.178 H 1656.7181 v 1.1716 H 1.1716535 Z"
       id="path13651"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="M -1.1716535,-1.1716535 H 1657.8898 V 2.3433071 H -1.1716535 Z"
       id="path13653"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:none"
       clip-path="url(#clipEmfPath2)"
       d="M -1.1716535,2860.0063 H 1657.8898 v 3.515 H -1.1716535 Z"
       id="path13655"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-opacity:1"
       clip-path="url(#clipEmfPath2)"
       d="M -1.1716535,-1.1716535 H 2.3433071 V 2863.5213 h -3.5149606 z"
       id="path13657"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><path
       style="fill:#000000;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-opacity:1"
       clip-path="url(#clipEmfPath2)"
       d="m 1654.3748,-1.1716535 h 3.515 V 2863.5213 h -3.515 z"
       id="path13659"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)" /><g
       id="g15703-5"
       style="stroke:#000000;stroke-opacity:1"
       transform="translate(83.164521,9.2156325)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1" /><g
         id="g15698-7"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19" /></g></g><g
       id="g15703-5-1"
       style="stroke:#000000;stroke-opacity:1"
       transform="translate(83.164521,36.174921)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4" /><g
         id="g15698-7-9"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8" /></g></g><g
       id="g15703-5-1-4"
       style="stroke:#000000;stroke-opacity:1"
       transform="translate(83.14213,41.638431)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2" /><g
         id="g15698-7-9-3"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1" /></g></g><g
       id="g13759"
       transform="matrix(0.13030134,0,0,0.12421712,0.00411059,2.7917926e-4)"><rect
         style="clip-rule:nonzero;display:inline;overflow:visible;visibility:visible;color-interpolation:sRGB;color-interpolation-filters:linearRGB;fill:#ffffff;stroke:none;stroke-dasharray:none;marker:none;enable-background:accumulate"
         width="88.987335"
         height="11.422485"
         x="0"
         y="-11.259552"
         transform="translate(147.61353,101.2038)"
         id="rect13757" /></g><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:400;font-size:2.23436px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.127223"
       x="18.783827"
       y="12.875729"
       id="text13765"
       transform="scale(1.0241975,0.97637415)"><tspan
         x="18.783827"
         y="12.875729"
         id="tspan13763"
         style="stroke-width:0.127223"><tspan
           dx="0"
           dy="0"
           style="font-style:normal;font-variant:normal;font-weight:400;font-size:2.23436px;font-family:Calibri;fill:#000000;stroke-width:0.127223"
           id="tspan13761">SELLO ONAC</tspan></tspan></text><g
       id="g15703-5-1-4-4"
       style="stroke:#000000;stroke-opacity:1"
       transform="translate(83.209304,46.810852)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-9" /><g
         id="g15698-7-9-3-1"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-1" /></g></g><g
       id="g15703-5-1-4-7"
       style="stroke:#000000;stroke-opacity:1"
       transform="translate(83.14213,52.050448)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-5" /><g
         id="g15698-7-9-3-9"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-2" /></g></g><g
       id="g15703-5-1-4-43"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0068089,0,0,0.76531115,82.444503,74.880612)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-50" /><g
         id="g15698-7-9-3-3"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-19" /></g></g><g
       id="g15703-5-1-4-76"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.49733,76.038519)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90" /><g
         id="g15698-7-9-3-10"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22" /></g></g><g
       id="g15703-5-1-4-76-4"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.474943,87.446955)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-0" /><g
         id="g15698-7-9-3-10-8"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-3" /></g></g><g
       id="g15703-5-1-4-76-3"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.474943,89.865231)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-5" /><g
         id="g15698-7-9-3-10-58"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-4" /></g></g><g
       id="g15703-5-1-4-76-40"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.519725,92.8209)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-06" /><g
         id="g15698-7-9-3-10-56"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-8" /></g></g><g
       id="g15703-5-1-4-76-2"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,82.564508,95.373523)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-15" /><g
         id="g15698-7-9-3-10-88"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-88" /></g></g><g
       id="g15703-5-1-4-76-49"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-28.900055,241.94786)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-55" /><g
         id="g15698-7-9-3-10-82"
         style="stroke:#000000;stroke-opacity:1">{'''<path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-20" />'''  if JSONquestions_mtto['fotografia'] == True else " " }</g></g><g
       id="g15703-5-1-4-76-75"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-10.85256,241.94786)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-8" /><g
         id="g15698-7-9-3-10-4"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-6" /></g></g><g
       id="g15703-5-1-4-76-6"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-81.833407,262.90624)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-81" /><g
         id="g15698-7-9-3-10-588"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-31" /></g></g><g
       id="g15703-5-1-4-76-9"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-81.788627,259.72666)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-4" /><g
         id="g15698-7-9-3-10-81"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-5" /></g></g><g
       id="g15703-5-1-4-76-1"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-81.833407,256.63664)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-9" /><g
         id="g15698-7-9-3-10-6"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-61" /></g></g><g
       id="g15703-5-1-4-76-0"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-81.833413,253.50185)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-78" /><g
         id="g15698-7-9-3-10-86"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-7" /></g></g><g
       id="g15703-5-1-4-76-34"
       style="stroke:#000000;stroke-opacity:1"
       transform="matrix(1.0062762,0,0,0.78219543,-81.833407,250.25509)"><path
         style="fill:none;stroke:#000000;stroke-width:0.195642px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:8;stroke-dasharray:none;stroke-opacity:1"
         d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
         id="path13679-1-4-2-90-98" /><g
         id="g15698-7-9-3-10-49"
         style="stroke:#000000;stroke-opacity:1"><path
           style="fill:#d9d9d9;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.127223;stroke-opacity:1"
           d="m 97.413256,77.807308 c 0,-0.227406 0.200374,-0.418424 0.438923,-0.418424 h 2.643061 c 0.23854,0 0.42938,0.191018 0.42938,0.418424 v 1.646414 c 0,0.227407 -0.19084,0.409332 -0.42938,0.409332 h -2.643061 c -0.238549,0 -0.438923,-0.181925 -0.438923,-0.409332 z"
           id="path13677-19-8-1-22-56" /></g></g><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:700;font-size:1.78573px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.117097"
       transform="scale(0.94268024,1.0608051)"
       x="58.391376"
       y="237.87152"
       id="text11753-8"><tspan
         x="58.391376"
         y="237.87152"
         id="tspan11751-3"
         style="stroke-width:0.117097">REGULAR</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="38.506187"
       y="29.322969"
       id="text30514"><tspan
         id="tspan30512"
         style="fill:#000000;stroke-width:0.306"
         x="38.506187"
         y="29.322969">{fecha_convertida}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="20.499691"
       y="34.865135"
       id="text30518"><tspan
         id="tspan30516"
         style="stroke-width:0.306"
         x="20.499691"
         y="34.865135">{companie.name}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="20.485865"
       y="41.447346"
       id="text30518-4"><tspan
         id="tspan30516-4"
         style="stroke-width:0.306"
         x="20.485865"
         y="41.447346">{companie.nit}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="20.488251"
       y="47.470985"
       id="text30518-6"><tspan
         id="tspan30516-0"
         style="stroke-width:0.306"
         x="20.488251"
         y="47.470985">{companieuser.usuario}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="20.467396"
       y="52.721764"
       id="text30518-1"><tspan
         id="tspan30516-5"
         style="stroke-width:0.306"
         x="20.467396"
         y="52.721764">{companieuser.address}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="20.629684"
       y="58.179844"
       id="text30518-7"><tspan
         id="tspan30516-06"
         style="stroke-width:0.306"
         x="20.629684"
         y="58.179844">{companieuser.phone}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="20.517611"
       y="63.585449"
       id="text30518-18"><tspan
         id="tspan30516-7"
         style="stroke-width:0.306"
         x="20.517611"
         y="63.585449">{companieuser.contact}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="165.06966"
       y="52.754219"
       id="text30619"><tspan
         id="tspan30617"
         style="stroke-width:0.306"
         x="165.06966"
         y="52.754219">{str(JSONtank_identification['capacidadNominal']) if JSONtank_identification['capacidadNominal'] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="161.35431"
       y="58.095707"
       id="text30518-5"><tspan
         id="tspan30516-46"
         style="stroke-width:0.306"
         x="161.35431"
         y="58.095707">{str(JSONtank_identification['fabricante']) if JSONtank_identification['fabricante'] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.64583px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="161.5766"
       y="63.770805"
       id="text30640"><tspan
         id="tspan30638"
         style="stroke-width:0.306"
         x="161.5766"
         y="63.770805">{str(JSONtank_identification['numeroSerie']) if JSONtank_identification['numeroSerie'] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="31.437572"
       y="72.637817"
       id="text30644"><tspan
         id="tspan30642"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="31.437572"
         y="72.637817">{ 'X' if JSONtank_identification['ubicacion'] == "Planta" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="48.831593"
       y="88.910789"
       id="text30644-35"><tspan
         id="tspan30642-37"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="48.831593"
         y="88.910789">{ 'X' if JSONtank_identification['hermeticidad']["presenta"] == "SÍ" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="144.97894"
       id="text30644-75"><tspan
         id="tspan30642-43"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="144.97894">{ 'X' if JSONtank_identification['corrosionEnLinea']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.146431"
       y="197.28534"
       id="text30644-85-1"><tspan
         id="tspan30642-905-0"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.146431"
         y="197.28534">{ 'X' if JSONquestion_views['orejasizaminto']["presenta"] == "Mal Estado" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.834305"
       y="197.28534"
       id="text30644-85-10"><tspan
         id="tspan30642-905-1"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.834305"
         y="197.28534">{ 'X' if JSONquestion_views['orejasizaminto']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.368988"
       y="201.40536"
       id="text30644-85-9"><tspan
         id="tspan30642-905-9"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.368988"
         y="201.40536">{ 'X' if JSONquestion_views['pintura']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.325562"
       y="201.40536"
       id="text30644-85-3"><tspan
         id="tspan30642-905-94"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.325562"
         y="201.40536">{ 'X' if JSONquestion_views['pintura']["presenta"] == "Mal Estado" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.744743"
       y="201.40536"
       id="text30644-85-90"><tspan
         id="tspan30642-905-3"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.744743"
         y="201.40536">{ 'X' if JSONquestion_views['pintura']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.189857"
       y="205.88365"
       id="text30644-85-8"><tspan
         id="tspan30642-905-6"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.189857"
         y="205.88365">{ 'X' if JSONquestion_views['proteccioncatodica']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="206.06277"
       id="text30644-85-7"><tspan
         id="tspan30642-905-7"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="206.06277">{ 'X' if JSONquestion_views['proteccioncatodica']["presenta"] == "Mal Estado" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="205.97322"
       id="text30644-85-37"><tspan
         id="tspan30642-905-18"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="205.97322">{ 'X' if JSONquestion_views['proteccioncatodica']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.279423"
       y="210.09325"
       id="text30644-85-89"><tspan
         id="tspan30642-905-67"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.279423"
         y="210.09325">{ 'X' if JSONquestion_views['continuidad']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="58.235996"
       y="210.1828"
       id="text30644-85-87"><tspan
         id="tspan30642-905-37"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="58.235996"
         y="210.1828">{ 'X' if JSONquestion_views['continuidad']["presenta"] == "Mal Estado" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="67.192574"
       y="210.09325"
       id="text30644-85-0"><tspan
         id="tspan30642-905-8"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="67.192574"
         y="210.09325">{ 'X' if JSONquestion_views['continuidad']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="48.831593"
       y="220.84113"
       id="text30644-85-89-1"><tspan
         id="tspan30642-905-67-3"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="48.831593"
         y="220.84113">{ 'X' if JSONquestions_deterioration['tuberiadefectosoldadura']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="48.921158"
       y="225.76724"
       id="text30644-85-89-10"><tspan
         id="tspan30642-905-67-6"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="48.921158"
         y="225.76724">{ 'X' if JSONquestions_deterioration['tuberiapresentacorrosion']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="48.652462"
       y="236.8734"
       id="text30644-85-89-2"><tspan
         id="tspan30642-905-67-74"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="48.652462"
         y="236.8734">{ 'X' if JSONquestions_deterioration['tuberiaaplastamiento']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="48.921158"
       y="242.42647"
       id="text30644-85-89-83"><tspan
         id="tspan30642-905-67-41"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="48.921158"
         y="242.42647">{ 'X' if JSONquestions_deterioration['roscaencuentrabuenestado']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="48.831593"
       y="258.54831"
       id="text30644-85-89-08"><tspan
         id="tspan30642-905-67-61"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="48.831593"
         y="258.54831">{ 'X' if JSONobservations_and_results['estadovalvulas']["presenta"] == "Bueno" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="49.100292"
       y="263.83267"
       id="text30644-85-89-34"><tspan
         id="tspan30642-905-67-33"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="49.100292"
         y="263.83267">{ 'X' if JSONobservations_and_results['estadovalvulasalivio']["presenta"] == "Bueno" else "" }</tspan></text><g
       clip-path="url(#clipEmfPath2)"
       id="g11341"
       transform="matrix(0.13030134,0,0,0.12421712,-2.3209546,0.08984492)"><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="0"
         y="12.730408"
         id="text10775"><tspan
           x="0"
           y="12.730408"
           id="tspan10773"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan10771">PLANTA</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="131.2252"
         y="12.730408"
         id="text10781"><tspan
           x="131.2252"
           y="12.730408"
           id="tspan10779"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:14.0625px;font-family:Arial;fill:#000000"
             id="tspan10777">IN-SITU</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="631.52124"
         y="12.000221"
         id="text10787"><tspan
           x="631.52124"
           y="12.000221"
           id="tspan10785"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan10783">1 VEZ</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="919.74805"
         y="12.000221"
         id="text10793"><tspan
           x="919.74805"
           y="12.000221"
           id="tspan10791"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:17.5625px;font-family:Calibri;fill:#000000"
             id="tspan10789">2 VEZ</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="161.74178"
         y="613.71118"
         id="text10799"><tspan
           x="161.74178"
           y="613.71118"
           id="tspan10797"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan10795">VERTICAL</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="1152.9071"
         y="43.09676"
         id="text10805"><tspan
           x="1152.9071"
           y="43.09676"
           id="tspan10803"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Arial;fill:#000000"
             id="tspan10801">ENTERRADO</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="399.37509"
         y="678.67041"
         id="text10811"><tspan
           x="399.37509"
           y="678.67041"
           id="tspan10809"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan10807">SI</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="462.64438"
         y="678.67041"
         id="text10817"><tspan
           x="462.64438"
           y="678.67041"
           id="tspan10815"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan10813">NO</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="527.08533"
         y="678.67041"
         id="text10823"><tspan
           x="527.08533"
           y="678.67041"
           id="tspan10821"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:12.875px;font-family:Calibri;fill:#000000"
             id="tspan10819">N/A</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="212.06929"
         y="143.22542"
         id="text10829"><tspan
           x="0"
           y="0"
           id="tspan10827"><tspan
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5625px;font-family:Calibri;fill:#f2f2f2"
             id="tspan10825" /></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;line-height:125%;font-family:Calibri;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         transform="translate(169.88976,567.08032)"
         x="1418.8724"
         y="143.83435"
         id="text10853"><tspan
           x="0"
           y="0"
           id="tspan10851"><tspan
             style="font-style:normal;font-variant:normal;font-weight:400;font-size:15.25px;font-family:Calibri;fill:#000000"
             id="tspan10849" /></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:16.375px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="374.77036"
         y="1474.7041"
         id="text11339"><tspan
           x="374.77036"
           y="1474.7041"
           id="tspan11337"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:16.375px;font-family:Arial;fill:#000000"
             id="tspan11335">BUENO</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:16.375px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none"
         x="377.42584"
         y="1732.7538"
         id="text11339-4"><tspan
           x="377.42584"
           y="1732.7538"
           id="tspan11337-3"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:16.375px;font-family:Arial;fill:#000000"
             id="tspan11335-8">BUENO</tspan></tspan></text><text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5129px;line-height:125%;font-family:Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.997177"
         transform="scale(0.99562284,1.0043964)"
         x="523.21808"
         y="1468.2401"
         id="text11565-6"><tspan
           x="523.21808"
           y="1468.2401"
           id="tspan11563-2"
           style="stroke-width:0.997177"><tspan
             dx="0"
             dy="0"
             style="font-style:normal;font-variant:normal;font-weight:700;font-size:17.5129px;font-family:Arial;fill:#000000;stroke-width:0.997177"
             id="tspan11561-9">N/A</tspan></tspan></text></g><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.09425"
       y="156.89119"
       id="text30644-85-89-235-2"><tspan
         id="tspan30642-905-67-42-80"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.09425"
         y="156.89119">{'X' if JSONtank_identification["AccionPorFuego"]["1"]["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.18382"
       y="161.90688"
       id="text30644-85-89-235-65"><tspan
         id="tspan30642-905-67-42-4"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.18382"
         y="161.90688">{'X' if JSONtank_identification["EstadoConexionCorrosion"]["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.27339"
       y="167.54951"
       id="text30644-85-89-235-3"><tspan
         id="tspan30642-905-67-42-46"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.27339"
         y="167.54951">{'X' if JSONtank_identification["EstadoConexionEvidenciaGolpes"]["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.18382"
       y="172.83389"
       id="text30644-85-89-235-01"><tspan
         id="tspan30642-905-67-42-00"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.18382"
         y="172.83389">{'X' if JSONtank_identification["EstadoConexionDesgaste"]["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.36296"
       y="177.93915"
       id="text30644-85-89-235-5"><tspan
         id="tspan30642-905-67-42-02"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.36296"
         y="177.93915">{'X' if JSONtank_identification["EstadoConexionOtros"]["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.18382"
       y="151.33812"
       id="text30644-85-89-235-22"><tspan
         id="tspan30642-905-67-42-20"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.18382"
         y="151.33812">{'X' if JSONtank_identification["corrosionGeneral"]["1"]["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.59938"
       y="151.15898"
       id="text30644-85-89-235-27"><tspan
         id="tspan30642-905-67-42-7"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.59938"
         y="151.15898">{'X' if JSONtank_identification["corrosionGeneral"]["1"]["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.50983"
       y="143.90416"
       id="text30644-85-89-235-7"><tspan
         id="tspan30642-905-67-42-21"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.50983"
         y="143.90416">{'X' if JSONtank_identification["corrosionEnLinea"]["1"]["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.27339"
       y="144.26242"
       id="text30644-85-89-235-34"><tspan
         id="tspan30642-905-67-42-09"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.27339"
         y="144.26242">{'X' if JSONtank_identification["corrosionEnLinea"]["1"]["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.09425"
       y="137.45543"
       id="text30644-85-89-235-99"><tspan
         id="tspan30642-905-67-42-6"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.09425"
         y="137.45543">{'X' if JSONtank_identification["corrosionAislada"]["1"]["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.42026"
       y="137.63455"
       id="text30644-85-89-235-04"><tspan
         id="tspan30642-905-67-42-42"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.42026"
         y="137.63455">{'X' if JSONtank_identification["corrosionAislada"]["1"]["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.50983"
       y="131.90236"
       id="text30644-85-89-235-49"><tspan
         id="tspan30642-905-67-42-63"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.50983"
         y="131.90236">{'X' if JSONtank_identification["abombamiento"]["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.77852"
       y="126.61797"
       id="text30644-85-89-235-08"><tspan
         id="tspan30642-905-67-42-88"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.77852"
         y="126.61797">{'X' if JSONtank_identification["abolladura"]["3"]["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.77852"
       y="121.60229"
       id="text30644-85-89-235-32"><tspan
         id="tspan30642-905-67-42-70"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.77852"
         y="121.60229">{'X' if JSONtank_identification["abolladura"]["2"]["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.77852"
       y="115.60139"
       id="text30644-85-89-235-03"><tspan
         id="tspan30642-905-67-42-3"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.77852"
         y="115.60139">{'X' if JSONtank_identification["abolladura"]["1"]["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.68895"
       y="110.49614"
       id="text30644-85-89-235-74"><tspan
         id="tspan30642-905-67-42-06"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.68895"
         y="110.49614">{'X' if JSONtank_identification['socavado']["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.77852"
       y="105.03263"
       id="text30644-85-89-235-95"><tspan
         id="tspan30642-905-67-42-37"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.77852"
         y="105.03263">{'X' if JSONtank_identification['salpicadura']["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.7785"
       y="99.882591"
       id="text30644-85-89-235-59"><tspan
         id="tspan30642-905-67-42-40"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.7785"
         y="99.882591">{'X' if JSONtank_identification['porosidad']["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="192.00243"
       y="94.329521"
       id="text30644-85-89-235-93"><tspan
         id="tspan30642-905-67-42-99"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="192.00243"
         y="94.329521">{'X' if JSONtank_identification['agrietamiento']["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="191.8233"
       y="88.821228"
       id="text30644-85-89-235-93-1"><tspan
         id="tspan30642-905-67-42-99-2"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="191.8233"
         y="88.821228">{'X' if JSONtank_identification['hermeticidad']["cumple"] == True else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.0047"
       y="88.821228"
       id="text30644-85-89-235-30"><tspan
         id="tspan30642-905-67-42-39"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.0047"
         y="88.821228">{'X' if JSONtank_identification['hermeticidad']["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.18382"
       y="94.105606"
       id="text30644-85-89-235-43"><tspan
         id="tspan30642-905-67-42-91"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.18382"
         y="94.105606">{'X' if JSONtank_identification['agrietamiento']["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.09425"
       y="99.569122"
       id="text30644-85-89-235-29"><tspan
         id="tspan30642-905-67-42-61"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.09425"
         y="99.569122">{'X' if JSONtank_identification['porosidad']["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.18382"
       y="105.21176"
       id="text30644-85-89-235-1"><tspan
         id="tspan30642-905-67-42-465"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.18382"
         y="105.21176">{'X' if JSONtank_identification['salpicadura']["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.27339"
       y="110.67527"
       id="text30644-85-89-235-12"><tspan
         id="tspan30642-905-67-42-05"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.27339"
         y="110.67527">{'X' if JSONtank_identification['socavado']["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.09425"
       y="115.87009"
       id="text30644-85-89-235-58"><tspan
         id="tspan30642-905-67-42-87"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.09425"
         y="115.87009">{'X' if JSONtank_identification["abolladura"]["1"]["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.09425"
       y="121.3336"
       id="text30644-85-89-235-07"><tspan
         id="tspan30642-905-67-42-34"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.09425"
         y="121.3336">{'X' if JSONtank_identification["abolladura"]["2"]["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.0047"
       y="126.61797"
       id="text30644-85-89-235-00"><tspan
         id="tspan30642-905-67-42-82"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.0047"
         y="126.61797">{'X' if JSONtank_identification["abolladura"]["3"]["cumple"] == False else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306002;stroke-dasharray:none;stroke-opacity:1"
       x="207.0047"
       y="132.35017"
       id="text30644-85-89-235-13"><tspan
         id="tspan30642-905-67-42-47"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="207.0047"
         y="132.35017">{'X' if JSONtank_identification["abombamiento"]["cumple"] == False else " "}</tspan></text>{'''<path
       d="m 180.72535,87.827024 c 0.007,0.0084 0.0237,0.02963 0.0517,0.09083 0.0135,0.02941 0.0236,0.05411 0.0429,0.09959 0.008,0.01958 0.0204,0.04798 0.0338,0.07692 0.0332,0.07572 0.0744,0.181422 0.13027,0.309923 0.0421,0.09676 0.0978,0.216747 0.17203,0.33551 0.0156,0.02987 0.0357,0.06081 0.0619,0.09034 0.0348,0.0393 0.0794,0.07499 0.13409,0.100462 0.0539,0.0251 0.11017,0.03678 0.16463,0.03747 0.0527,6.69e-4 0.10011,-0.0089 0.14023,-0.02258 0.0394,-0.01343 0.0737,-0.03142 0.10259,-0.05034 0.0287,-0.01879 0.054,-0.03981 0.076,-0.06151 0.0336,-0.03311 0.0637,-0.07178 0.0879,-0.114564 0.0485,-0.06894 0.0892,-0.138894 0.12118,-0.193135 0.0387,-0.0656 0.0668,-0.111608 0.0974,-0.151774 0.003,-0.0044 0.007,-0.0089 0.01,-0.01341 0.44577,-0.647021 0.92583,-1.15605 1.46199,-1.521096 0.1375,-0.09427 0.25309,-0.162413 0.32322,-0.202331 a 0.3405575,0.3405575 90 0 0 -0.33698,-0.59192 c -0.0805,0.04585 -0.2134,0.124179 -0.37047,0.23186 -0.62067,0.422579 -1.15573,0.997354 -1.63425,1.690697 -0.056,0.07434 -0.10104,0.150506 -0.13717,0.211717 -0.0399,0.06759 -0.068,0.115312 -0.0997,0.158547 -0.013,0.01773 -0.0242,0.03667 -0.0335,0.05656 0.009,-0.01884 0.0199,-0.03387 0.0328,-0.04658 0.007,-0.0069 0.0163,-0.0148 0.0284,-0.02272 0.0121,-0.0079 0.0291,-0.01723 0.0512,-0.02477 0.0226,-0.0077 0.0525,-0.01417 0.088,-0.01372 0.037,4.71e-4 0.0764,0.0085 0.11423,0.02613 0.0384,0.01786 0.0675,0.04198 0.0883,0.06542 0.0206,0.02324 0.0319,0.04459 0.0377,0.05779 l -0.0252,-0.04697 c -0.0503,-0.0785 -0.0924,-0.166374 -0.13168,-0.256678 -0.0479,-0.110072 -0.0914,-0.221411 -0.13383,-0.317893 -0.0112,-0.02437 -0.0198,-0.04459 -0.0278,-0.0633 -0.0163,-0.03831 -0.032,-0.07648 -0.0508,-0.117459 -0.0501,-0.109349 -0.0967,-0.180536 -0.14272,-0.237111 a 0.3405575,0.3405575 90 0 0 -0.52816,0.430086 z"
       id="path-1"
       style="opacity:1;fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.293169;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification['hermeticidad']["defectologia"] == True else " " }{'''<path
       d="m 180.74705,114.84933 c 0.007,0.008 0.0237,0.0296 0.0517,0.0908 0.0135,0.0294 0.0236,0.0541 0.0429,0.0996 0.008,0.0196 0.0204,0.048 0.0338,0.0769 0.0332,0.0757 0.0744,0.18142 0.13027,0.30992 0.0421,0.0968 0.0978,0.21674 0.17202,0.33551 0.0156,0.0299 0.0357,0.0608 0.0619,0.0903 0.0348,0.0393 0.0794,0.075 0.13412,0.10048 0.0539,0.0251 0.11019,0.0368 0.16466,0.0375 0.0527,6.6e-4 0.10012,-0.009 0.14023,-0.0226 0.0394,-0.0134 0.0737,-0.0314 0.10257,-0.0503 0.0287,-0.0188 0.054,-0.0398 0.076,-0.0615 0.0336,-0.0331 0.0636,-0.0718 0.0879,-0.11454 0.0485,-0.0689 0.0892,-0.13889 0.12118,-0.19313 0.0387,-0.0656 0.0667,-0.1116 0.0974,-0.15177 0.003,-0.004 0.007,-0.009 0.01,-0.0134 0.44577,-0.64702 0.92582,-1.15605 1.46199,-1.52109 0.1375,-0.0943 0.25309,-0.16241 0.32322,-0.20233 a 0.3405575,0.3405575 90 0 0 -0.33698,-0.59192 c -0.0805,0.0459 -0.2134,0.12418 -0.37046,0.23185 -0.62069,0.42259 -1.15574,0.99736 -1.63426,1.6907 -0.0559,0.0743 -0.10103,0.1505 -0.13717,0.21171 -0.0399,0.0676 -0.068,0.1153 -0.0996,0.15854 -0.013,0.0177 -0.0242,0.0367 -0.0335,0.0566 0.009,-0.0188 0.0199,-0.0338 0.0328,-0.0465 0.007,-0.007 0.0163,-0.0148 0.0283,-0.0227 0.0121,-0.008 0.0291,-0.0172 0.0512,-0.0248 0.0226,-0.008 0.0524,-0.0142 0.088,-0.0137 0.037,4.6e-4 0.0764,0.008 0.11426,0.0261 0.0384,0.0179 0.0676,0.042 0.0883,0.0654 0.0206,0.0233 0.0319,0.0446 0.0377,0.0578 l -0.0252,-0.047 c -0.0504,-0.0785 -0.0924,-0.16638 -0.13168,-0.25669 -0.0479,-0.11007 -0.0914,-0.22141 -0.13383,-0.31789 -0.0112,-0.0244 -0.0198,-0.0446 -0.0278,-0.0633 -0.0162,-0.0383 -0.032,-0.0765 -0.0508,-0.11746 -0.0501,-0.10935 -0.0967,-0.18053 -0.14272,-0.23711 a 0.3405575,0.3405575 90 0 0 -0.52816,0.43008 z"
       id="path-1-3"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.293169;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification["abolladura"]["1"]["defectologia"] == True else " " }{'''<path
       d="m 180.74705,120.26807 c 0.007,0.008 0.0237,0.0296 0.0517,0.0908 0.0135,0.0294 0.0236,0.0541 0.0429,0.0996 0.008,0.0196 0.0204,0.048 0.0338,0.0769 0.0332,0.0757 0.0744,0.18142 0.13027,0.30992 0.0421,0.0968 0.0978,0.21674 0.17203,0.3355 0.0156,0.0299 0.0357,0.0608 0.0619,0.0903 0.0348,0.0393 0.0794,0.075 0.13412,0.10048 0.0539,0.0251 0.11019,0.0368 0.16466,0.0374 0.0527,6.6e-4 0.10012,-0.009 0.14023,-0.0226 0.0394,-0.0134 0.0737,-0.0314 0.10257,-0.0503 0.0287,-0.0188 0.054,-0.0398 0.076,-0.0615 0.0336,-0.0331 0.0636,-0.0718 0.0879,-0.11454 0.0485,-0.0689 0.0892,-0.13889 0.12118,-0.19313 0.0387,-0.0656 0.0667,-0.1116 0.0974,-0.15177 0.003,-0.004 0.007,-0.009 0.01,-0.0134 0.44577,-0.64702 0.92583,-1.15604 1.46199,-1.52108 0.13749,-0.0943 0.25311,-0.16243 0.32322,-0.20234 a 0.3405575,0.3405575 90 0 0 -0.33698,-0.59192 c -0.0805,0.0458 -0.21342,0.12419 -0.37048,0.23187 -0.62066,0.42256 -1.15572,0.99734 -1.63424,1.69068 -0.0559,0.0743 -0.10103,0.1505 -0.13717,0.21171 -0.0399,0.0676 -0.068,0.1153 -0.0996,0.15854 -0.013,0.0177 -0.0242,0.0367 -0.0335,0.0566 0.009,-0.0188 0.0199,-0.0338 0.0328,-0.0465 0.007,-0.007 0.0163,-0.0148 0.0283,-0.0227 0.0121,-0.008 0.0291,-0.0172 0.0512,-0.0248 0.0226,-0.008 0.0524,-0.0142 0.088,-0.0137 0.037,4.6e-4 0.0764,0.008 0.11426,0.0261 0.0384,0.0179 0.0676,0.042 0.0883,0.0654 0.0206,0.0233 0.0319,0.0446 0.0377,0.0578 l -0.0252,-0.047 c -0.0504,-0.0785 -0.0924,-0.16638 -0.13168,-0.25668 -0.0479,-0.11007 -0.0914,-0.22141 -0.13383,-0.31789 -0.0112,-0.0244 -0.0198,-0.0446 -0.0278,-0.0633 -0.0162,-0.0383 -0.032,-0.0765 -0.0508,-0.11746 -0.0501,-0.10935 -0.0967,-0.18053 -0.14272,-0.23711 a 0.3405575,0.3405575 90 0 0 -0.52816,0.43008 z"
       id="path-1-6"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.293169;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification["abolladura"]["2"]["defectologia"] == True else " " }{'''<path
       d="m 180.74705,125.46288 c 0.007,0.008 0.0237,0.0296 0.0517,0.0908 0.0135,0.0294 0.0236,0.0541 0.0429,0.0996 0.008,0.0196 0.0204,0.048 0.0338,0.0769 0.0332,0.0757 0.0744,0.18141 0.13026,0.30991 0.0421,0.0968 0.0978,0.21675 0.17203,0.33551 0.0156,0.0299 0.0357,0.0608 0.0619,0.0903 0.0348,0.0393 0.0794,0.075 0.13412,0.10048 0.0539,0.0251 0.11019,0.0368 0.16466,0.0375 0.0527,6.6e-4 0.10012,-0.009 0.14023,-0.0226 0.0394,-0.0134 0.0737,-0.0314 0.10257,-0.0503 0.0287,-0.0188 0.054,-0.0398 0.076,-0.0615 0.0336,-0.0331 0.0636,-0.0718 0.0879,-0.11454 0.0485,-0.0689 0.0892,-0.13889 0.12118,-0.19313 0.0387,-0.0656 0.0667,-0.1116 0.0974,-0.15177 0.003,-0.004 0.007,-0.009 0.01,-0.0134 0.44577,-0.64702 0.92583,-1.15604 1.46199,-1.52108 0.13749,-0.0943 0.25311,-0.16243 0.32322,-0.20234 a 0.3405575,0.3405575 90 0 0 -0.33698,-0.59192 c -0.0805,0.0458 -0.21342,0.12419 -0.37048,0.23187 -0.62066,0.42256 -1.15572,0.99734 -1.63424,1.69068 -0.0559,0.0743 -0.10103,0.1505 -0.13717,0.21171 -0.0399,0.0676 -0.068,0.1153 -0.0996,0.15854 -0.013,0.0177 -0.0242,0.0367 -0.0335,0.0566 0.009,-0.0188 0.0199,-0.0338 0.0328,-0.0465 0.007,-0.007 0.0163,-0.0148 0.0283,-0.0227 0.0121,-0.008 0.0291,-0.0172 0.0512,-0.0248 0.0226,-0.008 0.0524,-0.0142 0.088,-0.0137 0.037,4.6e-4 0.0764,0.008 0.11426,0.0261 0.0384,0.0179 0.0676,0.042 0.0883,0.0654 0.0206,0.0233 0.0319,0.0446 0.0377,0.0578 l -0.0252,-0.047 c -0.0504,-0.0785 -0.0924,-0.16638 -0.13168,-0.25668 -0.0479,-0.11007 -0.0914,-0.22142 -0.13383,-0.3179 -0.0112,-0.0244 -0.0198,-0.0446 -0.0278,-0.0633 -0.0162,-0.0383 -0.032,-0.0765 -0.0508,-0.11745 -0.0501,-0.10935 -0.0967,-0.18053 -0.14272,-0.23711 a 0.3405575,0.3405575 90 0 0 -0.52816,0.43008 z"
       id="path-1-5"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.293169;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification["abolladura"]["3"]["defectologia"] == True else " "}{'''<path
       d="m 180.70227,130.65769 c 0.007,0.008 0.0237,0.0296 0.0517,0.0908 0.0135,0.0294 0.0236,0.0541 0.0429,0.0996 0.008,0.0196 0.0204,0.048 0.0338,0.0769 0.0332,0.0757 0.0744,0.18142 0.13027,0.30992 0.0421,0.0968 0.0978,0.21674 0.17203,0.3355 0.0156,0.0299 0.0357,0.0608 0.0619,0.0903 0.0348,0.0393 0.0794,0.075 0.13412,0.10048 0.0539,0.0251 0.11019,0.0368 0.16466,0.0375 0.0527,6.6e-4 0.10012,-0.009 0.14023,-0.0226 0.0394,-0.0134 0.0737,-0.0314 0.10257,-0.0503 0.0287,-0.0188 0.054,-0.0398 0.076,-0.0615 0.0336,-0.0331 0.0636,-0.0718 0.0879,-0.11453 0.0485,-0.0689 0.0892,-0.13888 0.12119,-0.19312 0.0387,-0.0656 0.0668,-0.11162 0.0974,-0.1518 0.003,-0.004 0.007,-0.009 0.01,-0.0134 0.44577,-0.64703 0.92582,-1.15605 1.46199,-1.52109 0.13749,-0.0943 0.25311,-0.16243 0.32322,-0.20234 a 0.3405575,0.3405575 90 0 0 -0.33698,-0.59192 c -0.0805,0.0458 -0.21342,0.12419 -0.37048,0.23187 -0.62067,0.42257 -1.15572,0.99735 -1.63425,1.6907 -0.0559,0.0743 -0.10102,0.15048 -0.13715,0.21169 -0.0399,0.0676 -0.068,0.1153 -0.0997,0.15853 -0.013,0.0177 -0.0242,0.0367 -0.0335,0.0566 0.009,-0.0188 0.0199,-0.0338 0.0328,-0.0465 0.007,-0.007 0.0163,-0.0148 0.0283,-0.0227 0.0121,-0.008 0.0291,-0.0172 0.0512,-0.0248 0.0226,-0.008 0.0524,-0.0142 0.088,-0.0137 0.0371,4.6e-4 0.0764,0.008 0.11426,0.0261 0.0384,0.0179 0.0676,0.042 0.0883,0.0654 0.0206,0.0233 0.0319,0.0446 0.0377,0.0578 l -0.0252,-0.047 c -0.0504,-0.0785 -0.0924,-0.16638 -0.13168,-0.25668 -0.0479,-0.11007 -0.0914,-0.22141 -0.13383,-0.31789 -0.0112,-0.0244 -0.0198,-0.0446 -0.0278,-0.0633 -0.0163,-0.0383 -0.032,-0.0765 -0.0508,-0.11746 -0.0501,-0.10935 -0.0967,-0.18053 -0.14272,-0.23711 a 0.3405575,0.3405575 90 0 0 -0.52816,0.43008 z"
       id="path-1-51"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.293169;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification['abombamiento']["defectologia"] == True else " " }{'''<path
       d="m 181.02913,135.2285 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0222 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0248 0.0347,0.0503 0.0597,0.0739 0.0319,0.03 0.0711,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0202 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0814 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification["corrosionAislada"]["1"]["defectologia"] == True else " " }{'''<path
       d="m 180.89474,137.67004 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0223 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0248 0.0347,0.0503 0.0597,0.0739 0.0319,0.03 0.0711,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.052 0.0674,-0.0813 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0752,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-2"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification["corrosionAislada"]["2"]["defectologia"] == True else " "}{'''<path
       d="m 180.84996,140.84963 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0222 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0248 0.0347,0.0504 0.0597,0.0739 0.0319,0.03 0.0711,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0814 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-29"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification["corrosionEnLinea"]["1"]["defectologia"] == True else " " }{'''<path
       d="m 180.80518,143.2679 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0222 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0248 0.0347,0.0503 0.0597,0.0739 0.0319,0.03 0.071,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0202 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0814 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-9"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification["corrosionEnLinea"]["2"]["defectologia"] == True else " "}{'''<path
       d="m 180.7604,145.77574 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0223 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0249 0.0347,0.0504 0.0597,0.0739 0.0319,0.0301 0.071,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0813 0.038,-0.0492 0.0713,-0.0997 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-95"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification["corrosionEnLinea"]["3"]["defectologia"] == True else " "}{'''<path
       d="m 180.80517,149.00011 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0223 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0249 0.0347,0.0504 0.0597,0.0739 0.0319,0.03 0.071,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.04 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.052 0.0675,-0.0813 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-4"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification["corrosionGeneral"]["1"]["defectologia"] == True else " "}{'''<path
       d="m 180.80517,151.46316 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0222 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0248 0.0347,0.0504 0.0597,0.0739 0.0319,0.0301 0.071,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0814 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-93"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification["corrosionGeneral"]["2"]["defectologia"] == True else " "}{'''<path
       d="m 180.80518,154.37405 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0223 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0249 0.0347,0.0504 0.0597,0.0739 0.0319,0.0301 0.071,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0813 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-92"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification["AccionPorFuego"]["1"]["defectologia"] == True else " " }{'''<path
       d="m 180.80517,156.92668 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0223 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.0179,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0249 0.0347,0.0504 0.0597,0.0739 0.0319,0.03 0.071,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0203 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.04 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.052 0.0675,-0.0813 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0753,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-91"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONtank_identification["AccionPorFuego"]["2"]["defectologia"] == True else " "}{'''<path
       d="m 48.534495,294.77252 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01154,0.0223 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.01521,0.0248 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07104,0.0554 0.116928,0.0714 0.04492,0.0157 0.08969,0.0203 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.0309,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0027,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" /> ''' if aprobado == True else " "}<path
       d="m 69.434239,303.74323 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01154,0.0222 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.01521,0.0248 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07104,0.0554 0.116928,0.0714 0.04492,0.0157 0.08969,0.0202 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.0309,-0.0458 0.05381,-0.0784 0.07788,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.0743,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0027,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03123,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-4"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />{'''<path
       d="m 16.331608,311.95395 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01155,0.0222 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.01521,0.0249 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07105,0.0553 0.116928,0.0714 0.04492,0.0157 0.08969,0.0202 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.04 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.052 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.03089,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0027,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-6"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONquestions_mtto['equipos1'] == True else " " }{'''<path
       d="m 16.339061,315.13595 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01155,0.0222 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.0152,0.0248 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07104,0.0554 0.116928,0.0714 0.04492,0.0157 0.08969,0.0202 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.0309,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0028,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-68"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONquestions_mtto['equipos2'] == True else " "}{'''<path
       d="m 16.302192,318.21301 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01154,0.0223 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.01521,0.0249 0.03469,0.0504 0.05969,0.0739 0.03187,0.0301 0.07105,0.0553 0.116928,0.0714 0.04492,0.0157 0.08969,0.0203 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.0309,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0028,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-1"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONquestions_mtto['equipos3'] == True else " "}{'''<path
       d="m 16.339061,321.34968 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01155,0.0222 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.0152,0.0248 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07104,0.0554 0.116928,0.0714 0.04492,0.0157 0.08969,0.0202 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.0309,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0028,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-3"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONquestions_mtto['equipos4'] == True else " "}{'''<path
       d="m 16.257409,324.76964 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01154,0.0222 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.01521,0.0248 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07105,0.0554 0.116928,0.0714 0.04492,0.0157 0.08969,0.0202 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.03089,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0027,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-47"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONquestions_mtto['equipos5'] == True else " "}{'''<path
       d="m 87.800676,303.61657 c 0.0047,0.005 0.01821,0.0197 0.042,0.0656 0.01154,0.0222 0.02036,0.0412 0.03724,0.0763 0.0073,0.0151 0.01794,0.0372 0.02963,0.0597 0.03497,0.0705 0.07168,0.15277 0.108952,0.2278 0.03561,0.0718 0.08302,0.16125 0.145585,0.24893 0.0152,0.0249 0.03469,0.0503 0.05969,0.0739 0.03187,0.0301 0.07104,0.0553 0.116928,0.0714 0.04492,0.0157 0.08969,0.0202 0.131017,0.0172 0.03993,-0.003 0.07507,-0.0127 0.104131,-0.0244 0.02866,-0.0115 0.05347,-0.0258 0.07426,-0.0401 0.02068,-0.0142 0.03901,-0.0296 0.05501,-0.0449 0.02545,-0.0244 0.0483,-0.0521 0.06745,-0.0813 0.03801,-0.0491 0.07131,-0.0996 0.09721,-0.13805 0.0309,-0.0458 0.05381,-0.0784 0.07787,-0.10623 0.0029,-0.003 0.0057,-0.007 0.0084,-0.0102 0.374153,-0.47854 0.775807,-0.85043 1.206801,-1.11337 0.129233,-0.0795 0.238333,-0.13629 0.303987,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.241778,-0.48256 c -0.07429,0.0372 -0.198183,0.10169 -0.344185,0.19152 -0.494655,0.30177 -0.941702,0.71985 -1.346243,1.23631 -0.04509,0.0529 -0.08219,0.10725 -0.112286,0.15187 -0.03328,0.0493 -0.05635,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.01529,0.0207 -0.02178,0.0318 0.0042,-0.007 0.0082,-0.012 0.01295,-0.0166 0.0028,-0.003 0.0071,-0.006 0.0133,-0.0107 0.0062,-0.004 0.01598,-0.0102 0.02954,-0.0156 0.01376,-0.006 0.03356,-0.0115 0.05842,-0.0133 0.02601,-0.002 0.05579,9.1e-4 0.08632,0.0116 0.03122,0.0109 0.05643,0.0277 0.07526,0.0455 0.01858,0.0175 0.0292,0.0343 0.03469,0.0446 l -0.02034,-0.0324 c -0.03986,-0.0545 -0.07399,-0.11681 -0.10648,-0.18228 -0.03815,-0.0769 -0.07321,-0.15567 -0.11136,-0.23255 -0.0097,-0.0188 -0.01723,-0.0342 -0.02417,-0.0487 -0.01416,-0.0295 -0.02816,-0.0594 -0.04471,-0.0913 -0.04437,-0.0855 -0.08516,-0.1407 -0.125376,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-0"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if JSONquestions_mtto['video'] == True else " "}{'''<path
       d="m 154.29985,294.89919 c 0.005,0.005 0.0182,0.0197 0.042,0.0656 0.0115,0.0222 0.0204,0.0412 0.0372,0.0763 0.007,0.0151 0.018,0.0372 0.0296,0.0597 0.035,0.0705 0.0717,0.15275 0.10894,0.22779 0.0356,0.0718 0.083,0.16125 0.14559,0.24893 0.0152,0.0248 0.0347,0.0503 0.0597,0.0739 0.0319,0.0301 0.0711,0.0553 0.11693,0.0714 0.0449,0.0157 0.0897,0.0202 0.13101,0.0172 0.0399,-0.003 0.0751,-0.0127 0.10413,-0.0244 0.0287,-0.0115 0.0535,-0.0258 0.0743,-0.0401 0.0207,-0.0142 0.039,-0.0296 0.055,-0.0449 0.0255,-0.0244 0.0483,-0.0521 0.0675,-0.0813 0.038,-0.0491 0.0713,-0.0996 0.0972,-0.13805 0.0309,-0.0458 0.0538,-0.0784 0.0779,-0.10623 0.003,-0.003 0.006,-0.007 0.008,-0.0102 0.37414,-0.47854 0.7758,-0.85043 1.20679,-1.11337 0.12924,-0.0795 0.23833,-0.13629 0.30399,-0.16919 a 0.26987221,0.26987221 90 0 0 -0.24178,-0.48256 c -0.0743,0.0372 -0.19817,0.10168 -0.34418,0.19152 -0.49466,0.30177 -0.94171,0.71985 -1.34624,1.23631 -0.0451,0.0529 -0.0822,0.10725 -0.11229,0.15187 -0.0333,0.0493 -0.0564,0.0842 -0.0822,0.11669 -0.008,0.0101 -0.0153,0.0207 -0.0218,0.0318 0.004,-0.007 0.008,-0.012 0.0129,-0.0166 0.003,-0.003 0.007,-0.006 0.0133,-0.0107 0.006,-0.004 0.016,-0.0102 0.0295,-0.0156 0.0138,-0.006 0.0336,-0.0115 0.0584,-0.0133 0.026,-0.002 0.0558,9.1e-4 0.0863,0.0116 0.0312,0.0109 0.0564,0.0277 0.0752,0.0455 0.0186,0.0175 0.0292,0.0343 0.0347,0.0446 l -0.0203,-0.0324 c -0.0399,-0.0545 -0.074,-0.11682 -0.10648,-0.18229 -0.0381,-0.0769 -0.0732,-0.15567 -0.11135,-0.23255 -0.01,-0.0188 -0.0172,-0.0342 -0.0242,-0.0487 -0.0142,-0.0295 -0.0282,-0.0594 -0.0447,-0.0913 -0.0444,-0.0855 -0.0852,-0.1407 -0.12538,-0.18405 a 0.26987221,0.26987221 90 0 0 -0.3957,0.36708 z"
       id="path-1-8-5-7"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.23232;stroke-dasharray:none;stroke-opacity:1" />''' if aprobado == False else " " }{'''<path
       d="m 57.09705,298.90505 c 0.0063,0.006 0.02678,0.0254 0.06456,0.0903 0.0184,0.0316 0.03279,0.059 0.06012,0.10979 0.01174,0.0218 0.02917,0.054 0.0481,0.0866 0.04163,0.075 0.09574,0.18293 0.169898,0.31511 0.05591,0.0996 0.130487,0.22412 0.227702,0.34482 0.02481,0.0355 0.0556,0.0708 0.09369,0.10283 0.04792,0.0403 0.104262,0.0726 0.167602,0.0929 0.06188,0.0199 0.123098,0.026 0.179953,0.0227 0.0552,-0.003 0.104638,-0.0151 0.146697,-0.0301 0.08052,-0.0288 0.145083,-0.0728 0.192508,-0.11332 0.03991,-0.0341 0.07563,-0.0725 0.105968,-0.11275 0.06069,-0.0695 0.114239,-0.14162 0.15532,-0.19572 0.04877,-0.0642 0.0843,-0.10906 0.121017,-0.14683 0.0047,-0.005 0.0092,-0.01 0.01362,-0.0147 0.590137,-0.67125 1.220867,-1.18543 1.876839,-1.54408 0.214261,-0.11828 0.395434,-0.20217 0.50363,-0.25034 a 0.39974936,0.39974936 90 0 0 -0.32519,-0.73038 c -0.120719,0.0537 -0.323991,0.14784 -0.563409,0.28001 -0.74536,0.40751 -1.445217,0.98228 -2.086143,1.70989 -0.07081,0.0739 -0.129688,0.15053 -0.177089,0.21295 -0.05264,0.0693 -0.08861,0.11752 -0.128433,0.16199 -0.01119,0.0125 -0.02158,0.0257 -0.03111,0.0395 0.0047,-0.007 0.0092,-0.0119 0.01558,-0.0173 0.0054,-0.005 0.02388,-0.0196 0.05791,-0.0318 0.01839,-0.007 0.04413,-0.0133 0.07602,-0.0151 0.03317,-0.002 0.07117,0.002 0.110687,0.0143 0.04055,0.013 0.07507,0.0333 0.102489,0.0563 0.02726,0.0229 0.04427,0.0458 0.05404,0.0617 l -0.0321,-0.0449 c -0.0589,-0.0713 -0.110552,-0.15455 -0.160555,-0.24367 -0.06069,-0.10816 -0.117579,-0.2209 -0.172165,-0.31905 -0.01564,-0.027 -0.02782,-0.0494 -0.03914,-0.0705 -0.02304,-0.0428 -0.04611,-0.0866 -0.07315,-0.13305 -0.07272,-0.12489 -0.138793,-0.2046 -0.203356,-0.26624 a 0.39974936,0.39974936 90 0 0 -0.552112,0.57824 z"
       id="path-1-8-26"
       style="fill:#000000;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.344125;stroke-dasharray:none;stroke-opacity:1" />''' if JSONquestions_mtto['ensayoNoDestructivo'] == True else " "}<text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="72.199097"
       y="295.12967"
       id="text38817"><tspan
         id="tspan38815"
         style="stroke-width:0.306"
         x="72.199097"
         y="295.12967">{ str(JSONquestions_mtto['numeroSticker']) if JSONquestions_mtto['numeroSticker'] != None else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="76.379044"
       y="299.43625"
       id="text38821"><tspan
         id="tspan38819"
         style="stroke-width:0.306"
         x="76.379044"
         y="299.43625">{ str(JSONquestions_mtto['cuales']) if JSONquestions_mtto['cuales'] != None else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="106.52534"
       y="303.61618"
       id="text38825"><tspan
         id="tspan38823"
         style="stroke-width:0.306"
         x="106.52534"
         y="303.61618">{ str(JSONquestions_mtto['otros1']) if JSONquestions_mtto['otros1']  != None else " "}</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="24.317099"
       y="312.1366"
       id="text38973"><tspan
         id="tspan38971"
         style="stroke-width:0.306"
         x="24.317099"
         y="312.1366">{str(JSONquestions_mtto['cantidadEquiposUtilizados1']) if JSONquestions_mtto['cantidadEquiposUtilizados1'] > 0 else " " }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="24.329475"
       y="315.64334"
       id="text38973-9"><tspan
         id="tspan38971-1"
         style="stroke-width:0.306"
         x="24.329475"
         y="315.64334">{str(JSONquestions_mtto['cantidadEquiposUtilizados2']) if JSONquestions_mtto['cantidadEquiposUtilizados2'] > 0 else " " }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="24.342592"
       y="318.91248"
       id="text38973-91"><tspan
         id="tspan38971-3"
         style="stroke-width:0.306"
         x="24.342592"
         y="318.91248">{str(JSONquestions_mtto['cantidadEquiposUtilizados3']) if JSONquestions_mtto['cantidadEquiposUtilizados3'] > 0 else " " }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="24.329475"
       y="322.09207"
       id="text38973-0"><tspan
         id="tspan38971-8"
         style="stroke-width:0.306"
         x="24.329475"
         y="322.09207">{str(JSONquestions_mtto['cantidadEquiposUtilizados4']) if JSONquestions_mtto['cantidadEquiposUtilizados4'] > 0 else " " }</tspan></text><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="24.316359"
       y="325.09253"
       id="text38973-3"><tspan
         id="tspan38971-4"
         style="stroke-width:0.306"
         x="24.316359"
         y="325.09253">{str(JSONquestions_mtto['cantidadEquiposUtilizados5']) if JSONquestions_mtto['cantidadEquiposUtilizados5'] > 0 else " " }</tspan></text><path
       style="opacity:1;fill:#000000;fill-opacity:1;stroke:none;stroke-width:2.1052;stroke-dasharray:none;stroke-opacity:1"
       d="m 914.46763,478.93835 c 0,0 -714.60767,-143.86938 -714.60767,-143.86938"
       id="path48235" /><text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.306001;stroke-dasharray:none;stroke-opacity:1"
       x="66.962624"
       y="220.39363"
       id="text30644-85-89-5-9"><tspan
         id="tspan30642-905-67-7-2"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:3.175px;font-family:Arial;-inkscape-font-specification:'Arial Bold';stroke-width:0.306"
         x="66.962624"
         y="220.39363">{ 'X' if JSONquestions_deterioration['tuberiadefectosoldadura']["presenta"] == "N/A" else "" }</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="1.2539203"
       y="281.5499"
       id="text2668"><tspan
         id="tspan2666"
         style="stroke-width:0.557"
         x="1.2539203"
         y="281.5499">{str(JSONobservations_and_results['observacionesConclusiones']) if JSONobservations_and_results['observacionesConclusiones'] != None else ""}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke-width:0.557001"
       x="2.242465"
       y="332.36917"
       id="text9489"><tspan
         id="tspan9487"
         style="stroke-width:0.557"
         x="2.242465"
         y="332.36917">Con la firma de este documento el usuario declara conocer: </tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke-width:0.557001"
       x="2.3419371"
       y="335.06012"
       id="text9493"><tspan
         id="tspan9491"
         style="stroke-width:0.557"
         x="2.3419371"
         y="335.06012">A) La inspección se realiza bajo los parametros de la Res. 40245 Númeral 10.1 y 10.3 de MINMINA.</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke-width:0.557001"
       x="2.1969938"
       y="337.75104"
       id="text9497"><tspan
         id="tspan9495"
         style="stroke-width:0.557"
         x="2.1969938"
         y="337.75104">B) Cualquier modificacion a los tanques estacionarios debe ser informada y automáticamente el certificado pierde validez.</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke-width:0.557001"
       x="2.242465"
       y="340.44199"
       id="text9501"><tspan
         id="tspan9499"
         style="stroke-width:0.557"
         x="2.242465"
         y="340.44199">C) Se puede presentar quejas y/o apelación de los resultados en los primeros 5 diás hábiles a la revisión al email qya@qcsas.com</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke-width:0.557001"
       x="2.2149992"
       y="343.1329"
       id="text9508"><tspan
         id="tspan9506"
         style="stroke-width:0.557"
         x="2.2149992"
         y="343.1329">D) Con la firma del presente documento el titular autoriza a que los Datos Personales sean recolectados y tratados de conformidad con las políticas y procedimiento en materia de protección y tratamiento de datos personales </tspan><tspan
         style="stroke-width:0.557"
         x="2.2149992"
         y="345.55811"
         id="tspan9510">lo cual se puede consultar en nuestra pagina web.</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;fill-opacity:1;stroke-width:0.557001"
       x="2.185626"
       y="347.94055"
       id="text9517"><tspan
         id="tspan9515"
         style="stroke-width:0.557"
         x="2.185626"
         y="347.94055">E) Eventos en los cuales la compañía Q-CHEKER SAS no necesita de la autorización del titular para suministrar los datos personales, Información requerida por una entidad pública como, Ministerios de Minas, Superintendencia de </tspan><tspan
         style="stroke-width:0.557"
         x="2.185626"
         y="350.36575"
         id="tspan9519">Industria y Comercio, Superservicios, Creg, Onac, entre otras.</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="96.255066"
       y="88.490967"
       id="text2073"><tspan
         id="tspan2071"
         style="stroke-width:0.557"
         x="96.255066"
         y="88.490967">{ str(JSONtank_identification['hermeticidad']["comentario"]) if JSONtank_identification['hermeticidad']["comentario"] != None else " "}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="6.3772225"
       y="328.31705"
       id="text11729"><tspan
         id="tspan11727"
         style="stroke-width:0.557"
         x="6.3772225"
         y="328.31705">{str(JSONquestions_mtto['otros2']) if JSONquestions_mtto['otros2']  != None else " "}</tspan></text><text
       xml:space="preserve"
       style="font-size:1.94015px;font-family:Arial;-inkscape-font-specification:Arial;fill:#000000;stroke-width:0.557001"
       x="111.01103"
       y="325.52872"
       id="text11733"><tspan
         id="tspan11731"
         style="stroke-width:0.557"
         x="111.01103"
         y="325.52872">{companieuser.contact}</tspan></text><image
       width="37.92271"
       height="10.795995"
       preserveAspectRatio="none"
       xlink:href="data:image/png;base64,{downloadImage(JSONsignatures['firmaUsuario'])}
"
       id="image51193"
       x="127.12847"
       y="311.36911" /><image
       width="38.68782"
       height="15.641693"
       preserveAspectRatio="none"
       xlink:href="data:image/png;base64,{downloadImage(JSONsignatures['firmaInspector'])}"
       id="image51193-4"
       x="43.650166"
       y="310.72003"
       style="display:inline" />       
       <image width="26.148102" height="19.267023" preserveAspectRatio="none" style="image-rendering:optimizeQuality" xlink:href="data:image/jpeg;base64,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 B0E8Z7tPceRB2IPYgFcv9XdL73pHm1Zid4Y58bD7Wiqtvdqacn3Xj17EdiCuqixf4gNE7ZrRhz7b +jp73QcU1rrHD6km3ONx/YdsAfLkey3eCYn+Aq7s/klx6uv7kG252WW0Nn72gv49P5f6lzj9uvtZ zHRT18sl1xq8VlgvlDJR3CgldBUQSDZzHjqP8D3CkV0RNSWaPm2cJU5OE1k1xQVTxm7yWDIbdeYi QaSpjlO3doPMfMbhUxElFSTi+YpzdOanHitTdl0sc7BPC4OjkaHscOhaRuD9ikZ+pVnaLZR/KLC4 qOeTiq7S76LJueZj23Yfs5fJXjP1Kg9Sk6FSVOXI6/SuY3dCFeHCSz/fYU6bqpCbup+bqpCbuq48 TCrkjP1+akZfxU9P1+akZfxV6JqKxTanoqXVKqVPRUuqWZTI5e8ymz/WUhL1Kn5/rKQl6lZtMi9y Skn114XuT668LJRp5cQiIvSkIiIAiIgCIiAIiIAiIgCIiAfBbOaJ6aOxSy/ygu8HDdblGCGOHOnh PMN9HHkT8grU0B0dlvcsWeZLREWyF+9vhkbyqZGn65HdjT9p+C2Jnh5krnO2WNOcXh1u9Pzv/wAf v4dJ3n2XbGSpJY7fR1f+Wn0P877fy9WvQyhzQ8PbkpSSNVmaH0UjNFsenJcrq0jtjRSpYlLPZsqn JH6KVlj9FgVKZQ0U98fcKA9inns27KBIzuFhzgUNEk5qhOZupt7VCc1YsolLRKkdivDmqO5u6hkK xKJSQCNl5I3UZzVDIVpopaIa8kbKIRuvKoaB5RCNkVto8PJGy8kbqIvJGy8BDReiN15VLWQCIi8A REQBERUsBERAFfOleEPye8C410O9soHhz9xylkHMM9R3P2d1buLY1cMsvEVpoGkcR4ppdvdij7uP 4DuVszZLNQY/a4LTbohHBTt4R5uPdx8yTzUt2WwN4hW/E1l/Di/+p9HYufgZNtR94958EToAA2A5 L6iLrBtAiIgCIiAIiIAiIgCIiAwB4oPDhTaq2t+V4rTRw5ZQRcgNmi4RN/zTj+2P1XfI8unPurpK q31U1DXU0tPU073RSxStLXxvB2LSDzBBXYNa8+JfwwUeqEEuY4bFDSZVAzeSPk2O4tA5Nce0nYO7 9D2Ik+CY1+Hytrh/DyfR1dnp2HK9uth/8S3sSw2P8X80V+brX9Xr28efqKZuVtuFmuFRartRTUlZ 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 " id="image11746" x="38.622414" y="0.83632028"></image>
       
       </g>
       
       <image width="31.144741" height="15.988744" preserveAspectRatio="none" style="image-rendering:optimizeQuality" xlink:href="data:image/jpeg;base64,/9j/4AAQSkZJRgABAgEAlgCWAAD/7QAsUGhvdG9zaG9wIDMuMAA4QklNA+0AAAAAABAAlgAAAAEA
AQCWAAAAAQAB/+FHzWh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8APD94cGFja2V0IGJlZ2lu
PSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4
PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNi4wLWMwMDQgNzkuMTY0
NTcwLCAyMDIwLzExLzE4LTE1OjUxOjQ2ICAgICAgICAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9
Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRm
OkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczpkYz0iaHR0cDovL3B1
cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICAgICAgICAgIHhtbG5zOnhtcD0iaHR0cDovL25z
LmFkb2JlLmNvbS94YXAvMS4wLyIKICAgICAgICAgICAgeG1sbnM6eG1wR0ltZz0iaHR0cDovL25z
LmFkb2JlLmNvbS94YXAvMS4wL2cvaW1nLyIKICAgICAgICAgICAgeG1sbnM6eG1wTU09Imh0dHA6
Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICAgICAgICAgIHhtbG5zOnN0UmVmPSJodHRw
Oi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIgogICAgICAgICAgICB4
bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZl
bnQjIgogICAgICAgICAgICB4bWxuczppbGx1c3RyYXRvcj0iaHR0cDovL25zLmFkb2JlLmNvbS9p
bGx1c3RyYXRvci8xLjAvIgogICAgICAgICAgICB4bWxuczpwZGY9Imh0dHA6Ly9ucy5hZG9iZS5j
b20vcGRmLzEuMy8iPgogICAgICAgICA8ZGM6Zm9ybWF0PmltYWdlL2pwZWc8L2RjOmZvcm1hdD4K
ICAgICAgICAgPGRjOnRpdGxlPgogICAgICAgICAgICA8cmRmOkFsdD4KICAgICAgICAgICAgICAg
PHJkZjpsaSB4bWw6bGFuZz0ieC1kZWZhdWx0Ij5TaW1ib2xvX0FjcmVkaXRhZG9fT05BQzwvcmRm
OmxpPgogICAgICAgICAgICA8L3JkZjpBbHQ+CiAgICAgICAgIDwvZGM6dGl0bGU+CiAgICAgICAg
IDx4bXA6TWV0YWRhdGFEYXRlPjIwMjEtMDktMDNUMTk6NTE6NDYtMDU6MDA8L3htcDpNZXRhZGF0
YURhdGU+CiAgICAgICAgIDx4bXA6TW9kaWZ5RGF0ZT4yMDIxLTA5LTA0VDAwOjUxOjUyWjwveG1w
Ok1vZGlmeURhdGU+CiAgICAgICAgIDx4bXA6Q3JlYXRlRGF0ZT4yMDIxLTA5LTAzVDE5OjUxOjQ2
LTA1OjAwPC94bXA6Q3JlYXRlRGF0ZT4KICAgICAgICAgPHhtcDpDcmVhdG9yVG9vbD5BZG9iZSBJ
bGx1c3RyYXRvciAyNS4yIChXaW5kb3dzKTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1w
OlRodW1ibmFpbHM+CiAgICAgICAgICAgIDxyZGY6QWx0PgogICAgICAgICAgICAgICA8cmRmOmxp
IHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHhtcEdJbWc6d2lk
dGg+MjU2PC94bXBHSW1nOndpZHRoPgogICAgICAgICAgICAgICAgICA8eG1wR0ltZzpoZWlnaHQ+
OTI8L3htcEdJbWc6aGVpZ2h0PgogICAgICAgICAgICAgICAgICA8eG1wR0ltZzpmb3JtYXQ+SlBF
RzwveG1wR0ltZzpmb3JtYXQ+CiAgICAgICAgICAgICAgICAgIDx4bXBHSW1nOmltYWdlPi85ai80
QUFRU2taSlJnQUJBZ0VBU0FCSUFBRC83UUFzVUdodmRHOXphRzl3SURNdU1BQTRRa2xOQSswQUFB
QUFBQkFBU0FBQUFBRUEmI3hBO0FRQklBQUFBQVFBQi8rNEFEa0ZrYjJKbEFHVEFBQUFBQWYvYkFJ
UUFCZ1FFQkFVRUJnVUZCZ2tHQlFZSkN3Z0dCZ2dMREFvS0N3b0smI3hBO0RCQU1EQXdNREF3UURB
NFBFQThPREJNVEZCUVRFeHdiR3hzY0h4OGZIeDhmSHg4Zkh3RUhCd2NOREEwWUVCQVlHaFVSRlJv
Zkh4OGYmI3hBO0h4OGZIeDhmSHg4Zkh4OGZIeDhmSHg4Zkh4OGZIeDhmSHg4Zkh4OGZIeDhmSHg4
Zkh4OGZIeDhmSHg4Zi84QUFFUWdBWEFFQUF3RVImI3hBO0FBSVJBUU1SQWYvRUFhSUFBQUFIQVFF
QkFRRUFBQUFBQUFBQUFBUUZBd0lHQVFBSENBa0tDd0VBQWdJREFRRUJBUUVBQUFBQUFBQUEmI3hB
O0FRQUNBd1FGQmdjSUNRb0xFQUFDQVFNREFnUUNCZ2NEQkFJR0FuTUJBZ01SQkFBRklSSXhRVkVH
RTJFaWNZRVVNcEdoQnhXeFFpUEImI3hBO1V0SGhNeFppOENSeWd2RWxRelJUa3FLeVkzUENOVVFu
azZPek5oZFVaSFREMHVJSUpvTUpDaGdaaEpSRlJxUzBWdE5WS0JyeTQvUEUmI3hBOzFPVDBaWFdG
bGFXMXhkWGw5V1oyaHBhbXRzYlc1dlkzUjFkbmQ0ZVhwN2ZIMStmM09FaFlhSGlJbUtpNHlOam8r
Q2s1U1ZscGVZbVomI3hBO3FibkoyZW41S2pwS1dtcDZpcHFxdXNyYTZ2b1JBQUlDQVFJREJRVUVC
UVlFQ0FNRGJRRUFBaEVEQkNFU01VRUZVUk5oSWdaeGdaRXkmI3hBO29iSHdGTUhSNFNOQ0ZWSmlj
dkV6SkRSRGdoYVNVeVdpWTdMQ0IzUFNOZUpFZ3hkVWt3Z0pDaGdaSmpaRkdpZGtkRlUzOHFPend5
Z3AmI3hBOzArUHpoSlNrdE1UVTVQUmxkWVdWcGJYRjFlWDFSbFptZG9hV3ByYkcxdWIyUjFkbmQ0
ZVhwN2ZIMStmM09FaFlhSGlJbUtpNHlOam8mI3hBOytEbEpXV2w1aVptcHVjblo2ZmtxT2twYWFu
cUttcXE2eXRycSt2L2FBQXdEQVFBQ0VRTVJBRDhBOUxhcjVsMExTbUNYOTRrTWhGUkgmI3hBO3U3
MDhlS0JtL0RJbVlITnc5VDJoZ3dHc2tnRDl2eUNYL3dES3hmSnYvVncvNUl6L0FQTkdSOFdMaS95
N3BQNS8reGwrcDMvS3hmSnYmI3hBOy9Wdy81SXovQVBOR1BpeFgrWGRKL1A4QTlqTDlUdjhBbFl2
azMvcTRmOGtaL3dEbWpIeFlyL0x1ay9uL0FPeGwrcDMvQUNzWHliLzEmI3hBO2NQOEFralAvQU0w
WStMRmY1ZDBuOC84QTJNdjFPLzVXTDVOLzZ1SC9BQ1JuL3dDYU1mRml2OHU2VCtmL0FMR1g2bmY4
ckY4bS93RFYmI3hBO3cvNUl6LzhBTkdQaXhYK1hkSi9QL3dCakw5VHYrVmkrVGY4QXE0ZjhrWi8r
YU1mRml2OEFMdWsvbi83R1g2bmY4ckY4bS84QVZ3LzUmI3hBO0l6LzgwWStMRmY1ZDBuOC8vWXkv
VTcvbFl2azMvcTRmOGtaLythTWZGaXY4dTZUK2Yvc1pmcWQveXNYeWIvMWNQK1NNL3dEelJqNHMm
I3hBO1YvbDNTZnovQVBZeS9VNy9BSldMNU4vNnVIL0pHZjhBNW94OFdLL3k3cFA1L3dEc1pmcWQv
d0FyRjhtLzlYRC9BSkl6L3dETkdQaXgmI3hBO1grWGRKL1AvQU5qTDlUditWaStUZityaC93QWta
LzhBbWpIeFlyL0x1ay9uL3dDeGwrcDMvS3hmSnY4QTFjUCtTTS8vQURSajRzVi8mI3hBO2wzU2Z6
LzhBWXkvVTcvbFl2azMvQUt1SC9KR2YvbWpIeFlyL0FDN3BQNS8reGwrcDMvS3hmSnYvQUZjUCtT
TS8vTkdQaXhYK1hkSi8mI3hBO1AvMk12MUw0ZlA4QTVRbWtFYWFpb1k5QzZTb3YvQk9xakQ0a2U5
bEh0clNTTkNmMkVmZUUvUjFkUTZFTWpBRldCcUNEMElPVGRtQ0MmI3hBO0xEZUtYWXE3RlhZcTg3
L05UekJlMjBsdnBWdEswS1N4K3RjTWhJWmdXS3F0UjIrRTE4Y296U1BKNVgyajFzNEdPS0pxeFpl
YVpqdkkmI3hBO094VjJLdXhWMkt1eFYyS3Bsb092WCtqWDhkMWF5TUZERDFvYS9ESXZkV0hUcGtv
eUlMbDZQV1QwOHhLSjk0NzBKZTNseGUzYzEzY00mI3hBO1htbmN1N0h4UDhQRElrMjBaY3Nza3pL
WE1xR0xXN0ZYWXE3RlhZcTdGWFlxN0ZYWXE3RlhZcTdGWFlxN0ZYWXE3RlhZcTlaL0ttL3UmI3hB
O0o5RW50NVdMcGF6VWhKTmFLNjE0L0lHdVpPRTdQYit6ZWFVc0ppZjRUc3piTG5vbllxN0ZYWXE4
bS9Oci9sSTdiL21EVC9rN0ptTG0mI3hBOzV2RCswdjhBakVmNmcrK1RDY3FlZVZyT3p1cjI1UzJ0
WW1tbmtORWpVVkp4QXRzeFlwWkpDTVJjaTlDMFg4cGxLTExyRnlReDNOdEImI3hBO1RiMmFRMXI5
QStuTDQ0ZTk2blNlelcxNVpmQWZyWkVuNWNlVDFVQTJKY2pxeG1tcWZ1Y0RMUENpN1VkaGFRRDZQ
dGwrdEJhaCtWZmwmI3hBOzY0US9WR2xzNVAyU0c5UkI4MWY0ai93V0E0UTQyZjJjd1NIb3VCK1kr
Mzliejd6SDVRMWZRWHJjS0piVmpTTzZqM1Fud2J1cCtlVVQmI3hBO2dZdkw2L3N2THBqNnQ0OTQv
R3lSNUIxenNWZGlyc1ZYUnh5U3lMSEdwZVJ6UlVVRWtrOWdCaW1NU1RRM0xLckg4c3ZORjFHSkhT
SzAmI3hBO0IzQ3p1UTMzSUhwOU9XREZJdTZ3K3orcG1MSUVmZWYxV3QxSDh0Zk5GbkdaRmlqdTFV
VmI2dXhacWY2ckJHUDBERTRwQkdmc0RVNHgmI3hBO2RDWDlYOEJpekt5TVZZRldVMFpUc1FSMk9W
dWxJcll0WXFuVnI1TTgwWFVBbmgwNlV4RVZVdHhRa2VJRGxTY21NY2owZGhqN0sxTTQmI3hBOzhR
Z2ErWDNwWGQybDFhVHRiM1VUd1RKOXFPUUZXSDBISUVVNFdURktFdUdRb3F0bHBXbzMwVnhMYVFO
TWxxb2VjcFFsVk5kNmRUMDcmI3hBO1lSRWxuaTAyVElDWUMrSG1vVzl2TmNYRVZ2Q3ZPYVoxamlR
ZDJZMFViK0pPQUJyaEF6a0lqbWRsYlVkTXZ0TnVUYTMwUmhuQURGQ1EmI3hBO1RROU9oT0Vnam0y
WjlQUEZMaG1La29Rd3l6VEpERXBlV1Jna2FEcVdZMEFIMDRHcU1USWdEbVZTK3NidXd1cExTN2pN
TnhGVG5HMUsmI3hBO2lvcU9uc2NKRk04MkdXT1JqTVZJS0dCclR1MDhsK2FMdTNGeEJwOGhpSXFw
WXFoSVBjSzVVbkpqSEk5SFlZdXlkVE9QRkdCcjVmZWwmI3hBO1YzYVhWcE8xdmRSUEJNbjJvNUFW
WWZRY2dSVGhaTVVvUzRaQ2lvNHNIcVA1US84QUhPMUQvak1uL0VjeU1ISjdMMlkvdTUvMWg5elAm
I3hBO3N2ZW5kaXJzVmRpcnliODJ2K1VqdHY4QW1EVC9BSk95Wmk1dWJ3L3RML2pFZjZnKytUQ2dD
U0FCVW5ZQVpVODg5cThrZVZJZEQwNVomI3hBO0pVQjFLNFVHNGtQVlFkeEdQWWQvRS9SbVhqaFFm
UXV5T3pScDhkbis4bHovQUZNa3l4MjdEdk12NWkyT21YdjFDMEhyVG8zRzVtcHkmI3hBO1NMZjRn
RnFuTmg0Y2hsVThvR3pvTmYyN0REUGdqdWVwNkQ3clB4VG13Z1RVYlNLOWkxYTV1SXBSeVIwTWNh
L0xpaUwwNkVOa2h2MWQmI3hBO2hoZ01zUk1aSlNCOXcrNGZldXU5T3Y4QTZ0SkMwZzFTMWtYakxh
WFNvcnN2Z3NrWVJhK0hKZjhBWkRyaElQdlRsd1Q0U0NmRWllY1omI3hBO1Zmd0lyN1I4UThhOHhh
U3VtYWs4VVJZMnpFbUgxQlIxRmQwY2RtWHY0N0hvUm1KS05GNERYYVlZY2hBK25wZlAzSHpIN2Vx
VjVGdzMmI3hBO1lxN0ZYcnY1ZGVWWU5QMDJMVkxoQTEvZG9IUW5mMDRtM1VEM1libjdzeXNVS0Z2
ZGRoZG14eFl4a2tQWEw3QW12bXp6WmFlWDdSWGQmI3hBO2ZXdTVxaTN0d2FWcDFaajJVWktjK0Z6
ZTB1MG82V0ZuZVI1Qlo1WjF0UE1GaDlhaHU1WXBsSVc0dHdJdjNiZTFVWWxUMkpPTUpjUVkmI3hB
OzluNnNhcUhFSkVIcU50dnM1TWEvTXJ5My9vcDFaVVV6UmtDYVpCeDVxVHhIcUtOdVEvbUhYcHR0
V3ZMRHE2anQvUWVueGVvNW52OEEmI3hBO2Y1K2Y3R1BmbHZwbHRmOEFtWlByQ2gwdG9tdUZSdWha
U3FydDdGcS9SbGVJV1hWZGc2ZU9UVURpL2hGL2o1cW5tSHozNWtmV3JqNnYmI3hBO2RQYXcyOHJK
REFnQUFDTngrTUVmRVRUZXVHV1EyeTEzYkdvT1k4TWpFUk93OTNlbTNtcVZOYzhpV091M0VZanY0
bjlObkFweUhJeHMmI3hBO0I3RWpsN1pLZThiYzd0R1ExT2lobmtLbURYMjErMWIrVWpoSmRXY2lv
V09Ja2ZJdmpnNm85bVRSeUh5SDZWV2J5MVkzV3JhVDVqOHYmI3hBO2Z2TlBsdklHdXJkUnZDM3Fy
VThld0g3UTdmTG84QUpCRE9mWjhKNWNlbzArOERPTmp1M0g0UGQ3a20vTS93RDVTcVQvQUl3eGZx
T1ImI3hBO3pmVTRIdEQvQUl5ZjZvVlB5NjAyQVhWenJ0NktXV2x4bHd4NkdXbGZwNHIrTk1jUTZu
b3k3QzA4ZUtXZWYwWXg5djQvUWl2UE1VT3QmI3hBO2FKWWVhYlJPSllDRzlRYjhUV2dyMCt5MVZy
N2pEazNIRTM5c1JHb3d3MU1CNVMvSHYyK1NWL2x6cHR0ZmVaNGhjS0hTM1Jwd2g2RmsmI3hBO29G
cjhpMWNqaUZsd3V3c0VjbXBIRnlpTFJIbVR6MTVqT3VYSzIxMDFyRGF6UEhGQ2xLVWpZclZxajRx
MDc0WjVEYmJyKzJOUjQwaEcmI3hBO1hDSWtnRDNkL2Vrdm1EekhxT3UzTWM5N3dEUklFUlkxNGdE
dWU1M08vWElTa1R6ZGRyZGZrMU1oS2RiRG9sV1JjTjZqK1VQL0FCenQmI3hBO1EvNHpKL3hITWpC
eWV5OW1QN3VmOVlmY3o3TDNwM1lxN0ZYWXE4bS9Oci9sSTdiL0FKZzAvd0NUc21ZdWJtOFA3Uy80
eEgrb1B2a2wmI3hBO1hrSFQwdnZOTm1rZzVSd2t6c1ArTVlxdi9EMHlPTVhKd3V4Y0F5YW1JUEli
L0w5cjI3TXg5RlNMenRyVW1rZVhyaTVoUEc0a3BEQTMmI3hBO2c3OS9vVUU1REpLZzYzdGJWbkJn
TWg5UjJIeGVIRWttcDNKNm5NTjg0WjErVld0eVE2bkpwTWpWZ3VsTWtLbnRLZ3FhZjZ5QTErV1gm
I3hBO1laYjA5TDdPYXN4eUhFZVV0eDd4K3o3bnFtWkwyanovQVBOZlJJM3M0ZFhpV2tzVENLNHAz
UnZzc2ZjRVUrbktNMGVyeS90SnBBWUQmI3hBO0tPWTJMekRNZDQ1Mkt1eFY5R3hxaVJxa1lBalVB
SUIwb0J0bWUrc1JBQW9jbmp2NW16VFNlYkowa3J3aGppU0d2OHBRTWFmN0pqbUomI3hBO2wrcDRI
MmdtVHFpRDBBcjVYOTZML0tlYVpmTUU4S2srbEpiTTBpOXFxNjhUOUhLbjA1TER6Yi9acVpHY2dj
akg5SWVtNjFERk5vOTcmI3hBO0ZLS3h2QklHQjhPQnpJbHlldzFjUkxGSUhsd243bmhtZzZ6Y2FO
cWtPb1FEazBSSWVNbWdkR0ZHVS9NWmhSbFJ0ODQwZXJscDhveVImI3hBOzZmYXpLNnZmeXgxaWY5
STNyeldkMUo4VThDcTRETjNyd1YxMzhRUmx4TUR1Ny9KbTdPenk4U2ZGR1I1amY5QUtUK2NQTnRy
cWR2QnAmI3hBO1dsUW0zMG0xb1VVaWhjcUtEYmVnRmY0bklUbmV3NU9CMnAybkhORVlzUTRjVWZ0
WCtRZk1HbDZQK2t2cjhoaitzUm9zVkZacWtjcS8mI3hBO1pCOGNPT1FGMnk3RjF1TEJ4OFpyaUcz
MnBmNVQ4MTNmbCs5OVJBWmJPVWdYTnY0Z2Z0TDRNTWpDZkNYRjdON1NscFoyTjRIbVB4MVgmI3hB
OytlTllzZFcxNXJ5eWN2QTBTS0N5bFRWUnVLSEhKSUU3SjdYMVVNK2ZqaHlvSjNGNTJzdEM4dVdO
aG9UTFBlVkwzc2tzYkJlVENyVXImI3hBO3hydWFBK0F5ZmlDSW9PeGoydERUYWVNTUc4LzRyQi9a
L1lGWFRmekVpMUszdmJEekp3anRiaUVwSEpER3hJWTdHb3EyKzlRZmJDTXQmI3hBOzdGc3dkdURO
R1VOUlFqSWRCL2F4RFJ0WG4wWFY0NzYxSWtNTEVVTlFzaUhZamZjVkgzWlZHVkczUTZYVXkwK1VU
anZYMmhtTjFmZmwmI3hBO2pyRS82UnZXbXM3cC9pbmdDeUFPM2NuMDFkZC9FRVphVEE3bDMrVE4y
ZG5sNGsrS01qekcrL3lCL1F4ZnpWZjZEZVg2dG8xbWJTM2omI3hBO1FJeE8zcUZkZzNEZmp0OS9m
S3BrRTdPbTdSellNazd3eDRZZ2ZQNEpMa1hYdlVmeWgvNDUyb2Y4WmsvNGptUmc1UFplekg5M1Ar
c1AmI3hBO3VaOWw3MDdzVmRpcnNWZVRmbTEveWtkdC93QXdhZjhBSjJUTVhOemVIOXBmOFlqL0FG
Qjk4a1ArVjB5UithVlZqUXl3U0ludVJSdjEmI3hBO0tjY1AxTlhzN0lEVTEzeFA2M3NPWlQzckN2
elloa2Z5OUJJdFNrZHlwY2RxRkhBUDM3ZlRsT2JrODk3U3hKd0E5MHYwRjVMbU04T3kmI3hBO1A4
dllwSlBOOWh3L1lNanNmQUNOdjlyTE1YMU8xN0RpVHFvVjUvY1h0bVpiNkl4bjh5SkVUeWhlSzNX
Um9sVDUrcXJmcVU1WGwrbDAmI3hBOy9iMGdOSkx6cjd3OFd6RWZQbllxN0ZYc1hrVHpRbDlvc2Nk
MC93Qy90QUlwWk56c05sTW44dndqN1IyUGpYTXJIT3c5NzJQMmlNbUUmI3hBO0NYT08zNnIvQUY4
a3YvTUR5L2I2MEk3N1RKb3B0UWlYZzl1akt6U3BXbzRnSDdTMVAwWkhMRzl3NHZiZWlqcUtuaklN
eDA3eCt4TXYmI3hBO0lQbEdUUTdTU2U4cCtrTHFuTlFhaU5CdUVxTzlldVN4d3B5K3hlekRwb0dV
L3JsOWc3djF0L21KNWdoMDNRNWJSV0J2TDVURkdnNmkmI3hBO050bmMrMU5oNzQ1WlVGN2Mxd3hZ
VEFmWFBiNGRTOGZ0YmFhNnVZcmFGZVUwenJIR3ZpekdnekZBdDRUSGpNNUNJNWsweXUrOGlvTmQm
I3hBOzAyd3M1eTlwZThvcExrajdNdHZYMXhUYitXcTVhY2U0RHU4M1k0OGFFSUgwejJ2emo5WDdF
SWxuNU52THl5dExBM3F6UzNjVUQrdDYmI3hBO1pWNG5jS3pnZ0FxMzBZS2llVFFNV2t5VGpDSEha
bUJ2VzRKNStTYXplVHRHa1lORkRlV2F4YWhCWnVMa3J4bVNXVUlXaVBGVFVEZnYmI3hBO2t1QWZh
NXN1eThKNUNjYXlSajZ2NGdUVzJ5elVQS3VqUWF0YWFlTE82aFdlOEZ2OVllYUoxZU1NUVNxcU9T
azlSWEV3RjB4ejluWW8mI3hBOzVZNCtHWTRwMWZFTndnNXRCMEM4aHVadE1OeEMybjNFVU41RE9W
WU1rMHZwQm8yVUNocjJPUjRRZVRqeTBXQ1lrY2ZFT0NRRWdlNG0mI3hBO3RrVGFhRDVYT29hell6
eFhUUHBTWE54eldSQUdpZ0lBWGRmdGI5Y0lqR3lPNXV4YUxUZUpsaElUdkdKSG1PVWZoelEybGVV
N1hWcksmI3hBOyt2TGIxSVE3R1BSNEpDR2FTU05USTZzUU4vaEZCNzRCQzJuVGRteHp3bk9OanBB
ZDVHNVU3SFN2TGNYbCswMURWRnVqSmRYRWtCYUImI3hBO2xIQUorMXhaVFhFQVZaWTRkTnA0NEk1
TXZGY3BFYlZzcjNIbFBTOUhYVUxuV0pacDdhMXVWdExlSzM0cTBqdkdKZ3pzM0lLT0RENmMmI3hB
O0pnQnpiTW5adVBCeHl5a21NWmNJNGV1M0Z2OEFCS2ZNV2syVmtiUzVzSkhrc2IrTDFvQk1BSkVv
ZUxLMU5qUWpxTWhLTmNuQjEybWgmI3hBO2o0WlFKTUppeGZNZVJTZkl1QzlSL0tIL0FJNTJvZjhB
R1pQK0k1a1lPVDJYc3gvZHovckQ3bWZaZTlPN0ZYWXE3RlhrMzV0ZjhwSGImI3hBO2Y4d2FmOG5a
TXhjM040ZjJsL3hpUDlRZmZKaVduWDgrbjM4RjdibWsxdTRkUEEwN0gyUFE1V0RSdDBlRE5MRk1U
anppWHZPa2F0YmEmI3hBO25hSmNRL0N4VlRKQ1NDeUZoVVZwMUJHNFBRanBtYkdWdnBlbDFNYzBP
SWZMdS9IUTlYYXpwY0dxNlhjYWZOc2s2Y1EzWGl3M1Z2b1kmI3hBO0E0eUZpazZ2VHh6WTVZenlr
OEoxWFNyM1M3NlN5dkl5azBacDdNT3pLZTRPWVVva0duelhVNmFlR1poTWJoNlgrV25sYWJUcmVU
VkwmI3hBOzFPRjFkS0ZoallmRWtYV3A4Q3hwbVJpaFc3MS9ZSFp4eFJPU1lxVXVYa1AyczR5NTZO
NXIrYkd0bzcyMmp4TUNZejY5elRzeEJDTDkmI3hBO3hKKzdNZk5MbzhqN1M2c0V4d2pwdWYwZmoz
UE9zb2VVZGlyc1ZSZW1hcmY2WGRyZDJNeGhuWGFvM0JIY01Ec1I4OElKSEp1MCtwbmgmI3hBO2x4
UU5GbmxqK2J4RVFXLzAvbEtCdkpBOUFUL3FzRFQvQUlMTGhuNzNwc1B0UHQ2NGIrUi9IM3JkUi9O
eVZvaW1uMklqa0kybG1ibFQmI3hBOy9ZS0IrdkU1KzVHZjJtSkZZNFVlOC9xWUZmNmhlYWhkUGQz
a3JUWEVocXp0K29Eb0FQQVpTVGJ6T2JQUExJeW1ia1ZYU05WbjBxK1cmI3hBOzl0MGplZU5XRVpr
QllLV0hIa0FDUGlGZHE0eE5HMmVsMU1zTStPSUhFTy83MGV2blB6QjZBaWt1RE84Y3lYRUZ4TFY1
SW5TbytBazAmI3hBO293TkNDRGt2RUxranRYUHcwVFpCQkJQTUVkMzZWU2Z6cGZTdEF5V1ZsYm1H
NFM3WXd3OFRKTEdlUUxtcFBYcnhwaWNoWno3Vm5JZ2kmI3hBO01JMUlTMmp6STcvMlUwM25YV1pl
SDFuMDdreFhhMzF1MDNOakU2dHk0SWVmMk8zRTl1bVBpRkI3V3pINnFsVStNWGV4N2h2eThsMDMm
I3hBO25PNGt1MHZGMHl3aXUwbkZ4NjhjVGgyY055UEk4enN4NjQrSjVKbjJySXlFK0RHSmNYRllC
dS9tcDN2bS9VTG1NUlIyOXJad21WWjUmI3hBO283YU1vSlpFUEpUSVN6TWQvZkV6TEhMMnBrbUtF
WXhGMmVFVlo4MUJQTXQ4bC9xZDZJNHZWMVdHYUM0V2pjVldjZ3NVK0tvSXB0VW4mI3hBO0J4bXll
OXFHdm1Kem5RdklDRC9uZDI2ckQ1eDF5Mmhzb0xTYjZyQlpLRlNHSGtxU0hseUxTZ2s4aXhPL2JE
eGxzaDJwbWdJeGdlR00mI3hBO09nNjlkKyswUkY1NHZZNHpIK2o3R1JSTzl6RUpJbmIwNUpEVWxB
WG9LSHBoOFJ0ajJ2TUN1REdmVVpiZzdFOTI2SHRmTnVxUlNYYlQmI3hBO3JEZlIzeityY3dYU2Vw
R3pqb3dBSzBJOXNBbVduSDJubGlaY1ZURXpaRWhZdEJhdnJONXF0eXM5endVUm9JNFlZbDRSeG92
UlVVZEImI3hBO2taU3RvMVdxbm1seFM2YkFEWUFlU0J3T005Ui9LSC9qbmFoL3htVC9BSWptUmc1
UFplekg5M1Arc1B1WjlsNzA3c1ZkaXJzVmVUZm0mI3hBOzEveWtkdC96QnAveWRrekZ6YzNoL2FY
L0FCaVA5UWZmSmhPVlBQTXM4b2VhYlcwS1dXcUYxdDFxTGEraUpXV0RrYWxhcnUwWk81WGYmI3hB
O2ZzY3NoT3RpN3ZzdnRHTUtobHZoNlNIT1AvSGZMN0hwOXZGZnpRSkxhNnNKN2R4VkptaWpja2VJ
YVBndi9DNWtpKzk3R0VaeWpjY24mI3hBO0ZFOWFCKzZoOWk1ZEJ0WHVZcnErZHI2NWdxWVhuQ2NZ
Ni95SWlxdjBrRSsrUEQzc2hvNG1RbFAxeUhLNjI5d0ZEOUtaWkp5MkwrYmYmI3hBO1BXbjZMRThG
dXkzR3BrVVdFR3F4bnhrSTZVL2w2NVhQSUI3M1RkcDlzWTlPREdQcXlkM2Q3LzFQSGJxNW51cmlT
NXVITWswckY1SGImI3hBO3FTY3hDYmVDeVpKVGtaU05rcVdMQmZOREpCTkpES3BXU0ppanFlb1pU
UWpGbE9KaVNEekN6Rmk3RlhZcTdGWFlxN0ZYWXE3RlhZcTcmI3hBO0ZYWXE3RlhZcTdGWFlxN0ZY
WXE5VS9LT0dSZEp2WldVaU9TY0JHUGZpdTlQdnpKd2NudFBabUpHS1I2R1g2R2Q1YzlLN0ZYWXE3
RlgmI3hBO2szNXRmOHBIYmY4QU1Hbi9BQ2RrekZ6YzNoL2FYL0dJL3dCUWZmSmhPVlBQSWlmVDcr
M2pXV2UybGlqYjdMdWpLcHI0RWpDUVd5ZUMmI3hBO2NSY29rRDNJblM5WDF6VFZhZlQ3aWFDSU1C
SVVxWStSNmNnYXBYYnZoRWlPVGRwOVRtdytyR1NCOW42bVFMK1pIbktLMldXUVJ2RkomI3hBO1ZV
bmVHZ0pIV2hYaXBPVDhXVHRCMjlxeEd6Vkhyd3BmZmVkZk51b3d5Y3JxUkxkQVBWRUNpTlZER2c1
TWdydWR0emtUa2tYRnpkcmEmI3hBO3JLRGNqdytXMzNNZkFabW9LbGlmbVNUa0hWODFhNXNMNjFD
bTV0cFlBLzJESWpKWDVjZ01KQkRaa3d6aDlVU1BlS1VNRFc5dDEzeUYmI3hBO29HczNKdXAxa2d1
Ry92SllHQ2w2ZnpCbFlWOTZabHl4Z3ZvZXM3R3dhaVhGS3hMeTYvZWxuL0twZkxuL0FDMDNuL0J4
ZjlVOGo0SWMmI3hBO1AvUTFwLzUwL21QK0pkL3lxWHk1L3dBdE41L3djWC9WUEh3UXYraHJUL3pw
L01mOFM3L2xVdmx6L2xwdlArRGkvd0NxZVBnaGY5RFcmI3hBO24vblQrWS80bDMvS3BmTG4vTFRl
ZjhIRi93QlU4ZkJDL3dDaHJUL3pwL01mOFM3L0FKVkw1Yy81YWJ6L0FJT0wvcW5qNElYL0FFTmEm
I3hBO2YrZFA1ai9pWGY4QUtwZkxuL0xUZWY4QUJ4ZjlVOGZCQy82R3RQOEF6cC9NZjhTNy9sVXZs
ei9scHZQK0RpLzZwNCtDRi8wTmFmOEEmI3hBO25UK1kvd0NKZC95cVh5NS95MDNuL0J4ZjlVOGZC
Qy82R3RQL0FEcC9NZjhBRXUvNVZMNWMvd0NXbTgvNE9ML3FuajRJWC9RMXAvNTAmI3hBOy9tUCtK
ZC95cVh5NS93QXRONS93Y1gvVlBId1F2K2hyVC96cC9NZjhTNy9sVXZsei9scHZQK0RpL3dDcWVQ
Z2hmOURXbi9uVCtZLzQmI3hBO2wzL0twZkxuL0xUZWY4SEYvd0JVOGZCQy93Q2hyVC96cC9NZjhT
Ny9BSlZMNWMvNWFiei9BSU9ML3FuajRJWC9BRU5hZitkUDVqL2kmI3hBO1hmOEFLcGZMbi9MVGVm
OEFCeGY5VThmQkMvNkd0UDhBenAvTWY4UzcvbFV2bHovbHB2UCtEaS82cDQrQ0YvME5hZjhBblQr
WS93Q0omI3hBO2QveXFYeTUveTAzbi9CeGY5VThmQkMvNkd0UC9BRHAvTWY4QUV0eC9sUDVhVjFa
cHJ0d0RVb3p4MFBzZU1ZUDQ0K0NHVWZaclRnODUmI3hBO240ajlUTHJLeXRiSzFqdGJTSVEyOFFw
SEd2UURMUUtkNWl4Unh4RVlpb2hXd3Rqc1ZkaXJzVmVUZm0xL3lrZHQvd0F3YWY4QUoyVE0mI3hB
O1hOemVIOXBmOFlqL0FGQjk4a3I4Z2l5UG1pMUYwRVAyL1FFbjJmVzRuaFg2ZW52a2NmMU9IMkx3
Zm1ZOFhuVjkvUmsya3Q1cWVUVmgmI3hBOzVvRW42SUVFbjFqNndBSStZK3g2UDhPUDY2WlpIaTM0
dVR0OU1kU1RrL00zNFhDYjR1WGx3L3MrOUxmSmQzWldubGZYWjc2Myt0V2cmI3hBO2UyV2VIdVZk
K0JJOXh5cVBmSTR6VVRiaWRrNVlRMDJXVXh4UnVOajNtbS9OOXBZMnZsRFNZN0NmNnpaTmNUU1c4
dmZnOVRSdjhwZWgmI3hBO3d6QUVSU2UxTVVJYVhHSUhpaHhTSVB2VGJ5enBkbFlhSEJZWDh0ckcr
dHF6M3NjOHF4emlGMUt3Q05EdVR5Mzlqa29BQVVlcm5kbjYmI3hBO2VHUENJVE1RYzMxV2FsWDhO
QkkvSjJublQvTnQ1WlhBVDlJMjBNNldBazJCdUJUZ1JYeFdwR1FnS2s2M3N2QjRXcWxDVmVKR011
Ry8mI3hBOzUzVDdGSFdIOC9Ob2MvNldXWDlIZXN2cW1ZSUdEMTJwWDQrUEx3MjhNRXVLdDJHcU91
T0UrTGZoMzFyKzJ2c1lwbGJwSDBmbWUrc3UmI3hBO3hWMkt1eFYyS3V4VjJLdXhWMkt1eFYyS3V4
VjJLdXhWMkt1eFYyS3V4VjJLdXhWMkt1eFYyS3ZKdnphLzVTTzIvd0NZTlA4QWs3Sm0mI3hBO0xt
NXZEKzB2K01SL3FENzVNUjAreW52YjJHMGdwNnN6QlZKMkE4V0o3QlJ1Y3JBc3Vqd1lwWkppTWVa
VHkvMHpYbXNaanFtcWNZYmEmI3hBO1o0SVlMbWFWL1VlSlF4OUphTUtjU0tIYXUyVElOYmwyT2JU
NStBK0xrMmlTQUpTTzVIZHpSU2VTdFpqUnJTUFVGK3JUaG1uaWpGd1EmI3hBO3pRY0RReEtsWktl
b0tGUWQ4UGhudmJoMlRtQTRSUDB5NWdjWDhOZEszNTlMUTMrRk5TbHNRa04vSExHcGVZV1JNcU1F
V1kyN3lpTjEmI3hBO1ViTW0vd0MxVEJ3R21yK1RjaGhRbUNOenc3aitMaE1xSTh0K3JWMzVmMUM2
ZU9XVFZGdkwyUzVheFZITXpQNmtSSE1GM1dnVkZZTlcmI3hBO3RLWW1KUFZHVFJaSmtFNU9LWmx3
ZnhYWTU3a2NoZHJ2OE02MWZYYzdYRjhyYWtrN1c4SW1lUnBKbmpRT09FaEREZEtjZVJHUEFTbism
I3hBO1Q4MlNSTXAvdk9LaFpOeUlGN0gzY3JhMW5Sdk1QNksrdDMyby9XeGJyRkpOWnZNOGtrQ3o3
UnNRM3c3K3h4bEUxdVYxV2x6K0Z4VG4mI3hBO3hjTkV4NGlUSGk1TWF5dDFENlB6UGZXWFlxN0ZY
WXE3RlhZcTdGWFlxN0ZYWXE3RlhZcTdGWFlxN0ZYWXE3RlhZcTdGWFlxN0ZYWXEmI3hBOzdGWGsv
d0NiU3QvaUcyYW53bTBRQTlxaVdTdjY4eHMzTjRqMm1INytQOVQ5SlloWTZoZVdNeG5zNVRETVZa
Qkt0T1FEQ2g0bnFwcDMmI3hBO0crVkEwNkxEbm5qUEZBMFVkSjVxOHdTUXlReTNqU0pLQUpPYW94
UEZPSExrVjVjdUd4YXRUM3c4WmNpWGFXY2dneXNIM2QxZk91dk4mI3hBO2QvaTN6QVg1dmRDUnFN
UDNrVVVnQ3Z4NUtBNk1BcDREYnBqeGxQOEFLZWU3TXI5NEI1KzhjdHVTMXZOT3VtMityQzRDUTE1
Y1k0b2smI3hBOy93QjJHV2xWUUhqek5lUFRIaktEMmptNGVHOXZJQWRiNkRsZlRrcFJlWU5ZaVpu
aXVDanRKTk56VlVEQ1M0VUxJeXNCVlNRbzZkTzImI3hBO1BFV0VkYmxpYkVxTms5T2N0aWZMOFVy
anpmNWpDTXYxd2t1S05JVWpNcCtIaFgxQ3ZPdkhhdGE0OFpiUjJwcUtyaSt3WDNjNnZrbzMmI3hB
O1BtTFdyblRrMDZlNlo3T01LRmpJV3RFK3lHWURrd1h0VTRtUnFtdkpyczA4WXh5bGNCK2o3VXVW
V1pncWlyTWFBRHFTY2k0Z0Z2bzcmI3hBO005OVpkaXJzVmRpcnNWZGlyc1ZkaXJzVmRpcnNWZGly
c1ZkaXJzVmRpcnNWZGlyc1ZkaXJzVmRpcnNWWWIrWmYrSHYwYkQra3VmMXkmI3hBO3ArcGVqVDFP
M0t0ZHVIU3Y0WlZscXQzUWR2OEFnZUdQRXZqL0FJYTUvd0JqeUkwcnQwekZlRmRpcnNWZGlyc1Zk
aXJzVlpSNUIvdzcmI3hBOyttb1AwcHorc2N4OVVyVDBmVS9aNTk2MTZkc3N4MWU3dU94ZnkvakR4
TDRyOVBkZm0vL1o8L3htcEdJbWc6aW1hZ2U+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAg
ICAgICAgICA8L3JkZjpBbHQ+CiAgICAgICAgIDwveG1wOlRodW1ibmFpbHM+CiAgICAgICAgIDx4
bXBNTTpJbnN0YW5jZUlEPnhtcC5paWQ6YzEzNjVkMDYtYmVhNy0yMTRmLWIxYTUtZTA2MTNlZTA1
YmJlPC94bXBNTTpJbnN0YW5jZUlEPgogICAgICAgICA8eG1wTU06RG9jdW1lbnRJRD54bXAuZGlk
OmMxMzY1ZDA2LWJlYTctMjE0Zi1iMWE1LWUwNjEzZWUwNWJiZTwveG1wTU06RG9jdW1lbnRJRD4K
ICAgICAgICAgPHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD51dWlkOjVEMjA4OTI0OTNCRkRCMTE5
MTRBODU5MEQzMTUwOEM4PC94bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+CiAgICAgICAgIDx4bXBN
TTpSZW5kaXRpb25DbGFzcz5wcm9vZjpwZGY8L3htcE1NOlJlbmRpdGlvbkNsYXNzPgogICAgICAg
ICA8eG1wTU06RGVyaXZlZEZyb20gcmRmOnBhcnNlVHlwZT0iUmVzb3VyY2UiPgogICAgICAgICAg
ICA8c3RSZWY6aW5zdGFuY2VJRD54bXAuaWlkOmQ5NWY2NThiLWE1MzUtZTY0Yy04NjhiLTg0Yzgz
MDdmYzE1ODwvc3RSZWY6aW5zdGFuY2VJRD4KICAgICAgICAgICAgPHN0UmVmOmRvY3VtZW50SUQ+
eG1wLmRpZDpkOTVmNjU4Yi1hNTM1LWU2NGMtODY4Yi04NGM4MzA3ZmMxNTg8L3N0UmVmOmRvY3Vt
ZW50SUQ+CiAgICAgICAgICAgIDxzdFJlZjpvcmlnaW5hbERvY3VtZW50SUQ+dXVpZDo1RDIwODky
NDkzQkZEQjExOTE0QTg1OTBEMzE1MDhDODwvc3RSZWY6b3JpZ2luYWxEb2N1bWVudElEPgogICAg
ICAgICAgICA8c3RSZWY6cmVuZGl0aW9uQ2xhc3M+cHJvb2Y6cGRmPC9zdFJlZjpyZW5kaXRpb25D
bGFzcz4KICAgICAgICAgPC94bXBNTTpEZXJpdmVkRnJvbT4KICAgICAgICAgPHhtcE1NOkhpc3Rv
cnk+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJz
ZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwv
c3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlk
OjJmNWQzMjgxLTM1NDgtYzU0OC1iZWE1LTYyNDUzOTdlYzgxNjwvc3RFdnQ6aW5zdGFuY2VJRD4K
ICAgICAgICAgICAgICAgICAgPHN0RXZ0OndoZW4+MjAyMS0wOC0yNlQxNDoyMzo1Mi0wNTowMDwv
c3RFdnQ6d2hlbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUg
SWxsdXN0cmF0b3IgMjUuMiAoV2luZG93cyk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAg
ICAgICAgICAgIDxzdEV2dDpjaGFuZ2VkPi88L3N0RXZ0OmNoYW5nZWQ+CiAgICAgICAgICAgICAg
IDwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNl
Ij4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwvc3RFdnQ6YWN0aW9uPgog
ICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOjNiNzUwNjJhLTdjNzct
MGY0Mi05MGMzLTVjNGM5ZjUyYWJkYzwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAg
ICAgPHN0RXZ0OndoZW4+MjAyMS0wOS0wMVQxMToyMDozNS0wNTowMDwvc3RFdnQ6d2hlbj4KICAg
ICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgSWxsdXN0cmF0b3IgMjUu
MiAoV2luZG93cyk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAgICAgICAgICAgIDxzdEV2
dDpjaGFuZ2VkPi88L3N0RXZ0OmNoYW5nZWQ+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAg
ICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAg
ICAgICAgPHN0RXZ0OmFjdGlvbj5jb252ZXJ0ZWQ8L3N0RXZ0OmFjdGlvbj4KICAgICAgICAgICAg
ICAgICAgPHN0RXZ0OnBhcmFtZXRlcnM+ZnJvbSBhcHBsaWNhdGlvbi9wb3N0c2NyaXB0IHRvIGFw
cGxpY2F0aW9uL3ZuZC5hZG9iZS5pbGx1c3RyYXRvcjwvc3RFdnQ6cGFyYW1ldGVycz4KICAgICAg
ICAgICAgICAgPC9yZGY6bGk+CiAgICAgICAgICAgICAgIDxyZGY6bGkgcmRmOnBhcnNlVHlwZT0i
UmVzb3VyY2UiPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6YWN0aW9uPnNhdmVkPC9zdEV2dDph
Y3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6MzRlNjIw
YzQtZjVhMS0zMjQzLWE4NjMtNzQ0NDUxYjJlOTkwPC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAg
ICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDIxLTA5LTAzVDE5OjQwOjMwLTA1OjAwPC9zdEV2dDp3
aGVuPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6c29mdHdhcmVBZ2VudD5BZG9iZSBJbGx1c3Ry
YXRvciAyNS4yIChXaW5kb3dzKTwvc3RFdnQ6c29mdHdhcmVBZ2VudD4KICAgICAgICAgICAgICAg
ICAgPHN0RXZ0OmNoYW5nZWQ+Lzwvc3RFdnQ6Y2hhbmdlZD4KICAgICAgICAgICAgICAgPC9yZGY6
bGk+CiAgICAgICAgICAgICAgIDxyZGY6bGkgcmRmOnBhcnNlVHlwZT0iUmVzb3VyY2UiPgogICAg
ICAgICAgICAgICAgICA8c3RFdnQ6YWN0aW9uPnNhdmVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAg
ICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6YzEzNjVkMDYtYmVhNy0yMTRmLWIx
YTUtZTA2MTNlZTA1YmJlPC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAgICAgICAgICAgICA8c3RF
dnQ6d2hlbj4yMDIxLTA5LTAzVDE5OjUxOjQ2LTA1OjAwPC9zdEV2dDp3aGVuPgogICAgICAgICAg
ICAgICAgICA8c3RFdnQ6c29mdHdhcmVBZ2VudD5BZG9iZSBJbGx1c3RyYXRvciAyNS4yIChXaW5k
b3dzKTwvc3RFdnQ6c29mdHdhcmVBZ2VudD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmNoYW5n
ZWQ+Lzwvc3RFdnQ6Y2hhbmdlZD4KICAgICAgICAgICAgICAgPC9yZGY6bGk+CiAgICAgICAgICAg
IDwvcmRmOlNlcT4KICAgICAgICAgPC94bXBNTTpIaXN0b3J5PgogICAgICAgICA8aWxsdXN0cmF0
b3I6U3RhcnR1cFByb2ZpbGU+UHJpbnQ8L2lsbHVzdHJhdG9yOlN0YXJ0dXBQcm9maWxlPgogICAg
ICAgICA8aWxsdXN0cmF0b3I6Q3JlYXRvclN1YlRvb2w+QWRvYmUgSWxsdXN0cmF0b3I8L2lsbHVz
dHJhdG9yOkNyZWF0b3JTdWJUb29sPgogICAgICAgICA8cGRmOlByb2R1Y2VyPkFkb2JlIFBERiBs
aWJyYXJ5IDE1LjAwPC9wZGY6UHJvZHVjZXI+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8
L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
IAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAog
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAg
ICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz7/4gxYSUNDX1BST0ZJTEUAAQEA
AAxITGlubwIQAABtbnRyUkdCIFhZWiAHzgACAAkABgAxAABhY3NwTVNGVAAAAABJRUMgc1JHQgAA
AAAAAAAAAAAAAAAA9tYAAQAAAADTLUhQICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAABFjcHJ0AAABUAAAADNkZXNjAAABhAAAAGx3dHB0AAAB8AAAABRia3B0
AAACBAAAABRyWFlaAAACGAAAABRnWFlaAAACLAAAABRiWFlaAAACQAAAABRkbW5kAAACVAAAAHBk
bWRkAAACxAAAAIh2dWVkAAADTAAAAIZ2aWV3AAAD1AAAACRsdW1pAAAD+AAAABRtZWFzAAAEDAAA
ACR0ZWNoAAAEMAAAAAxyVFJDAAAEPAAACAxnVFJDAAAEPAAACAxiVFJDAAAEPAAACAx0ZXh0AAAA
AENvcHlyaWdodCAoYykgMTk5OCBIZXdsZXR0LVBhY2thcmQgQ29tcGFueQAAZGVzYwAAAAAAAAAS
c1JHQiBJRUM2MTk2Ni0yLjEAAAAAAAAAAAAAABJzUkdCIElFQzYxOTY2LTIuMQAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWFlaIAAAAAAAAPNRAAEAAAAB
FsxYWVogAAAAAAAAAAAAAAAAAAAAAFhZWiAAAAAAAABvogAAOPUAAAOQWFlaIAAAAAAAAGKZAAC3
hQAAGNpYWVogAAAAAAAAJKAAAA+EAAC2z2Rlc2MAAAAAAAAAFklFQyBodHRwOi8vd3d3LmllYy5j
aAAAAAAAAAAAAAAAFklFQyBodHRwOi8vd3d3LmllYy5jaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAABkZXNjAAAAAAAAAC5JRUMgNjE5NjYtMi4xIERlZmF1bHQg
UkdCIGNvbG91ciBzcGFjZSAtIHNSR0IAAAAAAAAAAAAAAC5JRUMgNjE5NjYtMi4xIERlZmF1bHQg
UkdCIGNvbG91ciBzcGFjZSAtIHNSR0IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZGVzYwAAAAAAAAAs
UmVmZXJlbmNlIFZpZXdpbmcgQ29uZGl0aW9uIGluIElFQzYxOTY2LTIuMQAAAAAAAAAAAAAALFJl
ZmVyZW5jZSBWaWV3aW5nIENvbmRpdGlvbiBpbiBJRUM2MTk2Ni0yLjEAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAHZpZXcAAAAAABOk/gAUXy4AEM8UAAPtzAAEEwsAA1yeAAAAAVhZWiAAAAAAAEwJ
VgBQAAAAVx/nbWVhcwAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAo8AAAACc2lnIAAAAABDUlQg
Y3VydgAAAAAAAAQAAAAABQAKAA8AFAAZAB4AIwAoAC0AMgA3ADsAQABFAEoATwBUAFkAXgBjAGgA
bQByAHcAfACBAIYAiwCQAJUAmgCfAKQAqQCuALIAtwC8AMEAxgDLANAA1QDbAOAA5QDrAPAA9gD7
AQEBBwENARMBGQEfASUBKwEyATgBPgFFAUwBUgFZAWABZwFuAXUBfAGDAYsBkgGaAaEBqQGxAbkB
wQHJAdEB2QHhAekB8gH6AgMCDAIUAh0CJgIvAjgCQQJLAlQCXQJnAnECegKEAo4CmAKiAqwCtgLB
AssC1QLgAusC9QMAAwsDFgMhAy0DOANDA08DWgNmA3IDfgOKA5YDogOuA7oDxwPTA+AD7AP5BAYE
EwQgBC0EOwRIBFUEYwRxBH4EjASaBKgEtgTEBNME4QTwBP4FDQUcBSsFOgVJBVgFZwV3BYYFlgWm
BbUFxQXVBeUF9gYGBhYGJwY3BkgGWQZqBnsGjAadBq8GwAbRBuMG9QcHBxkHKwc9B08HYQd0B4YH
mQesB78H0gflB/gICwgfCDIIRghaCG4IggiWCKoIvgjSCOcI+wkQCSUJOglPCWQJeQmPCaQJugnP
CeUJ+woRCicKPQpUCmoKgQqYCq4KxQrcCvMLCwsiCzkLUQtpC4ALmAuwC8gL4Qv5DBIMKgxDDFwM
dQyODKcMwAzZDPMNDQ0mDUANWg10DY4NqQ3DDd4N+A4TDi4OSQ5kDn8Omw62DtIO7g8JDyUPQQ9e
D3oPlg+zD88P7BAJECYQQxBhEH4QmxC5ENcQ9RETETERTxFtEYwRqhHJEegSBxImEkUSZBKEEqMS
wxLjEwMTIxNDE2MTgxOkE8UT5RQGFCcUSRRqFIsUrRTOFPAVEhU0FVYVeBWbFb0V4BYDFiYWSRZs
Fo8WshbWFvoXHRdBF2UXiReuF9IX9xgbGEAYZRiKGK8Y1Rj6GSAZRRlrGZEZtxndGgQaKhpRGnca
nhrFGuwbFBs7G2MbihuyG9ocAhwqHFIcexyjHMwc9R0eHUcdcB2ZHcMd7B4WHkAeah6UHr4e6R8T
Hz4faR+UH78f6iAVIEEgbCCYIMQg8CEcIUghdSGhIc4h+yInIlUigiKvIt0jCiM4I2YjlCPCI/Ak
HyRNJHwkqyTaJQklOCVoJZclxyX3JicmVyaHJrcm6CcYJ0kneierJ9woDSg/KHEooijUKQYpOClr
KZ0p0CoCKjUqaCqbKs8rAis2K2krnSvRLAUsOSxuLKIs1y0MLUEtdi2rLeEuFi5MLoIuty7uLyQv
Wi+RL8cv/jA1MGwwpDDbMRIxSjGCMbox8jIqMmMymzLUMw0zRjN/M7gz8TQrNGU0njTYNRM1TTWH
NcI1/TY3NnI2rjbpNyQ3YDecN9c4FDhQOIw4yDkFOUI5fzm8Ofk6Njp0OrI67zstO2s7qjvoPCc8
ZTykPOM9Ij1hPaE94D4gPmA+oD7gPyE/YT+iP+JAI0BkQKZA50EpQWpBrEHuQjBCckK1QvdDOkN9
Q8BEA0RHRIpEzkUSRVVFmkXeRiJGZ0arRvBHNUd7R8BIBUhLSJFI10kdSWNJqUnwSjdKfUrESwxL
U0uaS+JMKkxyTLpNAk1KTZNN3E4lTm5Ot08AT0lPk0/dUCdQcVC7UQZRUFGbUeZSMVJ8UsdTE1Nf
U6pT9lRCVI9U21UoVXVVwlYPVlxWqVb3V0RXklfgWC9YfVjLWRpZaVm4WgdaVlqmWvVbRVuVW+Vc
NVyGXNZdJ114XcleGl5sXr1fD19hX7NgBWBXYKpg/GFPYaJh9WJJYpxi8GNDY5dj62RAZJRk6WU9
ZZJl52Y9ZpJm6Gc9Z5Nn6Wg/aJZo7GlDaZpp8WpIap9q92tPa6dr/2xXbK9tCG1gbbluEm5rbsRv
Hm94b9FwK3CGcOBxOnGVcfByS3KmcwFzXXO4dBR0cHTMdSh1hXXhdj52m3b4d1Z3s3gReG54zHkq
eYl553pGeqV7BHtje8J8IXyBfOF9QX2hfgF+Yn7CfyN/hH/lgEeAqIEKgWuBzYIwgpKC9INXg7qE
HYSAhOOFR4Wrhg6GcobXhzuHn4gEiGmIzokziZmJ/opkisqLMIuWi/yMY4zKjTGNmI3/jmaOzo82
j56QBpBukNaRP5GokhGSepLjk02TtpQglIqU9JVflcmWNJaflwqXdZfgmEyYuJkkmZCZ/JpomtWb
QpuvnByciZz3nWSd0p5Anq6fHZ+Ln/qgaaDYoUehtqImopajBqN2o+akVqTHpTilqaYapoum/adu
p+CoUqjEqTepqaocqo+rAqt1q+msXKzQrUStuK4trqGvFq+LsACwdbDqsWCx1rJLssKzOLOutCW0
nLUTtYq2AbZ5tvC3aLfguFm40blKucK6O7q1uy67p7whvJu9Fb2Pvgq+hL7/v3q/9cBwwOzBZ8Hj
wl/C28NYw9TEUcTOxUvFyMZGxsPHQce/yD3IvMk6ybnKOMq3yzbLtsw1zLXNNc21zjbOts83z7jQ
OdC60TzRvtI/0sHTRNPG1EnUy9VO1dHWVdbY11zX4Nhk2OjZbNnx2nba+9uA3AXcit0Q3ZbeHN6i
3ynfr+A24L3hROHM4lPi2+Nj4+vkc+T85YTmDeaW5x/nqegy6LzpRunQ6lvq5etw6/vshu0R7Zzu
KO6070DvzPBY8OXxcvH/8ozzGfOn9DT0wvVQ9d72bfb794r4Gfio+Tj5x/pX+uf7d/wH/Jj9Kf26
/kv+3P9t////7gAOQWRvYmUAZMAAAAAB/9sAhAABAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEB
AQEBAQEBAQEBAQEBAQEBAgICAgICAgICAgIDAwMDAwMDAwMDAQEBAQEBAQIBAQICAgECAgMDAwMD
AwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwP/wAARCAGAAuwDAREA
AhEBAxEB/8QA6gABAAIDAQADAQAAAAAAAAAAAAkKBgcIBQEDBAIBAQABBAMBAQAAAAAAAAAAAAAG
BQcICQMECgIBEAAABgEDAQMIBAwEAwUFCQAAAQIDBAUGEQcIEiETCSIU1FWVllcZMRXWGEEyI7R1
tRZ2tjd3OFEzNhdCUiRhcdO3eIFicpIlQzRUZdVWh8dIEQABAwICBAUKEAsFCAAFBQEAAQIDBAUR
BiExEgdBUWETCHGBkdEikhQVFhihsTJCcrLSI1OTVJTUNXVWwVJiM3OzNHS0NwnwoiQ2duGCwkPT
VTgZ8URktReDhCWFxUb/2gAMAwEAAhEDEQA/AL/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAOBd/wDxEdkdk507GqY5W6WbQVLZlU+KzIjNFWTG19DsK7yxwpUSLKaNKkra
iMT3mXE9DqGz+igXDMVDROWJmMs6cDV0IvEru0i4cOBiTvc6Y+6/djVS2S285fs0RKrXQ0r2JBE9
FwVk9Wu2xrk0o5sTJ3scmzI1ikbOVeK1yEt5Tn7M49t1iNf1mcdpNRaX1klvXUkSp9lbphSFERad
TcNj/u+jSNy5ruD196bGxvUVV7Krh6CGFN+6fm+C4Tu8R0dmt1Hj3Kc1LPJhxOkkm2HdVsLOoYh8
z3lV63wr3NhekDh8p7rxs70jvnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90P
me8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme
8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8q
vW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW
+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+F
e5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5
sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL
0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0g
PKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPK
e68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe6
8bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68b
O9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9
Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hn
z7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7
+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/
lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lF
r+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+
Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs
90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90
Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pm
e8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8
qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qv
W+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+
Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe
5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5sL0gPKe68bO9Hnz7+/lFr+Zs90Pme8qvW+Fe5s
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
a90tbDZ98VPHVWx7katwpo0jmix0bc1NGnNzMRdLuYbE9rcVbHM7BizdY/kFJlVJV5JjdpCu6G7h
R7Kptq2QiVBnwZSCcYkR32zNK0LSf/eR6kZEZGQm8cjJWJJGqOjcmKKmpUNoVou9sv8AbIL1ZZ4q
q01UTZIpY3I5kjHJi1zXJoVFTsalwVDUXIvYfFuRG2F3gGRNMMTnGnJ2KZApgnZWMZMwy4VdaxzL
RxUc1q7qW0lSfOIrjiNUmaVJ6dxoIrjSup5PVa2r+K7gXt8aFu98u6ew748jVWUby1rKpzVfS1Gz
i6mqWovNyt4dnFdiViKnOROezFFVHJU6y7Fb3BsoyDDcmgrrcgxi3n0dxBcMlebz62S5FkJQ4nVD
7Clt9TbiDNDrZktJmkyM7UTRSQSuhlTCRqqipyoefvMNguuVb7WZbvkSwXihqZIJmLp2ZI3K12Cp
oc3FMWuTFrmqjmqqKimPDiKOAAAFvDjV/bnsD/RTav8AgWhF3rb9XU/6BntUPRHuT/kzlH/TFr/g
YDdY7pc4jg508JYu/VW7uNt1Fh1+79JCNMiKRMRI24VbFbSTNZYSFd22zkMJlvogS3DJC0aR31E3
3TkeN32yJXs8JpkRKxqd+nEvKnAvWXRgqYX9KnowQb2aB2c8mxxw7xaWLum9yxtwjamiKR2hEqGI
mEErlwVMIZVRnNvhrmTYUutmS66wiyIU+BJfhTYUppbEqJLiurYkxZLDqUuMyI7yFIWhREpKiMjL
UW6c1WqrXJg5FwVDTJU01RRVMlHWRviq4nuY9j0VrmPaqtc1zVwVrmuRUVFTFFRUU/MPk4SSfwrP
7m5/9Lsq/W+LiTZV+s1/RO9Npmv0CP54zfYVV+upSxoLim5orY+J9/dTa/uThv5pJFtsz/Wq+waa
UenP/Puo+y6P2jiPIR0w8AAAAAAAnz8K3YpWL4Ff743kUkW+4a10OJk62knouHU01abCa2o0k62W
QZBGMjQfYpqvZcSZk4J9lWh5qB1c9O7k0N9ii6V66+knGba+gTuqWxZSq96V0jwuN4VYKTFNLaOF
6849F1p4RUNwVF0KynjeiqjyWgS02DGE7kYFQ7o4Hlm3uTM9/R5dSTaabolKnY/nLZ+bT4vXqlM2
slpbkMK/4Hmkq/AOCpgjqoH08v5t7VRe31U1pykYzplK057yncMn3xu1a7jSvhfqxbtJ3MjcdCPi
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
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP/Z

" id="image1813" x="2.5709589" y="0.5405001"></image>

<g id="g1801" transform="matrix(0.6931155,0,0,0.6931155,6.5394535,4.8796057)"><text xml:space="preserve" style="font-style:normal;font-variant:normal;font-weight:400;font-size:4.12501px;line-height:125%;font-family:'Trebuchet MS';text-align:start;letter-spacing:0;word-spacing:0;text-anchor:start;display:inline;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.120884" x="0.31308791" y="15.804644" transform="scale(0.90901656,1.10009)" id="text3687"><tspan x="0.31308791" y="15.804644" style="font-size:4.12501px;stroke-width:0.120884" id="tspan3685"><tspan dx="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0" dy="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0" style="font-style:normal;font-variant:normal;font-weight:400;font-size:4.12501px;font-family:'Trebuchet MS';fill:#4f5252;stroke-width:0.120884" id="tspan3683">ISO/IEC 17020:2012 </tspan></tspan></text><text xml:space="preserve" style="font-style:normal;font-variant:normal;font-weight:400;font-size:4.12501px;line-height:125%;font-family:'Trebuchet MS';text-align:start;letter-spacing:0;word-spacing:0;text-anchor:start;display:inline;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.120884" x="7.3109226" y="19.979807" transform="scale(0.90901656,1.10009)" id="text3695"><tspan x="7.3109226" y="19.979807" style="font-size:4.12501px;stroke-width:0.120884" id="tspan3693"><tspan dx="0 0 0 0 0 0 0 0 0 0" dy="0 0 0 0 0 0 0 0 0 0" style="font-style:normal;font-variant:normal;font-weight:400;font-size:4.12501px;font-family:'Trebuchet MS';fill:#4f5252;stroke-width:0.120884" id="tspan3689">22-OIN-040</tspan><tspan dx="0" dy="0" style="font-style:normal;font-variant:normal;font-weight:400;font-size:4.12501px;font-family:'Trebuchet MS';fill:#000000;stroke-width:0.120884" id="tspan3691"> </tspan></tspan></text></g>
       
       <metadata
     id="metadata1049"><rdf:RDF><cc:Work
         rdf:about=""><dc:creator><cc:Agent><dc:title>Julian Quintero</dc:title></cc:Agent></dc:creator><dc:rights><cc:Agent><dc:title>Julian Quintero</dc:title></cc:Agent></dc:rights><dc:publisher><cc:Agent><dc:title>Julian Quintero</dc:title></cc:Agent></dc:publisher><dc:language>español</dc:language><dc:subject><rdf:Bag><rdf:li>reporte</rdf:li></rdf:Bag></dc:subject><cc:license
           rdf:resource="http://scripts.sil.org/OFL" /></cc:Work><cc:License
         rdf:about="http://scripts.sil.org/OFL"><cc:permits
           rdf:resource="http://scripts.sil.org/pub/OFL/Reproduction" /><cc:permits
           rdf:resource="http://scripts.sil.org/pub/OFL/Distribution" /><cc:permits
           rdf:resource="http://scripts.sil.org/pub/OFL/Embedding" /><cc:permits
           rdf:resource="http://scripts.sil.org/pub/OFL/DerivativeWorks" /><cc:requires
           rdf:resource="http://scripts.sil.org/pub/OFL/Notice" /><cc:requires
           rdf:resource="http://scripts.sil.org/pub/OFL/Attribution" /><cc:requires
           rdf:resource="http://scripts.sil.org/pub/OFL/ShareAlike" /><cc:requires
           rdf:resource="http://scripts.sil.org/pub/OFL/DerivativeRenaming" /><cc:requires
           rdf:resource="http://scripts.sil.org/pub/OFL/BundlingWhenSelling" /></cc:License></rdf:RDF></metadata></svg>
    """

    return svg_code