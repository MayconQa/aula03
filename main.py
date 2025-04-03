import time

# Lista de placas cadastradas e permitidas
placas_cadastradas = ["ABC-1234", "DEF-5678", "GHI-9012", "JKL-3456"]

# Lista de placas proibidas
placas_proibidas = ["GHI-9012", "XYZ-9999"]

# Simulação de leitura de placas (substitua isso pela integração com a câmera)
def ler_placa():
    placas_detectadas = ["DEF-5678", "XYZ-9999", "MNO-6789", "ABC-1234", "GHI-9012"]
    for placa in placas_detectadas:
        yield placa  # Retorna cada placa detectada como se viesse de uma câmera
        time.sleep(2)  # Simula o tempo entre leituras

# Loop contínuo de verificação de placas
for placa in ler_placa():
    print(f"\n🔍 Placa detectada: {placa}")

    if placa in placas_proibidas:
        print(f"🚨 ALERTA! O veículo com placa {placa} está com ENTRADA PROIBIDA! Notificando a portaria.")
    elif placa in placas_cadastradas:
        print(f"✅ Entrada liberada para a placa {placa}.")
    else:
        print(f"❌ Placa {placa} NÃO CADASTRADA! Notificando a portaria para verificação.")


