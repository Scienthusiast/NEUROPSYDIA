# -*- coding: cp1252 -*-
import os,sys
sys.path.append('.\\Files\\Docs')
import neuropsydia as n
from neuropsydia import *

origin=os.getcwd()


#INFOS
version = 'v0.9'
authors = 'D. Makowski, L. Dutriaux et al. (2016)'
autorisations = n.autorisations






def launcher((column,row),test=['BPDQ','Switch','SimAct','Wordini','RIDE','IPIP6','Switch'],scale = W/7):

    #Tried to put some music during the intro... LOL
##    pygame.mixer.init()
##    pygame.mixer.music.load("sound.wav")
##    sound = pygame.mixer.Sound("sound.wav")
##    sound.play(loops=1, maxtime=3000, fade_ms=1000)

    pos_images=[]
    number=0
    screen.fill((255, 255, 255))
    for j in range(row):
        for i in range(column):
            if (number+1)>len(test):
                pass
            else:
                limage=pygame.image.load('./Files/Docs/Logo_'+test[number]+'.png')
                large=limage.get_width()
                haute=limage.get_height()
                limage=pygame.transform.smoothscale(limage,(large*scale/H,haute*scale/H))
                rectangle = limage.get_rect()
                rectangle.center = (((W/(column+1))*(i+1)),((H/(row+1))*(j+1)))
                pos_images.append((((W/(column+1))*(i+1)),((H/(row+1))*(j+1))))
                screen.blit(limage,rectangle)
                number=number+1
    pygame.display.flip()

    page=0
    boucle=True
    while boucle == True:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
            	boucle = False
            if event.type == KEYDOWN and event.key == K_RIGHT:
                page=page+(column*row)
            if event.type == KEYDOWN and event.key == K_LEFT:
                page=page-(column*row)
            for i in range((column*row)-(len(test)-page)):
                if x > pos_images[i][0]-((large*scale/H)/2) and x < pos_images[i][0]+((large*scale/H)/2) and y > pos_images[i][1]-((haute*scale/H)/2) and y < pos_images[i][1]+((haute*scale/H)/2):
                    affiche('Logo_'+test[i+page]+'_Clicked',pos_images[i],scale=scale,path='./Files/Docs/')
                    pygame.display.flip()
                    boucle2=True
                    while boucle2==True:
                        for ev in pygame.event.get():
                            a, b = pygame.mouse.get_pos()
                            if (a > pos_images[i][0]-((large*scale/H)/2) and a < pos_images[i][0]+((large*scale/H)/2) and b > pos_images[i][1]-((haute*scale/H)/2) and b < pos_images[i][1]+((haute*scale/H)/2))==False:
                                boucle2=False
                            if ev.type == KEYDOWN and event.key == K_ESCAPE:
                                boucle = False
                            if pygame.mouse.get_pressed()==(1,0,0):
                                return test[i+page]
                            else:
                                pass

            else:
                screen.fill((255,255,255))
                nombre=0+page
                for l in range(row):
                    for k in range(column):
                        if (nombre+1+page)>len(test):
                            pass
                        else:
                            limage=pygame.image.load('./Files/Docs/Logo_'+test[nombre+page]+'.png')
                            large=limage.get_width()
                            haute=limage.get_height()
                            limage=pygame.transform.smoothscale(limage,(large*scale/H,haute*scale/H))
                            rectangle = limage.get_rect()
                            rectangle.center = (((W/(column+1))*(k+1)),((H/(row+1))*(l+1)))
                            screen.blit(limage,rectangle)
                            nombre=nombre+1
                pygame.display.flip()





##                #Précedents et suivant ne marchent pas
##                if y >(H/4*0.7)and x > (W/2): #Suivant
##                    if pygame.mouse.get_pressed()==(1,0,0):
##                        print('suivant')
##                if y >(H/4*0.7)and x < (W/2): #Précédent
##                    if pygame.mouse.get_pressed()==(1,0,0):
##                        print('precedent')

def Anamnese():

    screen.fill((255, 255, 255))

    subject_test = ''
    create_new_subject = ''

    ecrire('Identification','arialblack',W/20,(W/2, H/9*1),(0,0,0))
#identification du neuropsychologue
    Neuropsychologist = text_input('Mot de passe ? : ',(W/8.5,H/9*3),allowable=autorisations)
#identification du sujet
    subject_test = text_input('Sujet test ? (o/n) : ',(W/8.5,H/9*4),allowable=['o','n'])
    if subject_test == 'o':
        subject_code = "XXXX_XX_XX_XX_x"
    if subject_test == 'n':
        create_new_subject = text_input('Créer un nouveau participant ? (o/n) : ',(W/8.5,H/9*5),allowable=['o','n'])

        screen.fill((255, 255, 255))
        ecrire('Identification','arialblack',W/20,(W/2, H/9*1),(0,0,0))
        Initials = text_input('Initiales : ',(W/8.5,H/9*3),(0,0,0))
        Sex = text_input('Sexe (m/f) : ',(W/8.5,H/9*4),(0,0,0),allowable=['m','f'])
        Birth_day = text_input('Jour de naissance (jj) : ',(W/8.5,H/9*5),(0,0,0))
        Birth_month = text_input('Mois de naissance (mm) : ',(W/8.5,H/9*6),(0,0,0))
        Birth_year = text_input('Année de naissance (aaaa) : ',(W/8.5,H/9*7),(0,0,0))
        subject_code = str(Birth_year) + '_' + str(Birth_month) + '_' + str(Birth_day) + '_' + Initials + '_' + Sex

#Create subject's directory
    if not os.path.exists("./Data/"+subject_code):
        if create_new_subject == 'n':
            ecrire("Ce sujet n'existe pas dans la base de données",'arialblack',W/50,(W/2, H/9*9),(0,0,0),passer="K_RETURN")
        os.makedirs("./Data/"+subject_code)



