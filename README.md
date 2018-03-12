# facebookLast500Visitors
Lista os ultimos 500 visitantes do seu perfil do facebook.


## Antes de executar runner.py
```shell
pip install -r requirements.txt
```

### Dentro do arquivo ./libs/checker.py
É necessário atualizar as seguintes linhas de codigo:
```python
21. browser.form['email'] = 'your_login'
22. browser.form['pass'] = 'your_password'
```

## Executar projeto
```python
python runner.py
```

## Tecnlogias utilizadas

* Mechanize
* BeautifulSoup
* Pandas
