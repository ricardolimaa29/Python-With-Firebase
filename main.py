import flet as ft
import pyrebase
import time

firebaseConfig = {
  'apiKey': "AIzaSyAzkdhg047I1hngspT5R6jvTIouGBwX4jA",
  'authDomain': "teste-login-d3e9c.firebaseapp.com",
  'projectId': "teste-login-d3e9c",
  'databaseURL': "https:Login.firebaseio.com",
  'storageBucket': "teste-login-d3e9c.firebasestorage.app",
  'messagingSenderId': "856646517273",
  'appId': "1:856646517273:web:b70f5f2df99ce0d77f6088",
  'measurementId': "G-D43XDB0BD6"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def main(pagina: ft.Page):
    pagina.window_height = 800 # TAMANHO DE TELA DO SISTEMA
    pagina.window_width = 1200 
    pagina.title = 'Gestão de cameras' # TITULO DO PROJETO
    pagina.fonts = { #Fontes do PROJETO
                    "Poppins": "fonts/Poppins-Bold.ttf",
                    "Poppins2": "fonts/Poppins-Light.ttf",
                    "Poppins3": "fonts/Poppins-Regular.ttf"}
    pagina.vertical_alignment = 'center'
    pagina.horizontal_alignment = 'center'
    pagina.spacing = 20
    # def barra_navegacao():
    #     rail = ft.NavigationRail(
    #         expand=True,
    #         selected_index=0,
    #         min_width=100,
    #         min_extended_width=400,
    #         label_type=ft.NavigationRailLabelType.ALL,
    #         leading=ft.FloatingActionButton(icon=ft.icons.CREATE,text='Abrir Mesas'),
    #         group_alignment=-0.9,
    #         destinations=[
    #             ft.NavigationRailDestination(icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORETE, label="Favorito")
    #         ]
    #     )
    def registrar(e):
        try: 
            auth.create_user_with_email_and_password(usuario.value, senha.value)
            pagina.snack_bar = ft.SnackBar(ft.Text('Usuario cadastrado com sucesso !',
                                    font_family='Poppins',
                                    size=15,color='White'),bgcolor='Green')
            pagina.snack_bar.open = True
            Loggin_Text.value = 'Bem vindo ! 🎉'
            usuario.border_color = 'Green'
            senha.border_color = 'Green'
            usuario.value = None
            senha.value = None
            pagina.update()
            time.sleep(3)
            # tirando
            Loggin_Text.value = 'Login'
            usuario.border_color = 'None'
            senha.border_color = 'None'
            pagina.update()
        except:
            pagina.snack_bar = ft.SnackBar(ft.Text('Erro, conta existente !',
                                    font_family='Poppins',
                                    size=15,color='White'),bgcolor='Red')
            pagina.snack_bar.open = True
            usuario.border_color = 'Red'
            senha.border_color = 'Red'
            pagina.snack_bar.open = True
            senha.value = None
            pagina.update()

    def loggin(e):
        try:
            auth.sign_in_with_email_and_password(usuario.value,senha.value)
            pagina.snack_bar = ft.SnackBar(content=ft.Text('Logado com sucesso'),bgcolor='Green',action='OK',duration=3000)
            pagina.snack_bar.open = True
            usuario.visible = False
            senha.visible = False
            botao_entrar.visible = False
            registrar_se.visible = False
            criar_conta.visible = False
            Loggin_Text.visible = False
            
            pagina.update()
        except:
            pagina.snack_bar = ft.SnackBar(content=ft.Text('ERRO!!'),bgcolor='Red',action='OK',duration=3000)
            pagina.snack_bar.open = True
            usuario.value = None
            senha.value = None
            pagina.update()

    Loggin_Text = ft.Text('Login',font_family='Poppins',size=30)
    usuario = ft.TextField(label='Usuario:',
        text_style=ft.Text(font_family='Poppins2',style=ft.ButtonStyle()),
        width=280,
        focused_border_color='Teal',)
    senha = ft.TextField(label='Senha:',
        text_style=ft.Text(font_family='Poppins2'),
        password=True,width=280,
        focused_border_color='Teal',
        can_reveal_password=True)
    criar_conta = ft.Text('Ainda não tem uma conta ?')
    registrar_se = ft.ElevatedButton('Registre-se',on_click=registrar,bgcolor=None,color='Green',on_focus=None)
    botao_entrar = ft.ElevatedButton(text='Entrar',color='White',bgcolor='Green',width=200,height=50,on_click=loggin)

    layoult = ft.Column(
            [
                Loggin_Text,
                usuario,
                senha,
                criar_conta,registrar_se,
                botao_entrar
            ]
        )
        
    pagina.add(layoult)
    
ft.app(target=main)