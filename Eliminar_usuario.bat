@echo off
  set /p user=escriba el usuario a eliminar:
  
net user | find /i "%user%" >nul 2>&1

if %errorlevel% equ 0 (


    set /p confirmar=¿Estas seguro de eliminarlo? (escribe SI para confirmar): 
    
    if /i "%confirmar%"=="SI" (
        net user "%user%" /delete
        
        if %errorlevel% equ 0 (
            echo [+] Usuario "%user%" eliminado con exito.
        ) else (
            echo [X] ERROR: No se pudo eliminar. ¿Iniciaste como Administrador?
        )
    ) else (
        echo Operacion cancelada por el usuario.
    )
  ) else (
    echo no existe
  )
  
  pause