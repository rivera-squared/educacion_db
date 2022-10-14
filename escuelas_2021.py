# Academic Year 2020-21 Study
import pandas as pd
import numpy as np

# Data merging and preprocessing 

# Loading dataset for schools' metrics
df = pd.read_csv('https://raw.githubusercontent.com/rivera-squared/educacion_db/main/aprovechamiento.csv')
df.columns # Listing df columns
df.metrica.unique() #Unique Academic years in the dataset
df[df['metrica'] == 'Tasa de Asistencia de los Maestros'].puntuacion
# Selecting columns of interest
columnas = ['region','municipioEscolar', 'nivel','codigo','nombreEscuela',
            'metrica','puntuacion']
df = df[columnas]

df.metrica.unique()

# Converting from long to wide format
x = pd.pivot(df, index=['codigo','region','nivel','municipioEscolar','nombreEscuela'], columns= 'metrica', values = 'puntuacion')
x = x.reset_index()
x.columns

# Selecting columns of interest
columnas = ['codigo', 'region', 'municipioEscolar', 'nombreEscuela', 'nivel',
            'Ausentismo Crónico de los Estudiantes',
            'Proficiencia en Ciencias',
           'Proficiencia en Español', 'Proficiencia en Inglés',
           'Proficiencia en Matemáticas', 'Tasa de Asistencia de los Estudiantes',
           'Tasa de Asistencia de los Maestros']

x = x[columnas]

# Renaming df and columns' names
escuelas = x.rename(columns = {'Ausentismo Crónico de los Estudiantes': 'ausentismo_cronico',
                    'Proficiencia en Ciencias':'ciencias_meta',
                    'Proficiencia en Español': 'espanol_meta',
                    'Proficiencia en Inglés': 'ingles_meta',
                    'Proficiencia en Matemáticas': 'mate_meta',
                    'Tasa de Asistencia de los Estudiantes':'asistencia_estudiantes_pct',
                    'Tasa de Asistencia de los Maestros':'asistencia_maestros_pct'})

escuelas[['ausentismo_cronico','ciencias_meta','espanol_meta','ingles_meta','mate_meta','asistencia_estudiantes_pct','asistencia_maestros_pct']].describe()

# Loading dataset for enrollment info
enrollment = pd.read_csv('https://raw.githubusercontent.com/rivera-squared/educacion_db/main/enrollment_by_acYear.csv')
# Filtering data for academic year 2020-21 only
enrollment = enrollment[enrollment['AcademicYear'] == 2021]

enrollment.columns
columnas = ['PartitionKey','All','Disabilities', 'EconomicallyDisadvantaged',
            'FosterCare','Female','Male','Migrants','Section504']

enrollment = enrollment[columnas]
# Renaming Columns
enrollment = enrollment.rename(columns = {'PartitionKey':'codigo',
                             'All':'matricula',
                             'EconomicallyDisadvantaged':'econ_des'})
# Left joining escuelas and enrollment datasets
escuelas_2021 = escuelas.merge(enrollment, how = 'left', on = 'codigo')

escuelas_2021.columns
# Calculating percentage of students economically disavantaged
escuelas_2021['econ_des_pct'] = escuelas_2021['econ_des'] / escuelas_2021['matricula']
# Calculating percentage of students with disabilities
escuelas_2021['disabilities_pct'] = escuelas_2021['Disabilities'] / escuelas_2021['matricula']

# Loading data
escuelasData = pd.read_csv('escuelasData.csv')
escuelasData.columns
escuelasData = escuelasData[['codigo','zona','latitud','longitud']]

escuelas_2021 = escuelas_2021.merge(escuelasData, how = 'left', on = 'codigo')

escuelas_2021.groupby('nivel')['econ_des_pct'].describe()
escuelas_2021.to_csv('escuelas_2021.csv', index = False)






















































