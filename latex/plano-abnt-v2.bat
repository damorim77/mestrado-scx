@echo off
rem Compila docs/plano/latex/plano-abnt-v2.tex (pdflatex + biber + 2x pdflatex).
rem Uso: duplo-clique ou plano-abnt-v2.bat no prompt, dentro desta pasta.
setlocal
set "PATH=C:\Users\danil\AppData\Local\Programs\MiKTeX\miktex\bin\x64;%PATH%"
cd /d "%~dp0"
call pdflatex -interaction=nonstopmode plano-abnt-v2.tex || exit /b 1
call biber plano-abnt-v2 || exit /b 1
call pdflatex -interaction=nonstopmode plano-abnt-v2.tex || exit /b 1
call pdflatex -interaction=nonstopmode plano-abnt-v2.tex || exit /b 1
echo OK: plano-abnt-v2.pdf atualizado.
