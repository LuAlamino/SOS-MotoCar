# 🚗 SOS-MotoCar

**SOS-MotoCar** é um aplicativo projetado para ajudar motoristas que enfrentam problemas com seus carros em uma cidade. Com o SOS-MotoCar, você pode localizar mecânicos disponíveis, ver quais tipos de veículos eles atendem e obter todas as informações necessárias para assistência rápida e eficiente.

## 📦 Funcionalidades

- **🔧 Localização de Mecânicos:** Encontre mecânicos próximos à sua localização atual ou em uma cidade específica.
- **📋 Detalhes dos Mecânicos:** Veja informações detalhadas sobre cada mecânico, incluindo horários de atendimento, serviços oferecidos e contato.
- **🚗 Tipo de Veículos:** Verifique quais tipos de veículos cada mecânico pode reparar.
- **💻 Interface Intuitiva:** Navegue facilmente pela aplicação para encontrar a ajuda que você precisa rapidamente.

## 🛠 Tecnologias Utilizadas

- **Front-end:** [React](https://reactjs.org/) (ou substitua pelo framework/language que você estiver usando)
- **Back-end:** [Django](https://www.djangoproject.com/) com Python
- **Banco de Dados:** [PostgreSQL](https://www.postgresql.org/) (ou substitua pelo banco de dados que você estiver usando, como MySQL ou SQLite)
- **API de Geolocalização:** [Google Maps API](https://developers.google.com/maps) (ou substitua pela API que você estiver usando)

## 🚀 Instalação

Para rodar o projeto localmente, siga os passos abaixo:

1. **Clone o Repositório:**

   ```sh
   git clone https://github.com/SeuUsuario/SOS-MotoCar.git
   cd SOS-MotoCar
2. **Instale as Dependências:**

Para o front-end:
   ```sh
 cd frontend
npm install  # ou yarn install, dependendo do gerenciador de pacotes
   ```



Para o back-end:
   ```sh
cd backend
pip install -r requirements.txt
   ```

3. **Configure as Variáveis de Ambiente:**

Crie um arquivo .env na raiz do diretório backend e adicione as seguintes variáveis (ajuste conforme necessário):
   ```sh
makefile
Copiar código
DATABASE_URL=postgres://usuario:senha@localhost:5432/sos_moto_car
SECRET_KEY=...
DEBUG=True
   ```
Nota: Se estiver usando um banco de dados diferente, ajuste a DATABASE_URL de acordo.

4. **Execute as Migrações do Banco de Dados (para o back-end):**


   ```sh
    python manage.py migrate


5. **Crie um Superusuário (opcional, para acesso ao painel de administração do Django):**


   ```sh

    python manage.py createsuperuser
   ```

6. **Inicie o Servidor de Desenvolvimento:**

Para o front-end:

   ```sh
npm start  # ou yarn start
   ```

Para o back-end:

   ```sh
python manage.py runserver
   ```

7. **Acesse a Aplicação:**

Abra seu navegador e vá para http://localhost:3000 para o front-end e http://localhost:8000 para o back-end.

🤝 Contribuindo
Se você quiser contribuir para o projeto, siga estas etapas:

8. **Faça um Fork do Repositório.**

9. **Crie uma Nova Branch:**


   ```sh
    git checkout -b minha-nova-feature

10. **Faça as Alterações e Testes Necessários.**

11. **Envie um Pull Request.**

📜 **Licença**

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

📬 Contato
Autor: Lucas Alamino Martins

[![Perfil DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-30A3DC?style=for-the-badge)](https://web.dio.me/users/alaminolucas/)

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=30A3DC)](www.linkedin.com/in/lucas-alamino-martins/)

[![E-mail](https://img.shields.io/badge/-Email-000?style=for-the-badge&logo=microsoft-outlook&logoColor=E94D5F)](mailto:alaminolucas@gmail.com)

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=LuAlamino&theme=transparent&bg_color=000&border_color=30A3DC&show_icons=true&icon_color=30A3DC&title_color=E94D5F&text_color=FFF)
![Top Langs](https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api/top-langs/?username=LuAlamino&layout=compact&bg_color=000&border_color=30A3DC&title_color=E94D5F&text_color=FFF)