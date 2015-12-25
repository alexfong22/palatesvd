
import os 
from flask import Flask
from flask import request
from flask import render_template
from flask import request, redirect, url_for
from Util import numb,name,posters
from Numb import numbv
import re
app = Flask(__name__)



import algorithm
algorithm.VERBOSE = True
from recsys.algorithm.factorize import SVD
svd = SVD()
svd.load_data(filename='./ratings1.dat', sep="::", format={'col':0, 'row':1, 'value':2, 'ids': int})
k = 100
svd.compute(k=k, min_values=4, pre_normalize=None, mean_center=True, post_normalize=True, savefile='/tmp/movielens')
from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template('palatelanding.html')
    
    
@app.template_filter('smooth')
def smooth(s):
    return str(s)[2:-2]
@app.template_filter('clip')
def clip(s):
    return str(s).replace("', '",", ").replace("[]","").replace("['","").replace("']","")   


@app.route('/<title>')
def title(title):
    from recsys.algorithm.factorize import SVD
    svd2 = SVD(filename='/tmp/movielens') # Loading already computed SVD model
    
    
    text1 = title.replace("+"," ")
    import re
    
    try:
        arr = []
        posterarr = []
        datak = text1
        v = svd2.similar(int(numb[datak]),n=36)
        for movie in v:
            try:
                posterurl0 = str(posters[str(movie[0])])
            except:
                posterurl0 = ""
            try:
                movtitle1 = str(re.findall("(.*?)\(.*?\)",name[str(movie[0])])[0].rstrip())
                if (len(movtitle1)>34):
                    movtitle1 = str(movtitle1[0:35] + "...")
            except:
                movtitle1 = ""
            try:
                movyear2 = str(re.findall("(.+)(\([0-9]*?\))",name[str(movie[0])])[0][1]).lstrip()
            except:
                movyear2 = ""
            try:
                href3 = str("/" + str(name[str(movie[0])]).replace(" ","+"))
            except:
                href3 = ""
           
            
            
            
            arr.append([[posterurl0],[movtitle1],[movyear2],[href3]])
    except:
        arr = ['---Oops! Insufficient Data---']
    
    
    
    return render_template(
        'nav.html',
        focus = arr[0],
        recs = arr[1:],
        posters = posterarr,
        
        )
        

@app.route('/mypalate')
def my_form():
    return render_template("my-form.html")

@app.route('/mypalate', methods=['POST'])
def recommendgo():
    import re
    humanity = request.form['five']
    sensitivity = request.form['sensitivity']
    text1 = request.form['text1']
    text2 = request.form['text2']
    text3 = request.form['text3']
    text4 = request.form['text4']
    text5 = request.form['text5']
    text6 = request.form['text6']
    text7 = request.form['text7']
    text8 = request.form['text8']
    text9 = request.form['text9']
    text10 = request.form['text10']
    text11 = request.form['text11']
    text12 = request.form['text12']
    text13 = request.form['text13']
    text14 = request.form['text14']
    text15 = request.form['text15']
    text16 = request.form['text16']
    text17 = request.form['text17']
    text18 = request.form['text18']
    text19 = request.form['text19']
    text20 = request.form['text20']
    text21 = request.form['text21']
    text22 = request.form['text22']
    text23 = request.form['text23']
    text24 = request.form['text24']
    text25 = request.form['text25']
    text26 = request.form['text26']
    text27 = request.form['text27']
    text28 = request.form['text28']
    text29 = request.form['text29']
    text30 = request.form['text30']
    
    arrkl = (int(humanity))
    
    a1='-empty-'
    a2='-empty-'
    a3='-empty-'
    a4='-empty-'
    a5='-empty-'
    a6='-empty-'
    a7='-empty-'
    a8='-empty-'
    a9='-empty-'
    a10='-empty-'
    a11='-empty-'
    a12='-empty-'
    a13='-empty-'
    a14='-empty-'
    a15='-empty-'
    
    
    if (arrkl>=2):
        a1 = str(str(numbv(str(text1))[0])+":"+str(text16)+", ")
        
    if (arrkl>=2):
        a2 = str(str(numbv(str(text2))[0])+":"+str(text17)+", ")

    if (arrkl>=2):
        a3 = str(str(numbv(str(text3))[0])+":"+str(text18)+", ")

    if (arrkl>=2):
        a4 = str(str(numbv(str(text4))[0])+":"+str(text19)+", ")

    if (arrkl>=2):
        a5 = str(str(numbv(str(text5))[0])+":"+str(text20)+", ")

    if (arrkl>=2):
        a6 = str(str(numbv(str(text6))[0])+":"+str(text21)+", ")

    if (arrkl>=2):
        a7 = str(str(numbv(str(text7))[0])+":"+str(text22)+", ")

    if (arrkl>=2):
        a8 = str(str(numbv(str(text8))[0])+":"+str(text23)+", ")

    if (arrkl>=2):
        a9 = str(str(numbv(str(text9))[0])+":"+str(text24)+", ")

    if (arrkl>=2):
        a10 = str(str(numbv(str(text10))[0])+":"+str(text25)+", ")

    if (arrkl>=2):
        a11 = str(str(numbv(str(text11))[0])+":"+str(text26)+", ")

    if (arrkl>=2):
        a12 = str(str(numbv(str(text12))[0])+":"+str(text27)+", ")

    if (arrkl>=2):
        a13 = str(str(numbv(str(text13))[0])+":"+str(text28)+", ")

    if (arrkl>=2):
        a14 = str(str(numbv(str(text14))[0])+":"+str(text29)+", ")

    if (arrkl>=2):
        a15 = str(str(numbv(str(text15))[0])+":"+str(text30)+", ")
        
    rawent = re.sub(", +}","}",str("{"+a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+"}").replace("~~~:,",""))
    
    
    rawgood = dict((k, v) for k, v in eval(rawent).items() if v >= 3)
    good = list(rawgood.keys())
    
    
    
    
    
    from recsys.algorithm.factorize import SVD
    svd2 = SVD(filename='/tmp/movielens') # Loading already computed SVD model
    
    
    #text1 = title.replace("+"," ")
    import re
    
    try:
        arr = []
        posterarr = []
        ko = good
        focused = []
        for each in ko:
            
            v = svd2.similar(int(each),n=5)
            for movie in v:
                try:
                    posterurl0 = str(posters[str(movie[0])])
                except:
                    posterurl0 = ""
                try:
                    movtitle1 = str(re.findall("(.*?)\(.*?\)",name[str(movie[0])])[0].rstrip())
                    if (len(movtitle1)>34):
                        movtitle1 = str(movtitle1[0:35] + "...")
                except:
                    movtitle1 = ""
                try:
                    movyear2 = str(re.findall("(.+)(\([0-9]*?\))",name[str(movie[0])])[0][1]).lstrip()
                except:
                    movyear2 = ""
                try:
                    href3 = str("/" + str(name[str(movie[0])]).replace(" ","+"))
                except:
                    href3 = ""
               
            
            
                if movie[0] not in ko:
                    if [[posterurl0],[movtitle1],[movyear2],[href3]] not in arr:
                        arr.append([[posterurl0],[movtitle1],[movyear2],[href3]])
                if movie[0] in ko:
                    focused.append([posterurl0])
    except:
        arr = ['---Oops! Insufficient Data---']
    
    
    
    return render_template(
        'nav.html',
        focus = focused,
        recs = arr,
        posters = posterarr,
        
        )



    
    
    
    
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.debug = True
    app.run()