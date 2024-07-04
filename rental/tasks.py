from celery import shared_task
from .models import Rental

@shared_task
def calculate_rental_cost(rental_id):
    rental = Rental.objects.get(pk=rental_id)
    duration = (rental.end_time - rental.start_time).total_seconds()/3600
    cost = duration * 200 # 200 рублей в час за аренду
    print(f'Total cost for rental {rental.id} id ${cost}')

