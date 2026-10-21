@echo off
rem Compila plano/latex/plano-abnt.tex (pdflatex + biber + 2x pdflatex).
rem Uso: duplo-clique ou plano-abnt.bat no prompt, dentro desta pasta.
setlocal
set "PATH=C:\Users\danil\AppData\Local\Programs\MiKTeX\miktex\bin\x64;%PATH%"
cd /d "%~dp0"
call pdflatex -interaction=nonstopmode plano-abnt.tex || exit /b 1
call biber plano-abnt || exit /b 1
call pdflatex -interaction=nonstopmode plano-abnt.tex || exit /b 1
call pdflatex -interaction=nonstopmode plano-abnt.tex || exit /b 1
echo OK: plano-abnt.pdf atualizado.
