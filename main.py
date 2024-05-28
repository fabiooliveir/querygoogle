from google.ads.googleads.client import GoogleAdsClient
from datetime import datetime

def main(client, customer_id):
    ga_service = client.get_service("GoogleAdsService")

    # Obtém o mês atual no formato AAAAMMDD
    current_month_start = datetime.now().strftime('%Y%m01')
    current_month_end = datetime.now().strftime('%Y%m%d')

    query = f"""
        SELECT
          ad_group.id,
          ad_group.name,
          ad_group.status,
          metrics.impressions,
          metrics.clicks,
          metrics.cost_micros
        FROM ad_group
        WHERE ad_group.status = 'ENABLED'
          AND metrics.impressions > 0
          AND segments.date BETWEEN '{current_month_start}' AND '{current_month_end}'
        ORDER BY ad_group.id"""

    # Issues a search request using streaming.
    stream = ga_service.search_stream(customer_id=customer_id, query=query)

    for batch in stream:
        for row in batch.results:
            print(
                f"Ad Group with ID {row.ad_group.id} and name "
                f'"{row.ad_group.name}" was found with status '
                f'"{row.ad_group.status}", {row.metrics.impressions} impressions, '
                f'{row.metrics.clicks} clicks, and cost {row.metrics.cost_micros} micros.'
            )

# Carrega as credenciais do arquivo google-ads.yaml
client = GoogleAdsClient.load_from_storage(r"C:\Users\fboli\querygoogle\google-ads.yaml")

# Chama a função main passando o cliente e o ID do cliente
main(client, 'id_do_cliente')
