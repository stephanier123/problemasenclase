# -*- coding:utf-8 -*-
import rufino
import sys
import math
import time

from scipy.stats.stats import pearsonr
from scipy.stats.stats import spearmanr

# parametros de la linea de comandos
tamano_corpus=int(sys.argv[1])  # funcion int(cadena) convierte la cadena en un numero entero
reportar_cada_x_articulos=int(sys.argv[2])
codigo_ISO=sys.argv[3]


dataset={
("tiger","tiger"):10,
("fuck","sex"):9.44,
("journey","voyage"):9.29,
("midday","noon"):9.29,
("money","cash"):9.15,
("coast","shore"):9.1,
("money","cash"):9.08,
("money","currency"):9.04,
("football","soccer"):9.03,
("magician","wizard"):9.02,
("gem","jewel"):8.96,
("car","automobile"):8.94,
("asylum","madhouse"):8.87,
("boy","lad"):8.83,
("furnace","stove"):8.79,
("Maradona","football"):8.62,
("king","queen"):8.58,
("money","bank"):8.5,
("Jerusalem","Israel"):8.46,
("vodka","gin"):8.46,
("planet","star"):8.45,
("money","dollar"):8.42,
("law","lawyer"):8.38,
("money","wealth"):8.27,
("psychology","Freud"):8.21,
("vodka","brandy"):8.13,
("bank","money"):8.12,
("physics","proton"):8.12,
("planet","galaxy"):8.11,
("stock","market"):8.08,
("psychology","psychiatry"):8.08,
("planet","moon"):8.08,
("planet","constellation"):8.06,
("planet","sun"):8.02,
("tiger","jaguar"):8,
("tiger","feline"):8,
("planet","astronomer"):7.94,
("movie","theater"):7.92,
("planet","space"):7.92,
("baby","mother"):7.85,
("wood","forest"):7.73,
("money","deposit"):7.73,
("psychology","mind"):7.69,
("Jerusalem","Palestinian"):7.65,
("Arafat","terror"):7.65,
("computer","keyboard"):7.62,
("computer","internet"):7.58,
("money","property"):7.57,
("tennis","racket"):7.56,
("food","fruit"):7.52,
("telephone","communication"):7.5,
("psychology","cognition"):7.48,
("book","paper"):7.46,
("book","library"):7.46,
("media","radio"):7.42,
("psychology","depression"):7.42,
("jaguar","cat"):7.42,
("movie","star"):7.38,
("bird","crane"):7.38,
("tiger","cat"):7.35,
("physics","chemistry"):7.35,
("money","possession"):7.29,
("jaguar","car"):7.27,
("cup","drink"):7.25,
("psychology","health"):7.23,
("bird","cock"):7.1,
("company","stock"):7.08,
("tiger","carnivore"):7.08,
("doctor","nurse"):7,
("tiger","animal"):7,
("psychology","anxiety"):7,
("money","withdrawal"):6.88,
("drink","eat"):6.87,
("drug","abuse"):6.85,
("tiger","mammal"):6.85,
("psychology","fear"):6.85,
("cup","tableware"):6.85,
("student","professor"):6.81,
("football","basketball"):6.81,
("love","sex"):6.77,
("television","radio"):6.77,
("Arafat","peace"):6.73,
("movie","critic"):6.73,
("psychology","science"):6.71,
("fertility","egg"):6.69,
("bishop","rabbi"):6.69,
("precedent","law"):6.65,
("football","tennis"):6.63,
("professor","doctor"):6.62,
("psychology","clinic"):6.58,
("cup","coffee"):6.58,
("tool","implement"):6.46,
("psychology","doctor"):6.42,
("train","car"):6.31,
("brother","monk"):6.27,
("bread","butter"):6.19,
("movie","popcorn"):6.19,
("precedent","antecedent"):6.04,
("drink","mouth"):5.96,
("cucumber","potato"):5.92,
("king","rook"):5.92,
("cup","liquid"):5.9,
("tiger","zoo"):5.87,
("journey","car"):5.85,
("precedent","example"):5.85,
("smart","stupid"):5.81,
("plane","car"):5.77,
("money","laundering"):5.65,
("tiger","fauna"):5.62,
("psychology","discipline"):5.58,
("alcohol","chemistry"):5.54,
("monk","oracle"):5,
("cup","food"):5,
("space","chemistry"):4.88,
("tiger","organism"):4.77,
("smart","student"):4.62,
("lad","brother"):4.46,
("food","rooster"):4.42,
("coast","hill"):4.38,
("precedent","information"):3.85,
("stock","live"):3.73,
("cup","object"):3.69,
("money","operation"):3.31,
("coast","forest"):3.15,
("shore","woodland"):3.08,
("drink","car"):3.04,
("cup","artifact"):2.92,
("precedent","cognition"):2.81,
("crane","implement"):2.69,
("drink","mother"):2.65,
("Arafat","Jackson"):2.5,
("precedent","collection"):2.5,
("cup","article"):2.4,
("cup","entity"):2.15,
("cemetery","woodland"):2.08,
("glass","magician"):2.08,
("cup","substance"):1.92,
("forest","graveyard"):1.85,
("stock","egg"):1.81,
("precedent","group"):1.77,
("stock","phone"):1.62,
("holy","sex"):1.62,
("stock","CD"):1.31,
("drink","ear"):1.31,
("stock","jaguar"):0.92,
("stock","life"):0.92,
("monk","slave"):0.92,
("lad","wizard"):0.92,
("rooster","voyage"):0.62,
("chord","smile"):0.54,
("noon","string"):0.54,
("professor","cucumber"):0.31,
("king","cabbage"):0.23,
("energy","secretary"):1.81,
("secretary","senate"):5.06,
("energy","laboratory"):5.09,
("computer","laboratory"):6.78,
("weapon","secret"):6.06,
("FBI","fingerprint"):6.94,
("FBI","investigation"):8.31,
("investigation","effort"):4.59,
("Mars","water"):2.94,
("Mars","scientist"):5.63,
("news","report"):8.16,
("canyon","landscape"):7.53,
("image","surface"):4.56,
("discovery","space"):6.34,
("water","seepage"):6.56,
("sign","recess"):2.38,
("Wednesday","news"):2.22,
("mile","kilometer"):8.66,
("computer","news"):4.47,
("territory","surface"):5.34,
("atmosphere","landscape"):3.69,
("president","medal"):3,
("war","troops"):8.13,
("record","number"):6.31,
("skin","eye"):6.22,
("Japanese","American"):6.5,
("theater","history"):3.91,
("volunteer","motto"):2.56,
("prejudice","recognition"):3,
("decoration","valor"):5.63,
("century","year"):7.59,
("century","nation"):3.16,
("delay","racism"):1.19,
("delay","news"):3.31,
("minister","party"):6.63,
("peace","plan"):4.75,
("minority","peace"):3.69,
("attempt","peace"):4.25,
("government","crisis"):6.56,
("deployment","departure"):4.25,
("deployment","withdrawal"):5.88,
("energy","crisis"):5.94,
("announcement","news"):7.56,
("announcement","effort"):2.75,
("stroke","hospital"):7.03,
("disability","death"):5.47,
("victim","emergency"):6.47,
("treatment","recovery"):7.91,
("journal","association"):4.97,
("doctor","personnel"):5,
("doctor","liability"):5.19,
("liability","insurance"):7.03,
("school","center"):3.44,
("reason","hypertension"):2.31,
("reason","criterion"):5.91,
("hundred","percent"):7.38,
("Harvard","Yale"):8.13,
("hospital","infrastructure"):4.63,
("death","row"):5.25,
("death","inmate"):5.03,
("lawyer","evidence"):6.69,
("life","death"):7.88,
("life","term"):4.5,
("word","similarity"):4.75,
("board","recommendation"):4.47,
("governor","interview"):3.25,
("OPEC","country"):5.63,
("peace","atmosphere"):3.69,
("peace","insurance"):2.94,
("territory","kilometer"):5.28,
("travel","activity"):5,
("competition","price"):6.44,
("consumer","confidence"):4.13,
("consumer","energy"):4.75,
("problem","airport"):2.38,
("car","flight"):4.94,
("credit","card"):8.06,
("credit","information"):5.31,
("hotel","reservation"):8.03,
("grocery","money"):5.94,
("registration","arrangement"):6,
("arrangement","accommodation"):5.41,
("month","hotel"):1.81,
("type","kind"):8.97,
("arrival","hotel"):6,
("bed","closet"):6.72,
("closet","clothes"):8,
("situation","conclusion"):4.81,
("situation","isolation"):3.88,
("impartiality","interest"):5.16,
("direction","combination"):2.25,
("street","place"):6.44,
("street","avenue"):8.88,
("street","block"):6.88,
("street","children"):4.94,
("listing","proximity"):2.56,
("listing","category"):6.38,
("cell","phone"):7.81,
("production","hike"):1.75,
("benchmark","index"):4.25,
("media","trading"):3.88,
("media","gain"):2.88,
("dividend","payment"):7.63,
("dividend","calculation"):6.48,
("calculation","computation"):8.44,
("currency","market"):7.5,
("OPEC","oil"):8.59,
("oil","stock"):6.34,
("announcement","production"):3.38,
("announcement","warning"):6,
("profit","warning"):3.88,
("profit","loss"):7.63,
("dollar","yen"):7.78,
("dollar","buck"):9.22,
("dollar","profit"):7.38,
("dollar","loss"):6.09,
("computer","software"):8.5,
("network","hardware"):8.31,
("phone","equipment"):7.13,
("equipment","maker"):5.91,
("luxury","car"):6.47,
("five","month"):3.38,
("report","gain"):3.63,
("investor","earning"):7.13,
("liquid","water"):7.89,
("baseball","season"):5.97,
("game","victory"):7.03,
("game","team"):7.69,
("marathon","sprint"):7.47,
("game","series"):6.19,
("game","defeat"):6.97,
("seven","series"):3.56,
("seafood","sea"):7.47,
("seafood","food"):8.34,
("seafood","lobster"):8.7,
("lobster","food"):7.81,
("lobster","wine"):5.7,
("food","preparation"):6.22,
("video","archive"):6.34,
("start","year"):4.06,
("start","match"):4.47,
("game","round"):5.97,
("boxing","round"):7.61,
("championship","tournament"):8.36,
("fighting","defeating"):7.41,
("line","insurance"):2.69,
("day","summer"):3.94,
("summer","drought"):7.16,
("summer","nature"):5.63,
("day","dawn"):7.53,
("nature","environment"):8.31,
("environment","ecology"):8.81,
("nature","man"):6.25,
("man","woman"):8.3,
("man","governor"):5.25,
("murder","manslaughter"):8.53,
("soap","opera"):7.94,
("opera","performance"):6.88,
("life","lesson"):5.94,
("focus","life"):4.06,
("production","crew"):6.25,
("television","film"):7.72,
("lover","quarrel"):6.19,
("viewer","serial"):2.97,
("possibility","girl"):1.94,
("population","development"):3.75,
("morality","importance"):3.31,
("morality","marriage"):3.69,
("Mexico","Brazil"):7.44,
("gender","equality"):6.41,
("change","attitude"):5.44,
("family","planning"):6.25,
("opera","industry"):2.63,
("sugar","approach"):0.88,
("practice","institution"):3.19,
("ministry","culture"):4.69,
("problem","challenge"):6.75,
("size","prominence"):5.31,
("country","citizen"):7.31,
("planet","people"):5.75,
("development","issue"):3.97,
("experience","music"):3.47,
("music","project"):3.63,
("glass","metal"):5.56,
("aluminum","metal"):7.83,
("chance","credibility"):3.88,
("exhibit","memorabilia"):5.31,
("concert","virtuoso"):6.81,
("rock","jazz"):7.59,
("museum","theater"):7.19,
("observation","architecture"):4.38,
("space","world"):6.53,
("preservation","world"):6.19,
("admission","ticket"):7.69,
("shower","thunderstorm"):6.31,
("shower","flood"):6.03,
("weather","forecast"):8.34,
("disaster","area"):6.25,
("governor","office"):6.34,
("architecture","century"):3.78,
}

