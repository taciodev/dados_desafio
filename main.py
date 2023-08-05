import pandas as pd
import matplotlib.pyplot as plt
import locale


# Função para formatar moeda
def format_brazilian_currency(value):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    formatted_value = locale.currency(value, grouping=True, symbol=None)
    return formatted_value


file_path = "dados_desafio.xlsx"
df = pd.read_excel(file_path)

# análise do número de pedidos
total_order_count = df['id_pedido'].nunique()
print(f"Quantidade total de pedidos: {total_order_count}")

# análise do número de clientes
unique_customer_count = df['id_unico_cliente'].nunique()
print(f"\nNúmero de clientes: {unique_customer_count}")

# contagem de clientes por estado
customer_count_by_state = df.groupby('estado_cliente')['id_unico_cliente'].nunique()
print("\nContagem de clientes por estado:")
print(customer_count_by_state)

# gráfico de contagem de clientes por estado
plt.figure(figsize=(8, 6))
customer_count_by_state.plot(kind='bar', color='skyblue')
plt.title('Contagem de Clientes por Estado')
plt.xlabel('Estado')
plt.ylabel('Contagem de Clientes')
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig('graficos/estado_cliente.png')

# análise da média de pedidos por cliente
average_orders_per_customer = df['id_unico_cliente'].value_counts().mean().round()
print(f"\nMédia de pedidos por cliente: {average_orders_per_customer}")

# análise da média de tempo de aprovação do pedido
df['data_hora_pedido'] = pd.to_datetime(df['data_hora_pedido'])
df['pedido_aprovado'] = pd.to_datetime(df['pedido_aprovado'])
df['tempo_aprovacao'] = df['pedido_aprovado'] - df['data_hora_pedido']
average_approval_time = df['tempo_aprovacao'].mean()

days = average_approval_time.days
seconds = average_approval_time.seconds
hours, seconds = divmod(seconds, 3600)
minutes, seconds = divmod(seconds, 60)

print(f"\nTempo médio de aprovação: {days}d {hours}h {minutes}m {seconds}s")

# análise dos status de pedidos
order_status_count = df['status_pedido'].value_counts()
print("\nContagem de pedidos:")
print(order_status_count)

# gráfico de contagem de pedidos por status
plt.figure(figsize=(8, 6))
order_status_count.plot(kind='bar', color='skyblue')
plt.title('Contagem de Pedidos por Status')
plt.xlabel('Status do Pedido')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('graficos/status_pedido.png')

# análise do faturamento em relação ao frete
total_freight_sum = df['valor_frete'].sum()
formatted_freight_sum = format_brazilian_currency(total_freight_sum)
print(f"\nSoma dos valores da coluna 'valor_frete': R$ {formatted_freight_sum}")

# análise do lucro total (Valor de Pagamento)
total_payment_sum = df['pagamento_valor'].sum()
formatted_payment_sum = format_brazilian_currency(total_payment_sum)
print(f"Soma dos valores da coluna 'valor_frete' (Lucro total): R$ {formatted_payment_sum}")

# análise dos vendedores
total_vendor_count = df['cep_vendedor'].nunique()
print(f"\nQuantidade total de vendedores: {total_vendor_count}")
vendor_count_by_state = df.groupby('estado_vendedor')['cep_vendedor'].nunique()
print("\nQuantidade de vendedores por estado:")
print(vendor_count_by_state)

# gráfico de quantidade de vendedores por estado
plt.figure(figsize=(8, 6))
vendor_count_by_state.plot(kind='bar', color='skyblue')
plt.title('Quantidade de vendedores por estado')
plt.xlabel('Estado')
plt.ylabel('Quantidade de Vendedores')
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig('graficos/estado_vendedor.png')

# análise de categoria
unique_category = df['categoria'].value_counts()
print(f"\nQuantidade de itens vendidos em cada categoria: {unique_category}")

plt.figure(figsize=(12, 15))
unique_category.plot(kind='barh', color='skyblue')
plt.title('Quantidade de Itens Vendidos em Cada Categoria')
plt.xlabel('Categoria')
plt.ylabel('Quantidade de Itens')
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig('graficos/categorias.png')

# Calcula a quantidade de avaliações para cada score
quantidade_por_score = df['score_avaliacao'].value_counts()

print("\nQuantidade de avaliações:")
print(quantidade_por_score)

plt.figure(figsize=(8, 6))
quantidade_por_score.plot(kind='bar', color='skyblue')
plt.title('Quantidade de Avaliações por Score')
plt.xlabel('Score')
plt.ylabel('Quantidade de Avaliações')
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig('graficos/score.png')
