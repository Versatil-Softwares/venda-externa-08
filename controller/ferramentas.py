from datetime import datetime

# Retorna a data atualizada
def get_date_now():
    s_date_now = datetime.now()
    s_date_table = s_date_now.strftime("%Y-%m-%d")
    return s_date_table

# Retorna o horário atual
def get_time_now():
    s_time_now = datetime.now()
    s_time_table = s_time_now.strftime("%H:%M:%S")
    return s_time_table

# formata a data para enviar para o banco de dados
def format_date_for_bd(date):
    if date is not False:
        data = datetime.strptime(str(date), '%d/%m/%Y')
        return data.strftime('%Y-%m-%d')
    else:
        return None

#Verifica se o valor for None e se for retorna 0
def is_none(valor):
    if valor is None:
        return 0
    else:
        return valor

# Recebe a data no formato do firebird e formata para o padrão brasileiro
def get_data_firebird(data):
    if data is not None:
        data_firebird = datetime.strptime(str(data), '%Y-%m-%d')
        return data_firebird.strftime('%d/%m/%Y')
    else:
        return False
