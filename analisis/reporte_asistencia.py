import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos\estudiante.csv')

print('ESTUDIANTES')
print()
print(df)


df1 = pd.read_csv('datos\listado_asistencia.csv')

print('ASISTENCIAS')
print()
print(df1)


asistencias_completas = pd.merge(df,df1,  how="left" )

print('ASISTENCIAS Y ESTUDIANTES')
print()
print(asistencias_completas)

print('ASISTENCIAS Y ESTUDIANTES by cedula = 1234567891')
print()
print(asistencias_completas[asistencias_completas.cedula == 1234567891])

asistencias_completas[asistencias_completas.cedula == 1234567891].to_csv('datos\informe_1234567891.csv', index=False)

asistencias_completas[asistencias_completas.cedula == 1234567891]['materia'].value_counts().plot(kind='bar')

plt.show()