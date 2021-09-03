# coding=utf-8
from flask import Flask,render_template,send_from_directory,send_file,jsonify,request,redirect,url_for,session,flash,abort,g
import os
from db import *
from zip_functions import *

app = Flask(__name__,template_folder='./templates',static_folder='./templates/static',)

ip_ban_list=[]

app.secret_key = 'dwjkisfsdlkjfsldfjk##%&/!hvd)(()==[]&$'


f = open("ip_ban_list.txt", "r")
for x in f:
    ip_ban_list.append(x)

print(f' * BANNED IPS:{ip_ban_list}')


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        if db_operations(str(session['user_id']),str(session['user_pass'])).verify_user() == True:
            user =session['user_id']
            g.user = user
 



@app.before_request
def block_method():
    ip = request.environ.get('REMOTE_ADDR')
    f = open("ip_ban_list.txt", "r")
    ip_ban_list=[]
    for x in f:
      ip_ban_list.append(x)
    if ip in ip_ban_list:
        print(f'O IP BANIDO {ip} TENTOU ACESSAR')
        abort(403)
    else:
        print(f'REQUEST RECEBIDO DO IP: {ip}')


@app.route('/<other>')
def other(other):
        return render_template('paginas/404.html')


#################home page######################################
@app.route('/')
def index_page():
    if not g.user:
        return redirect(url_for('login'))
    else:
        lista=[]
        main_list_pastas=[]
        main_list_ficheiros=[]
        main_=os.listdir('./files')
        for pasta in main_:
            lista=[]
            for pasta_ in os.listdir('./files/'+pasta):
                lista.append(pasta_)
            main_list_pastas.append(pasta)
            main_list_ficheiros.append(lista)
        return render_template('paginas/home.html',pastas=(main_list_pastas,main_list_ficheiros),len_pastas=len(main_list_pastas),len_ficheiros=len(main_list_ficheiros))
###################################################################

#################home page-category######################################
@app.route('/main/<categoria>')
def index_page_cat(categoria):
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        lista=[]
        main_list_pastas=[]
        main_list_ficheiros=[]
        main_=os.listdir(f'./files/{categoria}')
        for pasta in main_:
            lista=[]
            for pasta_ in os.listdir(f'./files/{categoria}/'+pasta):
                lista.append(pasta_)
            main_list_pastas.append(pasta)
            main_list_ficheiros.append(lista)
        return render_template('paginas/home _categoria.html',pastas=(main_list_pastas,main_list_ficheiros),len_pastas=len(main_list_pastas),len_ficheiros=len(main_list_ficheiros))
###################################################################




##################upload route #page render#################
@app.route('/upload/<f_id>/<folder_id>', methods=['GET'])
def main_page3(f_id='main',folder_id='main'):
    pasta_main=os.listdir(f'./files/{f_id}')#lista das pastas do diretorio principal
    pastas_list=[]
    print(pasta_main)
    for pastas in pasta_main:
        if os.path.isdir(os.path.join(f'./files/{f_id}', pastas)):
            pastas_list.append(pastas)

    if str(folder_id) in pastas_list or f_id=='main':
        return render_template('paginas/index.html')
    else:
       return render_template('paginas/404.html', title = '404'), 404
#####################################################################


###################route to send files######################
@app.route('/upload/<f1_id>/<folder_id>', methods=['POST'])
def upload_file(f1_id='main',folder_id='main'):
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(f'./files/{f1_id}/{folder_id}/'+uploaded_file.filename)
    return render_template('paginas/index.html')
######################################################################


########################view files (json)######################
@app.route('/files/<folder_id>')
def files_list(folder_id):
    ficheiros=os.listdir('./files')
    if folder_id =='main':
        return jsonify(filelist=ficheiros)#retorn a file list in json
    elif folder_id in ficheiros:
        ficheiros_pasta=os.listdir('./files/'+folder_id)
        return jsonify(filelist=ficheiros_pasta)
    else:
        return render_template('paginas/404.html', title = '404'), 404
######################################################################
@app.route('/file_list')
def list_all_files():
    lista=[]
    main_list=[]
    main_=os.listdir('./files')
    for pasta in main_:
        lista=[]
        for pasta_ in os.listdir('./files/'+pasta):
            lista.append(pasta_)
        main_list.append({'nome_pasta':pasta,'lista':lista})
    return jsonify(filelist=main_list)
#######################################################################


###################Login (page render)#############################
@app.route('/login', methods=['GET'])
def login():
    return render_template('paginas/login.html')
########################################################################

##################Login (POST ROUT)################################
@app.route('/login', methods=['POST'])
def make_login():
    print(request.form)
    session.pop('user_id', None)
    if db_operations(str(request.form['User']),str(request.form['Password'])).verify_user() == True:
        session['user_id']=request.form['User']
        session['user_pass']=request.form['Password']
        session['logged_in'] = True
        return redirect('/')
    else:
        #print('erro')
        flash('Pass/User Errados!!')
        return render_template('paginas/login.html')
        #return 'erro'#todo fazer pagina de erro
########################################################################


###########Rota de log-out##############################################
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect('/login')
########################################################################


@app.route("/get/<folder_id>/<folder1_id>/<file_id>")
def get_file(folder_id,folder1_id,file_id):
    # print(file_id)
    # print(folder_id)
    try:
        if folder_id=='main':
            filename = file_id
            return send_from_directory(directory='./files',filename=file_id, as_attachment=True)
        else:
            return send_from_directory(directory=f'./files/{folder_id}/{folder1_id}',path=file_id, as_attachment=True)
            print(file_id)
    except FileNotFoundError:#if file dont exist
        abort(404)

@app.route("/get/zip/<folder_id>")
def test(folder_id):
    zip_files().writezip(folder_id)
    return send_from_directory(directory='./temp',path=f'{folder_id}.zip', as_attachment=True)
    os.remove(f'./temp/{folder_id}.zip')
    print('files removed')





#create folder
@app.route("/create/<folder_name>")
def create_folder(folder_name):
    path="./files/"+folder_name
    pasta_main=os.listdir('./files')
    if folder_name not in pasta_main:#verify if the folder exists
        try:
            os.mkdir(path)#make a folder
            return render_template('paginas/404.html', title = '404'), 404 ##TODO make sucess page
        except OSError:
            return render_template('paginas/404.html', title = '404'), 404 ##TODO error page
    else:
        return render_template('paginas/404.html', title = '404'), 404 ##TODO error page


# create sub-folder
@app.route("/main/<cat>/create/<folder_name>")
def create_cat(cat,folder_name):
    path=f"./files/{cat}/{folder_name}"
    pasta_main=os.listdir(f'./files/{cat}')
    if folder_name not in pasta_main:#verify if the folder exists
        try:
            os.mkdir(path)##make a folder
            return render_template('paginas/404.html', title = '404'), 404 ##TODO make sucess page
        except OSError:
            return render_template('paginas/404.html', title = '404'), 404 ##TODO error page
    else:
        return render_template('paginas/404.html', title = '404'), 404 ##TODO error page




#main loop
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0',debug = True,port=6969)
