from flask import Flask, render_template, request, redirect, url_for
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from io import BytesIO
import base64
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph1')
def graph1():
    # Cargamos los datos
    df=pd.read_csv('graph1/Mescontagio2020.csv')

    #aqui obtengo los valores de los parametros para personalizar la grafica
    color = request.args.get('color', 'orange')
    plot_type = request.args.get('plot_type', 'line')
    zoom = float(request.args.get('zoom', '1'))

    #personalizamos la grafica con los paramentros obtenidos previamente
    if plot_type == 'line':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.lineplot(x="Mes",y="Ncontagios",data=df, color=color)
        plt.title("Contagios covid en 2020")
        plt.xlabel("Mes")
        plt.ylabel("Ncontagios")
        plt.ylim(0, df['Ncontagios'].max()*zoom)
        plt.tight_layout() #esto es para ajustar automaticamente el espacio entre los elementos de la grafica
    elif plot_type == 'scatter':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.scatterplot(x="Mes",y="Ncontagios",data=df, color=color)
        plt.title("Contagios covid en 2020")
        plt.xlabel("Mes")
        plt.ylabel("Ncontagios")
        plt.ylim(0, df['Ncontagios'].max()*zoom)
        plt.tight_layout()
    elif plot_type == 'bar':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.barplot(x="Mes",y="Ncontagios",data=df, color=color)
        plt.title("Contagios covid en 2020")
        plt.xlabel("Mes")
        plt.ylabel("Ncontagios")
        plt.ylim(0, df['Ncontagios'].max()*zoom)
        plt.tight_layout()
    else:
        return "Tipo de gráfica no soportada"
    #pasamos la grafica a una imagen png
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    plt.close()
    #codificamos la imagen en base64 y usando flask lo mostramos en la plantilla html
    tmpfile.seek(0)
    plot_url = base64.b64encode(tmpfile.getvalue()).decode('utf8')
    return render_template('graph1.html', plot_url=plot_url)

@app.route('/graph11')
def graph11():
    # Cargar los datos
    df=pd.read_csv('graph1/Mescontagio2021.csv')
    #aqui obtengo los valores de los parametros para personalizar la grafica
    color = request.args.get('color', 'orange')
    plot_type = request.args.get('plot_type', 'line')
    zoom = float(request.args.get('zoom', '1'))
    #personalizamos la grafica con los paramentros obtenidos previamente
    if plot_type == 'line':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.lineplot(x="Mes",y="Ncontagios",data=df, color=color)
        plt.title("Contagios covid en 2021")
        plt.xlabel("Mes")
        plt.ylabel("Ncontagios")
        plt.ylim(0, df['Ncontagios'].max()*zoom)
        plt.tight_layout()
    elif plot_type == 'scatter':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.scatterplot(x="Mes",y="Ncontagios",data=df, color=color)
        plt.title("Contagios covid en 2021")
        plt.xlabel("Mes")
        plt.ylabel("Ncontagios")
        plt.ylim(0, df['Ncontagios'].max()*zoom)
        plt.tight_layout()
    elif plot_type == 'bar':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.barplot(x="Mes",y="Ncontagios",data=df, color=color)
        plt.title("Contagios covid en 2021")
        plt.xlabel("Mes")
        plt.ylabel("Ncontagios")
        plt.ylim(0, df['Ncontagios'].max()*zoom)
        plt.tight_layout()
    else:
        return "Tipo de gráfica no soportada"
     #pasamos la grafica a una imagen png
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    plt.close()
    #codificamos la imagen en base64 y usando flask lo mostramos en la plantilla html
    tmpfile.seek(0)
    plot_url = base64.b64encode(tmpfile.getvalue()).decode('utf8')
    return render_template('graph1.html', plot_url=plot_url)

@app.route('/graph12')
def graph12():
    # Lógica para Graph12
    df = pd.read_csv('graph1/MesMuertes2020.csv')
    #aqui obtengo los valores de los parametros para personalizar la grafica
    color = request.args.get('color', 'red')
    plot_type = request.args.get('plot_type', 'line')
    zoom = float(request.args.get('zoom', '1'))
    palette = request.args.get('palette', 'Set2')
    #personalizamos la grafica con los paramentros obtenidos previamente
    if plot_type == 'bar':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.barplot(data=df, x='Mes', y='Ncontagio', color=color)
        plt.title('Muertes por covid en 2020')
        plt.ylim(0, df['Ncontagio'].max()*zoom)
        plt.xlabel('Mes')
        plt.ylabel('Nmuertes')
        plt.tight_layout()
    elif plot_type == 'line':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.lineplot(data=df, x='Mes', y='Ncontagio', color=color)
        plt.title('Muertes por covid en 2020')
        plt.ylim(0, df['Ncontagio'].max()*zoom)
        plt.xlabel('Mes')
        plt.ylabel('Nmuertes')
        plt.tight_layout()
    elif plot_type == 'scatter':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x="Mes",y="Ncontagio", color=color)
        plt.title("Muertes por covid en 2020")
        plt.ylim(0, df['Ncontagio'].max()*zoom)
        plt.xlabel('Mes')
        plt.ylabel('Nmuertes')
        plt.tight_layout()
    else:
        return "Tipo de gráfica no soportada"
     #pasamos la grafica a una imagen png
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    plt.close()
    #codificamos la imagen en base64 y usando flask lo mostramos en la plantilla html
    tmpfile.seek(0)
    plot_url = base64.b64encode(tmpfile.getvalue()).decode('utf8')
    return render_template('graph1.html', plot_url=plot_url)