#preparar diccionario par alas frecuencias de las palabras
lista_pares_palabras=dataset.keys()
dic_freq_palabras={}

for palabra1,palabra2 in lista_pares_palabras:
    if palabra1 not in dic_freq_palabras:
        dic_freq_palabras[palabra1]=0
    if palabra2 not in dic_freq_palabras:
        dic_freq_palabras[palabra2]=0
lista_palabras_vocabulario_dataset=dic_freq_palabras.keys()

# preparar diccionaro para los conetos de asociaciones de palabras en oraciones
dic_asoc_palabras={}
for palabra1,palabra2 in lista_pares_palabras:
    dic_asoc_palabras[(palabra1,palabra2)]=0

# recorrer el corpus recogiendo estadisticas
url=rufino.WIKIPEDIA_URLS[codigo_ISO]
# mirror alternativo
url="ftp://ftpmirror.your.org/pub/wikimedia/dumps/enwiki/20151002/enwiki-20151002-pages-meta-current.xml.bz2"
contador_palabras=0
contador_articulos=0
contador_oraciones=0
marca_de_tiempo=time.time()
for articulo in rufino.get_articles(url):
    contador_articulos+=1
    if contador_articulos%reportar_cada_x_articulos==0:
        print "\t"+codigo_ISO+"{0} articulos procesados, {1} palabras procesadas, en {2} segundos".format(contador_articulos,contador_palabras,time.time()-marca_de_tiempo)
        marca_de_tiempo=time.time()
    texto=rufino.clean_article(articulo).lower()
    oraciones=rufino.split_sentences(texto)
    contador_oraciones+=len(oraciones)
    for oracion in oraciones:
        palabras_oracion=rufino.split_words(oracion)
        for palabra_dataset in lista_palabras_vocabulario_dataset:
            if palabra_dataset.lower() in palabras_oracion:
                dic_freq_palabras[palabra_dataset]+=1
        
        for palabra1,palabra2 in lista_pares_palabras:
            if (palabra1.lower() in palabras_oracion) and (palabra2.lower() in palabras_oracion):
                dic_asoc_palabras[(palabra1,palabra2)]+=1

        contador_palabras=contador_palabras+len(palabras_oracion)
    if contador_palabras>tamano_corpus:
        break
    
# calcula pmi entre las palabras del dataset
predicciones=[]
gold_standard=[]
for palabra1,palabra2 in lista_pares_palabras:
    P_palabra1=float(dic_freq_palabras[palabra1])/contador_oraciones
    P_palabra2=float(dic_freq_palabras[palabra2])/contador_oraciones
    P_p1yp2=float(dic_asoc_palabras[(palabra1,palabra2)])/contador_oraciones
    if P_palabra1*P_palabra2==0 or P_p1yp2==0:
        pmi=0.0
    else:
        pmi=math.log(P_p1yp2/(P_palabra1*P_palabra2))
    print palabra1,palabra2,pmi,dataset[(palabra1,palabra2)]
    predicciones.append(pmi)
    gold_standard.append(dataset[(palabra1,palabra2)])
    

print "numero de pares en el conjunto de datos:",len(lista_pares_palabras)
print "tamano del vocabulario",len(dic_freq_palabras)
print "Pearson correlation r=",pearsonr(predicciones,gold_standard)
print "Spearman correlation rho=",spearmanr(predicciones,gold_standard)


        


