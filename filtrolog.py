log = {
'timestamp': '2021-06-23 10:00:00',
'level': 'ERROR', 
'message': 'Falha na conexão'
}

# Verifica se o nível de severidade é "ERROR"
if log['level'] == 'ERROR':
    print(f"🚨 ERRO DETECTADO ({log['timestamp']}): {log['message']}")