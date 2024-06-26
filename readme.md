### Iniciando django

```bash
django-admin startproject app .

#iniciar servidor
python manage.py runserver

# criar apps
python manage.py startapp nome_app

# usar app após criação
# alterar arquivo settings.py

# gera o script do banco de dados
python manage.py makemigrations

# executa as queries para o banco de dados.
python manage.py migrate

# criar superuser
python manage.py createsuperuser

```

### Sintaxes do Django

No Django template language, a sintaxe correta para acessar o primeiro elemento de uma lista é colocar o índice antes do atributo. Portanto, você deve usar `{{ header_banner.0.title }}` em vez de `{{ header_banner.title[0] }}`.

### Sequencia de criação


1. Settings
   1. Configurar arquivos estáticos
   2. Configurar Media settings
   3. Configurar Internacionalização
   4. Inserir novos apps criados
2. Models
   1. Criar classe
3. Admin
   1. Criar classe
   2. registrar admin
4. app
   1. settings.py: inserir novos apps criados


### Editor Rich Text

`pip install django-ckeditor`

https://pypi.org/project/django-ckeditor

https://www.youtube.com/watch?v=YsgCGsTF5eg

*adicionado rich text no campo horário de funcionamento, no rodapé do site*




### Chaves ssh git hub

- [Gerando uma nova chave SSH e adicionando-a ao agente SSH](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- Copiar a chave (git bash > `cat git.pub` ou `clip < git.pub`)
- [Settings > SSH Keys](https://github.com/settings/keys)

### Documentation

- `:notebook: doc: documentação`
- `:star: feat: describe feat...`
- `:recycle: refatc: ...`


parei #A027

https://bootstrapbrain.com/
