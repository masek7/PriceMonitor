from openpyxl import load_workbook
from captura_preco import captura_preco, armazena_link
from datetime import date
from winotify import Notification, audio

# Guardando a data do dia em que o script é executado e formatando para o formato brasileiro
data = date.today()
dataFormatada = data.strftime('%d/%m/%Y')


def escrevendo_preco():
    """Função que anota o preço na planilha definida"""
    try:
        # Carrega a planilha Excel
        workbook = load_workbook(r'C:\Users\GuiMo\Downloads\price_monitor.xlsx')
        sheet = workbook.active

        # Captura a última linha preenchida com texto na planilha
        ultima_linha = sheet.max_row

        # Próxima linha vazia para inserir os dados
        proxima_linha = ultima_linha + 1
        celula_a = sheet[f'A{proxima_linha}']
        celula_b = sheet[f'B{proxima_linha}']

        # Verifica o valor da última célula A com preço
        ultimo_valor_a = sheet[f'A{ultima_linha}']

        # Verifica se a célula atual está vazia, e anota o preço e data na próxima linha
        if celula_a.value is None:
            celula_a.value = captura_preco()
        if celula_b.value is None:
            celula_b.value = dataFormatada

        # Salva as alterações na planilha
        workbook.save(r'C:\Users\GuiMo\Downloads\price_monitor.xlsx')

        # Configura notificações
        notify_up = Notification(app_id="Monitorador de Preço", title="O PREÇO DO PRODUTO SUBIU",
                                 msg=f'O preço atual é: {celula_a.value} reais.',
                                 duration="short",
                                 icon=r"C:\Users\GuiMo\Downloads\pascall.gif")
        notify_up.set_audio(audio.Reminder, loop=False)
        notify_up.add_actions(label="Link para o produto",
                              launch=armazena_link())

        notify_down = Notification(app_id="Monitorador de Preço", title="O PREÇO DO PRODUTO CAIU",
                                   msg=f'O preço atual é: {celula_a.value} reais.',
                                   icon=r"C:\Users\GuiMo\Downloads\cerrisete.gif")
        notify_down.set_audio(audio.Reminder, loop=False)
        notify_down.add_actions(label="Link para o produto",
                                launch=armazena_link())




        # Compara o valor atual com o anterior e envia a notificação correta
        if celula_a.value and ultimo_valor_a.value:  # Verifica se os valores não são None
            if celula_a.value > ultimo_valor_a.value:
                notify_up.show()
            elif celula_a.value < ultimo_valor_a.value:
                notify_down.show()
        else:
            print("Valores inválidos encontrados na planilha.")


        preco_historico = sheet['A2']
        new_preco_historico = float(preco_historico.value)

        if new_preco_historico > celula_a.value:
            preco_historico = celula_a.value
            notify_record = Notification(app_id="Monitorador de Preço", title="MENOR PREÇO HISTÓRICO",
                                         msg=f'O PREÇO ATUAL É: {celula_a.value} REAIS!!',
                                         icon=r"C:\Users\GuiMo\Downloads\moneyrich.gif")
            notify_record.set_audio(audio.Reminder, loop=False)
            notify_record.add_actions(label="Link para o produto",
                                      launch=armazena_link())
            notify_record.show()


    except Exception as e:
        print(f"Ocorreu um erro: {e}")


escrevendo_preco()