@app.route('/graph13')
def graph13():
    # Lógica para Graph12
    df = pd.read_csv('graph1/MesMuertes2021.csv')
    #aqui obtengo los valores de los parametros para personalizar la grafica
    color = request.args.get('color', 'red')
    plot_type = request.args.get('plot_type', 'line')
    zoom = float(request.args.get('zoom', '1'))
    palette = request.args.get('palette', 'Set2')
   #personalizamos la grafica con los paramentros obtenidos previamente
    if plot_type == 'bar':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.barplot(data=df, x='Mes', y='Ncontagio', color=color)
        plt.title('Muertes por covid en 2021')
        plt.ylim(0, df['Ncontagio'].max()*zoom)
        plt.xlabel('Mes')
        plt.ylabel('Nmuertes')
        plt.tight_layout()
    elif plot_type == 'line':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.lineplot(data=df, x='Mes', y='Ncontagio', color=color)
        plt.title('Muertes por covid en 2021')
        plt.ylim(0, df['Ncontagio'].max()*zoom)
        plt.xlabel('Mes')
        plt.ylabel('Nmuertes')
        plt.tight_layout()
    elif plot_type == 'scatter':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x="Mes",y="Ncontagio", color=color)
        plt.title("Muertes por covid en 2021")
        plt.ylim(0, df['Ncontagio'].max()*zoom)
        plt.xlabel('Mes')
        plt.ylabel('Nmuertes')
        plt.tight_layout()
    else:
        return "Tipo de gráfica no soportada"
     #pasamos la grafica a una imagen png
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    plt.close()
    #codificamos la imagen en base64 y usando flask lo mostramos en la plantilla html
    tmpfile.seek(0)
    plot_url = base64.b64encode(tmpfile.getvalue()).decode('utf8')
    return render_template('graph1.html', plot_url=plot_url)

@app.route('/graph2')
def graph2():
    # Lógica para Graph2
    df=pd.read_csv('graph2/edadpaciente.csv')
    #aqui obtengo los valores de los parametros para personalizar la grafica
    color = request.args.get('color', 'blue')
    plot_type = request.args.get('plot_type', 'box')
    zoom = float(request.args.get('zoom', '1'))
    palette = request.args.get('palette', 'Set2')
    #personalizamos la grafica con los paramentros obtenidos previamente
    if plot_type == 'box':
        sns.boxplot(data=df,y='edad', color=color)
        plt.title('Edad promedio de los pacientes contagiados por covid')
        plt.ylim(0, df['edad'].max()*zoom)
        plt.tight_layout()
    elif plot_type == 'hist':
        sns.histplot(data=df, x='edad', color=color)
        plt.title('Distribución de la edad de los pacientes contagiados')
        plt.xlim(0, df['edad'].max()*zoom)
        plt.tight_layout()

    else:
        return "Tipo de gráfica no soportada"

     #pasamos la grafica a una imagen png
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    plt.close()

    #codificamos la imagen en base64 y usando flask lo mostramos en la plantilla html
    tmpfile.seek(0)
    plot_url = base64.b64encode(tmpfile.getvalue()).decode('utf8')
    return render_template('graph2.html', plot_url=plot_url, color=color, plot_type=plot_type, zoom=zoom, palette=palette)


@app.route('/graph21')
def graph21():
    # Lógica para la gráfica
    df=pd.read_csv('graph2/EdadPacienteContagiadosGenero.csv')
    sns.boxplot(data=df,y='edad',x='sexo')
    plt.title("Edad promedio de los pacientes contagiados por covid de acuerdo al género")
    
    #aqui obtengo los valores de los parametros para personalizar la grafica
    color = request.args.get('color', 'blue')
    plot_type = request.args.get('plot_type', 'box')
    zoom = float(request.args.get('zoom', '1'))
    palette = request.args.get('palette', 'Set2')
    #personalizamos la grafica con los paramentros obtenidos previamente
    if plot_type == 'box':
        sns.boxplot(data=df,y='edad',x='sexo', color=color)
        plt.title("Edad promedio de los pacientes contagiados por covid de acuerdo al género")
        plt.ylim(0, df['edad'].max()*zoom)
        plt.tight_layout()
    else:
        return "Tipo de gráfica no soportada"

     #pasamos la grafica a una imagen png
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    plt.close()

    #codificamos la imagen en base64 y usando flask lo mostramos en la plantilla html
    tmpfile.seek(0)
    plot_url = base64.b64encode(tmpfile.getvalue()).decode('utf8')
    return render_template('graph2.html', plot_url=plot_url)


