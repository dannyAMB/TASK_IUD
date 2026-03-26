@echo off
title Validador y Creador de Usuarios
color 0a

:: RECUERDA: Ejecutar como Administrador
set /p user=Nombre del nuevo usuario:

net user | find /i "%user%" >nul 2>&1

if %errorlevel% equ 0 (
  echo.
  echo ERROR: El nombre "%user%" ya esta en uso.
  echo Intenta con un nombre diferente.
  echo Si desea eliminarlo escribe si:
  set /p validar=Si desea eliminarlo escribe si:
  
  if /i "%validar%"=="si" (
    net user "%user%" /delete
    echo Usuario %user% eliminado.
  )
  
  ) else (
  echo.
  echo El nombre esta disponible.
  set /p pass=Asigna una contrasena para %user%:
  
  net user "%user%" "%pass%" /add
  net localgroup Administradores "%user%" /add
  if %errorlevel% equ 0 (
    echo Usuario "%user%" creado exitosamente.
    ) else (
    echo Error critico: Asegurate de tener permisos de Administrador.
  )
)

pause
