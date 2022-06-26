# ChatbotCendi
## Creando entorno para desarrollar
```python
python -m venv ia2_entorno
```
Abrir entorno desde windows, en CMD
```cmd
ia2_entorno\Scripts\activate.bat
```
En PowerShell
```Powershell
ia2_entorno\Scripts\activate.ps1
```
### Instalar dependencias
```python
ia2_entorno\Scripts\python.exe -m pip install --upgrade pip
pip install -U nltk  numpy tensorflow flask
```

### Instalar dependencias para fronted
Importante tener instalado node.js
```powershell
npm install -g npm@8.13.1
npm install express
npm install nodemon
```