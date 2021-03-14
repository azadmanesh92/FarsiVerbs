def Verb_Analyzer(text_path):
    
    import re
    f=open('E:\\morph1.txt', "bw")

    mazi=[]
    mozare=[]
    with open('E:\\mazi1.txt',encoding="utf-8")as V_file:
        for line in V_file:
            line = line.replace("\n","")
            line = line.replace("\ufeff","")
            mazi.append(line)
        
    with open('E:\\mozare.txt',encoding="utf-8")as V_file:
        for line in V_file:
            line = line.replace("\n","")
            line = line.replace("\ufeff","")
            mozare.append(line)       
    with open(text_path,encoding="utf-8")as VERB:
        for verb in VERB:
            f.write(verb.encode("UTF-8"))

            verb = verb.replace(" ","")
            verb = verb.replace("‌","")
            verb = verb.replace("\n","")
            verb = verb.replace("\ufeff","")

            for n in mazi:
                if n in verb: 
                    break
            

            P_verbs_mazi={
                r'\bن'+n+r'م':r'\bن +'+n+r' + م',r'\bن'+n+r'ی':r'\bن + '+n+r' + ی',r'\bن'+n+r'\bن':r'\bن'+n+r'\b',
               r'\bن'+n+r'یم':r'\bن +'+n+r' + یم',r'\bن'+n+r'ید':r'\bن'+n+r' + ید',r'\bن'+n+r'ند':r'\bن'+n+r' + ند',
               
               r'\bنمی'+n+r'م':r'\bن + می +  '+n+r' + م',r'\bنمی'+n+r'ی':r'\bن + می +  '+n+r' + ی',r'\bنمی'+n+r'\b':r'\bن + می +  '+n+r'\b',
               r'\bنمی'+n+r'یم':r'\bن + می +  '+n+r' + یم',r'\bنمی'+n+r'ید':r'\bن + می +  '+n+r' + ید',r'\bنمی'+n+r'ند':r'\bن + می +  '+n+r' + ند',

               r'\bن'+n+r'هباش'+r'م':r'\bن + '+n+r' + ه + باش'+r' +م',r'\bن'+n+r'هباش'+r'ی':r'\bن + '+n+r' + ه + باش'+r' +ی',r'\bن'+n+r'هباش'+r'د':r'\bن + '+n+r' + ه + باش'+r'+ د',
               r'\bن'+n+r'هباش'+r'یم':r'\bن + ' +n+r' + ه + باش'+r' +یم',r'\bن'+n+r'هباش'+r'ید':r'\bن + '+n+r' + ه + باش'+r' +ید',r'\bن'+n+r'هباش'+r'ند':r'\bن + '+n+r' + ه + باش'+r'+ ند',

               r'\bن'+n+r'ه'+r'ام':r'\bن + '+n+r' + ه + '+r'ام',r'\bن'+n+r'ه'+r'ای':r'\bن + '+n+r' + ه + '+r'ای',r'\bن'+n+r'ه'+r'است':r'\bن + '+n+r' + ه + '+r'است',
               r'\bن'+n+r'ه'+r'ایم':r'\bن + '+n+r' + ه + '+r'ایم',r'\bن'+n+r'ه'+r'اید':r'\bن + '+n+r' + ه + '+r'اید',r'\bن'+n+r'ه'+r'اند':r'\bن + '+n+r' + ه + '+r'اند',         

               r'\bن'+n+r'هبود'+r'م':r'\bن + '+n+r' + ه + بود +'+r'م',r'\bن'+n+r'هبود'+r'ی':r'\bن + '+n+r' + ه + بود +'+r'ی',r'\bن'+n+r'هبود'+r'\b':r'\bن + '+n+r' + ه + بود +'+r'\b',
               r'\bن'+n+r'هبود'+r'یم':r'\bن + '+n+r' + ه + بود +'+r'یم',r'\bن'+n+r'هبود'+r'ید':r'\bن + '+n+r' + ه + بود +'+r'ید',r'\bن'+n+r'هبود'+r'ند':r'\bن + '+n+r' + ه + بود +'+r'ند',

               r'\b'+n+r'م':r'\b'+n+r' + م',r'\b'+n+r'ی':r'\b'+n+r' + ی',r'\b'+n+r'\b':r'\b'+n+r'\b',
               r'\b'+n+r'یم':r'\b'+n+r' + یم',r'\b'+n+r'ید':r'\b'+n+r' + ید',r'\b'+n+r'ند':r'\b'+n+r' + ند',
               
               r'\bمی'+n+r'م':r'\bمی + '+n+r' + م',r'\bمی'+n+r'ی':r'\bمی + '+n+r' + ی',r'\bمی'+n+r'\b':r'\bمی +'+n+r'\b',
               r'\bمی'+n+r'یم':r'\bمی + '+n+r' + یم',r'\bمی'+n+r'ید':r'\bمی + '+n+r' + ید',r'\bمی'+n+r'ند':r'\bمی + '+n+r' + ند',

               r'\b'+n+r'هباش'+r'م':r'\b'+n+r' + ه + باش'+r' +م',r'\b'+n+r'هباش'+r'ی':r'\b'+n+r' + ه + باش'+r' +ی',r'\b'+n+r'هباش'+r'د':r'\b'+n+r' + ه + باش'+r'+ د',
               r'\b'+n+r'هباش'+r'یم':r'\b'+n+r' + ه + باش'+r' +یم',r'\b'+n+r'هباش'+r'ید':r'\b'+n+r' + ه + باش'+r' +ید',r'\b'+n+r'هباش'+r'ند':r'\b'+n+r' + ه + باش'+r'+ ند',

               r'\b'+n+r'ه'+r'ام':r'\b'+n+r' + ه + '+r'ام',r'\b'+n+r'ه'+r'ای':r'\b'+n+r' + ه + '+r'ای',r'\b'+n+r'ه'+r'است':r'\b'+n+r' + ه + '+r'است',
               r'\b'+n+r'ه'+r'ایم':r'\b'+n+r' + ه + '+r'ایم',r'\b'+n+r'ه'+r'اید':r'\b'+n+r' + ه + '+r'اید',r'\b'+n+r'ه'+r'اند':r'\b'+n+r' + ه + '+r'اند',         

               r'\b'+n+r'هبود'+r'م':r'\b'+n+r' + ه + بود +'+r'م',r'\b'+n+r'هبود'+r'ی':r'\b'+n+r' + ه + بود +'+r'ی',r'\b'+n+r'هبود'+r'\b':r'\b'+n+r' + ه + بود +'+r'\b',
               r'\b'+n+r'هبود'+r'یم':r'\b'+n+r' + ه + بود +'+r'یم',r'\b'+n+r'هبود'+r'ید':r'\b'+n+r' + ه + بود +'+r'ید',r'\b'+n+r'هبود'+r'ند':r'\b'+n+r' + ه + بود +'+r'ند' }              
              
            P_verbs_ayande={
               r'\bخواه'+r'م'+n+r'\b':r'\bخواه '+r' + م + '+n+r'\b',r'\bخواه'+r'ی'+n+r'\b':r'\bخواه '+r' + ی + '+n+r'\b',r'\bخواه'+r'د'+n+r'\b':r'\bخواه '+r' + د + '+n+r'\b',
               r'\bخواه'+r'یم'+n+r'\b':r'\bخواه '+r' + یم + '+n+r'\b',r'\bخواه'+r'ید'+n+r'\b':r'\bخواه '+r' + ید + '+n+r'\b',r'\bخواه'+r'ند'+n+r'\b':r'\bخواه '+r' + ند + '+n+r'\b',

               r'\bنخواه'+r'م'+n+r'\b':r'\bن + خواه '+r' + م + '+n+r'\b',r'\bنخواه'+r'ی'+n+r'\b':r'\bن + خواه '+r' + ی + '+n+r'\b',r'\bنخواه'+r'د'+n+r'\b':r'\bن + خواه '+r' + د + '+n+r'\b',
               r'\bنخواه'+r'یم'+n+r'\b':r'\bن + خواه '+r' + یم + '+n+r'\b',r'\bنخواه'+r'ید'+n+r'\b':r'\bن + خواه '+r' + ید + '+n+r'\b',r'\bنخواه'+r'ند'+n+r'\b':r'\bن + خواه '+r' + ند + '+n+r'\b'}

            for x in P_verbs_mazi.keys():
                if re.match(x,verb):
                    pattern_mazi=P_verbs_mazi[x]
                    analyse=re.sub(x,pattern_mazi,verb)+'\n'
                    f.write("«ماضی»".encode("UTF-8"))
                    f.write(analyse.encode("UTF-8"))
                    break

            for x in P_verbs_ayande.keys():
                if re.match(x,verb):
                    pattern_ayande=P_verbs_ayande[x]
                    analyse=re.sub(x,pattern_ayande,verb)+'\n'
                    f.write("«آینده»".encode("UTF-8"))
                    f.write(analyse.encode("UTF-8"))
                    break 


            for n in mozare:
                if n in verb:
                    break   


            P_verbs_mozare={
               r'\b'+n+r'م'+r'\b':r'\b'+n+r' + م'+r'\b',r'\b'+n+r'ی'+r'\b':r'\b'+n+r' + ی'+r'\b',r'\b'+n+r' + د'+r'\b'+r'\b':r'\b'+n+r' + د'+r'\b'+r'\b',
               r'\b'+n+r'یم'+r'\b':r'\b'+n+r' + یم'+r'\b',r'\b'+n+r'ید'+r'\b':r'\b'+n+r' + ید'+r'\b',r'\b'+n+r'ند'+r'\b':r'\b'+n+r' + ند'+r'\b',

               r'\bمی'+n+r'م'+r'\b':r'\bمی + '+n+r' + م'+r'\b',r'\bمی'+n+r'ی'+r'\b':r'\bمی + '+n+r' + ی'+r'\b',r'\bمی'+n+r' + د'+r'\b'+r'\b':r'\bمی +'+n+r' + د'+r'\b'+r'\b',
               r'\bمی'+n+r'یم'+r'\b':r'\bمی + '+n+r' + یم'+r'\b',r'\bمی'+n+r'ید'+r'\b':r'\bمی + '+n+r' + ید'+r'\b',r'\bمی'+n+r'ند'+r'\b':r'\bمی + '+n+r' + ند'+r'\b',

               r'\bب'+n+r'م'+r'\b':r'\bب + '+n+r' + م'+r'\b',r'\bب'+n+r'ی'+r'\b':r'\bب + '+n+r' + ی'+r'\b',r'\bب'+n+r' + د'+r'\b'+r'\b':r'\bب +'+n+r' + د'+r'\b'+r'\b',
               r'\bب'+n+r'یم'+r'\b':r'\bب + '+n+r' + یم'+r'\b',r'\bب'+n+r'ید'+r'\b':r'\bب + '+n+r' + ید'+r'\b',r'\bب'+n+r'ند'+r'\b':r'\bب + '+n+r' + ند'+r'\b',

               r'\bن'+n+r'م'+r'\b':r'\bن +'+n+r' + م'+r'\b',r'\bن'+n+r'ی'+r'\b':r'\bن + '+n+r' + ی'+r'\b',r'\bن'+n+r' + د'+r'\b'+r'\b':r'\bن'+n+r' + د'+r'\b'+r'\b',
               r'\bن'+n+r'یم'+r'\b':r'\bن +'+n+r' + یم'+r'\b',r'\bن'+n+r'ید'+r'\b':r'\bن'+n+r' + ید'+r'\b',r'\bن'+n+r'ند'+r'\b':r'\bن'+n+r' + ند'+r'\b',
               
               r'\bنمی'+n+r'م'+r'\b':r'\bن + می +  '+n+r' + م'+r'\b',r'\bنمی'+n+r'ی'+r'\b':r'\bن + می +  '+n+r' + ی'+r'\b',r'\bنمی'+n+r' + د'+r'\b'+r'\b':r'\bن + می +  '+n+r' + د'+r'\b'+r'\b',
               r'\bنمی'+n+r'یم'+r'\b':r'\bن + می +  '+n+r' + یم'+r'\b',r'\bنمی'+n+r'ید'+r'\b':r'\bن + می +  '+n+r' + ید'+r'\b',r'\bنمی'+n+r'ند'+r'\b':r'\bن + می +  '+n+r' + ند'}

            P_verbs_amri={r'\bب'+n+r'\b':r'\bب + '+n+r'\b',r'\bن'+n+r'\b':r'\bن +'+n+r'\b'}



            for x in P_verbs_mozare.keys():
                if re.match(x,verb):
                    pattern_mozare=P_verbs_mozare[x]
                    analyse=re.sub(x,pattern_mozare,verb)+'\n'
                    f.write("«مضارع»".encode("UTF-8"))
                    f.write(analyse.encode("UTF-8"))
                    break



            for x in P_verbs_amri.keys():
                if re.match(x,verb):
                    pattern_amri=P_verbs_amri[x]
                    analyse=re.sub(x,pattern_amri,verb)+'\n'
                    f.write("«امر»".encode("UTF-8"))
                    f.write(analyse.encode("UTF-8"))
                    break

        f.close()

Verb_Analyzer('E:\\Verbs1.txt')
  
