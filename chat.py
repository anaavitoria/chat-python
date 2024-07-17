import flet as ft # type: ignore
 
 
 # Mauricio Aires

def main(pagina):
    texto = ft.Text("Hashzap")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
    
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print("Enviar mensagem")

        pagina.pubsub.send_all(campo_mensagem.value)
        
        campo_mensagem.value = ""
        pagina.update()

    
    campo_mensagem = ft.TextField(label="Digite sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])    
    
    def entrar_chat(evento):    
        print("Entrar no chat")

        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        pagina.add(linha_enviar)
        pagina.update()


    titulo_popup = ft.Text("Bem vindo ao Haszap")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(open=False, modal=True, title=titulo_popup, content=nome_usuario, actions=[botao_entrar])


    def abrir_popup(evento):
        print("entrar no chat")
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)
    


    pagina.add(texto)
    pagina.add(botao_iniciar)
    
ft.app(target=main, view=ft.WEB_BROWSER)

    