@app.route('/graph22')
def graph22():
    df = pd.read_csv('graph2/EdadPacienteMuertesGenero.csv')
    sns.set_style('whitegrid')
    sns.boxplot(data=df, y='edad', x='sexo', palette=['#F8766D', '#00BFC4'])
    plt.title("Edad de los pacientes fallecidos por covid por género")
    plt.xlabel("Género")
    plt.ylabel("Edad")
    plt.tight_layout() 
     #pasamos la grafica a una imagen png
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    plt.close()
    # Renderiza el archivo HTML que mostrará la gráfica
    tmpfile.seek(0)
    plot_url = base64.b64encode(tmpfile.getvalue()).decode('utf8')
    return render_template('graph2.html', plot_url=plot_url)

@app.route('/graph3')
def graph3():
    df = pd.read_csv('graph3/Departamentos.csv')
    #aqui obtengo los valores de los parametros para personalizar la grafica
    plot_type = request.args.get('plot_type', 'bar')
    color = request.args.get('color', 'blue')
    zoom = float(request.args.get('zoom', '1'))
    colors = sns.color_palette("Set3")
    #personalizamos la grafica con los paramentros obtenidos previamente
    if plot_type == 'bar':
        plt.figure(figsize=(10, 7))
        yr = sns.barplot(data=df, y='Departamento', x='NumeroContagios', color=color, palette=colors)
        yr.set_xticklabels(yr.get_xticklabels(), size=8)
        for p in yr.containers:
            plt.bar_label(p, label_type='edge', fontsize=8, padding=2)
    elif plot_type == 'line':
        plt.figure(figsize=(10, 7))
        yr = sns.lineplot(data=df, x='NumeroContagios', y='Departamento', color=color)
    elif plot_type == 'box':
        #plt.figure(figsize=(10, 7))
        yr = sns.boxplot(data=df, x='NumeroContagios', color=color)
        yr.annotate('Promedio de contagios: {:.2f}'.format(df['NumeroContagios'].mean()), 
                    xy=(0.5, 0.9), xycoords='axes fraction', fontsize=12, ha='center')
    else:
        return "Error: Tipo de gráfica no válido"
    plt.title('Número de contagios por departamento', fontsize=12)
    plt.xlabel('Número de contagios', fontsize=10)
    plt.ylabel('Departamento', fontsize=10)
    plt.tight_layout()
    plt.xlim(0, df['NumeroContagios'].max()*zoom)
     #pasamos la grafica a una imagen png
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    plt.close()
    #codificamos la imagen en base64 y usando flask lo mostramos en la plantilla html
    tmpfile.seek(0)
    plot_url = base64.b64encode(tmpfile.getvalue()).decode('utf8')
    return render_template('graph3.html', plot_url=plot_url)



@app.route('/graph4')
def graph4():
    df1=pd.read_csv('graph3/Barranquilla.csv')
    df2=pd.read_csv('graph3/cartagenas.csv')
    df3=pd.read_csv('graph3/Santa Marta.csv')
    df4=pd.read_csv('graph3/Bogota.csv')
    dft=pd.concat([df1,df2,df3,df4])
    
    #aqui obtengo los valores de los parametros para personalizar la grafica
    color = request.args.get('color', 'blue')
    plot_type = request.args.get('plot_type', 'bar')
    zoom = float(request.args.get('zoom', '1'))
    palette = request.args.get('palette', 'Set2')

    #personalizamos la grafica con los paramentros obtenidos previamente
    if plot_type == 'bar':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.barplot(data=dft, x='Municipio', y='Ncontagios', color=color)
        plt.title('NContagios en algunos municipios importantes')
        plt.ylim(0, dft['Ncontagios'].max()*zoom)
        plt.xticks(rotation=90)
        ax.set_xlabel('')
        ax.set_ylabel('NContagios')
        plt.tight_layout()

    elif plot_type == 'line':
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        sns.lineplot(data=dft, x='Municipio', y='Ncontagios', color=color)
        plt.title('NContagios en algunos municipios importantes')
        plt.ylim(0, dft['Ncontagios'].max()*zoom)
        plt.xticks(rotation=90)
        ax.set_xlabel('')
        ax.set_ylabel('NContagios')
        plt.tight_layout()

    elif plot_type == 'pie':
        fig, ax = plt.subplots()
        data = dft.groupby('Municipio')['Ncontagios'].sum()
        data.plot(kind='pie', autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12})
        plt.axis('equal')
        plt.title('NContagios en algunos municipios importantes')
        plt.tight_layout()

    else:
        return "Tipo de gráfica no soportada"

     #pasamos la grafica a una imagen png
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    plt.close()

    #codificamos la imagen en base64 y usando flask lo mostramos en la plantilla html
    tmpfile.seek(0)
    plot_url = base64.b64encode(tmpfile.getvalue()).decode('utf8')
    return render_template('graph4.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