#anamnèse
#P1
    if create_new_subject == 'o':
        screen.fill((255, 255, 255))
        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
        ecrire('Informations générales (1/4)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))

        Age = calculate_age([int(Birth_year),int(Birth_month),int(Birth_day)])
        Laterality = text_input('Latéralisation (g/d) : ',(W/8.5,H/9*2),(0,0,0),allowable=['g','d'])
        Vision = text_input('Vision : ',(W/8.5,H/9*3),(0,0,0))
        Understanding = text_input('Compréhension : ',(W/8.5,H/9*4),(0,0,0))
        Nationality = text_input('Nationalité : ',(W/8.5,H/9*5),(0,0,0))
        Ethnicity = text_input('Culture : ',(W/8.5,H/9*6),(0,0,0))

#P2
        screen.fill((255, 255, 255))
        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
        ecrire('Informations générales (2/4)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))

        Birth_area = text_input('Département de naissance : ',(W/8.5,H/9*2),(0,0,0))
        Area = text_input('Département de vie : ',(W/8.5,H/9*3),(0,0,0))
        City = text_input('Ville : ',(W/8.5,H/9*4),(0,0,0))
        Street = text_input('N° et rue : ',(W/8.5,H/9*5),(0,0,0))
        Phone = text_input('N° de tél : ',(W/8.5,H/9*6),(0,0,0))
        Mail = text_input('mail : ',(W/8.5,H/9*7),(0,0,0)) #Probleme avec les points et les arobases
#P3
        screen.fill((255, 255, 255))
        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
        ecrire('Informations générales (3/4)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))

        Job = text_input('Profession : ',(W/8.5,H/9*2),(0,0,0))
        ecrire('0:<1095, 1:<1576, 2:<1924, 3:<3455, 4:<4415, 5:+','arialblack',W/70,(W/2, H/9*3.2),(179,224,255)) #http://www.inegalites.fr/spip.php?page=salaire
        Salary = text_input('Salaire net mensuel : ',(W/8.5,H/9*3.5),(0,0,0))
        ecrire('0:NA, 1:Brevet, 2:BEP-CAP, 3:Bac, 4:Bac+2, 5:Bac+3, 6:Bac+5, 7:Bac+8','arialblack',W/70,(W/2, H/9*4.7),(179,224,255))
        Current_study_level = text_input("Niveau d'étude actuel : ",(W/8.5,H/9*5),(0,0,0))
        Desired_study_level = text_input("Niveau d'étude souhaité : ",(W/8.5,H/9*6),(0,0,0))

#P4
        screen.fill((255, 255, 255))
        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
        ecrire('Informations générales (4/4)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))

        Native_language = text_input('Langue Maternelle : ',(W/8.5,H/9*2),(0,0,0))
        Marital_status = text_input('Statut familial : ',(W/8.5,H/9*3),(0,0,0))
        Number_children = text_input("Nombre d'enfants : ",(W/8.5,H/9*4),(0,0,0))
        Number_brothers = text_input("Nombre de frères : ",(W/8.5,H/9*5),(0,0,0))
        Number_sisters = text_input("Nombre de soeurs : ",(W/8.5,H/9*6),(0,0,0))
        Number_parents = text_input("Nombre de parents : ",(W/8.5,H/9*7),(0,0,0))

#P5
        screen.fill((255, 255, 255))
        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
        ecrire('Informations médicales (1/1)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))

        Referent_physician = text_input('Médecin traitant : ',(W/8.5,H/9*2),(0,0,0))
        Examination_demand = text_input("Origine de la demande d'évaluation : ",(W/8.5,H/9*3),(0,0,0))
        Complaint = text_input("Motif de plainte : ",(W/8.5,H/9*4),(0,0,0))
        Social_security = text_input("Couverture mutuelle : ",(W/8.5,H/9*5),(0,0,0))

#P6
        screen.fill((255, 255, 255))
        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
        ecrire('Antécédents familiaux (1/1)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))

        Family_history_disorder_1 = 'NA'
        Family_history_side_1 = 'NA'
        Family_history_degree_1 = 'NA'
        Family_history_confidence_1 = 'NA'
        Family_history_disorder_2 = 'NA'
        Family_history_side_2 = 'NA'
        Family_history_degree_2 = 'NA'
        Family_history_confidence_2 = 'NA'
        Family_history_disorder_3 = 'NA'
        Family_history_side_3 = 'NA'
        Family_history_degree_3 = 'NA'
        Family_history_confidence_3 = 'NA'
        Family_history_disorder_4 = 'NA'
        Family_history_side_4 = 'NA'
        Family_history_degree_4 = 'NA'
        Family_history_confidence_4 = 'NA'

        Ante_familiaux_1 = text_input('Tb neuropsychiatriques dans la famille ? (o/n) : ',(W/9,H/9*2),(0,0,0),allowable=['o','n'])
        if Ante_familiaux_1 == 'o':
            screen.fill((255, 255, 255))
            ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
            ecrire('Antécédents familiaux (1/1)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
            Family_history_disorder_1 = text_input('Nature du trouble ? : ',(W/8.5,H/9*3),(0,0,0))
            Family_history_side_1 = text_input('Quel côté ? (m/p) : ',(W/8.5,H/9*4),(0,0,0))
            ecrire('Degré : parents : 1, GP - Fratrie: 2, Arrière GP - Oncle/tantes : 3, ...','arialblack',W/70,(W/2, H/9*8),(179,224,255))
            Family_history_degree_1 = text_input('Quel degré ? : ',(W/8.5,H/9*5),(0,0,0))
            ecrire('Certitude : 0: Aucune, 1: Notions, 2: Trouble avéré, 3: Diagnostic formel posé','arialblack',W/70,(W/2, H/9*8),(179,224,255))
            Family_history_confidence_1 = text_input('Niveau de certitude ? : ',(W/8.5,H/9*6),(0,0,0))
            Other_Family_history = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
            if Other_Family_history == 'o':
                screen.fill((255, 255, 255))
                ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                ecrire('Antécédents familiaux (1/1)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                Family_history_disorder_2 = text_input('Nature du trouble ? : ',(W/8.5,H/9*3),(0,0,0))
                Family_history_side_2 = text_input('Quel côté ? (m/p) : ',(W/8.5,H/9*4),(0,0,0))
                ecrire('Degré : parents : 1, GP - Fratrie: 2, Arrière GP - Oncle/tantes : 3, ...','arialblack',W/70,(W/2, H/9*8),(179,224,255))
                Family_history_degree_2 = text_input('Quel degré ? : ',(W/8.5,H/9*5),(0,0,0))
                ecrire('Certitude : 0: Aucune, 1: Notions, 2: Trouble avéré, 3: Diagnostic formel posé','arialblack',W/70,(W/2, H/9*8),(179,224,255))
                Family_history_confidence_2 = text_input('Niveau de certitude ? : ',(W/8.5,H/9*6),(0,0,0))
                Other_Family_history = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
                if Other_Family_history == 'o':
                    screen.fill((255, 255, 255))
                    ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                    ecrire('Antécédents familiaux (1/1)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                    Family_history_disorder_3 = text_input('Nature du trouble ? : ',(W/8.5,H/9*3),(0,0,0))
                    Family_history_side_3 = text_input('Quel côté ? (m/p) : ',(W/8.5,H/9*4),(0,0,0))
                    ecrire('Degré : parents : 1, GP - Fratrie: 2, Arrière GP - Oncle/tantes : 3, ...','arialblack',W/70,(W/2, H/9*8),(179,224,255))
                    Family_history_degree_3 = text_input('Quel degré ? : ',(W/8.5,H/9*5),(0,0,0))
                    ecrire('Certitude : 0: Aucune, 1: Notions, 2: Trouble avéré, 3: Diagnostic formel posé','arialblack',W/70,(W/2, H/9*8),(179,224,255))
                    Family_history_confidence_3 = text_input('Niveau de certitude ? : ',(W/8.5,H/9*6),(0,0,0))
                    Other_Family_history = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
                    if Other_Family_history == 'o':
                        screen.fill((255, 255, 255))
                        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                        ecrire('Antécédents familiaux (1/1)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                        Family_history_disorder_4 = text_input('Nature du trouble ? : ',(W/8.5,H/9*3),(0,0,0))
                        Family_history_side_4 = text_input('Quel côté ? (m/p) : ',(W/8.5,H/9*4),(0,0,0))
                        ecrire('Degré : parents : 1, GP - Fratrie: 2, Arrière GP - Oncle/tantes : 3, ...','arialblack',W/70,(W/2, H/9*8),(179,224,255))
                        Family_history_degree_4 = text_input('Quel degré ? : ',(W/8.5,H/9*5),(0,0,0))
                        ecrire('Certitude : 0: Aucune, 1: Notions, 2: Trouble avéré, 3: Diagnostic formel posé','arialblack',W/70,(W/2, H/9*8),(179,224,255))
                        Family_history_confidence_4 = text_input('Niveau de certitude ? : ',(W/8.5,H/9*6),(0,0,0))

#P7
        screen.fill((255, 255, 255))
        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
        ecrire('Antécédents personnels (1/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))

        Personal_developmental_disorder_1 = 'NA'
        Personal_developmental_severity_1 = 'NA'
        Personal_developmental_state_1 = 'NA'
        Personal_developmental_disorder_2 = 'NA'
        Personal_developmental_severity_2 = 'NA'
        Personal_developmental_state_2 = 'NA'
        Personal_developmental_disorder_3 = 'NA'
        Personal_developmental_severity_3 = 'NA'
        Personal_developmental_state_3 = 'NA'
        Personal_developmental_disorder_4 = 'NA'
        Personal_developmental_severity_4 = 'NA'
        Personal_developmental_state_4 = 'NA'

        ecrire('dyslexie, dysphasie, dysgraphie, dyspraxie, TDAH, TSA, ...','arialblack',W/70,(W/2, H/9*7),(179,224,255))
        Personal_developmental = text_input('Tb neuro-développementaux ? (o/n) : ',(W/9,H/9*2),(0,0,0),allowable=['o','n'])
        if Personal_developmental == 'o':
            screen.fill((255, 255, 255))
            ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
            ecrire('Antécédents personnels (1/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
            Personal_developmental_disorder_1 = text_input('Nature du trouble ? : ',(W/8.5,H/9*3),(0,0,0))
            ecrire('Séverité : 0: subsyndromique, 1: léger, 2: modéré, 3: sévère','arialblack',W/70,(W/2, H/9*7),(179,224,255))
            Personal_developmental_severity_1 = text_input('Séverité ? : ',(W/8.5,H/9*4),(0,0,0))
            Personal_developmental_state_1 = text_input('Toujours présent ? (o/n) : ',(W/8.5,H/9*5),(0,0,0))
            Other_Personal_developmental = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*6),(0,0,0))
            if Other_Personal_developmental == 'o':
                screen.fill((255, 255, 255))
                ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                ecrire('Antécédents personnels (1/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                Personal_developmental_disorder_2 = text_input('Nature du trouble ? : ',(W/8.5,H/9*3),(0,0,0))
                ecrire('Séverité : 0: subsyndromique, 1: léger, 2: modéré, 3: sévère','arialblack',W/70,(W/2, H/9*7),(179,224,255))
                Personal_developmental_severity_2 = text_input('Séverité ? :',(W/8.5,H/9*4),(0,0,0))
                Personal_developmental_state_2 = text_input('Toujours présent ? (o/n) : ',(W/8.5,H/9*5),(0,0,0))
                Other_Personal_developmental = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*6),(0,0,0))
                if Other_Personal_developmental == 'o':
                    screen.fill((255, 255, 255))
                    ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                    ecrire('Antécédents personnels (1/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                    Personal_developmental_disorder_3 = text_input('Nature du trouble ? : ',(W/8.5,H/9*3),(0,0,0))
                    ecrire('Séverité : 0: subsyndromique, 1: léger, 2: modéré, 3: sévère','arialblack',W/70,(W/2, H/9*7),(179,224,255))
                    Personal_developmental_severity_3 = text_input('Séverité ? : ',(W/8.5,H/9*4),(0,0,0))
                    Personal_developmental_state_3 = text_input('Toujours présent ? (o/n) : ',(W/8.5,H/9*5),(0,0,0))
                    Other_Personal_developmental = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*6),(0,0,0))
                    if Other_Personal_developmental == 'o':
                        screen.fill((255, 255, 255))
                        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                        ecrire('Antécédents personnels (1/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                        Personal_developmental_disorder_4 = text_input('Nature du trouble ? : ',(W/8.5,H/9*3),(0,0,0))
                        ecrire('Séverité : 0: subsyndromique, 1: léger, 2: modéré, 3: sévère','arialblack',W/70,(W/2, H/9*7),(179,224,255))
                        Personal_developmental_severity_4 = text_input('Séverité ? : ',(W/8.5,H/9*4),(0,0,0))
                        Personal_developmental_state_4 = text_input('Toujours présent ? (o/n) : ',(W/8.5,H/9*5),(0,0,0))
                        Other_Personal_developmental = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*6),(0,0,0))
#P8
        screen.fill((255, 255, 255))
        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
        ecrire('Antécédents personnels (2/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))

        Personal_neurological_disorder_1 = 'NA'
        Personal_neurological_onset_year_1 = 'NA'
        Personal_neurological_onset_month_1 = 'NA'
        Personal_neurological_remission_1 = 'NA'
        Personal_neurological_disorder_2 = 'NA'
        Personal_neurological_onset_year_2 = 'NA'
        Personal_neurological_onset_month_2 = 'NA'
        Personal_neurological_remission_2 = 'NA'
        Personal_neurological_disorder_3 = 'NA'
        Personal_neurological_onset_year_3 = 'NA'
        Personal_neurological_onset_month_3 = 'NA'
        Personal_neurological_remission_3 = 'NA'
        Personal_neurological_disorder_4 = 'NA'
        Personal_neurological_onset_year_4 = 'NA'
        Personal_neurological_onset_month_4 = 'NA'
        Personal_neurological_remission_4 = 'NA'

        ecrire('épilépsie, AVC, TC, ...','arialblack',W/70,(W/2, H/9*8),(179,224,255))
        Personal_neurological = text_input('Tb neurologiques ? (o/n) : ',(W/9,H/9*2),(0,0,0),allowable=['o','n'])
        if Personal_neurological == 'o':
            screen.fill((255, 255, 255))
            ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
            ecrire('Antécédents personnels (2/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
            Personal_neurological_disorder_1 = text_input("Nature de l'affection ? : ",(W/8.5,H/9*3),(0,0,0))
            Personal_neurological_onset_year_1 = text_input('Année de début : ',(W/8.5,H/9*4),(0,0,0))
            Personal_neurological_onset_month_1 = text_input('Mois de début : ',(W/8.5,H/9*5),(0,0,0))
            ecrire('Rémission en pourcentage (ex: 100 = rémission complète)','arialblack',W/70,(W/2, H/9*8),(179,224,255))
            Personal_neurological_remission_1 = text_input('Rémission : ',(W/8.5,H/9*6),(0,0,0))
            Other_Personal_neurological = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
            if Other_Personal_neurological == 'o':
                screen.fill((255, 255, 255))
                ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                ecrire('Antécédents personnels (2/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                Personal_neurological_disorder_2 = text_input("Nature de l'affection ? : ",(W/8.5,H/9*3),(0,0,0))
                Personal_neurological_onset_year_2 = text_input('Année de début : ',(W/8.5,H/9*4),(0,0,0))
                Personal_neurological_onset_month_2 = text_input('Mois de début : ',(W/8.5,H/9*5),(0,0,0))
                ecrire('Rémission en pourcentage (ex: 100 = rémission complète)','arialblack',W/70,(W/2, H/9*8),(179,224,255))
                Personal_neurological_remission_2 = text_input('Rémission : ',(W/8.5,H/9*6),(0,0,0))
                Other_Personal_neurological = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
                if Other_Personal_neurological == 'o':
                    screen.fill((255, 255, 255))
                    ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                    ecrire('Antécédents personnels (2/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                    Personal_neurological_disorder_3 = text_input("Nature de l'affection ? : ",(W/8.5,H/9*3),(0,0,0))
                    Personal_neurological_onset_year_3 = text_input('Année de début : ',(W/8.5,H/9*4),(0,0,0))
                    Personal_neurological_onset_month_3 = text_input('Mois de début : ',(W/8.5,H/9*5),(0,0,0))
                    ecrire('Rémission en pourcentage (ex: 100 = rémission complète)','arialblack',W/70,(W/2, H/9*8),(179,224,255))
                    Personal_neurological_remission_3 = text_input('Rémission : ',(W/8.5,H/9*6),(0,0,0))
                    Other_Personal_neurological = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
                    if Other_Personal_neurological == 'o':
                        screen.fill((255, 255, 255))
                        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                        ecrire('Antécédents personnels (2/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                        Personal_neurological_disorder_4 = text_input("Nature de l'affection ? : ",(W/8.5,H/9*3),(0,0,0))
                        Personal_neurological_onset_year_4 = text_input('Année de début : ',(W/8.5,H/9*4),(0,0,0))
                        Personal_neurological_onset_month_4 = text_input('Mois de début : ',(W/8.5,H/9*5),(0,0,0))
                        ecrire('Rémission en pourcentage (ex: 100 = rémission complète)','arialblack',W/70,(W/2, H/9*8),(179,224,255))
                        Personal_neurological_remission_4 = text_input('Rémission : ',(W/8.5,H/9*6),(0,0,0))
                        Other_Personal_neurological = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
#P9
        screen.fill((255, 255, 255))
        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
        ecrire('Antécédents personnels (3/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))

        Personal_psychiatric_disorder_1 = 'NA'
        Personal_psychiatric_onset_year_1 = 'NA'
        Personal_psychiatric_duration_1 = 'NA'
        Personal_psychiatric_remission_1 = 'NA'
        Personal_psychiatric_disorder_2 = 'NA'
        Personal_psychiatric_onset_year_2 = 'NA'
        Personal_psychiatric_duration_2 = 'NA'
        Personal_psychiatric_remission_2 = 'NA'
        Personal_psychiatric_disorder_3 = 'NA'
        Personal_psychiatric_onset_year_3 = 'NA'
        Personal_psychiatric_duration_3 = 'NA'
        Personal_psychiatric_remission_3 = 'NA'
        Personal_psychiatric_disorder_4 = 'NA'
        Personal_psychiatric_onset_year_4 = 'NA'
        Personal_psychiatric_duration_4 = 'NA'
        Personal_psychiatric_remission_4 = 'NA'

        ecrire('dépression, anxiété, phobies, ...','arialblack',W/70,(W/2, H/9*8),(179,224,255))
        Personal_psychiatric = text_input('Tb psychiatriques ? (o/n) : ',(W/9,H/9*2),(0,0,0),allowable=['o','n'])
        if Personal_psychiatric == 'o':
            screen.fill((255, 255, 255))
            ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
            ecrire('Antécédents personnels (3/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
            Personal_psychiatric_disorder_1 = text_input("Diagnostic DSM 5 : ",(W/8.5,H/9*3),(0,0,0))
            Personal_psychiatric_onset_year_1 = text_input('Année de début : ',(W/8.5,H/9*4),(0,0,0))
            Personal_psychiatric_duration_1 = text_input('Durée en mois : ',(W/8.5,H/9*5),(0,0,0))
            ecrire('Rémission en pourcentage (ex: 100 = rémission complète)','arialblack',W/70,(W/2, H/9*8),(179,224,255))
            Personal_psychiatric_remission_1 = text_input('Rémission : ',(W/8.5,H/9*6),(0,0,0))
            Other_Personal_psychiatric = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
            if Other_Personal_psychiatric == 'o':
                screen.fill((255, 255, 255))
                ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                ecrire('Antécédents personnels (3/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                Personal_psychiatric_disorder_2 = text_input("Diagnostic DSM 5 : ",(W/8.5,H/9*3),(0,0,0))
                Personal_psychiatric_onset_year_2 = text_input('Année de début : ',(W/8.5,H/9*4),(0,0,0))
                Personal_psychiatric_duration_2 = text_input('Durée en mois : ',(W/8.5,H/9*5),(0,0,0))
                ecrire('Rémission en pourcentage (ex: 100 = rémission complète)','arialblack',W/70,(W/2, H/9*8),(179,224,255))
                Personal_psychiatric_remission_2 = text_input('Rémission : ',(W/8.5,H/9*6),(0,0,0))
                Other_Personal_psychiatric = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
                if Other_Personal_psychiatric == 'o':
                    screen.fill((255, 255, 255))
                    ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                    ecrire('Antécédents personnels (3/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                    Personal_psychiatric_disorder_3 = text_input("Diagnostic DSM 5 : ",(W/8.5,H/9*3),(0,0,0))
                    Personal_psychiatric_onset_year_3 = text_input('Année de début : ',(W/8.5,H/9*4),(0,0,0))
                    Personal_psychiatric_duration_3 = text_input('Durée en mois : ',(W/8.5,H/9*5),(0,0,0))
                    ecrire('Rémission en pourcentage (ex: 100 = rémission complète)','arialblack',W/70,(W/2, H/9*8),(179,224,255))
                    Personal_psychiatric_remission_3 = text_input('Rémission : ',(W/8.5,H/9*6),(0,0,0))
                    Other_Personal_psychiatric = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
                    if Other_Personal_psychiatric == 'o':
                            screen.fill((255, 255, 255))
                            ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                            ecrire('Antécédents personnels (3/3)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                            Personal_psychiatric_disorder_4 = text_input("Diagnostic DSM 5 : ",(W/8.5,H/9*3),(0,0,0))
                            Personal_psychiatric_onset_year_4 = text_input('Année de début : ',(W/8.5,H/9*4),(0,0,0))
                            Personal_psychiatric_duration_4 = text_input('Durée en mois : ',(W/8.5,H/9*5),(0,0,0))
                            ecrire('Rémission en pourcentage (ex: 100 = rémission complète)','arialblack',W/70,(W/2, H/9*8),(179,224,255))
                            Personal_psychiatric_remission_4 = text_input('Rémission : ',(W/8.5,H/9*6),(0,0,0))
                            Other_Personal_psychiatric = text_input('Autre chose ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))



#P10
        screen.fill((255, 255, 255))
        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
        ecrire('Psychotropes (1/2)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))

        Medical_drug_1 = 'NA'
        Medical_drug_time_1 = 'NA'
        Medical_drug_quantity_1 = 'NA'
        Medical_drug_2 = 'NA'
        Medical_drug_time_2 = 'NA'
        Medical_drug_quantity_2 = 'NA'
        Medical_drug_3 = 'NA'
        Medical_drug_time_3 = 'NA'
        Medical_drug_quantity_3 = 'NA'
        Medical_drug_4 = 'NA'
        Medical_drug_time_4 = 'NA'
        Medical_drug_quantity_4 = 'NA'

        Medical_drug = text_input('Médicaments actuels ? (o/n) : ',(W/9,H/9*2),(0,0,0),allowable=['o','n'])
        if Medical_drug == 'o':
            screen.fill((255, 255, 255))
            ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
            ecrire('Psychotropes (1/2)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
            Medical_drug_1 = text_input("Molécule : ",(W/8.5,H/9*3),(0,0,0))
            Medical_drug_time_1 = text_input('Durée de prise (en mois) : ',(W/8.5,H/9*4),(0,0,0))
            Medical_drug_quantity_1 = text_input('Quantité moyenne : ',(W/8.5,H/9*5),(0,0,0))
            Other_Medical_drug = text_input('Autre médicament ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
            if Other_Medical_drug == 'o':
                screen.fill((255, 255, 255))
                ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                ecrire('Psychotropes (1/2)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                Medical_drug_2 = text_input("Molécule : ",(W/8.5,H/9*3),(0,0,0))
                Medical_drug_time_2 = text_input('Durée de prise (en mois) : ',(W/8.5,H/9*4),(0,0,0))
                Medical_drug_quantity_2 = text_input('Quantité moyenne : ',(W/8.5,H/9*5),(0,0,0))
                Other_Medical_drug = text_input('Autre médicament ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
                if Other_Medical_drug == 'o':
                    screen.fill((255, 255, 255))
                    ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                    ecrire('Psychotropes (1/2)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                    Medical_drug_3 = text_input("Molécule : ",(W/8.5,H/9*3),(0,0,0))
                    Medical_drug_time_3 = text_input('Durée de prise (en mois) : ',(W/8.5,H/9*4),(0,0,0))
                    Medical_drug_quantity_3 = text_input('Quantité moyenne : ',(W/8.5,H/9*5),(0,0,0))
                    Other_Medical_drug = text_input('Autre médicament ? (o/n) : ',(W/8.5,H/9*7),(0,0,0))
                    if Other_Medical_drug == 'o':
                        screen.fill((255, 255, 255))
                        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                        ecrire('Psychotropes (1/2)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                        Medical_drug_4 = text_input("Molécule : ",(W/8.5,H/9*3),(0,0,0))
                        Medical_drug_time_4 = text_input('Durée de prise (en mois) : ',(W/8.5,H/9*4),(0,0,0))
                        Medical_drug_quantity_4 = text_input('Quantité moyenne : ',(W/8.5,H/9*5),(0,0,0))
 #P11


        Tobacco = '0'
        Tobacco_time = 'NA'
        Alcool = '0'
        Alcool_time = 'NA'

        Drug_1 = 'NA'
        Drug_quantity_1 = 'NA'

        Drug_time_1 = '0'
        Drug_2 = 'NA'
        Drug_quantity_2 = 'NA'
        Drug_time_2 = '0'
        Drug_3 = 'NA'
        Drug_quantity_3 = 'NA'
        Drug_time_3 = '0'
        Drug_4 = 'NA'
        Drug_quantity_4 = 'NA'
        Drug_time_4 = '0'

        screen.fill((255, 255, 255))
        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
        ecrire('Psychotropes (2/2)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
        Tobacco = text_input("Nb de paquet de cigarettes / semaine ? : ",(W/8.5,H/9*3),(0,0,0))
        Tobacco_time = text_input('Depuis quel âge : ',(W/8.5,H/9*4),(0,0,0))
        Alcool = text_input("Nb de verres / semaine ? : ",(W/8.5,H/9*5),(0,0,0))
        Alcool_time = text_input('Depuis quel âge : ',(W/8.5,H/9*6),(0,0,0))

        screen.fill((255, 255, 255))
        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
        ecrire('Psychotropes (2/2)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
        Drug = text_input('Stupéfiants (o/n) : ',(W/8.5,H/9*3),(0,0,0),allowable=['o','n'])
        if Drug == 'o':
            screen.fill((255, 255, 255))
            ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
            ecrire('Psychotropes (2/2)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
            Drug_1 = text_input("Nom : ",(W/8.5,H/9*3),(0,0,0))
            Drug_quantity_1 = text_input('Quantité moyenne (en Euros/semaine) : ',(W/8.5,H/9*4),(0,0,0))
            Drug_time_1 = text_input('Depuis quel âge ? : ',(W/8.5,H/9*5),(0,0,0))
            Other_drug = text_input('Autre stupéfiant ? (o/n) : ',(W/8.5,H/9*7),(0,0,0),allowable=['o','n'])
            if Other_drug == 'o':
                screen.fill((255, 255, 255))
                ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                ecrire('Psychotropes (2/2)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                Drug_2 = text_input("Nom : ",(W/8.5,H/9*3),(0,0,0))
                Drug_quantity_2 = text_input('Quantité moyenne (en Euros/semaine) : ',(W/8.5,H/9*4),(0,0,0))
                Drug_time_2 = text_input('Depuis quel âge : ',(W/8.5,H/9*5),(0,0,0))
                Other_drug = text_input('Autre stupéfiant ? (o/n) : ',(W/8.5,H/9*7),(0,0,0),allowable=['o','n'])
                if Other_drug == 'o':
                    screen.fill((255, 255, 255))
                    ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                    ecrire('Psychotropes (2/2)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                    Drug_3 = text_input("Nom : ",(W/8.5,H/9*3),(0,0,0))
                    Drug_quantity_3 = text_input('Quantité moyenne (en Euros/semaine) : ',(W/8.5,H/9*4),(0,0,0))
                    Drug_time_3 = text_input('Depuis quel âge : ',(W/8.5,H/9*5),(0,0,0))
                    Other_drug = text_input('Autre stupéfiant ? (o/n) : ',(W/8.5,H/9*7),(0,0,0),allowable=['o','n'])
                    if Other_drug == 'o':
                        screen.fill((255, 255, 255))
                        ecrire('Anamnèse','arialblack',W/30,(W/2, H/9*1),(0,0,0))
                        ecrire('Psychotropes (2/2)','arialblack',W/50,(W/2, H/9*1.5),(0,0,0))
                        Drug_4 = text_input("Nom : ",(W/8.5,H/9*3),(0,0,0))
                        Drug_quantity_4 = text_input('Quantité moyenne (en Euros/semaine) : ',(W/8.5,H/9*4),(0,0,0))
                        Drug_time_4 = text_input('Depuis quel âge : ',(W/8.5,H/9*5),(0,0,0),allowable=['o','n'])



    if subject_test == 'o':
        Initials = "XX"
        Sex = "XX"
        Birth_day = "XX"
        Birth_month = "XX"
        Birth_year = "XX"
        Age = 20
        Laterality = "XX"
        Vision = "XX"
        Understanding = "XX"
        Nationality = "XX"
        Ethnicity = "XX"
        Birth_area = "XX"
        Area = "XX"
        City = "XX"
        Street = "XX"
        Phone = "XX"
        Mail = "XX"
        Job = "XX"
        Salary = "XX"
        Current_study_level = "XX"
        Desired_study_level = "XX"
        Native_language = "XX"
        Marital_status = "XX"
        Number_children = "XX"
        Number_brothers = "XX"
        Number_sisters = "XX"
        Number_parents = "XX"
        Referent_physician = "XX"
        Examination_demand = "XX"
        Complaint = "XX"
        Social_security = "XX"
        Family_history_disorder_1 = "XX"
        Family_history_side_1 = "XX"
        Family_history_degree_1 = "XX"
        Family_history_confidence_1 = 'XX'
        Family_history_disorder_2 = "XX"
        Family_history_side_2 = "XX"
        Family_history_degree_2 = "XX"
        Family_history_confidence_2 = 'XX'
        Family_history_disorder_3 = "XX"
        Family_history_side_3 = "XX"
        Family_history_degree_3 = "XX"
        Family_history_confidence_3 = 'XX'
        Family_history_disorder_4 = "XX"
        Family_history_side_4 = "XX"
        Family_history_degree_4 = "XX"
        Family_history_confidence_4 = 'XX'
        Personal_developmental_disorder_1 = "XX"
        Personal_developmental_severity_1 = "XX"
        Personal_developmental_state_1 = "XX"
        Personal_developmental_disorder_2 = "XX"
        Personal_developmental_severity_2 = "XX"
        Personal_developmental_state_2 = "XX"
        Personal_developmental_disorder_3 = "XX"
        Personal_developmental_severity_3 = "XX"
        Personal_developmental_state_3 = "XX"
        Personal_developmental_disorder_4 = "XX"
        Personal_developmental_severity_4 = "XX"
        Personal_developmental_state_4 = "XX"
        Personal_neurological_disorder_1 = 'XX'
        Personal_neurological_onset_year_1 = 'XX'
        Personal_neurological_onset_month_1 = 'XX'
        Personal_neurological_remission_1 = 'XX'
        Personal_neurological_disorder_2 = 'XX'
        Personal_neurological_onset_year_2 = 'XX'
        Personal_neurological_onset_month_2 = 'XX'
        Personal_neurological_remission_2 = 'XX'
        Personal_neurological_disorder_3 = 'XX'
        Personal_neurological_onset_year_3 = 'XX'
        Personal_neurological_onset_month_3 = 'XX'
        Personal_neurological_remission_3 = 'XX'
        Personal_neurological_disorder_4 = 'XX'
        Personal_neurological_onset_year_4 = 'XX'
        Personal_neurological_onset_month_4 = 'XX'
        Personal_neurological_remission_4 = 'XX'
        Personal_psychiatric_disorder_1 = 'XX'
        Personal_psychiatric_onset_year_1 = 'XX'
        Personal_psychiatric_duration_1 = 'XX'
        Personal_psychiatric_remission_1 = 'XX'
        Personal_psychiatric_disorder_2 = 'XX'
        Personal_psychiatric_onset_year_2 = 'XX'
        Personal_psychiatric_duration_2 = 'XX'
        Personal_psychiatric_remission_2 = 'XX'
        Personal_psychiatric_disorder_3 = 'XX'
        Personal_psychiatric_onset_year_3 = 'XX'
        Personal_psychiatric_duration_3 = 'XX'
        Personal_psychiatric_remission_3 = 'XX'
        Personal_psychiatric_disorder_4 = 'XX'
        Personal_psychiatric_onset_year_4 = 'XX'
        Personal_psychiatric_duration_4 = 'XX'
        Personal_psychiatric_remission_4 = 'XX'
        Medical_drug_1 = 'XX'
        Medical_drug_time_1 = 'XX'
        Medical_drug_quantity_1 = 'XX'
        Medical_drug_2 = 'XX'
        Medical_drug_time_2 = 'XX'
        Medical_drug_quantity_2 = 'XX'
        Medical_drug_3 = 'XX'
        Medical_drug_time_3 = 'XX'
        Medical_drug_quantity_3 = 'XX'
        Medical_drug_4 = 'XX'
        Medical_drug_time_4 = 'XX'
        Medical_drug_quantity_4 = 'XX'
        Tobacco = 'XX'
        Tobacco_time = '0'
        Alcool = 'XX'
        Alcool_time = '0'
        Drug_1 = 'XX'
        Drug_quantity_1 = 'XX'
        Drug_time_1 = '0'
        Drug_2 = 'XX'
        Drug_quantity_2 = 'XX'
        Drug_time_2 = '0'
        Drug_3 = 'XX'
        Drug_quantity_3 = 'XX'
        Drug_time_3 = '0'
        Drug_4 = 'XX'
        Drug_quantity_4 = 'XX'
        Drug_time_4 = '0'



#File creation
    data = open("./Data/"+subject_code+'/'+subject_code+'_INFOS.csv','w')
    print>>data, 'Examination_date'+';'+'Examination_time'+';'+'Neuropsychologist'+';'+'subject_code'+';'+'Initials' +';'+ 'Sex' +';'+'Birth_day'  +';'+'Birth_month' +';'+'Birth_year' +';'+'Age'+';'+'Laterality'+';'+'Vision'\
    +';'+'Understanding'+';'+'Nationality'+';'+'Ethnicity'+';'+'Birth_area'+';'+'Area'+';'+'City'+';'+'Street'+';'+'Phone'+';'+'Mail'+';'+'Job'\
    +';'+'Salary'+';'+'Current_study_level'+';'+'Desired_study_level'+';'+'Native_language'+';'+'Marital_status'+';'+'Number_children'\
    +';'+'Number_brothers'+';'+'Number_sisters'+';'+'Number_parents'+';'+'Referent_physician'+';'+'Examination_demand'+';'+'Complaint'+';'+'Social_security'\
    +';'+'Family_history_disorder_1'+';'+'Family_history_side_1'+';'+'Family_history_degree_1'+';'+'Family_history_confidence_1'\
    +';'+'Family_history_disorder_2'+';'+'Family_history_side_2'+';'+'Family_history_degree_2'+';'+'Family_history_confidence_2'\
    +';'+'Family_history_disorder_3'+';'+'Family_history_side_3'+';'+'Family_history_degree_3'+';'+'Family_history_confidence_3'\
    +';'+'Family_history_disorder_4'+';'+'Family_history_side_4'+';'+'Family_history_degree_4'+';'+'Family_history_confidence_4'\
    +';'+'Personal_developmental_disorder_1'+';'+'Personal_developmental_severity_1'+';'+'Personal_developmental_state_1'\
    +';'+'Personal_developmental_disorder_2'+';'+'Personal_developmental_severity_2'+';'+'Personal_developmental_state_2'\
    +';'+'Personal_developmental_disorder_3'+';'+'Personal_developmental_severity_3'+';'+'Personal_developmental_state_3'\
    +';'+'Personal_developmental_disorder_4'+';'+'Personal_developmental_severity_4'+';'+'Personal_developmental_state_4'\
    +';'+'Personal_neurological_disorder_1' +';'+ 'Personal_neurological_onset_year_1' +';'+ 'Personal_neurological_onset_month_1'  +';'+ 'Personal_neurological_remission_1'\
    +';'+'Personal_neurological_disorder_2'  +';'+'Personal_neurological_onset_year_2'  +';'+'Personal_neurological_onset_month_2'  +';'+'Personal_neurological_remission_2'\
    +';'+'Personal_neurological_disorder_3'  +';'+'Personal_neurological_onset_year_3'  +';'+'Personal_neurological_onset_month_3'  +';'+'Personal_neurological_remission_3'\
    +';'+'Personal_neurological_disorder_4'  +';'+'Personal_neurological_onset_year_4'  +';'+'Personal_neurological_onset_month_4'  +';'+'Personal_neurological_remission_4'\
    +';'+'Personal_psychiatric_disorder_1'  +';'+'Personal_psychiatric_onset_year_1'  +';'+'Personal_psychiatric_duration_1'  +';'+'Personal_psychiatric_remission_1'\
    +';'+'Personal_psychiatric_disorder_2'  +';'+'Personal_psychiatric_onset_year_2'  +';'+'Personal_psychiatric_duration_2'  +';'+'Personal_psychiatric_remission_2'\
    +';'+'Personal_psychiatric_disorder_3'  +';'+'Personal_psychiatric_onset_year_3'  +';'+'Personal_psychiatric_duration_3'  +';'+'Personal_psychiatric_remission_3'\
    +';'+'Personal_psychiatric_disorder_4'  +';'+'Personal_psychiatric_onset_year_4'  +';'+'Personal_psychiatric_duration_4'  +';'+'Personal_psychiatric_remission_4'\
    +';'+'Medical_drug_1'+';'+'Medical_drug_time_1'+';'+'Medical_drug_quantity_1'\
    +';'+'Medical_drug_2'+';'+'Medical_drug_time_2'+';'+'Medical_drug_quantity_2'\
    +';'+'Medical_drug_3'+';'+'Medical_drug_time_3'+';'+'Medical_drug_quantity_3'\
    +';'+'Medical_drug_4'+';'+'Medical_drug_time_4'+';'+'Medical_drug_quantity_4'\
    +';'+'Tobacco'+';'+'Tobacco_time'+';'+'Alcool'+';'+'Alcool_time'\
    +';'+'Drug_1'+';'+'Drug_quantity_1'+';'+'Drug_time_1'\
    +';'+'Drug_2'+';'+'Drug_quantity_2'+';'+'Drug_time_2'\
    +';'+'Drug_3'+';'+'Drug_quantity_3'+';'+'Drug_time_3'\
    +';'+'Drug_4'+';'+'Drug_quantity_4'+';'+'Drug_time_4'



    print>>data, strftime("%Y-%m-%d") +';' + strftime("%H:%M:%S") +';'+ Neuropsychologist + ';' + subject_code + ';' + Initials +';'+ Sex +';'+Birth_day  +';'+Birth_month +';'+Birth_year +';'+str(Age)+';'+Laterality+';'+Vision\
    +';'+Understanding+';'+Nationality+';'+Ethnicity+';'+Birth_area+';'+Area+';'+City+';'+Street+';'+Phone+';'+Mail+';'+Job\
    +';'+Salary+';'+Current_study_level+';'+Desired_study_level+';'+Native_language+';'+Marital_status+';'+Number_children\
    +';'+Number_brothers+';'+Number_sisters+';'+Number_parents+';'+Referent_physician+';'+Examination_demand+';'+Complaint+';'+Social_security\
    +';'+Family_history_disorder_1+';'+Family_history_side_1+';'+Family_history_degree_1+';'+Family_history_confidence_1\
    +';'+Family_history_disorder_2+';'+Family_history_side_2+';'+Family_history_degree_2+';'+Family_history_confidence_2\
    +';'+Family_history_disorder_3+';'+Family_history_side_3+';'+Family_history_degree_3+';'+Family_history_confidence_3\
    +';'+Family_history_disorder_4+';'+Family_history_side_4+';'+Family_history_degree_4+';'+Family_history_confidence_4\
    +';'+Personal_developmental_disorder_1+';'+Personal_developmental_severity_1+';'+Personal_developmental_state_1\
    +';'+Personal_developmental_disorder_2+';'+Personal_developmental_severity_2+';'+Personal_developmental_state_2\
    +';'+Personal_developmental_disorder_3+';'+Personal_developmental_severity_3+';'+Personal_developmental_state_3\
    +';'+Personal_developmental_disorder_4+';'+Personal_developmental_severity_4+';'+Personal_developmental_state_4\
    +';'+Personal_neurological_disorder_1 +';'+ Personal_neurological_onset_year_1 +';'+ Personal_neurological_onset_month_1  +';'+Personal_neurological_remission_1\
    +';'+Personal_neurological_disorder_2  +';'+Personal_neurological_onset_year_2  +';'+Personal_neurological_onset_month_2  +';'+Personal_neurological_remission_2\
    +';'+Personal_neurological_disorder_3  +';'+Personal_neurological_onset_year_3  +';'+Personal_neurological_onset_month_3  +';'+Personal_neurological_remission_3\
    +';'+Personal_neurological_disorder_4  +';'+Personal_neurological_onset_year_4  +';'+Personal_neurological_onset_month_4  +';'+Personal_neurological_remission_4\
    +';'+Personal_psychiatric_disorder_1  +';'+Personal_psychiatric_onset_year_1  +';'+Personal_psychiatric_duration_1  +';'+Personal_psychiatric_remission_1\
    +';'+Personal_psychiatric_disorder_2  +';'+Personal_psychiatric_onset_year_2  +';'+Personal_psychiatric_duration_2  +';'+Personal_psychiatric_remission_2\
    +';'+Personal_psychiatric_disorder_3  +';'+Personal_psychiatric_onset_year_3  +';'+Personal_psychiatric_duration_3  +';'+Personal_psychiatric_remission_3\
    +';'+Personal_psychiatric_disorder_4  +';'+Personal_psychiatric_onset_year_4  +';'+Personal_psychiatric_duration_4  +';'+Personal_psychiatric_remission_4\
    +';'+Medical_drug_1+';'+Medical_drug_time_1+';'+Medical_drug_quantity_1\
    +';'+Medical_drug_2+';'+Medical_drug_time_2+';'+Medical_drug_quantity_2\
    +';'+Medical_drug_3+';'+Medical_drug_time_3+';'+Medical_drug_quantity_3\
    +';'+Medical_drug_4+';'+Medical_drug_time_4+';'+Medical_drug_quantity_4\
    +';'+Tobacco+';'+str(Age-int(Tobacco_time))+';'+Alcool+';'+str(Age-int(Alcool_time))\
    +';'+Drug_1+';'+Drug_quantity_1+';'+str(Age-int(Drug_time_1))\
    +';'+Drug_2+';'+Drug_quantity_2+';'+str(Age-int(Drug_time_2))\
    +';'+Drug_3+';'+Drug_quantity_3+';'+str(Age-int(Drug_time_3))\
    +';'+Drug_4+';'+Drug_quantity_4+';'+str(Age-int(Drug_time_4))
    data.close()

    return(subject_code)



try:
    n.autre_test = 'o'
    pygame.init()
    screen.fill((255, 255, 255))
    affiche('Logo_Launcher',(W/2,H/2.40),scale=W/12,path='./Files/Docs/')
##    for i in range (7):
##        affiche('./Animated_Logo/Animated_Logo (' + str(i+1) + ')',(W/2,H/2.40),scale=W/12,path='./Files/Docs/')
##        pygame.display.flip()
    #ecrire(version,'arialblack', W/70,(W/1.3, H/9*2.5),(0,0,0))
    #ecrire(authors,'arialblack', W/70,(W/2, H/9*5),(0,0,0))
    ecrire('Appuyez sur ENTREE pour commencer.','arialblack',W/50,(W/2, H/9*8.5),(0,0,0),passer="K_RETURN")
    pygame.display.flip()

    subject_code = Anamnese()

    boucle=True

    while boucle==True:

        pygame.mouse.set_visible(True)
        test=launcher((2,3),scale=W/8)
        os.chdir(".\\Files\\Tests\\"+test)
        try:
            execfile(test+".py")
        except SystemExit:
            pass
        os.chdir(origin)
        screen.fill((255,255,255))

        if n.autre_test=='o':
            pass
        else:
            boucle=False





# On peut récupérer des variables de BPDQ, genre n.suj ou n.init






finally:
    #Merge des data
    try:
        df = pandas.read_csv(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_INFOS.csv',header = 0,engine='python',sep=';',index_col="subject_code")

        if os.path.isfile(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_IPIP6.csv') == True:
            df_IPIP6 = pandas.read_csv(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_IPIP6.csv',header = 0,engine='python',sep=';',index_col="subject_code")
            df = pandas.concat([df, df_IPIP6], axis=1)
        if os.path.isfile(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_RIDE.csv') == True:
            df_RIDE = pandas.read_csv(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_RIDE.csv',header = 0,engine='python',sep=';',index_col="subject_code")
            df = pandas.concat([df, df_RIDE], axis=1)
        if os.path.isfile(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_BPDQ.csv') == True:
            df_BPDQ = pandas.read_csv(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_BPDQ.csv',header = 0,engine='python',sep=';',index_col="subject_code")
            df = pandas.concat([df, df_BPDQ], axis=1)
        if os.path.isfile(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_Switch.csv') == True:
            df_Switch = pandas.read_csv(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_Switch.csv',header = 0,engine='python',sep=';',index_col="subject_code")
            df = pandas.concat([df, df_Switch], axis=1)
        if os.path.isfile(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_SimAct.csv') == True:
            df_SimAct = pandas.read_csv(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_SimAct.csv',header = 0,engine='python',sep=';',index_col="subject_code")
            df = pandas.concat([df, df_SimAct], axis=1)
        if os.path.isfile(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_Wordini.csv') == True:
            df_Wordini = pandas.read_csv(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_Wordini.csv',header = 0,engine='python',sep=';',index_col="subject_code")
            df = pandas.concat([df, df_Wordini], axis=1)
        df.to_csv(os.getcwd().split('\\Files')[0] + '/Data/'+subject_code+'/'+subject_code+'_SUMMARY.csv',sep = ';',decimal=',', index=True,na_rep='NA') #celui-ci avec les décimales virgules
    except:
        pass

    pygame.quit()

#     # if BPDQ == 'o':
#     #     os.system('./Files/Exe/BPDQ/BPDQ.py')
#     # if WORDINI == 'o':
#     #     os.system('./Files/Exe/Wordini/Wordini.py')
#     # if SWITCH == 'o':
#     #     os.system('./Files/Exe/Switch/Switch.py')
#     # if MEMUP == 'o':
#     #     os.system('./Files/Exe/Memup/Memup.py')


#     # screen.fill((255, 255, 255))
#     # ecrire('Merci !','arialblack', W/30,(W/2, H/2),(0,0,0))
#     # pygame.display.flip()
#     # pygame.time.wait(1000)
#     # pygame.quit()
#     # quit()
