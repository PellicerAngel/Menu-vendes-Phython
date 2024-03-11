#Angel Pellicer Grau 

# Llistes
noms = [] 

preus = []

qVenudes = []



final_programa = False

while final_programa == False:

    print(" ")
    print("- 1. Introduir un article nou ")
    print(" ")
    print("- 2. Fer una venda ")
    print(" ")
    print("- 3. Mostrar informacio ")
    print(" ")
    print("- 4. Esborrar un article ")
    print(" ")
    print("- 5. Esborrar tots els articles ")
    print(" ")
    print("- 6. Eixir ")
    print(" ")

    opcio = int(input("Quina opcio vols? "))
    print(" ")

    #es crea un controlador de errors

    while opcio < 1 or opcio > 6 :
        opcio = int(input("Tornam a dir l'opcio que vols fer, perfa :3"))


        
    #Be

    if opcio == 1:
        print("Estas en l'introduccio d'articles nous")
        print(" ")
        noms.append(input("Disme el nom del article nou que vols introduir:  "))
        print(" ")
        preus.append(int(input("Disme el preu que va a tindre el article introduit:  ")))
        print("")
        qVenudes.append(0)





        
    elif opcio == 2:
        article_existix = False
        numero_ventes = 0
        print("Estas en l'opcio de fer una venda")
        print(" ")
        nom_ventes = input("Disme el nom d'article que ha fet la venda: ")
        print(" ")

        for i in range (0,len(noms)): 
                
            if nom_ventes == noms[i]:
                article_existix = True
                numero_ventes = int(input("Disme la quantitat de vendes que ha tingut este producte:   "))
                print(" ")
                qVenudes[i] = qVenudes[i] + numero_ventes
                    
                  
            else:
                article_existix = False

        if article_existix == False:
            print("Error, el article indicat no existix.    ")


    #Ns que falla 
                   
    elif opcio == 3:
        print("Estas en l'opcio de mostrar informacio")
        print(" ")

        tabla_inversa = False
        

        opcio_de_taula = input("Vols mostrar l'informacio a l'inversa ? (indica en una s o S)")
        print(" ")

        if opcio_de_taula == "s" or opcio_de_taula == "S":

            tabla_inversa = True


        if tabla_inversa == True :
            article_mes_venut = "Cap"
            mes_venut = 0
            total = 0
            article_mes_ingresos = "Cap"
            total_article_mes_ingresos = 0
            print("NOM      QUANT       PREU        IMPORT")
            print(" ")
            for i in range (len(noms)-1,-1,-1):
                import_preu = preus[i] * qVenudes[i] 
                print(noms[i],"        ",qVenudes[i],"        ",preus[i],"        ",import_preu)
                print(" ")
                total = total + import_preu
                if qVenudes[i] > mes_venut:
                    article_mes_venut = noms[i]
                    mes_venut = qVenudes[i] 

                if import_preu > total_article_mes_ingresos:
                    article_mes_ingresos = noms[i]
                    total_article_mes_ingresos= import_preu   

            print("                                    Total :   " , total)
            print(" ")
            print("Article mes venut : ",article_mes_venut , " amb ",mes_venut , " unitats")
            print(" ")
            print("Article amb mes ingresos : ", article_mes_ingresos, " amb ", total_article_mes_ingresos, " euros")

        else:

            article_mes_venut = "Cap"
            mes_venut = 0
            total = 0
            article_mes_ingresos = "Cap"
            total_article_mes_ingresos = 0
            print("NOM      QUANT       PREU        IMPORT")
            print(" ")
            for i in range (0,len(noms)):
                import_preu = preus[i] * qVenudes[i] 
                print(noms[i],"        ",qVenudes[i],"        ",preus[i],"        ",import_preu)
                print(" ")
                total = total + import_preu
                if qVenudes[i] > mes_venut:
                    article_mes_venut = noms[i]
                    mes_venut = qVenudes[i]            
                if import_preu > total_article_mes_ingresos:
                    article_mes_ingresos = noms[i]
                    total_article_mes_ingresos= import_preu       
            print("                                    Total :   " , total)
            print(" ")
            print("Article mes venut : ",article_mes_venut , " amb ",mes_venut , " unitats")
            print(" ")
            print("Article amb mes ingresos : ", article_mes_ingresos, " amb ", total_article_mes_ingresos, " euros")

        


    #Be
    elif opcio == 4:
        article_borrar = "Cap"
        podem_borrar = False

        print("Estas en l'opcio de borrar un article:   ")
        print(" ")
        article_borrar = input("Disme el article que vols esborrar:    ")
        print(" ")

        for i in range (len(noms)):

            if article_borrar ==noms[i]:
                podem_borrar = True
                posicio_borrar = i

            
        if podem_borrar == True:
            noms.pop(posicio_borrar)
            preus.pop(posicio_borrar)
            qVenudes.pop(posicio_borrar)

            print("Article esborrat ")
        else:
            print("Article no trobat")

        
    #Be
    elif opcio == 5:
        print("Estas en l'opcio de borrar tots els articles: ")

        noms.clear()
        preus.clear()
        qVenudes.clear()
        

    #Be
    elif opcio == 6:
        tancar_programa = input("Estas segur de que vols ixir s/n")

        if tancar_programa == "s" or tancar_programa == "S":
            final_programa = True
        else:
            final_programa = False

   
print(" ")
print("Adeu, i gracies per gastar la nostra aplicacio de vendes")



