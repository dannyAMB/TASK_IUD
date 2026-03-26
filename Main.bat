@echo off
title Mi Script Fundamentos de programacion
echo Iniciando proceso...

set var_fecha=%date:/=-%
set var_carpeta=DocumentosSO_%var_fecha%
:: md "%var_carpeta%"
set crear_archivo=nuevo_archivo.bat
set ruta_destino=C:\Users\asus\Escritorio\DESARROLLO-WEB\TAREAS_IUD

echo Fecha: %var_fecha%

if not exist "%var_carpeta%" (
  md "%var_carpeta%"
  echo Carpeta "%var_carpeta%" creada.
  
  echo @echo off > %crear_archivo%
  
  echo echo Registro de inicio: %date% %time% >> %crear_archivo%
  echo echo archivo creado >> %crear_archivo%
  echo md "%ruta_destino%\%var_carpeta%\nuevacarpeta" >> %crear_archivo%
  echo pause >> %crear_archivo%
  echo Datos guardados en %crear_archivo%.
  
  move "%crear_archivo%" "%ruta_destino%\%var_carpeta%"
  echo Archivo movido con exito a: "%ruta_destino%\%var_carpeta%"
  start "" "%ruta_destino%\%var_carpeta%\%crear_archivo%"
  
  ) else (
  echo La carpeta "%var_carpeta%" ya existe, limpiamos
  rd /s /q "%var_carpeta%"
  
)

pause
