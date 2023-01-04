from reportlab.pdfgen import canvas
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def extract():
    url = 'https://api.sportsdata.io/v3/nba/projections/json/PlayerSeasonProjectionStatsByTeam/2022/MIA'
    with open('config.txt') as f:
        api_key = f.read().strip()

    miami = requests.get(url + api_key)
    miami = miami.json()
    miami = pd.DataFrame(miami)

    return miami

def transform(miami):
    miami = miami.sort_values('FieldGoalsPercentage',ascending=False)
    plt.figure(figsize=(10, 4.5))
    ax = sns.barplot(x=miami['Name'], y=miami['FieldGoalsPercentage'], orient='v')
    plt.xticks(rotation=90)
    plt.xlabel('Jugadores')
    plt.ylabel('Porcentaje de Goles')
    plt.savefig('%_goles.jpeg',bbox_inches='tight')

    miami = miami.sort_values('TwoPointersPercentage',ascending=False)
    plt.figure(figsize=(10, 4.5))
    ax = sns.barplot(x=miami['Name'], y=miami['TwoPointersPercentage'], orient='v')
    plt.xticks(rotation=90)
    plt.xlabel('Jugadores')
    plt.ylabel('Porcentaje de Dobles')
    plt.savefig('%_dobles.jpeg',bbox_inches='tight')

    miami = miami.sort_values('ThreePointersPercentage',ascending=False)
    plt.figure(figsize=(10, 4.5))
    ax = sns.barplot(x=miami['Name'], y=miami['ThreePointersPercentage'], orient='v')
    plt.xticks(rotation=90)
    plt.xlabel('Jugadores')
    plt.ylabel('Porcentaje de Triples')
    plt.savefig('%_triples.jpeg',bbox_inches='tight')

    miami = miami.sort_values('Points',ascending=False)
    plt.figure(figsize=(10, 4.5))
    ax = sns.barplot(x=miami['Name'], y=miami['Points'], orient='v')
    plt.xticks(rotation=90)
    plt.xlabel('Jugadores')
    plt.ylabel('Puntos')
    plt.savefig('puntos.jpeg',bbox_inches='tight')

    miami = miami.sort_values('Assists',ascending=False)
    plt.figure(figsize=(10, 4.5))
    ax = sns.barplot(x=miami['Name'], y=miami['Assists'], orient='v')
    plt.xticks(rotation=90)
    plt.xlabel('Jugadores')
    plt.ylabel('Asistencias')
    plt.savefig('asistencias.jpeg',bbox_inches='tight')

    miami = miami.sort_values('PersonalFouls',ascending=False)
    plt.figure(figsize=(10, 4.5))
    ax = sns.barplot(x=miami['Name'], y=miami['PersonalFouls'], orient='v')
    plt.xticks(rotation=90)
    plt.xlabel('Jugadores')
    plt.ylabel('Faltas')
    plt.savefig('faltas.jpeg',bbox_inches='tight')

    stats = ['Position','Games','Minutes','Points','Rebounds','Assists','Steals','BlockedShots','Turnovers','PersonalFouls','FieldGoalsPercentage','FreeThrowsPercentage','TwoPointersPercentage','ThreePointersPercentage']
    nombres = list(miami['Name'])
    lista = []

    for nombre in nombres:
        dic = {}
        for i in stats:
            dic[i] = miami[miami['Name'] == nombre][i].values[0]
        lista.append(dic)

    return lista


def load(lista):
    c = canvas.Canvas('reporte_nba.pdf')

    c.setFont('Times-BoldItalic',40)
    c.drawString(100, 720, "REPORTE EJECUTIVO")
    c.drawString(70, 660, "DE EQUIPO MIAMI HEAT")

    c.drawImage('NBA-Logo.jpeg',-100,200,width=800,height=400)

    c.setFont('Courier',12)
    c.drawString(50,50, 'Jimena Monteagudo Ruiz')
    c.drawString(510,50, '01/01/23')

    c.showPage()

    c.setFont('Helvetica-Bold',15)
    c.setFillColorRGB(0, 0, 1)
    c.drawString(210,750,'INTRODUCCIÓN INFORME')
    c.setFillColorRGB(0, 0, 0)

    intro = c.beginText(50,700)
    intro.setFont('Times-Roman',12)
    intro.textLines('Con este reporte ejecutivo se pretende dar a conocer algunas estadísticas sobre el equipo de baloncesto\nde Miami Heat. Primero se mostrarán las estadísticas de cada jugador individualmente.\nLuego, se analizará el porcentaje de goles por jugador, el de tiros dobles y triples metidos.\nAdemás, se analizará el número de puntos, asistencias y faltas cometidas por cada jugador.')
    c.drawText(intro)
    c.setFont('Helvetica-Bold',15)
    c.setFillColorRGB(0, 0, 1)
    c.drawString(550,30, '1')

    c.setFont('Helvetica',12)
    c.drawString(50,600, 'DUNCAN ROBINSON')
    c.drawImage('duncan.jpeg',55,520,width=100,height=80)

    c.setFont('Helvetica',12)
    c.drawString(250,600, 'MAX STRUS')
    c.drawImage('max.jpeg',240,520,width=90,height=70)

    c.setFont('Helvetica',12)
    c.drawString(400,600, 'DEWAYNE DEDMON')
    c.drawImage('dewayne.jpeg',410,520,width=100,height=80)

    c.setFont('Helvetica',12)
    c.drawString(50,500, 'MYCHAL MULDER')
    c.drawImage('mychal.jpeg',60,420,width=80,height=70)

    c.setFont('Helvetica',12)
    c.drawString(240,500, 'BAM ADEBAYO')
    c.drawImage('bam.jpeg',240,420,width=100,height=80)

    c.setFont('Helvetica',12)
    c.drawString(400,500, 'ÖMER YURTSEVEN')
    c.drawImage('omer.jpeg',410,420,width=100,height=80)

    c.setFont('Helvetica',12)
    c.drawString(50,400, 'MARKIEFF MORRIS')
    c.drawImage('markieff.jpeg',60,320,width=80,height=70)

    c.setFont('Helvetica',12)
    c.drawString(240,400, 'JIMMY BUTLER')
    c.drawImage('jimmy.jpeg',245,320,width=80,height=70)

    c.setFont('Helvetica',12)
    c.drawString(410,400, 'GABE VINCENT')
    c.drawImage('gabe.jpeg',415,320,width=80,height=70)

    c.setFont('Helvetica',12)
    c.drawString(50,300, 'KYLE LOWRY')
    c.drawImage('kyle.jpeg',60,220,width=80,height=70)

    c.setFont('Helvetica',12)
    c.drawString(230,300, 'UDONIS HASLEM')
    c.drawImage('udonis.jpeg',240,220,width=80,height=70)

    c.setFont('Helvetica',12)
    c.drawString(410,300, 'TYLER HERRO')
    c.drawImage('tyler.jpeg',405,220,width=100,height=80)

    c.setFont('Helvetica',12)
    c.drawString(50,200, 'VICTOR OLADIPO')
    c.drawImage('victor.jpeg',55,120,width=80,height=70)

    c.setFont('Helvetica',12)
    c.drawString(240,200, 'P.J. TUCKER')
    c.drawImage('pj.jpeg',240,120,width=80,height=70)

    c.setFont('Helvetica',12)
    c.drawString(410,200, 'CALEB MARTIN')
    c.drawImage('caleb.jpeg',410,120,width=80,height=70)

    c.showPage()

    c.drawString(50,780, 'DUNCAN ROBINSON')
    duncan = c.beginText(50,760)
    duncan.setFont('Times-Roman',12)
    duncan.textLines('- Position: '+str(lista[8]['Position'])+'\n- Games: '+str(lista[8]['Games'])+'\n- Minutes: '+str(lista[8]['Minutes'])+'\n- Points: '+str(lista[8]['Points'])+'\n- Rebounds: ' +str(lista[8]['Rebounds'])+'\n- Assists: '+ str(lista[8]['Assists'])+'\n- Steals: ' +str(lista[8]['Steals'])+'\n- Blocked Shots: ' +str(lista[8]['BlockedShots'])+'\n- Turnovers: ' +str(lista[8]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[8]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[8]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[8]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[8]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[8]['ThreePointersPercentage']))
    c.drawText(duncan)

    c.drawString(250,780, 'MAX STRUS')
    max = c.beginText(250,760)
    max.setFont('Times-Roman',12)
    max.textLines('- Position: '+str(lista[11]['Position'])+'\n- Games: '+str(lista[11]['Games'])+'\n- Minutes: '+str(lista[11]['Minutes'])+'\n- Points: '+str(lista[11]['Points'])+'\n- Rebounds: ' +str(lista[11]['Rebounds'])+'\n- Assists: '+ str(lista[11]['Assists'])+'\n- Steals: ' +str(lista[11]['Steals'])+'\n- Blocked Shots: ' +str(lista[11]['BlockedShots'])+'\n- Turnovers: ' +str(lista[11]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[11]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[11]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[11]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[11]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[11]['ThreePointersPercentage']))
    c.drawText(max)

    c.drawString(430,780, 'DEWAYNE DEDMON')
    dedmon = c.beginText(430,760)
    dedmon.setFont('Times-Roman',12)
    dedmon.textLines('- Position: '+str(lista[2]['Position'])+'\n- Games: '+str(lista[2]['Games'])+'\n- Minutes: '+str(lista[2]['Minutes'])+'\n- Points: '+str(lista[2]['Points'])+'\n- Rebounds: ' +str(lista[2]['Rebounds'])+'\n- Assists: '+ str(lista[2]['Assists'])+'\n- Steals: ' +str(lista[2]['Steals'])+'\n- Blocked Shots: ' +str(lista[2]['BlockedShots'])+'\n- Turnovers: ' +str(lista[2]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[2]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[2]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[2]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[2]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[2]['ThreePointersPercentage']))
    c.drawText(dedmon)

    c.drawString(50,520, 'MYCHAL MULDER')
    mychal = c.beginText(50,500)
    mychal.setFont('Times-Roman',12)
    mychal.textLines('- Position: '+str(lista[13]['Position'])+'\n- Games: '+str(lista[13]['Games'])+'\n- Minutes: '+str(lista[13]['Minutes'])+'\n- Points: '+str(lista[13]['Points'])+'\n- Rebounds: ' +str(lista[13]['Rebounds'])+'\n- Assists: '+ str(lista[13]['Assists'])+'\n- Steals: ' +str(lista[13]['Steals'])+'\n- Blocked Shots: ' +str(lista[13]['BlockedShots'])+'\n- Turnovers: ' +str(lista[13]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[13]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[13]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[13]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[13]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[13]['ThreePointersPercentage']))
    c.drawText(mychal)

    c.drawString(250,520, 'BAM ADEBAYO')
    bam = c.beginText(250,500)
    bam.setFont('Times-Roman',12)
    bam.textLines('- Position: '+str(lista[7]['Position'])+'\n- Games: '+str(lista[7]['Games'])+'\n- Minutes: '+str(lista[7]['Minutes'])+'\n- Points: '+str(lista[7]['Points'])+'\n- Rebounds: ' +str(lista[7]['Rebounds'])+'\n- Assists: '+ str(lista[7]['Assists'])+'\n- Steals: ' +str(lista[7]['Steals'])+'\n- Blocked Shots: ' +str(lista[7]['BlockedShots'])+'\n- Turnovers: ' +str(lista[7]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[7]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[7]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[7]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[7]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[7]['ThreePointersPercentage']))
    c.drawText(bam)

    c.drawString(430,520, 'ÖMER YURTSEVEN')
    omer = c.beginText(430,500)
    omer.setFont('Times-Roman',12)
    omer.textLines('- Position: '+str(lista[14]['Position'])+'\n- Games: '+str(lista[14]['Games'])+'\n- Minutes: '+str(lista[14]['Minutes'])+'\n- Points: '+str(lista[14]['Points'])+'\n- Rebounds: ' +str(lista[14]['Rebounds'])+'\n- Assists: '+ str(lista[14]['Assists'])+'\n- Steals: ' +str(lista[14]['Steals'])+'\n- Blocked Shots: ' +str(lista[14]['BlockedShots'])+'\n- Turnovers: ' +str(lista[14]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[14]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[14]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[14]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[14]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[14]['ThreePointersPercentage']))
    c.drawText(omer)

    c.drawString(50,260, 'MARKIEFF MORRIS')
    markieff = c.beginText(50,240)
    markieff.setFont('Times-Roman',12)
    markieff.textLines('- Position: '+str(lista[5]['Position'])+'\n- Games: '+str(lista[5]['Games'])+'\n- Minutes: '+str(lista[5]['Minutes'])+'\n- Points: '+str(lista[5]['Points'])+'\n- Rebounds: ' +str(lista[5]['Rebounds'])+'\n- Assists: '+ str(lista[5]['Assists'])+'\n- Steals: ' +str(lista[5]['Steals'])+'\n- Blocked Shots: ' +str(lista[5]['BlockedShots'])+'\n- Turnovers: ' +str(lista[5]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[5]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[5]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[5]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[5]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[5]['ThreePointersPercentage']))
    c.drawText(markieff)

    c.drawString(250,260, 'JIMMY BUTLER')
    jimmy = c.beginText(250,240)
    jimmy.setFont('Times-Roman',12)
    jimmy.textLines('- Position: '+str(lista[1]['Position'])+'\n- Games: '+str(lista[1]['Games'])+'\n- Minutes: '+str(lista[1]['Minutes'])+'\n- Points: '+str(lista[1]['Points'])+'\n- Rebounds: ' +str(lista[1]['Rebounds'])+'\n- Assists: '+ str(lista[1]['Assists'])+'\n- Steals: ' +str(lista[1]['Steals'])+'\n- Blocked Shots: ' +str(lista[1]['BlockedShots'])+'\n- Turnovers: ' +str(lista[1]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[1]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[1]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[1]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[1]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[1]['ThreePointersPercentage']))
    c.drawText(jimmy)

    c.drawString(430,260, 'GABE VINCENT')
    gabe = c.beginText(430,240)
    gabe.setFont('Times-Roman',12)
    gabe.textLines('- Position: '+str(lista[9]['Position'])+'\n- Games: '+str(lista[9]['Games'])+'\n- Minutes: '+str(lista[9]['Minutes'])+'\n- Points: '+str(lista[9]['Points'])+'\n- Rebounds: ' +str(lista[9]['Rebounds'])+'\n- Assists: '+ str(lista[9]['Assists'])+'\n- Steals: ' +str(lista[9]['Steals'])+'\n- Blocked Shots: ' +str(lista[9]['BlockedShots'])+'\n- Turnovers: ' +str(lista[9]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[9]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[9]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[9]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[9]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[9]['ThreePointersPercentage']))
    c.drawText(gabe)

    c.setFont('Helvetica-Bold',15)
    c.setFillColorRGB(0, 0, 1)
    c.drawString(550,30, '2')

    c.showPage()

    c.drawString(50,750, 'KYLE LOWRY')
    kyle = c.beginText(50,730)
    kyle.setFont('Times-Roman',12)
    kyle.textLines('- Position: '+str(lista[0]['Position'])+'\n- Games: '+str(lista[0]['Games'])+'\n- Minutes: '+str(lista[0]['Minutes'])+'\n- Points: '+str(lista[0]['Points'])+'\n- Rebounds: ' +str(lista[0]['Rebounds'])+'\n- Assists: '+ str(lista[0]['Assists'])+'\n- Steals: ' +str(lista[0]['Steals'])+'\n- Blocked Shots: ' +str(lista[0]['BlockedShots'])+'\n- Turnovers: ' +str(lista[0]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[0]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[0]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[0]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[0]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[0]['ThreePointersPercentage']))
    c.drawText(kyle)

    c.drawString(250,750, 'UDONIS HASLEM')
    udonis = c.beginText(250,730)
    udonis.setFont('Times-Roman',12)
    udonis.textLines('- Position: '+str(lista[4]['Position'])+'\n- Games: '+str(lista[4]['Games'])+'\n- Minutes: '+str(lista[4]['Minutes'])+'\n- Points: '+str(lista[4]['Points'])+'\n- Rebounds: ' +str(lista[4]['Rebounds'])+'\n- Assists: '+ str(lista[4]['Assists'])+'\n- Steals: ' +str(lista[4]['Steals'])+'\n- Blocked Shots: ' +str(lista[4]['BlockedShots'])+'\n- Turnovers: ' +str(lista[4]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[4]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[4]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[4]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[4]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[4]['ThreePointersPercentage']))
    c.drawText(udonis)

    c.drawString(450,750, 'TYLER HERRO')
    tyler = c.beginText(450,730)
    tyler.setFont('Times-Roman',12)
    tyler.textLines('- Position: '+str(lista[10]['Position'])+'\n- Games: '+str(lista[10]['Games'])+'\n- Minutes: '+str(lista[10]['Minutes'])+'\n- Points: '+str(lista[10]['Points'])+'\n- Rebounds: ' +str(lista[10]['Rebounds'])+'\n- Assists: '+ str(lista[10]['Assists'])+'\n- Steals: ' +str(lista[10]['Steals'])+'\n- Blocked Shots: ' +str(lista[10]['BlockedShots'])+'\n- Turnovers: ' +str(lista[10]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[10]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[10]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[10]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[10]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[10]['ThreePointersPercentage']))
    c.drawText(tyler)

    c.drawString(50,450, 'VICTOR OLADIPO')
    victor = c.beginText(50,430)
    victor.setFont('Times-Roman',12)
    victor.textLines('- Position: '+str(lista[3]['Position'])+'\n- Games: '+str(lista[3]['Games'])+'\n- Minutes: '+str(lista[3]['Minutes'])+'\n- Points: '+str(lista[3]['Points'])+'\n- Rebounds: ' +str(lista[3]['Rebounds'])+'\n- Assists: '+ str(lista[3]['Assists'])+'\n- Steals: ' +str(lista[3]['Steals'])+'\n- Blocked Shots: ' +str(lista[3]['BlockedShots'])+'\n- Turnovers: ' +str(lista[3]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[3]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[3]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[3]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[3]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[3]['ThreePointersPercentage']))
    c.drawText(victor)

    c.drawString(250,450, 'P.J. TUCKER')
    pj = c.beginText(250,430)
    pj.setFont('Times-Roman',12)
    pj.textLines('- Position: '+str(lista[6]['Position'])+'\n- Games: '+str(lista[6]['Games'])+'\n- Minutes: '+str(lista[6]['Minutes'])+'\n- Points: '+str(lista[6]['Points'])+'\n- Rebounds: ' +str(lista[6]['Rebounds'])+'\n- Assists: '+ str(lista[6]['Assists'])+'\n- Steals: ' +str(lista[6]['Steals'])+'\n- Blocked Shots: ' +str(lista[6]['BlockedShots'])+'\n- Turnovers: ' +str(lista[6]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[6]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[6]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[6]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[6]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[6]['ThreePointersPercentage']))
    c.drawText(pj)

    c.drawString(450,450, 'CALEB MARTIN')
    caleb = c.beginText(450,430)
    caleb.setFont('Times-Roman',12)
    caleb.textLines('- Position: '+str(lista[12]['Position'])+'\n- Games: '+str(lista[12]['Games'])+'\n- Minutes: '+str(lista[12]['Minutes'])+'\n- Points: '+str(lista[12]['Points'])+'\n- Rebounds: ' +str(lista[12]['Rebounds'])+'\n- Assists: '+ str(lista[12]['Assists'])+'\n- Steals: ' +str(lista[12]['Steals'])+'\n- Blocked Shots: ' +str(lista[12]['BlockedShots'])+'\n- Turnovers: ' +str(lista[12]['Turnovers'])+'\n- Personal Fouls: '+ str(lista[12]['PersonalFouls'])+'\n- Field Goals %: '+ str(lista[12]['FieldGoalsPercentage'])+'\n- Free Throws %: '+ str(lista[12]['FreeThrowsPercentage'])+'\n- 2 Points %: '+ str(lista[12]['TwoPointersPercentage'])+'\n- 3 Points %: '+ str(lista[12]['ThreePointersPercentage']))
    c.drawText(caleb)

    c.setFont('Helvetica-Bold',15)
    c.setFillColorRGB(0, 0, 1)
    c.drawString(550,30, '3')

    c.showPage()

    c.setFont('Helvetica-Bold',15)
    c.drawString
    c.setFont('Helvetica-Bold',15)
    c.setFillColorRGB(0, 0, 1)
    c.drawString(150,750, 'PORCENTAJE DE TIROS DOBLES METIDOS')

    c.drawImage('%_dobles.jpeg',85,450,width=400,height=250)

    c.setFont('Helvetica-Bold',15)
    c.setFillColorRGB(0, 0, 1)
    c.drawString(150,380, 'PORCENTAJE DE TIROS TRIPLES METIDOS')

    c.drawImage('%_triples.jpeg',85,80,width=400,height=250)
    c.drawString(550,30, '4')

    c.showPage()

    c.setFont('Helvetica-Bold',15)
    c.setFillColorRGB(0, 0, 1)
    c.drawString(150,750, 'PORCENTAJE DE GOLES POR JUGADOR')

    c.drawImage('%_goles.jpeg',85,450,width=400,height=250)

    c.setFont('Helvetica-Bold',15)
    c.setFillColorRGB(0, 0, 1)
    c.drawString(210,380, 'PUNTOS POR JUGADOR')

    c.drawImage('puntos.jpeg',85,80,width=400,height=250)
    c.drawString(550,30, '5')

    c.showPage()

    c.setFont('Helvetica-Bold',15)
    c.setFillColorRGB(0, 0, 1)
    c.drawString(200,750, 'ASISTENCIAS POR JUGADOR')

    c.drawImage('asistencias.jpeg',85,450,width=400,height=250)

    c.setFont('Helvetica-Bold',15)
    c.setFillColorRGB(0, 0, 1)
    c.drawString(210,380, 'FALTAS POR JUGADOR')

    c.drawImage('faltas.jpeg',85,80,width=400,height=250)
    c.drawString(550,30, '6')

    c.showPage()

    c.save()

if __name__ == '__main__':
    miami = extract()
    lista = transform(miami)
    load(lista)